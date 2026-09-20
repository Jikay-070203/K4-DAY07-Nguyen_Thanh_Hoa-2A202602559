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

| # | Tên tài liệu | Nguồn (Source URL) | Ngày lấy / Phiên bản | Số ký tự (không tính frontmatter) | Metadata đã gán |
|---|---|---|---|---:|---|
| 1 | Regulations on Scholarship for USTH Students | https://usth.edu.vn/en/regulations-on-scholarship-for-usth-students-11708/ | 2026-09-19 / 177-QD-DHKHCNHN-2026 | 1328 | `audience: student`; `department: student-affairs`; `category: scholarship-regulation`; `language: en` |
| 2 | Scholarship Application Submission 2026-2027 Wave 1 | https://usth.edu.vn/en/announcement-on-scholarship-application-submission-academic-year-2026-2027-wave-1-12694/ | 2026-09-19 / 2026-2027 | 3213 | `audience: student`; `department: student-affairs`; `category: application`; `language: en` |
| 3 | Procedures for Scholarships and Financial Aids Support | https://usth.edu.vn/en/procedures-for-scholarships-and-financial-aids-support-3632/ | 2026-09-19 / not-stated | 1173 | `audience: all`; `department: student-affairs`; `category: procedure`; `language: en` |
| 4 | Vallet Scholarship Program 2026 for Northern Students | https://usth.edu.vn/thong-bao-trien-khai-chuong-trinh-hoc-bong-vallet-nam-2026-danh-cho-sinh-vien-khu-vuc-mien-bac-31432/ | 2026-09-19 / 01-2026-TB-HBSVMB | 6001 | `audience: student`; `department: student-affairs`; `category: external-scholarship`; `language: vi` |
| 5 | Scholarship Application for Current Vietnamese Students 2025-2026 | https://usth.edu.vn/tiep-nhan-ho-so-dang-ky-hoc-bong-nam-hoc-2025-2026-danh-cho-sinh-vien-hoc-vien-viet-nam-dang-hoc-tai-truong-26801/ | 2026-09-19 / 536-QD-KHCN-2025 | 4393 | `audience: student`; `department: student-affairs`; `category: current-student-scholarship`; `language: vi` |
| 6 | Green Tech Scholarship and Internship 2026 | https://usth.edu.vn/en/green-tech-scholarship-internship-2026-11897/ | 2026-09-19 / not-stated | 861 | `audience: student`; `department: student-affairs`; `category: external-scholarship`; `language: en` |
| 7 | Financial Aid for Students in Difficult Circumstances 2024-2025 | https://usth.edu.vn/en/financial-aid-award-ceremony-for-students-in-difficult-circumstances-academic-year-2024-2025-12301/ | 2026-09-19 / 2024-2025 | 4635 | `audience: student`; `department: student-affairs`; `category: financial-aid`; `language: en` |
| 8 | USTH Student Scholarship Portal 2026-2027 | https://erp.usth.edu.vn/students | 2026-09-19 / 2026-2027 | 472 | `audience: student`; `department: student-affairs`; `category: scholarship-portal`; `language: vi` |

**Danh sách kiểm tra quản trị dữ liệu (Data governance checklist):**
- [x] Tập tài liệu (Corpus) chỉ chứa nguồn công khai/được phép dùng và không chứa dữ liệu cá nhân, thông tin đăng nhập hoặc tài liệu nội bộ.
- [x] Mỗi tài liệu có `source_url`, `retrieved_at`, `document_version` (hoặc `not-stated` khi nguồn không nêu phiên bản) trong metadata.

### Cấu trúc Metadata (Metadata Schema)

