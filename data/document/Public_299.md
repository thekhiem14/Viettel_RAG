**VIETTEL AI RACE** TD299 **ĐĂNG KÝ TUYỂN DỤNG TRÊN WEB DÀNH CHO BƯU TÁ** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

## **1. Tổng quan** 

## **1.1 Mục đích tài liệu** 

- Tài liệu này được xây dựng nhằm mục đích mô tả thiết kế các chức năng đáp ứng yêu cầu nghiệp vụ đăng ký tuyển dụng cho bưu tá, nhân viên lái xe trên website: viettelpost.com.vn 

## **1.2 Phạm vi** 

- Luồng nghiệp vụ được áp dụng cho chức năng đăng ký tuyển dụng trên web: https://viettelpost.com.vn/ 

## **1.3 Thuật ngữ và chữ viết tắt** 

|**Thuật ngữ/Từ viết tắt**|**Định nghĩa**|
|---|---|
|VTP|ViettelPost|
|KH|Khách hàng|

## **1.4 Danh mục chức năng** 

|---|---|---|---|
|**STT**|**UC**|**Ứng dụng**|**Chức năng**|
|1|UC01|App/Web<br>ViettelPost|Xây dựng chức năng đăng ký tuyển dụng trên<br>Website cho đối tượng bưu tá|
|2|UC02|Quản lý nhân sự|Báo cáo nhu cầu tuyển dụng|

## **2. THIẾT KẾ CHỨC NĂNG** 

## **2.1 Mô tả chung** 

|**2.1 Mô tả chung**||
|---|---|
||Cho phép người dùng đăng ký tuyển dụng trên website:<br>https://viettelpost.com.vn/|
|**Description**||
||Người dùng, VTP, Hệ thống quản lý nhân sự|
|**Actor(s)**||
||Người dùng vào web: https://viettelpost.com.vn/|
|**Pre-**<br>**Condition(s)**||
||Người dùng click vào ứng tuyển nhanh trên website:<br>https://viettelpost.com.vn/|
|**Trigger**||
||1.  Người dùng vào web: https://viettelpost.com.vn/|
|**Main flow**||
||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD299|
|---|---|---|---|
||**ĐĂNG KÝ TUYỂN DỤNG TRÊN WEB**<br>**DÀNH CHO BƯU TÁ**||Lần ban hành: 1|
|||2. Chọn ứng tuyển nhanh<br>3. Nhập thông tin ứng tuyển<br>4. Click Đăng ký<br>5. Hiển thị popup đăng ký thành công||
|||1. Người dùng đăng ký thông tin ứng tuyển thành công<br>2. Dữ liệu người dùng đăng ký đẩy về hệ thống tuyển dụng||
|**Post-**<br>**Condition(s)**||||

## **2.2 Mô tả nghiệp vụ** 

