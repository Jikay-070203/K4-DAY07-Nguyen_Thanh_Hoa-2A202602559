from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from src import Document, EmbeddingStore, LocalEmbedder, RecursiveChunker

DATA = ROOT / "data" / "scholarship"

QUERIES = [
    ("Số suất và giá trị Green Tech", "Học bổng Green Tech 2026 có bao nhiêu suất, giá trị bao nhiêu và kéo dài bao lâu?", None, ["18,000,000", "6 months"]),
    ("Mốc thời gian Green Tech", "Hạn cuối nộp hồ sơ học bổng Green Tech 2026 là ngày nào và thời gian dự kiến bắt đầu là khi nào?", None, ["March 23, 2026", "April 2026"]),
    ("Quy trình", "Quy trình xét học bổng và hỗ trợ tài chính của USTH gồm những bước nào?", None, ["Step 1", "Step 2", "Step 3"]),
    ("Quỹ học bổng 2026-2027", "Trong năm học 2026-2027, USTH dự kiến dành bao nhiêu tiền cho quỹ học bổng và áp dụng cho những nhóm người học nào?", None, ["VND 16 billion", "undergraduate"]),
    ("Đối tượng quy định 2026", "Đối tượng sinh viên nào được áp dụng các quy định học bổng năm 2026 của USTH?", {"audience": "student", "category": "scholarship-regulation"}, ["Vietnamese students", "international students"]),
]


def parse_file(path: Path):
    raw = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", raw, re.S)
    if not match:
        return {}, raw
    metadata = {}
    for line in match.group(1).splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        value = value.strip().strip('"')
        metadata[key.strip()] = value
    return metadata, match.group(2).strip()


def build_store():
    try:
        embedder = LocalEmbedder()
        backend = embedder._backend_name
    except Exception as exc:
        print(f"Local embedding unavailable ({exc}); using mock embeddings.")
        embedder = None
        backend = "mock embeddings fallback"
    store = EmbeddingStore("scholarship_benchmark", embedding_fn=embedder)
    chunker = RecursiveChunker(chunk_size=500)
    count = 0
    for path in sorted(DATA.glob("*.md")):
        metadata, content = parse_file(path)
        metadata["doc_id"] = path.stem
        chunks = heading_chunks(content, chunker)
        for index, chunk in enumerate(chunks):
            store.add_documents([Document(f"{path.stem}#{index}", chunk, metadata)])
            count += 1
    return store, count, backend


def heading_chunks(content, fallback_chunker):
    """Keep Markdown heading sections together so heading-specific facts stay retrievable."""
    sections = re.split(r"(?m)(?=^#{1,6}\s+)", content)
    output = []
    for section in sections:
        section = section.strip()
        if not section:
            continue
        if len(section) <= 500:
            output.append(section)
            continue
        heading = section.splitlines()[0]
        for piece in fallback_chunker.chunk(section):
            output.append(f"{heading}\n{piece}")
    return output


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    store, count, backend = build_store()
    print(f"Embedding backend: {backend}")
    print(f"Documents: {len(list(DATA.glob('*.md')))}")
    print(f"Chunks loaded: {count}")
    print("Note: mock embeddings are deterministic but do not encode semantic meaning.\n")
    for number, (title, question, metadata_filter, gold_markers) in enumerate(QUERIES, 1):
        print(f"=== Query {number}: {title} ===")
        print(question)
        for label, results in (("FILTERED" if metadata_filter else "TOP-3", store.search_with_filter(question, 3, metadata_filter)),):
            print(f"{label}:")
            for rank, result in enumerate(results, 1):
                content = result["content"].replace("\n", " ")
                print(f"  {rank}. score={result['score']:.6f} doc={result['metadata'].get('doc_id')} id={result['id']}")
                print(f"     {content[:240]}")
            joined = " ".join(r["content"] for r in results)
            found = [marker for marker in gold_markers if marker.lower() in joined.lower()]
            print(f"Gold markers found in top-3: {found} / {gold_markers}")
        if number == 5:
            unfiltered = store.search(question, 3)
            print("UNFILTERED (A/B comparison):")
            for rank, result in enumerate(unfiltered, 1):
                print(f"  {rank}. score={result['score']:.6f} doc={result['metadata'].get('doc_id')} id={result['id']}")
        print()


if __name__ == "__main__":
    main()
