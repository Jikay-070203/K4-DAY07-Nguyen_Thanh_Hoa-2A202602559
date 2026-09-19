# Báo Cáo Nhóm — Lab 7

# Báo Cáo Nhóm — Lab 7: Embedding & Vector Store

**Nhóm:** [Tên nhóm của bạn]  
**Ngày nộp:** 19/09/2023

## Phân công thành viên & Chiến lược Chunking

| Thành viên         | Chiến lược                 |
| :----------------- | :------------------------- |
| Hồ Đăng Phúc       | Heading + RecursiveChunker |
| Lê Nguyễn Trâm Anh | FixedSizeChunker           |
| Nguyễn Thanh Hòa   | SentenceChunker            |

## 1. Lựa chọn tài liệu

**Chủ đề:** Dịch vụ và quy định học bổng đại học USTH.

Nhóm chọn chủ đề này vì phù hợp yêu cầu K4-L3A và có đủ thông tin định lượng, thời hạn, điều kiện, đối tượng và quy trình để đánh giá retrieval. Corpus gồm 8 nguồn công khai trong `data/scholarship/`, có `sources.csv` và frontmatter metadata.

Metadata chính: `audience`, `department`, `category`, `language`, `source_url`, `retrieved_at`, `document_version`, `license_or_permission`. Tất cả tài liệu đều có nguồn công khai, không chứa dữ liệu cá nhân hay thông tin đăng nhập.

Các tài liệu tiêu biểu gồm `usth-green-tech-scholarship-2026.md`, `usth-scholarship-application-2026.md`, `usth-scholarship-procedure.md`, `usth-scholarship-regulation-2026.md` và `usth-vallet-scholarship-2026.md`. Tổng cộng có 8 tài liệu.

## 2. Thiết kế chiến lược

Chiến lược cá nhân là **heading/section-aware kết hợp RecursiveChunker**. Văn bản được tách theo heading Markdown để các mục như `Scholarship Value` và `Important Dates` giữ được ngữ cảnh. Section dài hơn 500 ký tự tiếp tục được chia recursive và giữ heading trong từng chunk.

Benchmark Heading-based nạp 8 tài liệu thành **63 chunks**, dùng local multilingual embedding:

```text
sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2
```

Chiến lược này phù hợp với tài liệu quy định vì heading thường biểu thị một đơn vị ý nghĩa hoàn chỉnh. Heading-based đạt 4/5 query, bằng RecursiveChunker nhưng dùng nhiều hơn 10 chunks (63 so với 53). Điểm yếu là thông tin ngày tháng vẫn có thể không lọt top-3.

## 3. Câu hỏi và chất lượng truy xuất

| #   | Query                                                | Gold answer                                                                                        | Filter                                                |
| --- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| 1   | Green Tech có bao nhiêu suất, giá trị và thời hạn?   | 4 suất; 18.000.000 VND/suất trong 6 tháng.                                                         | Không                                                 |
| 2   | Hạn cuối Green Tech và thời gian bắt đầu?            | 23/03/2026; dự kiến bắt đầu tháng 04/2026.                                                         | Không                                                 |
| 3   | Quy trình học bổng và hỗ trợ tài chính gồm bước nào? | 3 bước: nhận hồ sơ; lập danh sách/trình Hội đồng SFA; công bố danh sách.                           | Không                                                 |
| 4   | Quỹ học bổng 2026-2027 bao nhiêu và dành cho ai?     | 16 tỷ VND cho undergraduate, master và doctoral candidates.                                        | Không                                                 |
| 5   | Ai thuộc phạm vi quy định học bổng 2026?             | Sinh viên Việt Nam và quốc tế trong chương trình chính quy; loại trừ exchange/internship theo MoU. | `audience=student`, `category=scholarship-regulation` |

| #   | Kết quả      | Evidence                                                                         |
| --- | ------------ | -------------------------------------------------------------------------------- |
| 1   | Đạt          | Top-3 chứa `18,000,000` và `6 months`.                                           |
| 2   | Failure case | Đúng tài liệu ở top-2 nhưng thiếu `March 23, 2026` và `April 2026`.              |
| 3   | Đạt          | Top-3 chứa Step 1, Step 2 và Step 3.                                             |
| 4   | Đạt          | Top-3 chứa `VND 16 billion` và `undergraduate`.                                  |
| 5   | Đạt          | Filtered top-3 đều thuộc regulation; unfiltered top-3 không lấy đúng regulation. |

**Tổng:** 4/5 câu có chunk liên quan và gold markers trong top-3.

Metadata filter giúp rõ rệt ở Query 5. Khi lọc theo `audience=student` và `category=scholarship-regulation`, kết quả tập trung đúng tài liệu quy định; khi bỏ filter, kết quả bị lẫn portal và application. Query 2 cho thấy đúng tài liệu chưa đủ nếu chunk không chứa chi tiết cần trả lời.

## 4. Bài học

- Local multilingual embedding tốt hơn mock embedding cho corpus Việt-Anh.
- Chunk theo heading giữ tốt các đơn vị ngữ nghĩa của văn bản quy định.
- Cần kết hợp semantic retrieval với keyword/gold-marker check cho câu hỏi số liệu và ngày tháng.

Nếu làm lại, nhóm sẽ chuẩn hóa toàn bộ tài liệu về UTF-8, bổ sung query expansion cho câu hỏi tiếng Việt và dùng metadata category cụ thể hơn.

## Tự đánh giá

| Tiêu chí             |      Điểm |
| -------------------- | --------: |
| Document Set Quality |      9/10 |
| Strategy Design      |     13/15 |
| Retrieval Quality    |      8/10 |
| Demo & lessons       |       4/5 |
| **Tổng**             | **34/40** |
