**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD300|
|---|---|---|
||**Nghiệm thu hợp đồng thuê ngoài**|Lần ban hành: 1|

## **1. GIỚI THIỆU** 

## **1.1 Mục đích** 

VTP bổ sung đối tượng bưu tá thuê ngoài vào đội ngũ giao nhận để đảm bảo đủ nguồn lực vận hành → Phát triển chính sách lương khoán riêng cho đối tượng này → Hệ thống tính lương khoán cần điều chỉnh để đáp ứng việc tính lương cho những đối tượng bưu tá khác nhau. 

## **1.2 Phạm vi** 

Hệ thống SCS, FICO 

## **1.3 Danh mục khái niệm, từ viết tắt** 

## **1.4 Tài liệu liên quan** 

|**1.4 **|**Tài liệu liênquan**|||
|---|---|---|---|
|**#**|**Tài liệu**|**Người tạo**|**Ngày cập nhật**|
|1|Phụ lục lỗi|NhungPAC|22/03/2024|
|2|Phụ lục phân quyền|NhungPAC|22/03/2024|
|3|QLNVVP-2393 Tính lương cho bưu tá thuê ngoài (Bản chốt)|NhungPAC|15/11/2023|

## **1.5 Tóm tắt tài liệu** 

## **2. ĐẶC TẢ YÊU CẦU** 

## **2.1 Yêu cầu chức năng** 

## **2.1.1 Đặc tả use case:** 

|---|---|---|---|---|
|**#**|**Nhóm**|**UCID**|**Use Case**|**Priority**|
|1|Kỳ lương|UC1.1|Tra cứu kỳ lương|High|
**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD300|
|---|---|---|
||**Nghiệm thu hợp đồng thuê ngoài**|Lần ban hành: 1|

|---|---|---|---|---|
|||UC1.2|Tạo kỳ lương|High|
|||UC1.3|Chỉnh sửa kỳ lương|Low|
|||UC1.4|Xóa kỳ lương|Low|
|2|Dữ liệu đầu vào|UC2.1|Lấy dữ liệu đầu vào|High|
|||UC2.2|Xuất dữ liệu đầu vào|Medium|
|3|Bảng chi|UC3.1|Tra cứu bảng chi|High|
|||UC3.2|Tạo bảng chi|High|
|||UC3.3|Chỉnh sửa bảng chi|Low|
|||UC3.4|Xóa bảng chi|Low|
|||UC3.5|Yêu cầu chi|High|
|4|Biên bản|UC4.1|Tổng hợp biên bản|High|
|||UC4.2|Xem danh sách biên bản|High|
|||UC4.3|Loại/Bỏ loại biên bản|High|
|||UC4.5|Theo dõi tiến độ chi lương|Low|
||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD300|
|---|---|---|---|
||**Nghiệm thu hợp đồng thuê ngoài**||Lần ban hành: 1|
|_2.1.1.1. Kỳ lương:_<br>_2.1.1.2. _**_UC1.1 - Tra cứu kỳ lương_**||||
|**Use Case**||Tra cứu kỳ lương||
|**Use Case ID**||UC1.1||
|**Description**||Cho phép người dùng tìm kiếm danh sách các kỳ lương đã tạo theo bộ lọc tự thiết lập để sử dụng.||
|**Actor(s)**||SCS, TTVH, TCLĐ||
|**Priority**||High||
|**Trigger**||Người dùng truy cập vào SCS → Hợp đồng thuê khoán → Quản lý kỳ lương.||
|**Pre-Condition(s)**||•<br>Người dùng đăng nhập thành công vào web SCS.<br>•<br>Người dùng đang ở màn hình SCS → Hợp đồng thuê khoán||
|**Post-Condition(s)**||Người dùng chọn thành công 1 kỳ lương để sử dụng.||
||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD300|
|---|---|---|---|
||**Nghiệm thu hợp đồng thuê ngoài**||Lần ban hành: 1|
|**Main Flow**||(1) SCS hiển thị giao diện tra cứu kỳ lương và thiết lập bộ lọc mặc định.<br>(2) SCS tìm kiếm theo bộ lọc đã thiết lập.<br>(3) Yes - Tìm kiếm thành công.<br>(4) SCS hiển thị kết quả tìm kiếm.<br>(5) Yes - Kết quả tìm kiếm có bao gồm kỳ lương người dùng muốn sử dụng.<br>(6) Người dùng chọn kỳ lương và chọn button "Sử dụng".<br>(7) Hệ thống đóng giao diện tra cứu + fill tên kỳ lương muốn sử dụng vào mục kỳ lương tại trang chủ Hợp đồng thuê<br>khoán.<br>Use Case hoàn thành.||
|**Alternative Flow**||(5) No - Kết quả tìm kiếm KHÔNG bao gồm kỳ lương người dùng muốn sử dụng.<br>(8) Người dùng thiết lập bộ lọc và chọn tìm kiếm.<br>Use Case tiếp tục ở bước (2).||
|**Exception Flow**||(3) No - Tìm kiếm thất bại.<br>(6) Hệ thống báo lỗi tương ứng, tham chiếu phụ lục lỗi.<br>Use Case kết thúc.||
**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD300|
|---|---|---|
||**Nghiệm thu hợp đồng thuê ngoài**|Lần ban hành: 1|

