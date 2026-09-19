# Báo Cáo Nhóm — Lab 7: Embedding & Vector Store

**Nhóm:** AuraFarming
**Thành viên:** Hồ Đăng Phúc, Lê Nguyễn Trâm Anh, Nguyễn Thanh Hòa
**Ngày:** 19/09/2026

> **Nộp 1 bản / nhóm.** Phần cá nhân (hướng tiếp cận, kết quả riêng, dự đoán…) mỗi thành viên nộp riêng trong `REPORT_CANHAN.md`. Chi tiết thang điểm: `docs/SCORING.md`.

**Tổng điểm phần nhóm: 40** = Lựa chọn tài liệu (10) + Thiết kế chiến lược (15) + Chất lượng truy xuất (10) + Thuyết trình (5).

---

## 1. Lựa chọn tài liệu (Document Set Quality) — Nhóm (10 điểm)

### Chủ đề (Domain) & Lý Do Chọn

**Chủ đề:** Học bổng và hỗ trợ tài chính dành cho người học tại Trường Đại học Khoa học và Công nghệ Hà Nội (USTH).

**Tại sao nhóm chọn chủ đề này?**

> Bộ tài liệu tập hợp các quy định, tiêu chí, giá trị, hồ sơ, quy trình và thời hạn học bổng từ các nguồn công khai của USTH. Phạm vi này phù hợp để xây dựng hệ thống truy xuất vì người học thường cần đối chiếu thông tin cụ thể giữa nhiều loại học bổng và năm học khác nhau.

**Mô tả corpus:** Corpus gồm đúng 8 tài liệu Markdown: 5 tài liệu tiếng Anh và 3 tài liệu tiếng Việt, được lấy ngày 2026-09-19. Nội dung bao phủ quy định chung, thông báo nộp hồ sơ, quy trình, học bổng Vallet, học bổng cho sinh viên hiện tại, chương trình Green Tech, hỗ trợ tài chính và các đợt đang hiển thị trên cổng học bổng. Nguồn tuyển sinh tiến sĩ bị chặn bởi `robots.txt` không được đưa vào corpus.

### Danh sách tài liệu (Data Inventory)

| #   | Tên tài liệu                                                      | Nguồn (Source URL)                                                                                                                     | Ngày lấy / Phiên bản              | Số ký tự (không tính frontmatter) | Metadata đã gán                                                                                             |
| --- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------- | --------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| 1   | Regulations on Scholarship for USTH Students                      | https://usth.edu.vn/en/regulations-on-scholarship-for-usth-students-11708/                                                             | 2026-09-19 / 177-QD-DHKHCNHN-2026 | 1328                              | `audience: student`; `department: student-affairs`; `category: scholarship-regulation`; `language: en`      |
| 2   | Scholarship Application Submission 2026-2027 Wave 1               | https://usth.edu.vn/en/announcement-on-scholarship-application-submission-academic-year-2026-2027-wave-1-12694/                        | 2026-09-19 / 2026-2027            | 3213                              | `audience: student`; `department: student-affairs`; `category: application`; `language: en`                 |
| 3   | Procedures for Scholarships and Financial Aids Support            | https://usth.edu.vn/en/procedures-for-scholarships-and-financial-aids-support-3632/                                                    | 2026-09-19 / not-stated           | 1173                              | `audience: all`; `department: student-affairs`; `category: procedure`; `language: en`                       |
| 4   | Vallet Scholarship Program 2026 for Northern Students             | https://usth.edu.vn/thong-bao-trien-khai-chuong-trinh-hoc-bong-vallet-nam-2026-danh-cho-sinh-vien-khu-vuc-mien-bac-31432/              | 2026-09-19 / 01-2026-TB-HBSVMB    | 6001                              | `audience: student`; `department: student-affairs`; `category: external-scholarship`; `language: vi`        |
| 5   | Scholarship Application for Current Vietnamese Students 2025-2026 | https://usth.edu.vn/tiep-nhan-ho-so-dang-ky-hoc-bong-nam-hoc-2025-2026-danh-cho-sinh-vien-hoc-vien-viet-nam-dang-hoc-tai-truong-26801/ | 2026-09-19 / 536-QD-KHCN-2025     | 4393                              | `audience: student`; `department: student-affairs`; `category: current-student-scholarship`; `language: vi` |
| 6   | Green Tech Scholarship and Internship 2026                        | https://usth.edu.vn/en/green-tech-scholarship-internship-2026-11897/                                                                   | 2026-09-19 / not-stated           | 861                               | `audience: student`; `department: student-affairs`; `category: external-scholarship`; `language: en`        |
| 7   | Financial Aid for Students in Difficult Circumstances 2024-2025   | https://usth.edu.vn/en/financial-aid-award-ceremony-for-students-in-difficult-circumstances-academic-year-2024-2025-12301/             | 2026-09-19 / 2024-2025            | 4635                              | `audience: student`; `department: student-affairs`; `category: financial-aid`; `language: en`               |
| 8   | USTH Student Scholarship Portal 2026-2027                         | https://erp.usth.edu.vn/students                                                                                                       | 2026-09-19 / 2026-2027            | 472                               | `audience: student`; `department: student-affairs`; `category: scholarship-portal`; `language: vi`          |

