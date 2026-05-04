|---|---|---|
||**VIETTEL AI RACE**|Public 611|
||**QUY TRÌNH GIÁM SÁT, XỬ LÝ VÀ ỨNG CỨU SỰ CÓ ATTT**|Lần ban hành: 1|

**==> picture [37 x 36] intentionally omitted <==**

## **1. GIẢI THÍCH THUẬT NGỮ, ĐỊNH NGHĨA, KHÁI NIỆM** 

- Sự kiện an toàn thông tin (Information security event): Là sự việc xác định liên quan đến trạng thái của một hệ thống, dịch vụ hoặc trạng thái mạng nằm ngoài việc vận hành thông thường, cho thấy có khả năng vi phạm chính sách ATTT hay lỗi kiểm soát ATTT, hoặc một tình huống không lường trước liên quan đến ATTT. Không phải tất cả các sự kiện ATTT đều là sự cố ATTT. 

- Sự cố an toàn thông tin (Information security incidient): Là một hoặc một loạt các sự kiện ATTT không mong muốn hoặc không dự tính có khả năng ảnh hưởng đáng kể đến các hoạt động nghiệp vụ và đe dọa ATTT. 

- SOC (Security Operation Center): được giao nhiệm vụ giám sát, điều phối, ứng cứu, xử lý sự cố ATTT và đảm bảo ATTT cho Công ty. 

- Tier 1: bộ phận thuộc Phòng Vận hành dịch vụ số của Trung tâm Dịch vụ hạ tầng số/TT VHKT làm đầu mối chịu trách nhiệm thực hiện giám sát hệ thống. an 

- Tier 2: bộ phận trực SOC thuộc BU MSSP- Trung tâm Hợp tác kinh doanh làm đầu mối chịu trách nhiệm thực hiện tiếp nhận các ticket từ Tier 1, tiến hành xác minh, phối hợp với SO xử lý ticket. 

- Tier 3: bộ phận SOC thuộc BU MSSP- Trung tâm Hợp tác kinh doanh làm đầu mối thực hiện xử lý, trong trường hợp Tier 2 không thể xử lý được hoặc đã xử lý nhưng không thành công. Trường hợp Tier 3- Viettel IDC không thể xử lý thì chuyển lên SOC manager để tiếp tục xử lý. 

- SLA: thời gian xử lý cảnh báo 

- Ticket: Ticket sự cố ATTT được tạo và đưa lên hệ thống SOAR để điều phối luồng xử lý sự cố ATTT. 

- SOAR (Security Orchestration, Automation and Response): là giải pháp điều phối, tự động hóa phản ứng an ninh thông tin tập trung giúp xác định, ưu tiên và tiêu chuẩn hóa cho các chức năng ứng phó sự cố, lỗ hồng, vấn đề ATTT. 

- SOC manager: làm nhiệm vụ điều hành xử lý sự cố, phê duyệt yêu cầu về thời gian xử lý sự cố của SO (nếu có); phê duyệt yêu cầu hỗ trợ xử lý ticket của SO (nếu có) và đóng ticket. 

- Ban lãnh đạo: Ban lãnh đạo quản lý sự cố ATTT chịu trách nhiệm xác nhận hoặc phê duyệt kế hoạch ứng cứu sự cố ATTT ATTT và chủ trì xử lý sự cố ATTT nghiêm trọng. 

## **2. QUY TRÌNH XỬ LÝ SỰ CỐ** 

**==> picture [94 x 66] intentionally omitted <==**
**==> picture [745 x 510] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE  Public 611<br>QUY TRÌNH GIÁM SÁT, XỬ LÝ VÀ ỨNG CỨU SỰ CÓ ATTT  Lần ban hành: 1<br>Bước  Hoạt động  Mô tả chi tiết  Vai trò  Đầu vào  Đầu ra  Thời gian<br>thực hiện<br>1  Tiếp nhận và  1. Tiếp nhận thông tin cảnh báo về sự cố  Tier 1  - Dấu hiệu sự cố  Cảnh báo về  Ngay  khi<br>xác minh  ATTT từ:  ATTT được nhận  ATTT được  phát  hiện<br>thông tin  - Cảnh báo của các giải pháp ATTT: SIEM,  diện từ:  báo cáo  cảnh báo từ<br>cảnh báo về  - Email, điện thoại của Phòng/Ban, cá nhân  - Cảnh báo của các  các  nguồn<br>sự cố  phát hiện sự cố ATTT báo cho bộ phận  giải pháp ATTT  tương ứng<br>ATTT qua email: idc.attt@123com.vn; - Email, điện thoại<br>- Đe dọa Hungting, Pentest  của  các  Chi<br>2. Thực hiện xác minh thông tin cảnh báo:  nhánh, Phòng/ban<br>-<br>Cảnh báo đúng: Chuyển bước 2a. Phân  cá nhân phát hiện<br>loại, đánh giá mức độ  sự cố ATTT<br>- -<br>Cảnh báo sai: cảnh báo nhầm nghiệp vụ  Săn lùng mối đe<br>quản trị, nghiệp vụ đơn vị, tác động có kế  dọa, Pentest<br>hoạch... Chuyển bước 2b. Cập nhật trạng<br>thái cảnh báo REJECT-False Positive,<br>đóng case.<br>2a  Phân loại sự  Phân loại, đánh giá mức độ nguy hiểm của  Tier 1  Cảnh báo/thông báo  Cảnh  báo<br>cố ATTT  cảnh báo gồm 2 mức độ: nghiêm trọng và  ATTT được<br>thông thường (PL 01: Hướng dẫn phân loại  phân loại<br>mức độ sự cố ATTT).<br>Với các sự cố xử lý qua ticket trên hệ thống<br>SOAR thì thực hiện tiếp bước 3.<br>Với các sự cố cần thông báo cho SO xử lý<br>luôn thì liên hệ SO hệ thống theo Phụ lục 02.<br>Danh sách liên lạc ứng cứu sự cố ATTT và<br>**----- End of picture text -----**<br>