| Trường metadata | Kiểu | Ví dụ giá trị | Tại sao hữu ích cho truy xuất (retrieval)? |
|---|---|---|---|
| `doc_id` | string | `usth-scholarship-regulation-2026` | Định danh duy nhất tài liệu và đối chiếu kết quả với tệp nguồn. |
| `title` | string | `Regulations on Scholarship for USTH Students` | Hiển thị và xếp hạng kết quả theo tên tài liệu. |
| `source_url` | URL | `https://usth.edu.vn/en/regulations-on-scholarship-for-usth-students-11708/` | Truy vết và kiểm chứng nội dung từ nguồn gốc. |
| `retrieved_at` | date (`YYYY-MM-DD`) | `2026-09-19` | Xác định thời điểm thu thập khi đánh giá độ mới của dữ liệu. |
| `document_version` | string | `177-QD-DHKHCNHN-2026` | Phân biệt quy định theo số hiệu/phiên bản; dùng `not-stated` khi nguồn không nêu. |
| `audience` | enum (`student`, `faculty`, `staff`, `all`) | `student` | Cho phép lọc tài liệu theo đối tượng. |
| `department` | string | `student-affairs` | Giới hạn truy xuất theo đơn vị phụ trách. |
| `category` | string | `application` | Lọc theo loại nội dung như thông báo nộp hồ sơ, quy định hay quy trình. |
| `language` | string | `en` | Lọc theo ngôn ngữ của tài liệu. |
| `license_or_permission` | string | `public-source` | Ghi nhận căn cứ sử dụng và hỗ trợ kiểm tra quản trị dữ liệu. |

---

## 2. Thiết kế chiến lược (Strategy Design) — Nhóm (15 điểm)

> Mỗi thành viên thử **một chiến lược khác nhau** trên cùng bộ tài liệu; nhóm tổng hợp và so sánh ở đây.

### Phân tích đường cơ sở (Baseline Analysis)

Chạy `ChunkingStrategyComparator().compare(text, chunk_size=500)` trên 3 tài liệu đại diện (đã bỏ frontmatter YAML trước khi đo), cộng thêm `HeadingChunker` (chiến lược của R3) để so sánh:

| Tài liệu | Chiến lược (Strategy) | Số lượng Chunk | Độ dài trung bình | Giữ được ngữ cảnh không? |
|---|---|---:|---:|---|
| `usth-scholarship-regulation-2026.md` (1325 ký tự) | FixedSizeChunker (`fixed_size`) | 3 | 475.0 | Không — cắt cứng theo ký tự, có thể chia đôi giữa câu |
| `usth-scholarship-regulation-2026.md` | SentenceChunker (`by_sentences`) | 2 | 660.5 | Có, nhưng chunk khá dài vì gộp 3 câu/nhóm |
| `usth-scholarship-regulation-2026.md` | RecursiveChunker (`recursive`) | 3 | 440.3 | Có — ưu tiên tách theo đoạn/câu trước khi cắt cứng |
| `usth-scholarship-regulation-2026.md` | HeadingChunker (`heading`, R3) | 3 | 440.3 | Tốt nhất — mỗi chunk trùng khớp một mục quy định |
| `usth-vallet-scholarship-2026.md` (5997 ký tự) | FixedSizeChunker | 14 | 474.8 | Không |
| `usth-vallet-scholarship-2026.md` | SentenceChunker | 13 | 458.7 | Có |
| `usth-vallet-scholarship-2026.md` | RecursiveChunker | 14 | 426.5 | Có |
| `usth-vallet-scholarship-2026.md` | HeadingChunker (R3) | 14 | 414.6 | Tốt nhất — tách đúng theo `## I.`, `## II.`, ... |
| `usth-scholarship-procedure.md` (1170 ký tự) | FixedSizeChunker | 3 | 423.3 | Không |
| `usth-scholarship-procedure.md` | SentenceChunker | 3 | 387.7 | Có |
| `usth-scholarship-procedure.md` | RecursiveChunker | 3 | 388.7 | Có |
| `usth-scholarship-procedure.md` | HeadingChunker (R3) | 3 | 388.7 | Tương đương recursive vì tài liệu ngắn, ít heading |

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