## **1. Người dùng có thể thiết lập bộ lọc bao gồm:** 

   - 1.1. Mã hoặc tên chu kỳ: 

      - Không bắt buộc 

      - Nhập chuỗi tối đa 100 ký tự 

      - • Tự động loại bỏ khoảng trắng ở đầu chuỗi nhập trước khi tìm kiếm. 

      - Thỏa mãn chuối đã nhập trùng với ít nhất 1 ký tự với tên hoặc mã của kỳ lương (không phân biệt có dấu/ không dấu, hoa thường). 

- Chuỗi nhập trống (Mặc định) → Luôn thỏa mãn. 

- 1.2. Thời gian • Bắt buộc 

- • 0 ngày ≤ Ngày kết thúc - Ngày bắt đầu ≤ 365 ngày 

- **Business rule** • Mặc định: Ngày hiện tại trừ 365 ngày → Ngày hiện tại. 

- • Thỏa mãn khi Ngày bắt đầu kỳ lọc ≤ Ngày kết thúc của kỳ ≤ Ngày kết thúc kỳ lọc 

- 1.3 Loại chu kỳ 

      - Không bắt buộc 

      - • Chọn 1 hoặc nhiều trong danh sách: Tuần; Tháng 

      - • Không chọn (Mặc định) → Luôn thỏa mãn. 

   2. Mỗi kỳ lấy ra các thông tin sau: Tên kỳ lương; Mã kỳ lương; Tên loại kỳ lương; Ngày bắt đầu kỳ lương (dd/MM/yyyy); Ngày kết thúc kỳ lương (dd/MM/yyyy); Người cập nhật kỳ lương gần nhất (Họ và tên + username); Thời gian cập nhật kỳ lương gần nhất (HH:MM dd/MM/yyyy); Kỳ hiện tại (Có/Không?) 

   **3. Người dùng có thể trích xuất dữ liệu tra cứu dưới định dạng .xlsx theo template sau:** Danh+sách+kỳ+lương+thuê+khoán.xlsx **4. Phân quyền (Tham chiếu phụ lục phân quyền).** 

## _2.1.1.3._ _**UC1.2 Tạo kỳ lương**_ 