|---|---|---|---|---|
|**Bước**|**Nghiệp vụ**|**Hệ thống**|**Đối**<br>**tượng**|**Mô tả**|
|1|Vào web<br>viettelpost.co<br>m.vn|VTP|Người<br>dùng|Người dùng vào web<br>viettelpost.com.vn > Chọn ứng<br>tuyển giao hàng|
|2|Nhập thông<br>tin|VTP|Người<br>dùng|Người dùng nhập thông tin Họ và<br>tên, Năm sinh, Số điện thoại trên<br>màn tuyển dụng|
|3|Chọn vị trí<br>ứng tuyển|VTP|Người<br>dùng|Chọn 1 trong 3 vị trí ứng tuyển:<br>Nhân viên bưu tá, Nhân viên khai<br>thác, Tài xế xe tải|
|4|Chọn khu<br>vực ứng<br>tuyển: Tỉnh|VTP|Người<br>dùng|Người dùng chọn khu vực ứng<br>tuyển: Tỉnh|
|5|Lấy dữ liệu<br>chi nhánh từ<br>Hệ thống<br>quản lý nhân<br>sự|VTP|Hệ<br>thống|VTP lấy dữ liệu chi nhánh từ Hệ<br>thống quản lý nhân sự:|
|6|Trả ra dữ<br>liệu chi<br>nhánh|Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hệ thống quản lý nhân sự trả dữ<br>liệu chi nhánh cho VTP<br>Dữ liệu chi nhánh: Toàn bộ Chi<br>nhánh bưu chính Viettel|
|||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD299|
|---|---|---|---|---|---|---|
|||**ĐĂNG KÝ TUYỂN DỤNG TRÊN WEB**<br>**DÀNH CHO BƯU TÁ**||||Lần ban hành: 1|
||||||||
|7|Hiển thị dữ<br>liệu chi<br>nhánh||VTP|Hệ<br>thống|Hiển thị dữ liệu tỉnh từ Hệ thống<br>quản lý nhân sự trả về||
|8|Chọn khu<br>vực ứng<br>tuyển: Bưu<br>cục||VTP|Người<br>dùng|Người dùng chọn khu vực ứng<br>tuyển: Bưu cục||
|9|Lấy dữ liệu<br>bưu cục từ<br>Hệ thống<br>quản lý nhân<br>sự||VTP|Hệ<br>thống|VTP lấy dữ liệu bưu cục từ Hệ<br>thống quản lý nhân sự||
|10|Trả ra dữ<br>liệu bưu cục||Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hệ thống quản lý nhân sự trả dữ<br>liệu bưu cục cho VTP<br>Dữ liệu bưu cục: Bưu cục, Kho<br>vùng||
|11|Hiển thị dữ<br>liệu bưu cục||VTP|Hệ<br>thống|Hiển thị dữ liệu bưu cục từ Hệ<br>thống quản lý nhân sự trả về||
|12|Đăng ký||VTP|Người<br>dùng|Người dùng click đăng ký ở trên<br>web viettelpost.com.vn||
|13|Đẩy dữ liệu<br>về Hệ thống<br>quản lý nhân<br>sự||VTP|Hệ<br>thống|Đẩy dữ liệu đăng ký ứng tuyển về<br>Hệ thống quản lý nhân sự||
|14|Lưu dữ liệu<br>ứng viên||Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hệ thống Hệ thống quản lý nhân<br>sự lưu dữ liệu ứng viên<br>_(Trong vòng 7 ngày: Cùng thông_<br>_tin cá nhân, cùng vị trí ứng tuyển,_<br>_cùng khu vực ứng tuyển, cùng_<br>_trạng thái chưa xử lý hồ sơ =>_||
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD299|
|---|---|---|
||**ĐĂNG KÝ TUYỂN DỤNG TRÊN WEB**<br>**DÀNH CHO BƯU TÁ**|Lần ban hành: 1|

|---|---|---|---|---|
|||||_Không tiếp nhận hồ sơ có cùng_<br>_thông tin tương tự)_|
|15|Hiển thị<br>danh sách<br>ứng viên|Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hiển thị danh sách hồ sơ ứng viên<br>được đẩy về từ VTP kèm các<br>trạng thái:<br>•<br>Tạo mới<br>•<br>Đang xử lý<br>•<br>Đạt<br>•<br>Không đạt|
|16|Cập nhật<br>trạng thái hồ<br>sơ ứng viên|Hệ thống<br>quản lý nhân<br>sự|Người<br>dùng|Người dùng cập nhật trạng thái hồ<br>sơ ứng viên, chuyển trạng thái hồ<br>sơ trên danh sách ứng viên|
|17|Trả kết quả<br>ứng tuyển<br>qua SMS/<br>Mocha|Hệ thống<br>quản lý nhân<br>sự|Hệ<br>thống|Hệ thống gửi thông báo về tiến<br>trình xử lý hồ sơ:<br>•<br>Đang xử lý: Hồ sơ đã được<br>tiếp nhận<br>•<br>Đạt: Hồ sơ ứng tuyển đạt<br>yêu cầu, bộ phận tuyển<br>dụng thực hiện quy trình<br>tuyển dụng thủ công<br>•<br>Không đạt: Hồ sơ bị từ<br>chối, người dùng có thể<br>ứng tuyển lại|

