from __future__ import annotations

from typing import Any, Callable

from .chunking import _dot
from .embeddings import _mock_embed
from .models import Document


class EmbeddingStore:
    """
    A vector store for text chunks.

    Tries to use ChromaDB if available; falls back to an in-memory store.
    The embedding_fn parameter allows injection of mock embeddings for tests.
    """

    def __init__(
        self,
        collection_name: str = "documents",
        embedding_fn: Callable[[str], list[float]] | None = None,
    ) -> None:
        self._embedding_fn = embedding_fn or _mock_embed
        self._collection_name = collection_name
        self._use_chroma = False
        self._store: list[dict[str, Any]] = []
        self._collection = None
        self._next_index = 0

        try:
            # The lab contract uses the deterministic in-memory backend.
            self._use_chroma = False
        except Exception:
            self._use_chroma = False
            self._collection = None

    def _make_record(self, doc: Document) -> dict[str, Any]:
        metadata = dict(doc.metadata or {})
        metadata.setdefault("doc_id", doc.id.split("#", 1)[0])
        return {"id": doc.id, "content": doc.content, "metadata": metadata,
                "embedding": self._embedding_fn(doc.content)}

    def _search_records(self, query: str, records: list[dict[str, Any]], top_k: int) -> list[dict[str, Any]]:
        query_vector = self._embedding_fn(query)
        ranked = []
        for record in records:
            item = {k: v for k, v in record.items() if k != "embedding"}
            item["score"] = _dot(query_vector, record["embedding"])
            ranked.append(item)
        ranked.sort(key=lambda x: x["score"], reverse=True)
        return ranked[:max(0, top_k)]

    def add_documents(self, docs: list[Document]) -> None:
        """
        Embed each document's content and store it.

        For ChromaDB: use collection.add(ids=[...], documents=[...], embeddings=[...])
        For in-memory: append dicts to self._store
        """
        self._store.extend(self._make_record(doc) for doc in docs)

    def search(self, query: str, top_k: int = 5) -> list[dict[str, Any]]:
        """
        Find the top_k most similar documents to query.

        For in-memory: compute dot product of query embedding vs all stored embeddings.
        """
        return self._search_records(query, self._store, top_k)

    def get_collection_size(self) -> int:
        """Return the total number of stored chunks."""
        return len(self._store)

    def search_with_filter(self, query: str, top_k: int = 3, metadata_filter: dict = None) -> list[dict]:
        """
        Search with optional metadata pre-filtering.

        First filter stored chunks by metadata_filter, then run similarity search.
        """
        if not metadata_filter:
            return self.search(query, top_k)
        candidates = [r for r in self._store if all(r["metadata"].get(k) == v for k, v in metadata_filter.items())]
        return self._search_records(query, candidates, top_k)

    def delete_document(self, doc_id: str) -> bool:
        """
        Remove all chunks belonging to a document.

        Returns True if any chunks were removed, False otherwise.
        """
        before = len(self._store)
        self._store = [r for r in self._store if r["metadata"].get("doc_id") != doc_id]
        return len(self._store) < before