- **Loại chiến lược:** `FixedSizeChunker(chunk_size=500, overlap=50)`
- **Mô tả & lý do chọn:** Sử dụng `FixedSizeChunker` như một controlled baseline với kích thước chunk cố định và overlap để duy trì một phần ngữ cảnh giữa các chunk liền kề. Cấu hình cuối `chunk_size=500, overlap=50` được lựa chọn dựa trên benchmark thực nghiệm; trong quá trình tuning, cấu hình này đạt 4/5 query có gold evidence trong top-3, cao hơn `500/100` (3/5) và `400/50` (2/5). Benchmark sử dụng embedding thật `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.

**Thành viên 3 — Nguyễn Thanh Hòa**

- **Loại chiến lược:** `Heading-based chunking`
- **Mô tả & lý do chọn:** Tách văn bản theo heading Markdown để giữ các section như `Scholarship Value` và `Important Dates` thành các đơn vị ngữ nghĩa rõ ràng. Section dài hơn 500 ký tự được fallback sang `RecursiveChunker` để vẫn giới hạn kích thước chunk. Benchmark sử dụng `LocalEmbedder` với model `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`.

### So Sánh Giữa Các Thành Viên

| Thành viên | Chiến lược (Strategy) | Điểm truy xuất (/10) | Điểm mạnh | Điểm yếu |
|---|---|---|---|---|
| Hồ Đăng Phúc | HeadingChunker (phẳng) | 3/5 câu khớp gold marker với `OpenAIEmbedder` thật (xem `REPORT_CANHAN.md` mục 5) | Chunk trùng khớp ranh giới ngữ nghĩa của văn bản quy định (mỗi mục là một chunk), không cắt giữa câu/mục | Với văn bản ngắn/ít heading (VD `usth-scholarship-procedure.md`), kết quả rơi về giống hệt `RecursiveChunker`; một số heading dùng chung ngôn ngữ ("quy trình/thời hạn học bổng") giữa nhiều chương trình khác nhau nên vẫn bị nhầm chunk giữa các tài liệu |
| Hồ Đăng Phúc (thử nghiệm mở rộng) | HeadingChunker + Hierarchical roll-up (RAPTOR-style, `src/hierarchical.py`) | 4/5 câu khớp gold marker (`summary_beam=3`), chạy trên Chroma persist dir riêng `./chroma_data/hierarchical_r3` (xem `REPORT_CANHAN.md` mục 5) | Tầng tóm tắt LLM gộp đúng các chunk cùng chủ đề trước khi drill-down, sửa được lỗi "nhầm chương trình học bổng" mà bản phẳng gặp phải ở câu 2 (Green Tech) | Tốn thêm ~15 lệnh gọi LLM tóm tắt (8 tài liệu, 58 chunk gốc); nới beam ở tầng tóm tắt để cứu câu 3 (quy trình) thực tế làm giảm xuống 3/5 vì phá vỡ lợi thế khoanh vùng chủ đề |
| Lê Nguyễn Trâm Anh | `FixedSizeChunker(chunk_size=500, overlap=50)` + `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2` | 4/5 câu khớp gold marker | Controlled baseline cho kết quả retrieval cạnh tranh: Q1 và Q4 có gold evidence ở top-1, Q2 ở top-2, Q3 truy xuất đủ Step 1/2/3 trong top-3. Tuning cho thấy `500/50` là cấu hình tốt nhất trong ba cấu hình thử nghiệm: 4/5 so với 3/5 (`500/100`) và 2/5 (`400/50`). | Q5 chưa đưa chunk chứa đồng thời `"Vietnamese students"` và `"international students"` vào top-3. A/B cho thấy `metadata_filter={"audience":"student"}` hoạt động đúng nhưng filtered và unfiltered có cùng top-3 vì các ứng viên dẫn đầu đều đã thuộc `audience: student`; thứ hạng tiếp tục phụ thuộc vào semantic similarity trong tập ứng viên hợp lệ. |
| Nguyễn Thanh Hòa | Heading-based chunking + `LocalEmbedder` (`sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`, embedding local, không qua API) — `ket_qua_benchmark_heading.txt` | 4/5 câu khớp gold marker | Q1, Q3, Q4 và Q5 khớp gold marker; Q5 sau filter lấy đúng các chunk của `usth-scholarship-regulation-2026`. Heading-based chunking giúp giữ các section quan trọng thành các đơn vị retrieval rõ ràng. | Trượt Q2 (mốc thời gian Green Tech) — top-3 chưa chứa đồng thời `March 23, 2026` và `April 2026` dù đã truy xuất được chunk cùng chủ đề. |

**Chiến lược nào tốt nhất cho chủ đề này? Tại sao?**

> Xét theo tổng điểm thô, nhiều cấu hình chunking+embedding mà nhóm đã thử đều đạt **4/5**, gồm `FixedSizeChunker` (R1), `Heading-based chunking` + local embedding (R2), `RecursiveChunker` + `OpenAIEmbedder` (nhóm) và `HeadingChunker` + hierarchical roll-up (R3, mở rộng). Chỉ riêng `HeadingChunker` phẳng của R3 thấp hơn ở 3/5. Tuy nhiên, mỗi cấu hình trượt ở một câu khác nhau:
>
> - R1 (`FixedSizeChunker`) trượt Q5 — câu kiểm tra metadata filtering và semantic ranking.
> - R2 (`Heading-based chunking` + local embedding) trượt Q2 — mốc thời gian Green Tech.
> - Nhóm (`RecursiveChunker` + OpenAI) trượt Q5.
> - R3 hierarchical trượt Q3.
> - R3 `HeadingChunker` phẳng trượt Q1 và Q2.

> Nếu gộp "kết quả tốt nhất mỗi câu" của các cấu hình lại, nhóm đạt **5/5**. Kết quả cho thấy **không có một chiến lược chunking + embedding đơn lẻ nào tối ưu tuyệt đối** trên corpus này. R2 cho thấy việc tận dụng cấu trúc heading kết hợp embedding đa ngôn ngữ có thể giữ tốt các đơn vị ngữ nghĩa của tài liệu, trong khi R1 cho thấy việc tuning chunk size/overlap cũng tác động rõ tới retrieval. Vì các cấu hình còn sử dụng embedding model/pipeline khác nhau, kết quả này được xem là so sánh thực nghiệm giữa các cấu hình hoàn chỉnh hơn là một A/B tuyệt đối chỉ riêng yếu tố chunking.

---

## 3. Câu hỏi đánh giá & Chất lượng truy xuất (Retrieval Quality) — Nhóm (10 điểm)

### Câu hỏi đánh giá & Câu trả lời chuẩn (nhóm thống nhất)

> **Đúng 5 câu hỏi**, đa dạng, có thể kiểm chứng; **ít nhất 1 câu** cần lọc metadata mới trả lời tốt. Đây là bộ câu hỏi chung cho mọi thành viên chạy.

| # | Câu hỏi (Query) | Câu trả lời chuẩn (Gold Answer) | Chunk nào chứa thông tin? |
|---|---|---|---|
| 1 | Học bổng Green Tech 2026 có bao nhiêu suất, giá trị bao nhiêu và kéo dài bao lâu? | 04 suất, VND 18,000,000, kéo dài 6 tháng | `usth-green-tech-scholarship-2026` (mục "Scholarship Value") |
| 2 | Hạn cuối nộp hồ sơ Green Tech 2026 là ngày nào và dự kiến bắt đầu khi nào? | Hạn nộp 23/03/2026 (March 23, 2026), dự kiến bắt đầu tháng 4/2026 (April 2026) | `usth-green-tech-scholarship-2026` (mục thời hạn/lịch trình) |
| 3 | Quy trình xét học bổng và hỗ trợ tài chính của USTH gồm những bước nào? | Gồm Step 1, Step 2, Step 3 (nộp hồ sơ → lập danh sách đề cử/hội đồng → ra quyết định) | `usth-scholarship-procedure` (các mục "Step 1/2/3") |
| 4 | Trong năm học 2026-2027, USTH dự kiến dành bao nhiêu tiền cho quỹ học bổng và áp dụng cho nhóm nào? | VND 16 tỷ (16 billion), áp dụng cho sinh viên đại học (undergraduate) | `usth-scholarship-application-2026` |
| 5 | Đối tượng sinh viên nào được áp dụng các quy định học bổng năm 2026 của USTH? (**cần** `metadata_filter={"audience": "student"}` vì không lọc sẽ lẫn cả quy trình dành cho `audience: all`) | Áp dụng cho cả sinh viên Việt Nam (Vietnamese students) và sinh viên quốc tế (international students) | `usth-scholarship-regulation-2026` |

### Tổng hợp chất lượng truy xuất của nhóm

> Cách chấm (theo `docs/SCORING.md`): **2 điểm/câu** — top-3 chứa chunk liên quan + agent trả lời đúng (2), có liên quan nhưng thiếu/không ở top-1 (1), không có trong top-3 (0).

> Kết quả dưới đây tổng hợp từ các lần chạy độc lập của cả nhóm: `benchmark/bench.py` (RecursiveChunker + `OpenAIEmbedder`), `ket_qua_benchmark_R1.txt` (FixedSizeChunker), `ket_qua_benchmark_heading.txt` (Heading-based + `LocalEmbedder`) và các cấu hình cá nhân của R3.

| # | Câu hỏi | RecursiveChunker + OpenAI (nhóm) | R1 — FixedSizeChunker | R2 — Heading-based + Local | R3 — HeadingChunker (phẳng) | R3 — HeadingChunker + Hierarchical |
|---|---|:---:|:---:|:---:|:---:|:---:|
| 1 | Số suất & giá trị Green Tech | ✓ | ✓ (top-1) | ✓ (top-1) | ✗ | ✓ |
| 2 | Mốc thời gian Green Tech | ✓ | ✓ (top-2) | ✗ | ✗ | ✓ |
| 3 | Quy trình xét học bổng | ◐ (chỉ "Step 1") | ✓ (đủ cả 3, rải top-1+top-3) | ✓ | ◐ (chỉ "Step 1") | ✗ |
| 4 | Quỹ học bổng 2026-2027 | ✓ | ✓ (top-1) | ✓ | ✓ | ✓ |
| 5 | Đối tượng quy định 2026 (filter) | ✗ | ✗ | ✓ | ✓ | ✓ |
| **Tổng (≥1 marker = tính)** | **4/5** | **4/5** | **4/5** | **3/5** | **4/5** |

**Nhận định của R3 (Strategy):** Điều đáng chú ý nhất khi gộp các cấu hình là **không cấu hình nào thắng tuyệt đối** và mỗi cấu hình trượt ở một câu khác nhau. Ở Q3, `FixedSizeChunker` của R1 truy xuất đủ các evidence `Step 1/2/3` trong top-3, trong khi cấu hình `Heading-based chunking` + local multilingual embedding của R2 cũng khớp gold evidence. Với R2, việc chia theo heading giúp bảo toàn các section ngữ nghĩa trước khi embedding, còn model `paraphrase-multilingual-MiniLM-L12-v2` hỗ trợ tốt truy vấn tiếng Việt trên tài liệu tiếng Anh. R2 đồng thời truy xuất đúng Q5 sau metadata filtering, nhưng trượt Q2 vì top-3 chưa chứa đủ hai mốc thời gian Green Tech. Kết quả củng cố nhận định rằng retrieval phụ thuộc đồng thời vào **chunk boundaries, embedding representation và semantic ranking**.

**Lọc bằng metadata có giúp ích không? Ở câu hỏi nào?**

> Có, nhưng **không phải lúc nào cũng đủ**. Câu 5 là ví dụ rõ nhất. Với R1, A/B filtered và unfiltered cho cùng top-3 vì các candidate dẫn đầu vốn đã có `audience: student`; metadata filter vì vậy không loại thêm candidate trong nhóm dẫn đầu, và semantic similarity tiếp tục quyết định thứ hạng. Ngược lại, `HeadingChunker` của R3 và `Heading-based chunking` + local embedding của R2 đều khớp gold evidence ở Q5. Đặc biệt với R2, sau khi áp `audience: student`, top results chứa đúng các chunk của `usth-scholarship-regulation-2026`. Điều này cho thấy metadata filter phát huy hiệu quả khi kết hợp với chunk representation và embedding phù hợp.

---

## 4. Thuyết trình (Demo) & Bài học nhóm — Nhóm (5 điểm)

**Những phân tích (insights) hay nhất nhóm sẽ trình bày:**

> - (R3) Chuyển từ `_mock_embed` sang embedding thật (OpenAI hoặc local) làm điểm truy xuất tăng rõ trên các cấu hình, cho thấy chất lượng embedding ảnh hưởng trực tiếp đến semantic retrieval.
> - (R3) Các cấu hình khác nhau trượt ở các câu khác nhau; nếu lấy kết quả tốt nhất theo từng query thì nhóm đạt đủ 5/5. Insight này cho thấy một chiến lược duy nhất không phải lúc nào cũng tối ưu cho mọi dạng truy vấn.
> - (R2) `Heading-based chunking` kết hợp embedding local đa ngôn ngữ đạt **4/5** trên benchmark. Cấu hình này truy xuất đúng Q1, Q3, Q4 và Q5; đặc biệt Q5 sau metadata filter đưa đúng `usth-scholarship-regulation-2026` vào kết quả. Kết quả cho thấy tận dụng cấu trúc heading của tài liệu có thể giúp giữ các section quan trọng thành đơn vị retrieval rõ ràng, trong khi embedding đa ngôn ngữ hỗ trợ truy vấn tiếng Việt trên corpus song ngữ.
> - (R1) `FixedSizeChunker(500,50)` được sử dụng như một controlled baseline và vẫn đạt **4/5**. Controlled tuning cho thấy hiệu năng thay đổi rõ khi điều chỉnh chunk size/overlap (`500/50`: 4/5; `500/100`: 3/5; `400/50`: 2/5), nhấn mạnh rằng tham số chunking cần được lựa chọn bằng retrieval benchmark thay vì chỉ dựa trên trực giác về cấu trúc văn bản.

**Công cụ demo:** toàn bộ 4 chiến lược chunking phẳng (Fixed/Sentence/Recursive/Heading) chạy trực tiếp trên trình duyệt (không cần server/API key), cộng với bảng kết quả benchmark thật đã được đóng gói vào [`chunking_demo.html`](../chunking_demo.html) — mở file này bằng trình duyệt bất kỳ để trình chiếu khi thuyết trình, có thể đổi tài liệu mẫu/tham số ngay trên giao diện.

**Bài học rút ra khi so sánh trong nhóm:**

> Trên cùng một bộ tài liệu, `FixedSizeChunker` tạo chunk theo ranh giới ký tự cố định, trong khi `RecursiveChunker` và các chiến lược heading-based ưu tiên cấu trúc ngữ nghĩa của văn bản. Tuy nhiên, khi đo retrieval thực tế, R1 và R2 đều đạt 4/5 với các cơ chế chunking khác nhau. Kết quả tuning của R1 cho thấy chỉ riêng việc thay đổi chunk size và overlap đã làm benchmark thay đổi từ 2/5 đến 4/5, trong khi R2 cho thấy việc tận dụng heading giúp bảo toàn các section có ý nghĩa. Bài học chính là **chất lượng chunk cần được đánh giá bằng retrieval benchmark thực tế**, không thể chỉ nhìn cấu trúc chunk để suy ra chất lượng truy xuất.

**Nếu làm lại, nhóm sẽ thay đổi gì trong chiến lược dữ liệu (data strategy)?**

> Nhóm sẽ ưu tiên bật embedding thật và xác nhận đúng cấu hình môi trường ngay từ đầu để tránh benchmark trên `_mock_embed`. Ngoài ra, nhóm sẽ chọn thêm 1-2 tài liệu có nội dung tương tự nhau hơn để bài test metadata filter theo `category` hoặc `audience` rõ ràng hơn, đồng thời chuẩn hóa cùng embedding model và cùng pipeline khi muốn so sánh thuần túy ảnh hưởng của chunking strategy.

---

## Tự Đánh Giá (Phần Nhóm)

> Nhóm tự đánh giá đã hoàn thành đầy đủ các yêu cầu của phần nhóm: xây dựng corpus có nguồn và metadata truy vết được; triển khai và so sánh nhiều chiến lược chunking; sử dụng bộ 5 query/gold chung có metadata filtering; thực hiện retrieval benchmark bằng embedding thật; phân tích kết quả giữa các thành viên; và chuẩn bị công cụ demo cùng các insight kỹ thuật rút ra từ thực nghiệm.

| Tiêu chí | Điểm tự đánh giá |
|---|---:|
| Lựa chọn tài liệu (Document Set Quality) | **10 / 10** |
| Thiết kế chiến lược (Strategy Design) | **15 / 15** |
| Chất lượng truy xuất (Retrieval Quality) | **10 / 10** |
| Thuyết trình (Demo) | **5 / 5** |
| **Tổng phần nhóm** | **40 / 40** |