## **2.3 Mô tả màn hình** 

|**STT**|**Thông**<br>**tin**|**Kiểu**<br>**control**|**Bắt**<br>**buộc**|**Mặc**<br>**định**|**Mô tả**|
|---|---|---|---|---|---|
|**Vào web viettelpost.com.vn > Chọn ứng tuyển giao hàng > Điều hướng về màn ứng**<br>**tuyển nhanh**||||||
|**Thông tin cá nhân**||||||
|1|Họ và<br>tên|Textbox|Có|Hint<br>text:|Cho phép nhập họ và tên<br>**Message:**|
||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD299|
|---|---|---|---|---|---|---|---|
||||**ĐĂNG KÝ TUYỂN DỤNG TRÊN WEB**<br>**DÀNH CHO BƯU TÁ**||||Lần ban hành: 1|
|||||||||
||||||Nhập họ<br>và tên|Để trống trường thông tin > Hiển thị<br>message:||
|2||Năm<br>sinh|Textbox|Có|Hint<br>text:<br>Nhập<br>năm sinh|Chỉ cho phép nhập số, tối đa 4 số<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:||
|3||Số<br>điện<br>thoại|Textbox|Có|Hint<br>text:<br>Nhập số<br>điện<br>thoại|Chỉ cho phép nhập số, tối đa 10 số, không<br>chứa ký tự đặc biệt<br>**Message:**<br>- Nhập sai định dạng > Hiển thị message:<br>“Số điện thoại không hợp lệ.”<br>- Để trống trường thông tin > Hiển thị<br>message:||
|**Vị trí ứng tuyển**||||||||
|1||Vị trí<br>ứng<br>tuyển|Check box|Có|N/A|Chọn 1 trong 3 vị trí ứng tuyển:<br>- Nhân viên bưu tá<br>- Nhân viên khai thác<br>- Tài xế xe tải<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:||
|**Khu vực ứng tuyển**||||||||
|1||Tỉnh|Dropdown<br>list|Có|Hint<br>text:<br>Chọn<br>tỉnh|Chọn tỉnh từ danh sách Hệ thống quản lý<br>nhân sự trả về<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:||
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD299|
|---|---|---|
||**ĐĂNG KÝ TUYỂN DỤNG TRÊN WEB**<br>**DÀNH CHO BƯU TÁ**|Lần ban hành: 1|

**==> picture [201 x 22] intentionally omitted <==**

|---|---|---|---|---|---|
|2|Bưu<br>cục|Dropdown<br>list|Có|Hint<br>text:<br>Chọn<br>bưu cục|Chọn bưu cục theo tỉnh từ danh sách Hệ<br>thống quản lý nhân sự trả về. Chỉ được chọn<br>bưu cục khi đã chọn tỉnh<br>**Message:**<br>Để trống trường thông tin > Hiển thị<br>message:|
|3|Điều<br>khoản<br>quy<br>định|Check box|Có|N/A|Mặc định tích điều khoản quy định<br>**Message:**<br>Bỏ tích điều khoản quy định > Hiển thị<br>message:|
|4|Đăng<br>ký|Button|N/A|N/A|Click on => Hiển thị popup<br>**_Message:_**<br>Trong vòng 7 ngày: Cùng thông tin cá nhân,<br>cùng vị trí ứng tuyển, cùng khu vực ứng<br>tuyển, cùng trạng thái Chưa xử lý => Không<br>tiếp nhận hồ sơ tương tự.<br>Khi click on button => Hiển thị message:<br>“Bạn đã ứng tuyển cho vị trí này, vui lòng<br>đợi xét duyệt"<br>Click hủy => Giữ nguyên màn ứng tuyển<br>Click Xác nhận => Điều hướngmàn hình|
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD299|
|---|---|---|
||**ĐĂNG KÝ TUYỂN DỤNG TRÊN WEB**<br>**DÀNH CHO BƯU TÁ**|Lần ban hành: 1|

**==> picture [248 x 142] intentionally omitted <==**

**==> picture [210 x 137] intentionally omitted <==**