**Danh sách kiểm tra quản trị dữ liệu (Data governance checklist):**

- [x] Tập tài liệu (Corpus) chỉ chứa nguồn công khai/được phép dùng và không chứa dữ liệu cá nhân, thông tin đăng nhập hoặc tài liệu nội bộ.
- [x] Mỗi tài liệu có `source_url`, `retrieved_at`, `document_version` (hoặc `not-stated` khi nguồn không nêu phiên bản) trong metadata.

### Cấu trúc Metadata (Metadata Schema)

| Trường metadata         | Kiểu                                        | Ví dụ giá trị                                                                | Tại sao hữu ích cho truy xuất (retrieval)?                                        |
| ----------------------- | ------------------------------------------- | ---------------------------------------------------------------------------- | --------------------------------------------------------------------------------- |
| `doc_id`                | string                                      | `usth-scholarship-regulation-2026`                                           | Định danh duy nhất tài liệu và đối chiếu kết quả với tệp nguồn.                   |
| `title`                 | string                                      | `Regulations on Scholarship for USTH Students`                               | Hiển thị và xếp hạng kết quả theo tên tài liệu.                                   |
| `source_url`            | URL                                         | `https://usth.edu.vn/en/regulations-on-scholarship-for-usth-students-11708/` | Truy vết và kiểm chứng nội dung từ nguồn gốc.                                     |
| `retrieved_at`          | date (`YYYY-MM-DD`)                         | `2026-09-19`                                                                 | Xác định thời điểm thu thập khi đánh giá độ mới của dữ liệu.                      |
| `document_version`      | string                                      | `177-QD-DHKHCNHN-2026`                                                       | Phân biệt quy định theo số hiệu/phiên bản; dùng `not-stated` khi nguồn không nêu. |
| `audience`              | enum (`student`, `faculty`, `staff`, `all`) | `student`                                                                    | Cho phép lọc tài liệu theo đối tượng.                                             |
| `department`            | string                                      | `student-affairs`                                                            | Giới hạn truy xuất theo đơn vị phụ trách.                                         |
| `category`              | string                                      | `application`                                                                | Lọc theo loại nội dung như thông báo nộp hồ sơ, quy định hay quy trình.           |
| `language`              | string                                      | `en`                                                                         | Lọc theo ngôn ngữ của tài liệu.                                                   |
| `license_or_permission` | string                                      | `public-source`                                                              | Ghi nhận căn cứ sử dụng và hỗ trợ kiểm tra quản trị dữ liệu.                      |

---

## 2. Thiết kế chiến lược (Strategy Design) — Nhóm (15 điểm)

> Mỗi thành viên thử **một chiến lược khác nhau** trên cùng bộ tài liệu; nhóm tổng hợp và so sánh ở đây.

### Phân tích đường cơ sở (Baseline Analysis)

Chạy `ChunkingStrategyComparator().compare(text, chunk_size=500)` trên 3 tài liệu đại diện (đã bỏ frontmatter YAML trước khi đo), cộng thêm `HeadingChunker` (chiến lược của R3) để so sánh:

| Tài liệu                                           | Chiến lược (Strategy)            | Số lượng Chunk | Độ dài trung bình | Giữ được ngữ cảnh không?                              |
| -------------------------------------------------- | -------------------------------- | -------------- | ----------------- | ----------------------------------------------------- |
| `usth-scholarship-regulation-2026.md` (1325 ký tự) | FixedSizeChunker (`fixed_size`)  | 3              | 475.0             | Không — cắt cứng theo ký tự, có thể chia đôi giữa câu |
| `usth-scholarship-regulation-2026.md`              | SentenceChunker (`by_sentences`) | 2              | 660.5             | Có, nhưng chunk khá dài vì gộp 3 câu/nhóm             |
| `usth-scholarship-regulation-2026.md`              | RecursiveChunker (`recursive`)   | 3              | 440.3             | Có — ưu tiên tách theo đoạn/câu trước khi cắt cứng    |
| `usth-scholarship-regulation-2026.md`              | HeadingChunker (`heading`, R3)   | 3              | 440.3             | Tốt nhất — mỗi chunk trùng khớp một mục quy định      |
| `usth-vallet-scholarship-2026.md` (5997 ký tự)     | FixedSizeChunker                 | 14             | 474.8             | Không                                                 |
| `usth-vallet-scholarship-2026.md`                  | SentenceChunker                  | 13             | 458.7             | Có                                                    |
| `usth-vallet-scholarship-2026.md`                  | RecursiveChunker                 | 14             | 426.5             | Có                                                    |
| `usth-vallet-scholarship-2026.md`                  | HeadingChunker (R3)              | 14             | 414.6             | Tốt nhất — tách đúng theo `## I.`, `## II.`, ...      |
| `usth-scholarship-procedure.md` (1170 ký tự)       | FixedSizeChunker                 | 3              | 423.3             | Không                                                 |
| `usth-scholarship-procedure.md`                    | SentenceChunker                  | 3              | 387.7             | Có                                                    |
| `usth-scholarship-procedure.md`                    | RecursiveChunker                 | 3              | 388.7             | Có                                                    |
| `usth-scholarship-procedure.md`                    | HeadingChunker (R3)              | 3              | 388.7             | Tương đương recursive vì tài liệu ngắn, ít heading    |

### Chiến lược của từng thành viên

> Mỗi thành viên điền một khối dưới đây (copy thêm nếu nhóm có nhiều hơn 3 người).

**Thành viên 1 — Hồ Đăng Phúc (R3 · Strategy)**

- **Loại chiến lược:** custom — `HeadingChunker` (chunk theo heading Markdown)
- **Mô tả & lý do chọn cho chủ đề này:** Các tài liệu học bổng USTH đều được biên soạn theo mục (`## I. Thông Tin Chung`, `## II. Đối Tượng...`), mỗi mục là một đơn vị ngữ nghĩa trọn vẹn do người soạn chia sẵn. Thay vì cắt cứng theo số ký tự hay số câu, `HeadingChunker` tách văn bản tại từng dòng heading rồi hạ các mục quá dài xuống `RecursiveChunker`, giữ nguyên heading ở đầu mỗi mảnh con để không chunk nào mất ngữ cảnh "đang thuộc mục nào" (ví dụ mục V "Phương Pháp Thẩm Định" của Vallet dài hơn 500 ký tự vẫn giữ được tiêu đề khi bị chia nhỏ tiếp).
- **Code snippet (nếu custom):**

```python
class HeadingChunker:
    HEADING_RE = re.compile(r"^#{2,3}\s+.+$", re.MULTILINE)

    def chunk(self, text: str) -> list[str]:
        headings = list(self.HEADING_RE.finditer(text))
        if len(headings) < 2:
            return RecursiveChunker(chunk_size=self.chunk_size).chunk(text)
        # tách theo từng heading -> section; section dài quá chunk_size
        # được hạ xuống RecursiveChunker, heading được lặp lại ở mỗi mảnh con
        ...
```

**Thành viên 2 — Lê Nguyễn Trâm Anh**

- **Loại chiến lược: FixedSizeChunker**
- **Mô tả & lý do chọn: Là hình thức chunking đơn giản, cắt văn bản theo số lượng ký tự cố định. Có thể làm nhanh và hiệu quả.**

**Thành viên 3 — Nguyễn Thanh Hòa**