**==> picture [88 x 66] intentionally omitted <==**
**==> picture [745 x 510] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE  Public 611<br>QUY TRÌNH GIÁM SÁT, XỬ LÝ VÀ ỨNG CỨU SỰ CÓ ATTT  Lần ban hành: 1<br>thực hiện theo Quy trình quản lý và xử lý sự<br>cố<br>2b  Đóng  cảnh  Trường hợp là cảnh báo giả: Cập nhật trạng  Cảnh báo về sự cố  Cảnh  báo  Ngay sau khi<br>báo về sự cô  thái cảnh báo REJECT-False Positive, đóng  ATTT được đánh giá  được đóng  có kết quả<br>ATTT  cảnh báo trên hệ thống SOAR  không phải là sự cố  đánh  giá<br>cảnh báo<br>3  Tạo ra các sự  Tier 1 tạo case sự cố (Status = OPEN) trên  Tier 1  Case chưa được xử lý  Case  được  Ngay  sau<br>cố  SOAR Case sự sự cố được gán cho:  gán cho Tier  bước 2a<br>Tier 1 đối với case đã có hướng dẫn xử lý.  1<br>Chuyển bước 4b thực hiện nhiệm vụ Case<br>Management điều hành xử lý sự cố<br>Tier 2 đối với case sự cố chưa có hướng dẫn<br>xử lý (Bước 4a)<br>4a  Tier 2 tiếp  Tier 2 tiếp nhận case sự cố, trạng thái case là  Tier 2  Case chưa được xử lý  Case  được  Ngay  sau<br>nhận sự cố  OPEN.  gán cho Tier  bước 3<br>Thực hiện xác minh thông tin cảnh báo:  2<br>Cảnh báo sai chuyển bước 5 và cập nhật trạng<br>thái cảnh báo REJECT - False Positive, đóng<br>case.<br>Cảnh báo đúng:<br>+ Cảnh báo đã biết hướng xử lý chuyển sang<br>bước 4b thực hiện nhiệm vụ Case<br>Management điều hành xử lý.<br>Cảnh báo không xác minh được hướng xử lý<br>gán sự cố cho Tier 3 (bước 6)<br>**----- End of picture text -----**<br>

**==> picture [88 x 66] intentionally omitted <==**
**==> picture [745 x 510] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE  Public 611<br>QUY TRÌNH GIÁM SÁT, XỬ LÝ VÀ ỨNG CỨU SỰ CÓ ATTT  Lần ban hành: 1<br>4b  Case  Case Management thực hiện điều hành xử lý  Tier 1,   Ticket chưa được xử  Ticket  đã<br>Management  case:  Tier 2,   lý  được xử lý<br>điều hành xử<br>Tạo các ticket nghiệp vụ cho System  Tier 3<br>lý case  Owner/IT Admin<br>A Nêu Tier 1 hoặc Tier 2 thực hiện theo<br>hướng dẫn nhưng không xử lý thành công<br>hoặc xác định mức độ sự cố Nghiêm trọng,<br>chuyển case cho Tier 3 điều hành xử lý (Bước<br>6)<br>Nếu xử lý thành công: Đóng case. Trạng thái<br>Case là CLOSE.<br>Nếu cần xác minh nghiệp vụ cần tạo Ticket<br>cho SO/IT Admin<br>5  Cập  nhật  Cảnh báo sai chuyển bước 5 và cập nhật trạng  Tier 2  Cảnh báo sai  Đóng case<br>trạng thái  -thái cảnh báo REJECT – False Positive,<br>Reject  –  đóng case.<br>False<br>positive<br>6  Tier 3 tiếp  OPEN. Tier 3 tiếp nhận case sự cố, trạng thái  Tier 3  Case sự cố<br>nhận case  case là<br>Chuyển bước 4b thực hiện nhiệm vụ<br>CaseManagement điều hành xử lý sự cố.<br>7a  Xác  minh  SO/IT admin xác minh thông tin ticket nhận  SO,  IT  Ticket trên SOAR<br>thông  tin  được:  Admin<br>ticket  nhận<br>được<br>**----- End of picture text -----**<br>

