# Báo Cáo Cá Nhân — Lab 7

**Họ tên:** Nguyễn Thanh Hòa
**Nhóm:** [Tên nhóm]
**Ngày:** 19/09/2023

## 1. Khởi động

Cosine similarity cao nghĩa là hai vector có hướng gần nhau, thường biểu diễn nội dung tương tự. Cosine phù hợp với text embedding vì ít phụ thuộc độ dài văn bản hơn Euclidean distance.

Với 10.000 ký tự, `chunk_size=500`, `overlap=50`: `ceil((10000-50)/(500-50)) = 23 chunks`. Với overlap 100: `ceil((10000-100)/(500-100)) = 25 chunks`. Overlap lớn hơn giữ ngữ cảnh tốt hơn nhưng tăng số chunk và chi phí embedding.

## 2. Hướng tiếp cận

`SentenceChunker` dùng regex tách sau dấu `.`, `!`, `?` khi theo sau là khoảng trắng hoặc xuống dòng, sau đó gom tối đa số câu cấu hình trong mỗi chunk. Text rỗng trả về list rỗng.

`RecursiveChunker` thử separator theo thứ tự paragraph, newline, sentence, space rồi cắt cứng. Base case là văn bản đã nhỏ hơn `chunk_size`, không còn separator hoặc separator rỗng.

`EmbeddingStore` lưu record gồm id, content, metadata và embedding. Search embedding query rồi xếp hạng bằng dot product. Filter được thực hiện trước search; `delete_document` xóa mọi chunk có cùng `metadata['doc_id']`.

`KnowledgeBaseAgent` lấy top-k chunk, đánh số context `[1]`, thêm nguồn vào prompt và yêu cầu chỉ trả lời dựa trên context. Store rỗng được xử lý bằng thông báo thay vì gọi LLM.

## 3. Hoàn thiện code

Đã hoàn thiện `src/chunking.py`, `src/store.py` và `src/agent.py`.

```text
42 passed in 0.30s
```

## 4. Kết quả truy xuất cá nhân

Chiến lược: **Heading-based chunking**, dùng RecursiveChunker làm fallback cho section dài. Corpus được nạp thành 63 chunks. Backend: `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.

| #   | Chunk liên quan                                                                       |    Score | Kết quả                                |
| --- | ------------------------------------------------------------------------------------- | -------: | -------------------------------------- |
| 1   | Top-1 `usth-green-tech-scholarship-2026#0` (0.724620); đáp án ở `#1` top-2 (0.698088) | 0.698088 | Đạt; top-3 có 18,000,000 và 6 months.  |
| 2   | `usth-green-tech-scholarship-2026#0` ở top-2                                          | 0.618118 | Chưa đủ; thiếu ngày 23/03 và tháng 04. |
| 3   | `usth-scholarship-procedure#1`                                                        | 0.687724 | Đạt; top-3 có Step 1–3.                |
| 4   | `usth-scholarship-application-2026#0`                                                 | 0.686447 | Đạt; có 16 tỷ VND và undergraduate.    |
| 5   | `usth-scholarship-regulation-2026#1`                                                  | 0.739502 | Đạt sau metadata filter.               |

**Kết quả:** 4/5 query có chunk liên quan và gold markers trong top-3.

Failure case của Query 2 cho thấy hệ thống nhận diện đúng tài liệu nhưng không đưa section chứa ngày tháng vào top-3. Semantic similarity theo chủ đề không luôn đồng nghĩa với khả năng trả lời đúng chi tiết.

## Tự đánh giá

| Tiêu chí               |      Điểm |
| ---------------------- | --------: |
| Warm-up                |       5/5 |
| My Approach            |      9/10 |
| Core Implementation    |     30/30 |
| Similarity Predictions |       4/5 |
| Competition Results    |      8/10 |
| **Tổng**               | **56/60** |
