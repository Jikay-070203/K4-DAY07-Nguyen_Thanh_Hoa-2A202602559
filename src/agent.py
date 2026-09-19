from typing import Callable

from .store import EmbeddingStore


class KnowledgeBaseAgent:
    """
    An agent that answers questions using a vector knowledge base.

    Retrieval-augmented generation (RAG) pattern:
        1. Retrieve top-k relevant chunks from the store.
        2. Build a prompt with the chunks as context.
        3. Call the LLM to generate an answer.
    """

    def __init__(self, store: EmbeddingStore, llm_fn: Callable[[str], str]) -> None:
        self.store = store
        self.llm_fn = llm_fn

    def answer(self, question: str, top_k: int = 3) -> str:
        results = self.store.search(question, top_k=top_k)
        if not results:
            return "Không tìm thấy thông tin phù hợp trong cơ sở tri thức."
        context = "\n\n".join(
            f"[{i}] source={r.get('metadata', {}).get('source_url', r.get('id', 'unknown'))}\n{r['content']}"
            for i, r in enumerate(results, 1)
        )
        prompt = (
            "Answer the question using only the context below. If the context does not contain the answer, say so. "
            "Cite the relevant context number(s).\n\n"
            f"Question: {question}\n\nContext:\n{context}"
        )
        return self.llm_fn(prompt)