**==> picture [88 x 66] intentionally omitted <==**
**==> picture [745 x 510] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE  Public 611<br>QUY TRÌNH GIÁM SÁT, XỬ LÝ VÀ ỨNG CỨU SỰ CÓ ATTT  Lần ban hành: 1<br>Nếu ticket gán đúng nghiệp vụ cho nhóm:<br>Cập nhật trạng thái ticket IN PROGRESS để<br>bắt đầu công việc (Bước 8a);<br>Nếu ticket gán sai: Cập nhật trạng thái ticket<br>AWAITING REASSIGNMENT để Case<br>Management thực hiện gán lại (Bước 8b).<br>7b  Đóng case  Đóng case khi tất cả các ticket điều hành đã  Case  Ticket trên SOAR  Ticket được  Ngay  sau<br>được xử lý xong.  management  xử lý  bước 2b<br>8a  Bắt đầu xử lý  Bắt đầu xử lý công việc theo chức năng,  SO,  IT  Ticket trên SOAR  Ticket được  Ngay  sau<br>công  việc  nghiệp vụ của nhóm A Nếu cần hỗ trợ từ Case  Admin  xử lý  bước 6<br>theo  chức  Management chuyển sang bước 9a;<br>năng, nghiệp  thêm thời gian để xử lý hoặc cần ngoại Nếu<br>vụ của nhóm  cần lệ cho ticket.<br>Cập nhật trạng thái A WAITING PENDING<br>(Bước b)<br>Xử lý xong ticket: Cập nhật thông tin xử lý<br>và trạng thái CLOSE cho ticket (Bước 9c).<br>8b  Case  Case Management thực hiện gán lại ticket có  Tier 1,   Ticket trên SOAR  Ticket được  Ngay  sau<br>Management  trạng thái AWATING REASSIGNMENT về  Tier 2,   cập  nhật  bước 6<br>tiếp  nhận  đúng nhóm, người xử lý. Cập nhật lại trạng  trạng thái<br>Tier 3<br>ticket  thái OPEN cho ticket.<br>9a  Tiếp nhận hỗ  Case Management xác minh yêu cầu hỗ trợ:  SOC  Ticket trên SOAR  Ticket được  Ngay  sau<br>trợ  Nếu yêu cầu hỗ trợ sai (hoặc đã có hướng  Manager  cập  nhật  bước 8a<br>dẫn, Case Management không có quyền) thì  trạng thái<br>từ chối hỗ trợ;<br>**----- End of picture text -----**<br>

**==> picture [88 x 66] intentionally omitted <==**
**==> picture [745 x 510] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE  Public 611<br>QUY TRÌNH GIÁM SÁT, XỬ LÝ VÀ ỨNG CỨU SỰ CÓ ATTT  Lần ban hành: 1<br>- Nếu yêu cầu hỗ trợ đúng (SO chưa có hướng<br>dẫn, không có quyền...) thì chuyển sang bước<br>4b cho Case Management tiếp tục điều hành<br>xử lý sự cố.<br>- Thông báo lại cho SO/IT Admin sau khi<br>hoàn thành yêu cầu hỗ trợ.<br>9b  Tiếp  nhận  Case Management xác minh yêu cầu hỗ trợ:  Tier 1,<br>ticket  -Nếu yêu cầu hỗ trợ sai (hoặc đã có hướng  Tier 2,<br>trạng thái  dẫn, Case Management không có quyền) thì  Tier 3<br>AWAITING  từ chối hỗ trợ;<br>PENDING<br>-Nếu yêu cầu hỗ trợ đúng (SO chưa có hướng<br>dẫn, không có quyền...) thì chuyển sang bước<br>4b cho Case Management tiếp tục điều hành<br>xử lý sự cố.<br>- Thông báo lại cho SO/IT Admin sau khi<br>hoàn thành yêu cầu hỗ trợ.<br>9c  Cập  nhật  Cập nhật thông tin xử lý và đóng ticket khi:  SO,  IT  Ticket trên SOAR  Ticket được  Ngay  sau<br>thông tin xử  Ticket sự vụ được xử lý thành công.  Admin  xử lý  bước 8a<br>lý ticket<br>TicKet trùng do đã nhận được ticket tương tự<br>trước đó và đã xử lý thành công.<br>Thông báo kêt quả cho Case Management<br>10  Đồng  ý  Đồng ý xét duyệt thêm thời gian xử lý ticket  Tier 1,   Ticket trên SOAR  Ticket  Ngay  sau<br>pending  hoặc ngoại lệ cho ticket. Trạng thái ticket  Tier 2,   pending  bước 9c<br>PENDING.<br>Tier 3<br>**----- End of picture text -----**<br>

**==> picture [88 x 66] intentionally omitted <==**
**==> picture [38 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 611 **QUY TRÌNH GIÁM SÁT, XỬ LÝ VÀ ỨNG CỨU SỰ CÓ ATTT** Lần ban hành: 1