- **Loại chiến lược: Heading-based chunking**
- **Mô tả & lý do chọn: Tách văn bản theo heading Markdown để giữ các section như Scholarship Value và Important Dates thành các đơn vị ngữ nghĩa rõ ràng. Section dài hơn 500 ký tự được fallback sang RecursiveChunker để vẫn giới hạn kích thước chunk.**

### So Sánh Giữa Các Thành Viên

| Thành viên                        | Chiến lược (Strategy)                                                                                                                                                                                         | Điểm truy xuất (/10)                                                                                                                           | Điểm mạnh                                                                                                                                                                                                                                                           | Điểm yếu                                                                                                                                                                                                                                                                                            |
| --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Hồ Đăng Phúc                      | HeadingChunker (phẳng)                                                                                                                                                                                        | 3/5 câu khớp gold marker với `OpenAIEmbedder` thật (xem `REPORT_CANHAN.md` mục 5)                                                              | Chunk trùng khớp ranh giới ngữ nghĩa của văn bản quy định (mỗi mục là một chunk), không cắt giữa câu/mục                                                                                                                                                            | Với văn bản ngắn/ít heading (VD `usth-scholarship-procedure.md`), kết quả rơi về giống hệt `RecursiveChunker`; một số heading dùng chung ngôn ngữ ("quy trình/thời hạn học bổng") giữa nhiều chương trình khác nhau nên vẫn bị nhầm chunk giữa các tài liệu                                         |
| Hồ Đăng Phúc (thử nghiệm mở rộng) | HeadingChunker + Hierarchical roll-up (RAPTOR-style, `src/hierarchical.py`)                                                                                                                                   | 4/5 câu khớp gold marker (`summary_beam=3`), chạy trên Chroma persist dir riêng `./chroma_data/hierarchical_r3` (xem `REPORT_CANHAN.md` mục 5) | Tầng tóm tắt LLM gộp đúng các chunk cùng chủ đề trước khi drill-down, sửa được lỗi "nhầm chương trình học bổng" mà bản phẳng gặp phải ở câu 2 (Green Tech)                                                                                                          | Tốn thêm ~15 lệnh gọi LLM tóm tắt (8 tài liệu, 58 chunk gốc); nới beam ở tầng tóm tắt để cứu câu 3 (quy trình) thực tế làm **giảm** xuống 3/5 vì phá vỡ lợi thế "khoanh vùng chủ đề" — xác nhận đây là đánh đổi recall/precision thật, không phải bug đơn giản có thể sửa một chiều                 |
| Lê Nguyễn Trâm Anh                | FixedSizeChunker (`chunk_size=500, overlap=0`) — xác định lại từ `ket_qua_benchmark_R1.txt` bằng cách khớp đúng ranh giới cắt ký tự (R3 chạy lại cùng tham số ra đúng cùng vị trí cắt "…flexible hybrid: on") | 4/5 câu khớp gold marker                                                                                                                       | Q1 và Q4 khớp ngay ở top-1 (điểm rất cao, 0.80/0.71) vì cắt cứng theo 500 ký tự vô tình giữ trọn số liệu quan trọng trong 1 chunk; Q3 (quy trình) khớp đủ cả 3 "Step 1/2/3" nhờ ranh giới cắt tình cờ giữ "Step 1"+"Step 2" trong chunk#0 và "Step 3" trong chunk#1 | Trượt Q5 (câu cần `metadata_filter=audience:student`) — top-3 dù đã lọc đúng vẫn không đưa `usth-scholarship-regulation-2026` (chứa "Vietnamese/international students") lên đủ cao, vì cắt cứng không theo mục nên câu quan trọng bị pha loãng trong chunk dài chứa nhiều nội dung không liên quan |
| Nguyễn Thanh Hòa                  | Heading-based chunking + `LocalEmbedder` (`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, embedding **local**, không qua API) — `ket_qua_benchmark_heading.txt`                | 4/5 câu khớp gold marker                                                                                                                       | Q1, Q3, Q4 và Q5 khớp gold marker; Q5 sau filter lấy đúng các chunk của `usth-scholarship-regulation-2026`                                                                                                          | Trượt Q2 (mốc thời gian Green Tech) — `Gold markers found in top-3: []`, top-3 không chứa `March 23, 2026`/`April 2026` dù truy xuất được chunk cùng chủ đề |

**Chiến lược nào tốt nhất cho chủ đề này? Tại sao?**

> Xét theo tổng điểm thô, 4 trong 5 cấu hình chunking+embedding mà nhóm đã thử đều dừng ở **4/5**: `FixedSizeChunker` (R1), `RecursiveChunker` + local embedding (R2), `RecursiveChunker` + `OpenAIEmbedder` (nhóm, `benchmark/bench.py`), và `HeadingChunker` + hierarchical roll-up (R3, mở rộng) — chỉ riêng `HeadingChunker` phẳng (R3) thấp hơn ở 3/5. Nhưng con số tổng này che giấu một phát hiện quan trọng hơn: **mỗi cấu hình trượt ở một câu khác nhau**:
>
> - R1 (FixedSizeChunker) trượt Q5 — câu cần lọc metadata.
> - R2 (RecursiveChunker + local embedding) trượt Q2 — mốc thời gian Green Tech.
> - Nhóm (RecursiveChunker + OpenAI) trượt Q5 — giống R1.
> - R3 hierarchical trượt Q3 — quy trình xét học bổng.
> - R3 HeadingChunker phẳng trượt cả Q1 và Q2.
>
> Nếu gộp "kết quả tốt nhất mỗi câu" của cả 4 cấu hình lại, nhóm đạt **5/5** (Q1: R1/R2/nhóm/R3-hier đều đúng; Q2: R1 đúng; Q3: R2 đúng đủ cả 3 marker; Q4: mọi cấu hình đều đúng; Q5: R2 đúng). Điều này cho thấy **không có một chiến lược chunking + embedding đơn lẻ nào là tối ưu tuyệt đối** trên corpus này — độ ngẫu nhiên của ranh giới cắt (FixedSizeChunker cắt đúng chỗ giữ trọn "Step 1/2/3" là may mắn hơn là thiết kế) và lựa chọn embedding (local đa ngôn ngữ hiểu tốt câu hỏi tiếng Việt hơn cho Q3 dù văn bản gốc tiếng Anh) đóng vai trò lớn ngang với — thậm chí hơn — bản thân chiến lược chunk. Trong bối cảnh phải chọn một chiến lược duy nhất để triển khai, `RecursiveChunker` là lựa chọn an toàn nhất (không phụ thuộc cấu trúc heading có sẵn hay không, hoạt động ổn định 4/5 với cả 2 loại embedding đã thử), còn `HeadingChunker` nên đi kèm hierarchical roll-up nếu ngân sách cho phép gọi thêm LLM.

---

## 3. Câu hỏi đánh giá & Chất lượng truy xuất (Retrieval Quality) — Nhóm (10 điểm)

### Câu hỏi đánh giá & Câu trả lời chuẩn (nhóm thống nhất)

> **Đúng 5 câu hỏi**, đa dạng, có thể kiểm chứng; **ít nhất 1 câu** cần lọc metadata mới trả lời tốt. Đây là bộ câu hỏi chung cho mọi thành viên chạy.

| #   | Câu hỏi (Query)                                                                                                                                                                             | Câu trả lời chuẩn (Gold Answer)                                                                       | Chunk nào chứa thông tin?                                    |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| 1   | Học bổng Green Tech 2026 có bao nhiêu suất, giá trị bao nhiêu và kéo dài bao lâu?                                                                                                           | 04 suất, VND 18,000,000, kéo dài 6 tháng                                                              | `usth-green-tech-scholarship-2026` (mục "Scholarship Value") |
| 2   | Hạn cuối nộp hồ sơ Green Tech 2026 là ngày nào và dự kiến bắt đầu khi nào?                                                                                                                  | Hạn nộp 23/03/2026 (March 23, 2026), dự kiến bắt đầu tháng 4/2026 (April 2026)                        | `usth-green-tech-scholarship-2026` (mục thời hạn/lịch trình) |
| 3   | Quy trình xét học bổng và hỗ trợ tài chính của USTH gồm những bước nào?                                                                                                                     | Gồm Step 1, Step 2, Step 3 (nộp hồ sơ → lập danh sách đề cử/hội đồng → ra quyết định)                 | `usth-scholarship-procedure` (các mục "Step 1/2/3")          |
| 4   | Trong năm học 2026-2027, USTH dự kiến dành bao nhiêu tiền cho quỹ học bổng và áp dụng cho nhóm nào?                                                                                         | VND 16 tỷ (16 billion), áp dụng cho sinh viên đại học (undergraduate)                                 | `usth-scholarship-application-2026`                          |
| 5   | Đối tượng sinh viên nào được áp dụng các quy định học bổng năm 2026 của USTH? (**cần** `metadata_filter={"audience": "student"}` vì không lọc sẽ lẫn cả quy trình dành cho `audience: all`) | Áp dụng cho cả sinh viên Việt Nam (Vietnamese students) và sinh viên quốc tế (international students) | `usth-scholarship-regulation-2026`                           |

### Tổng hợp chất lượng truy xuất của nhóm

> Cách chấm (theo `docs/SCORING.md`): **2 điểm/câu** — top-3 chứa chunk liên quan + agent trả lời đúng (2), có liên quan nhưng thiếu/không ở top-1 (1), không có trong top-3 (0).

> Kết quả dưới đây tổng hợp từ 5 lần chạy độc lập của cả nhóm: `benchmark/bench.py` (RecursiveChunker + `OpenAIEmbedder`, sau khi sửa lỗi khai báo `.env` — `EMBEDDING_PROVIDER` thay vì `EMBEDDING_PROVIDER_ENV`, khiến trước đó mọi script âm thầm rơi về `_mock_embed`), `ket_qua_benchmark_R1.txt` (FixedSizeChunker), `ket_qua_benchmark_R2.txt` (RecursiveChunker + `LocalEmbedder` đa ngôn ngữ), và 2 cấu hình cá nhân của R3 (`REPORT_CANHAN.md` mục 5).

| #                           | Câu hỏi                          | RecursiveChunker + OpenAI (nhóm) |    R1 — FixedSizeChunker     | R2 — Heading-based + Local | R3 — HeadingChunker (phẳng) | R3 — HeadingChunker + Hierarchical |
| --------------------------- | -------------------------------- | :------------------------------: | :--------------------------: | :---------------------------: | :-------------------------: | :--------------------------------: |
| 1                           | Số suất & giá trị Green Tech     |                ✓                 |          ✓ (top-1)           |           ✓ (top-1)           |              ✗              |                 ✓                  |
| 2                           | Mốc thời gian Green Tech         |                ✓                 |          ✓ (top-2)           |               ✗               |              ✗              |                 ✓                  |
| 3                           | Quy trình xét học bổng           |         ◐ (chỉ "Step 1")         | ✓ (đủ cả 3, rải top-1+top-3) | ✓ (đủ cả 3, ngay top-1+top-2) |      ◐ (chỉ "Step 1")       |                 ✗                  |
| 4                           | Quỹ học bổng 2026-2027           |                ✓                 |          ✓ (top-1)           |               ✓               |              ✓              |                 ✓                  |
| 5                           | Đối tượng quy định 2026 (filter) |                ✗                 |              ✗               |               ✓               |              ✓              |                 ✓                  |
| **Tổng (≥1 marker = tính)** | **4/5**                          |             **4/5**              |           **4/5**            |            **4/5**            |           **4/5**           |

**Nhận định của R3 (Strategy):** Điều bất ngờ nhất khi gộp cả 5 cấu hình là **không cấu hình nào thắng tuyệt đối** và **mỗi cấu hình trượt một câu khác nhau** (xem phân tích đầy đủ ở mục 2 "Chiến lược nào tốt nhất"). Đáng chú ý nhất là Q3 (quy trình): `FixedSizeChunker` (R1) khớp đủ cả 3 "Step 1/2/3" **nhờ may mắn** — ranh giới cắt cứng 500 ký tự tình cờ giữ "Step 1"+"Step 2" trong cùng 1 chunk và "Step 3" trong chunk kế — trong khi cả `RecursiveChunker` (OpenAI) lẫn `HeadingChunker` (R3) của nhóm chỉ khớp được 1/3 marker cho câu này. Ngược lại, `RecursiveChunker` + embedding local đa ngôn ngữ (R2) khớp Q3 đủ cả 3 marker một cách "có chủ đích" hơn (nhờ model hiểu tốt câu hỏi tiếng Việt đối chiếu văn bản tiếng Anh), đồng thời cũng là cấu hình duy nhất thắng cả Q3 và Q5. Kết luận: **embedding model** vẫn là yếu tố quyết định lớn nhất so với `_mock_embed` (mọi cấu hình đều nhảy từ ~1/5 lên 3-4/5), nhưng ở mức fine-grained hơn, **sự tình cờ của ranh giới chunk** cũng ảnh hưởng đáng kể tới câu nào lọt top-3 — một chunk "may mắn" gộp đúng 2 mốc thông tin có thể thắng một chunk "đúng thiết kế" nhưng chia tách chúng ra 2 nơi.

**Lọc bằng metadata có giúp ích không? Ở câu hỏi nào?**

> Có, nhưng **không phải lúc nào cũng đủ** — bằng chứng rõ nhất là câu 5 lại chính là câu duy nhất mà 2/4 cấu hình trượt (`RecursiveChunker` + OpenAI của nhóm, và `FixedSizeChunker` của R1) **dù cả hai đều đã áp filter `audience: student`** đúng cơ chế. So sánh A/B (filter vs. không filter) trong `benchmark/bench.py` xác nhận `search_with_filter` lọc đúng — loại bỏ `audience: all`/`PhD` trước khi tính điểm — nhưng lọc metadata chỉ thu hẹp _tập ứng viên_, không đảm bảo _tài liệu đúng_ sẽ có điểm cosine cao nhất trong tập còn lại: với R1, `usth-scholarship-regulation-2026` (chứa "Vietnamese/international students") vẫn xếp dưới các tài liệu `audience: student` khác vì FixedSizeChunker chia câu quan trọng vào một chunk dài chứa nhiều nội dung không liên quan, làm loãng tín hiệu. Ngược lại, `HeadingChunker` (R3) và `RecursiveChunker` + embedding local (R2) đều khớp đủ 2 gold marker ở câu này — cho thấy filter metadata phát huy tác dụng tốt nhất khi kết hợp với chunk giữ nguyên vẹn đoạn văn chứa thông tin cần tìm, chứ bản thân filter không tự sửa được một chunk "loãng".

---

## 4. Thuyết trình (Demo) & Bài học nhóm — Nhóm (5 điểm)

**Những phân tích (insights) hay nhất nhóm sẽ trình bày:**

> - (R3) Chuyển từ `_mock_embed` sang embedding thật (OpenAI hoặc local) làm điểm truy xuất nhảy vọt trên mọi cấu hình: từ ~1/5 câu khớp gold marker lên 3-4/5, chứng minh bằng số liệu rằng chất lượng embedding quan trọng hơn nhiều so với lựa chọn chiến lược chunking trên corpus này.
> - (R3) Gộp 5 cấu hình chunking+embedding khác nhau mà nhóm đã thử (bench.py, R1, R2, HeadingChunker phẳng, HeadingChunker+hierarchical), **mỗi cấu hình trượt một câu khác nhau** và không cấu hình nào đạt 5/5 — nếu lấy kết quả tốt nhất mỗi câu thì nhóm mới đạt 5/5. Đây là insight mạnh nhất để trình bày: chọn một chiến lược "thắng chung cuộc" là không đủ, hệ thống RAG thực tế nên cân nhắc ensemble (chạy song song nhiều chiến lược, hợp nhất kết quả) thay vì chỉ tin vào một cấu hình.
> - (R2) Câu 3 (quy trình) là câu duy nhất một `RecursiveChunker` + embedding **local đa ngôn ngữ** khớp đủ cả 3 gold marker "Step 1/2/3" ngay từ top-2, cho thấy với câu hỏi tiếng Việt tra cứu nội dung tiếng Anh, một model embedding được huấn luyện đa ngôn ngữ tốt đôi khi thắng cả `text-embedding-3-small` của OpenAI.
> - (R1) `FixedSizeChunker` — chiến lược "ngây thơ" nhất — vẫn đạt 4/5, ngang với các chiến lược phức tạp hơn, nhưng vì lý do khác hẳn: ranh giới cắt 500 ký tự tình cờ giữ đúng các cụm thông tin quan trọng trong cùng 1 chunk ở 2/5 câu. Đây là lời nhắc rằng benchmark trên corpus nhỏ (8 tài liệu) có thể lẫn yếu tố may rủi, không nên kết luận vội "chiến lược X luôn tốt hơn Y" chỉ từ một lần chạy.

**Công cụ demo:** toàn bộ 4 chiến lược chunking phẳng (Fixed/Sentence/Recursive/Heading) chạy trực tiếp trên trình duyệt (không cần server/API key), cộng với bảng kết quả benchmark thật (RecursiveChunker vs. HeadingChunker vs. Hierarchical roll-up) đã được đóng gói vào [`chunking_demo.html`](../chunking_demo.html) — mở file này bằng trình duyệt bất kỳ để trình chiếu khi thuyết trình, có thể đổi tài liệu mẫu/tham số ngay trên giao diện.

**Bài học rút ra khi so sánh trong nhóm:**

> Trên cùng một bộ tài liệu, `FixedSizeChunker` luôn cho nhiều chunk nhất và dễ cắt ngang câu/mục nhất về mặt _cấu trúc_ (thấy rõ khi demo trực tiếp trên `chunking_demo.html`), trong khi `RecursiveChunker` và `HeadingChunker` giữ ngữ cảnh tốt hơn hẳn — nhưng bất ngờ là khi đo _retrieval_ thật (bảng mục 3), `FixedSizeChunker` (R1) vẫn đạt 4/5, ngang với các chiến lược "sạch" hơn. Bài học lớn nhất, sau khi so đủ 5 cấu hình của cả nhóm: **chất lượng chunk (nhìn bằng mắt) không tỷ lệ thuận với điểm retrieval** — một `FixedSizeChunker` cắt "xấu" vẫn có thể vô tình nhốt đúng 2 mốc thông tin cần thiết vào 1 chunk, trong khi một `HeadingChunker` cắt "đẹp" theo đúng mục vẫn có thể tách chúng ra 2 mục khác nhau khiến câu hỏi cần cả hai bị trượt. Kết luận thực dụng: **đánh giá chunking phải dựa trên retrieval benchmark thật**, không thể chỉ nhìn cấu trúc chunk để suy ra chất lượng.

**Nếu làm lại, nhóm sẽ thay đổi gì trong chiến lược dữ liệu (data strategy)?**

> Nhóm sẽ ưu tiên bật embedding thật (`OpenAIEmbedder`) và chốt đúng tên biến `.env` (`EMBEDDING_PROVIDER`, không phải `EMBEDDING_PROVIDER_ENV`) ngay từ đầu, thay vì để cả nhóm benchmark hàng chục lượt trên `_mock_embed` mà không biết mọi script đang âm thầm rơi về giả lập — đây là lỗi tốn nhiều thời gian nhất trong cả quá trình. Ngoài ra, nếu làm lại sẽ chọn thêm 1-2 tài liệu có nội dung tương tự nhau hơn (nhiều chương trình học bổng cùng nói "quy trình"/"thời hạn" bằng ngôn ngữ gần giống nhau) để bài test filter theo `category`/`audience` rõ ràng hơn, thay vì để corpus quá đa dạng chủ đề khiến một số câu hỏi (như Q3 "quy trình") khó phân biệt do tài liệu đúng quá ngắn và ít từ khoá trùng với câu hỏi.

---

## Tự Đánh Giá (Phần Nhóm)

> Điểm dưới đây là tự đánh giá tạm thời của R3 dựa trên phần đã hoàn thành (lựa chọn tài liệu, baseline, chiến lược HeadingChunker/hierarchical, benchmark, GUI demo); cần R1/R2/Report Lead xác nhận lại trước khi nộp vì bảng "So sánh giữa các thành viên" và một số insight demo vẫn còn dòng để trống chờ điền.

| Tiêu chí                                 | Điểm tự đánh giá |
| ---------------------------------------- | ---------------- |
| Lựa chọn tài liệu (Document Set Quality) | 9 / 10           |
| Thiết kế chiến lược (Strategy Design)    | 13 / 15          |
| Chất lượng truy xuất (Retrieval Quality) | 8 / 10           |
| Thuyết trình (Demo)                      | 4 / 5            |
| **Tổng phần nhóm**                       | **34 / 40**      |