|---|---|
|**Use Case**|Tạo kỳ lương|
|**Use Case ID**|UC1.2|
||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD300|
|---|---|---|---|
||**Nghiệm thu hợp đồng thuê ngoài**||Lần ban hành: 1|
|**Description**||Cho phép người dùng tạo mới 1 kỳ lương.||
|**Actor(s)**||SCS, TCLĐ, TTVH||
|**Priority**||High||
|**Trigger**||Tại pop up quản lý kỳ lương, người dùng chọn "Thêm mới"||
|**Pre-Condition(s)**||Người dùng đăng nhập thành công vào web SCS.||
|**Post-Condition(s)**||Thông tin kỳ lương mới được lưu thành công vào CSDL.||
|**Main Flow**||(1) Hệ thống hiển thị biểu mẫu dưới dạng 1 tab cho người dùng nhập thông tin kỳ lương.<br>(2) Người dùng nhập thông tin.<br>(3) Yes - Người dùng chọn "Ghi lại".<br>(4) Hệ thống kiểm tra điều kiện hợp lệ của dữ liệu.<br>(5) Yes - Thông tin đã nhập là hợp lệ.<br>(7) Yes - Hệ thống tạo mới chu kỳ tính lương và lưu vào CSDL thành công.<br>(8) Hệ thống thông báo cho người dùng rằng chu kỳ tính lương đã được thêm thành công + đóng tab Thêm mới.<br>_Use case hoàn thành._||
||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD300|
|---|---|---|---|
||**Nghiệm thu hợp đồng thuê ngoài**||Lần ban hành: 1|
|**Alternative Flow**||(3) No - Người dùng đóng form nhập.<br>(9) Yes - Đang nhập dở ít nhất 1 trường thông tin.<br>(10) Hệ thống yêu cầu người dùng xác nhận hủy thông tin đang nhập dở.<br>(11) No - Người dùng hủy yêu cầu đóng form.<br>_Use Case quay lại bước (2)_<br>(5) No - Thông tin đã nhập không hợp lệ.<br>(12) Hệ thống trả ra lỗi tuong ứng cho phép người dùng điều chỉnh thông tin đã nhập. (Tham chiếu phụ lục lỗi)<br>_Use Case quay lại bước (3)_||
|**Exception Flow**||(9) No - Không có trường nào đang nhập dở<br>(13) Đóng form nhập.<br>Use Case kết thúc<br>(11) Yes - Người dùng hủy yêu cầu đóng form.<br>(13) Đóng form nhập.<br>Use Case kết thúc<br>(7) No - Lưu vào CSDL thất bại.<br>(13) Hệ thông trả ra lỗi tương ứng, yêu cầu người dùng thử lại sau. (Tham chiếu phụ lục lỗi)<br>_Use Case kết thúc._||
**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD300|
|---|---|---|
||**Nghiệm thu hợp đồng thuê ngoài**|Lần ban hành: 1|

|**Business rule**|**Business rule**||
|---|---|---|
||**Business rule**|1. Quy tắc nhập thông tin kỳ lương.<br>•<br>Mã kỳ lương:<br>`o` Bắt buộc<br>`o` Là duy nhất (không kể các kỳ đã xóa)<br>`o` Chỉ chứa chữ cái và số (không bao gồm khoảng trắng, chữ có dấu và các ký tự đặc biệt)<br>`o` Tối thiểu 3 ký tự, tối đa 20 ký tự.<br>`o` Tự động loại bỏ khoảng trắng ở đầu và cuối chuỗi nhập trước khi lưu vào CSDL.<br>•<br>Tên kỳ lương<br>`o` Bắt buộc<br>`o` Tối thiểu 3 ký tự, tối đa 100 ký tự.<br>`o` Tự động loại bỏ khoảng trắng ở đầu và cuối chuối nhập trước khi lưu vào CSDL.<br>•<br>Loại kỳ lương<br>`o` Bắt buộc<br>`o` Chọn 1 trong danh sách: Tuần & Tháng<br>•<br>Thời gian kỳ lương<br>`o` Bắt buộc<br>`o` 0 ngày ≤ Ngày kết thúc - Ngày bắt đầu ≤ 31 ngày<br>`o` Các kỳ cùng loại thì thời gian không được giao nhau.<br>•<br>Kỳ hiện tại<br>`o` Bắt buộc<br>`o` Chọn 1 trong danh sách: Là kỳ hiện tại / Không là kỳ hiện tại<br>`o` Tại 1 thời điểm, hệ thống chỉ cho phép 01 kỳ là kỳ hiện tại.<br>2. Phân quyền: (Tham chiếu phụ lục phân quyền).|