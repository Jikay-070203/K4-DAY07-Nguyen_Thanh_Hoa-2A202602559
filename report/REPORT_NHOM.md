# Báo Cáo Nhóm — Lab 7: Embedding & Vector Store

**Nhóm:** [Tên nhóm]
**Thành viên:** [Họ tên từng thành viên]
**Ngày:** [Ngày nộp]

> **Nộp 1 bản / nhóm.** Phần cá nhân (hướng tiếp cận, kết quả riêng, dự đoán…) mỗi thành viên nộp riêng trong `REPORT_CANHAN.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần nhóm: 40** = Lựa chọn tài liệu (10) + Thiết kế chiến lược (15) + Chất lượng truy xuất (10) + Thuyết trình (5).

---

## 1. Lựa chọn tài liệu (Document Set Quality) — Nhóm (10 điểm)

### Chủ đề (Domain) & Lý Do Chọn

**Chủ đề:** [ví dụ: Customer support FAQ, Luật Việt Nam, công thức nấu ăn, ...]

**Tại sao nhóm chọn chủ đề này?**

> _Viết 2-3 câu:_

### Danh sách tài liệu (Data Inventory)

| #   | Tên tài liệu | Nguồn (Source URL) | Ngày lấy / Phiên bản | Số ký tự | Metadata đã gán |
| --- | ------------ | ------------------ | -------------------- | -------- | --------------- |
| 1   |              |                    |                      |          |                 |
| 2   |              |                    |                      |          |                 |
| 3   |              |                    |                      |          |                 |
| 4   |              |                    |                      |          |                 |
| 5   |              |                    |                      |          |                 |

**Danh sách kiểm tra quản trị dữ liệu (Data governance checklist):**

- [ ] Tập tài liệu (Corpus) chỉ chứa nguồn công khai/được phép dùng và không chứa dữ liệu cá nhân, thông tin đăng nhập hoặc tài liệu nội bộ.
- [ ] Mỗi tài liệu có `source_url`, `retrieved_at`, `document_version` (hoặc ngày hiệu lực) trong metadata.

### Cấu trúc Metadata (Metadata Schema)

| Trường metadata | Kiểu | Ví dụ giá trị | Tại sao hữu ích cho truy xuất (retrieval)? |
| --------------- | ---- | ------------- | ------------------------------------------ |
|                 |      |               |                                            |
|                 |      |               |                                            |

---

## 2. Thiết kế chiến lược (Strategy Design) — Nhóm (15 điểm)

> Mỗi thành viên thử **một chiến lược khác nhau** trên cùng bộ tài liệu; nhóm tổng hợp và so sánh ở đây.

### Phân tích đường cơ sở (Baseline Analysis)

Chạy `ChunkingStrategyComparator().compare()` trên 2-3 tài liệu:

| Tài liệu | Chiến lược (Strategy)            | Số lượng Chunk | Độ dài trung bình | Giữ được ngữ cảnh không? |
| -------- | -------------------------------- | -------------- | ----------------- | ------------------------ |
|          | FixedSizeChunker (`fixed_size`)  |                |                   |                          |
|          | SentenceChunker (`by_sentences`) |                |                   |                          |
|          | RecursiveChunker (`recursive`)   |                |                   |                          |

### Chiến lược của từng thành viên

> Mỗi thành viên điền một khối dưới đây (copy thêm nếu nhóm có nhiều hơn 3 người).

**Thành viên 1 — [Tên]**

- **Loại chiến lược:** [FixedSize / Sentence / Recursive / custom]
- **Mô tả & lý do chọn cho chủ đề này:** _(2-3 câu)_
- **Code snippet (nếu custom):**

```python
# Dán mã nguồn (implementation) vào đây
```

**Thành viên 2 — [Tên]**

- **Loại chiến lược:**
- **Mô tả & lý do chọn:**
- **Code snippet (nếu custom):**

**Thành viên 3 — [Tên]**

- **Loại chiến lược:**
- **Mô tả & lý do chọn:**
- **Code snippet (nếu custom):**

### So Sánh Giữa Các Thành Viên

| Thành viên | Chiến lược (Strategy) | Điểm truy xuất (/10) | Điểm mạnh | Điểm yếu |
| ---------- | --------------------- | -------------------- | --------- | -------- |
|            |                       |                      |           |          |
|            |                       |                      |           |          |
|            |                       |                      |           |          |

**Chiến lược nào tốt nhất cho chủ đề này? Tại sao?**

> _Viết 2-3 câu — đây là phần được đánh giá cao nhất (khả năng suy nghĩ & giải thích):_

---

## 3. Câu hỏi đánh giá & Chất lượng truy xuất (Retrieval Quality) — Nhóm (10 điểm)

### Câu hỏi đánh giá & Câu trả lời chuẩn (nhóm thống nhất)

> **Đúng 5 câu hỏi**, đa dạng, có thể kiểm chứng; **ít nhất 1 câu** cần lọc metadata mới trả lời tốt. Đây là bộ câu hỏi chung cho mọi thành viên chạy.

| #   | Câu hỏi                                                                                                             | Gold answer                                                                                                                                                                  | Tài liệu nguồn                         | Filter                    |
| --- | ------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------- |
| 1   | Học bổng Green Tech 2026 có bao nhiêu suất, giá trị bao nhiêu và kéo dài bao lâu?                                   | Có 4 suất học bổng, mỗi suất trị giá 18.000.000 VND trong 6 tháng.                                                                                                           | `usth-green-tech-scholarship-2026.md`  | Không                     |
| 2   | Hạn cuối nộp hồ sơ học bổng Green Tech 2026 là ngày nào và thời gian dự kiến bắt đầu là khi nào?                    | Hạn nộp hồ sơ là ngày 23/03/2026; thời gian dự kiến bắt đầu là tháng 04/2026.                                                                                                | `usth-green-tech-scholarship-2026.md`  | Không                     |
| 3   | Quy trình xét học bổng và hỗ trợ tài chính của USTH gồm những bước nào?                                             | Gồm 3 bước: tiếp nhận hồ sơ; lập danh sách và trình Hội đồng SFA để ra quyết định; công bố danh sách sinh viên nhận học bổng/hỗ trợ.                                         | `usth-scholarship-procedure.md`        | Không                     |
| 4   | Trong năm học 2026–2027, USTH dự kiến dành bao nhiêu tiền cho quỹ học bổng và áp dụng cho những nhóm người học nào? | USTH dự kiến dành 16 tỷ VND cho sinh viên đại học, học viên cao học và nghiên cứu sinh.                                                                                      | `usth-scholarship-application-2026.md` | Không                     |
| 5   | Đối tượng sinh viên nào được áp dụng các quy định học bổng năm 2026 của USTH?                                       | Sinh viên Việt Nam và sinh viên quốc tế đang theo học chương trình đào tạo chính quy; sinh viên trao đổi/thực tập theo MoU hoặc thỏa thuận hợp tác không thuộc quy định này. | `usth-scholarship-regulation-2026.md`  | `{"audience": "student"}` |

### Tổng hợp chất lượng truy xuất của nhóm

> Cách chấm (theo `docs/SCORING.md`): **2 điểm/câu** — top-3 chứa chunk liên quan + agent trả lời đúng (2), có liên quan nhưng thiếu/không ở top-1 (1), không có trong top-3 (0).

| #   | Câu hỏi | Chiến lược tốt nhất cho câu này | Có chunk liên quan trong top-3? | Ghi chú |
| --- | ------- | ------------------------------- | ------------------------------- | ------- |
| 1   |         |                                 |                                 |         |
| 2   |         |                                 |                                 |         |
| 3   |         |                                 |                                 |         |
| 4   |         |                                 |                                 |         |
| 5   |         |                                 |                                 |         |

**Lọc bằng metadata có giúp ích không? Ở câu hỏi nào?**

> _Viết 2-3 câu:_

---

## 4. Thuyết trình (Demo) & Bài học nhóm — Nhóm (5 điểm)

**Những phân tích (insights) hay nhất nhóm sẽ trình bày:**

> _Liệt kê 2-3 ý:_

**Bài học rút ra khi so sánh trong nhóm:**

> _Viết 2-3 câu — cùng tài liệu nhưng chiến lược khác nhau dẫn tới khác biệt gì?_

**Nếu làm lại, nhóm sẽ thay đổi gì trong chiến lược dữ liệu (data strategy)?**

> _Viết 2-3 câu:_

---

## Tự Đánh Giá (Phần Nhóm)

| Tiêu chí                                 | Điểm tự đánh giá |
| ---------------------------------------- | ---------------- |
| Lựa chọn tài liệu (Document Set Quality) | / 10             |
| Thiết kế chiến lược (Strategy Design)    | / 15             |
| Chất lượng truy xuất (Retrieval Quality) | / 10             |
| Thuyết trình (Demo)                      | / 5              |
| **Tổng phần nhóm**                       | **/ 40**         |
