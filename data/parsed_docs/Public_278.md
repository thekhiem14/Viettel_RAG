**VIETTEL AI RACE** TD278 **BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

## **1. Tổng quan** 

## **1.1 Mục đích** 

Tài liệu trình bày tổng quan giải pháp và quy trình nghiệp vụ đáp ứng cho bài toán tích hợp đối tác kinh doanh tại Tổng công ty cổ phần Bưu chính Viettel. 

Thiết kế, mô tả các quy trình nghiệp vụ của Hệ thống đảm bảo cung cấp giải pháp hoàn chỉnh, xuyên suốt quá trình khai báo và phê duyệt mã KH chi COD 

## **1.2 Phạm vi** 

|**_STT_**|**_Nghiệp vụ_**|**_Phạm vi áp dụng_**|
|---|---|---|
|_1._|_Khai báo cấu hình_|_- Khai báo cấu hình sản lượng doanh thu theo địa_<br>_bàn_<br>_- Khai báo mã KH cấu hình chi COD_|
|_2._|_Phê duyệt mã KH_|_Thực hiện phê duyệt mã KH đã khai báo theo sản_<br>_lượng/doanh thu cam kết_<br>-<br>_Hệ thống tự động phê duyệt nếu đạt sản_<br>_lượng hoặc doanh thu theo địa bàn_<br>-<br>_Hệ thống thự hiện trình ký phê duyệt_<br>_Voffice với các trường hợp không đạt_<br>_doanh thu sản lượng theo địa bàn_|
|_3._|_Báo cáo sản lượng doanh thu_<br>_theo mã KH_|_Báo cáo cấu hình chi của mã KH_<br>_Báo cáo sản lượng/doanh thu_|

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## TD278 

**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** Lần ban hành: 1 

## **2. Quy trình tổng quan** 

**==> picture [482 x 142] intentionally omitted <==**

**----- Start of picture text -----**<br>
1. Chức năng khai báo  7. Lưu thông tin kỳ thanh  8. Đồng bộ kỳ thanh toán<br>mã KH cusID toán Cusid sang mã EVTP<br>Đồng ý<br>2. Chọn mã KH hoặc<br>import file  Không xác thực 9. Tự động hủy yêu cầu sau 72h<br>3. Hiển thị thông tin thanh  4. Chọn Thanh COD toán  5. Đẩy yêu cầu xác thực  6. Hiển thị yêu cầu xác<br>K/T KH Chưa khai báo toán của KH hàng ngày OTP trên app KH thực OTP trên app KH<br>10. Cập nhật trạng thái<br>xác thực<br>KH đã khai báo 3.1 Hiển thị thông báo lỗi<br>**----- End of picture text -----**<br>

## **Mô tả quy trình:** 

|**Bước**|**Nội dung**|**Đối tượng**<br>**thực hiện**|**Hệ thống**<br>**thực hiện**|**Mô tả**|
|---|---|---|---|---|
|1|Chức năng khai<br>báo mã KH cusID|User được<br>phân quyền|FICO|User được phân quyền truy cập vào chức năng khai<br>báo mã KH cusID trên hệ thống FICO.<br>Chuyển bước 2.|
|2|Chọn<br>mã<br>KH<br>hoặc Import file|User được<br>phân<br>quyền|FICO|Người dùng nhập mã KH hoặc import danh sách KH<br>cần khai báo chi COD hàng ngày.<br>Hệ thống kiếm tra:<br>-<br>Nếu KH đang có kỳ thanh toán COD hàng<br>ngày→Thông báo lỗi<br>-<br>Nếu KH đang không có kỳ thanh toán COD<br>hàngngày →chuyển bước 3.|
|3|Hiển thị thông tin<br>thanh toán của<br>KH|Hệ thống|FICO|Hiển thị thông tin thanh toán hiện tại của cus tìm kiếm.<br>Chuyển bước 4.|
|4|Chọn Thanh toán<br>COD hàng ngày|User được<br>phân quyền|FICO|Chọn loại kỳ thanh toán Hàng ngày cho các mã KH<br>khai báo.<br>Chuyển bước 5.|
|5|Xác nhận đẩy yêu<br>cầu xác thực OTP<br>trên app KH|User được<br>phân quyền|FICO|Người dùng xác nhận khai báo các mã KH về hình<br>thức thanh toán COD hàng ngày. Hệ thống tự động<br>đẩy yêu cầu xác thực OTP lên app KH.<br>Chuyển bước 6.|
|6|Hiển thị yêu cầu<br>xác thực lên app<br>KH|Hệ thống|App KH|KH thực hiện xác thực OTP trên App KH.<br>-<br>Xác thực thành công→chuyển bước 7<br>-<br>Khôngxác thực→Chuyển bước 9|

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## TD278 

**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** Lần ban hành: 1 

|**Bước**|**Nội dung**|**Đối tượng**<br>**thực hiện**|**Hệ thống**<br>**thực hiện**|**Mô tả**|
|---|---|---|---|---|
|7|Lưu thông tin kỳ<br>thanh toán cusID|Hệ thống|FICO|KH xác thực thành công→hệ thống tự động cập nhật<br>thông tin thanh toán mới của KH.<br>-<br>Hiển thị Ngày thanh toán mới và lịch sử cập<br>nhật trên app KH<br>-<br>Cập nhật thông tin kỳ thanh toán trên hệ thống<br>FICO,HR→Chuyển bước 8.|
|8|Đồng bộ kỳ thanh<br>toán<br>sang<br>mã<br>EVTP|Hệ thống|FICO|Đồng bộ kỳ thanh toán từ mã Cus sang toàn bộ mã<br>EVTP thuộc cus.<br>Chuyển bước 10.|
|9|Tự động hủy yêu<br>cầu sau 72h|Hệ thống|FICO|Với yêu cầu xác thực quá 72h không có phản hồi từ<br>KH→hệ thống tự động cập nhật về trạng thái Xác<br>thực thất bại.<br>-<br>Khi KH click vào yêu cầu trên app→hệ thống<br>thông báo Yêu cầu không tồn tại hoặc đã quá<br>hạn xử lý<br>-<br>Hệ thống cập nhật trạng thái Xác thực thất bại.<br>Chuyển bước 10.|
|10|Cập nhật trạng<br>thái xác thực|Hệ thống|FICO|Hệ thống cập nhật chính xác trạng thái xác thực.<br>Kết thúc luồng.|

**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

Lần ban hành: 1 

## **3. Chi tiết chức năng Quản lý CusID và khai báo KH thanh toán hàng ngày trên FICO** 

## **3.1 SCR1: Màn hình Quản lý khách hàng CusID** 

## **3.1.1 Màn hình** 

**==> picture [541 x 155] intentionally omitted <==**

Phân quyền: User được phân quyền theo quy định của TTDVCP 

## **3.1.2 Mô tả màn hình** 

|---|---|---|---|---|---|
|**No**|**Field**<br>**Name**|**Control**<br>**Type**|**Mandatory**<br>**(Yes/No)**|**Editable/**<br>**Read-**<br>**only**|**Description/Note**|
|**Chức năng tra cứu**||||||
|**1**|Khách<br>hàng cus|Textbox|No|Editable|Cho phép user nhập thông tin KH<br>để tìm kiếm.<br>Cho phép nhập các giá trị sau:<br>-<br>Mã CusID<br>-<br>Số điện thoại (sđt đăng nhập<br>hệ thống app/web)<br>-<br>Email (Email đăng nhập hệ<br>thống app/web)<br>Hệ thống tìm kiếm mã cus theo điều<br>kiện nhập.|
|**2**|Khách<br>hàng EVTP|Textbox|No|Editable|Cho phép KH nhập mã EVTP để<br>tìm kiếm mã KH CusID|
|**3**|Tìm kiếm|Button|Yes|Editable|Click button thực hiện tra cứu.<br>Hiển thị toàn bộ dữ liệu theo điều<br>kiện tìm kiếm|
|**Chi tiết thông tin KH**||||||
**VIETTEL AI RACE** 

**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|---|
|**No**|**Field**<br>**Name**|**Control**<br>**Type**|**Mandatory**<br>**(Yes/No)**|**Editable/**<br>**Read-**<br>**only**|**Description/Note**|
|**4**|STT|Text|No|Read-<br>only|Hiển thị số thứ tự|
|**5**|Mã cusid|Text|No|Editable|Hiển thị mã Cusid|
|**6**|Số điện<br>thoại|Text|No|Read-<br>only|Hiển thị số điện thoại KH|
|**7**|Tên KH|Text|No|Read-<br>only|Hiển thị Tên KH|
|**8**|Loại kỳ<br>thanh toán|Text|No|Read-<br>only|Hiển thị loại kỳ thanh toán theo<br>HDDT|
|**9**|Email|Text|No|Read-<br>only|Hiển thị email KH|
|**10**|Hình thức<br>thanh toán|Text|No|Read-<br>only|Hiện thị hình thức thanh toán của KH|
|**11**|Ngân hàng|Text|No|Read-<br>only|Hiển thị ngân hàng nhận COD theo<br>HDDT|
|**12**|Chi nhánh|Text|No|Read-<br>only|Hiển thị chi nhánh của ngân hàng<br>Không có để trống|
|**13**|Số tài<br>khoản|Text|No|Read-<br>only|Hiển thị số tài khoản theo HDDT|
|**14**|Người thụ<br>hưởng|Text|No|Read-<br>only|Hiển thị tên người thụ hưởng theo<br>HDDT|
|**15**|Thao tác|Button|Yes|Editable|Cho phép thao tác sửa và xóa cấu hình<br>theo từng địa bàn.<br>- Click Button Xem→cho phép xem<br>chi tiết danh sách KH EVTP của mã<br>cus<br>- Click Xem lịch sử→Hiển thị lịch sử<br>cập nhật của cusid.<br>Hiển thị tooltip khi Hower chuột<br>“Xem” và “Lịch sử cập nhật”|
|**Chi tiết thông tin KH EVTP**<br>**Hiển thị danh sách mã KH EVTP thuộc mã CusID**||||||
|**1**|STT|Text|No|Read-<br>only|Hiển thị số thứ tự|
**VIETTEL AI RACE** 

**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|---|
|**No**|**Field**<br>**Name**|**Control**<br>**Type**|**Mandatory**<br>**(Yes/No)**|**Editable/**<br>**Read-**<br>**only**|**Description/Note**|
|**2**|Chi nhánh|Text|No|Read-<br>only|Hiển thị tên chi nhánh|
|**3**|Bưu cục|Text|No|Read-<br>only|Hiển thị tên bưu cục|
|**4**|Mã KH<br>EVTP|Text|No|Read-<br>only|Hiển thị mã KH EVTP|
|**5**|Tên KH|Text|No|Read-<br>only|Hiển thị tên KH EVTP|
|**6**|Hình thức<br>cấn trừ|Text|No|Read-<br>only|Hiển thị hình thức cấn trừ của mã<br>EVTP<br>Không có để trống.|
|**7**|Kỳ cấn trừ|Text|No|Read-<br>only|Hiển thị kỳ cấn trừ.<br>Không có để trống.|
|**8**|Ngày lấy<br>cấn trừ|Text|No|Read-<br>only|Hiển thị ngày lấy cấn trừ<br>Không có để trống.|
|**9**|Kết xuất<br>excel|Button|Yes|Editable|Khi click thì thực hiện kết xuất danh<br>sách excel trên grid.<br>**Quy Tắc Kết Xuất:**<br>❖ Nếu kết quả tìm kiếm không có<br>dữ liệu thì hệ thống hiển thị<br>thông báo “Không tồn tại kết<br>quả”.<br>❖ Nếu kết quả tìm kiếm có dữ liệu<br>thì hệ thống thực hiện kết xuất<br>toán bộ dữ liệu trên grid.<br>Tên file: Danh sách KH EVTP mã<br>cusID {Mã cusid}|

## **3.2 SCR2: Màn hình Khai báo mã khách hàng** 

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

Lần ban hành: 1 

## **3.2.1 Màn hình** 

**==> picture [548 x 161] intentionally omitted <==**

## **3.2.2 Mô tả Màn hình** 

|**No**|**Field Name**|**Control**<br>**Type**|**Mandatory**<br>**(Yes/No)**|**Editable/**<br>**Read-only**|**Description/Note**|
|---|---|---|---|---|---|
|**Chức năng tra cứu**||||||
|**1**|Khách hàng cus|Textbox|No|Editable|Cho phép user nhập thông tin KH để<br>tìm kiếm.<br>Cho phép nhập các giá trị sau:<br>-<br>Mã CusID<br>-<br>Số điện thoại (sđt đăng nhập hệ<br>thống app/web)<br>-<br>Email (Email đăng nhập hệ thống<br>app/web)<br>Hệ thống tìm kiếm mã cus theo điều kiện<br>nhập.|
|**2**|Khách hàng<br>EVTP|Textbox|No|Editable|Cho phép KH nhập mã EVTP để tìm kiếm<br>mã KH CusID|
|**3**|Tìm kiếm|Button|Yes|Editable|Click button thực hiện tra cứu.<br>Hiển thị toàn bộ dữ liệu theo điều kiện<br>tìm kiếm|

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

Lần ban hành: 1 

|**No**|**Field Name**|**Control**<br>**Type**|**Mandatory**<br>**(Yes/No)**|**Editable/**<br>**Read-only**|**Description/Note**|
|---|---|---|---|---|---|
|**4**|Kết xuất excel|Button|Yes|Editable|Khi click thì thực hiện kết xuất danh sách<br>excel trên grid.<br>**Quy Tắc Kết Xuất:**<br>❖ Nếu kết quả tìm kiếm không có dữ<br>liệu thì hệ thống hiển thị thông báo<br>“Không tồn tại kết quả”.<br>❖ Nếu kết quả tìm kiếm có dữ liệu thì<br>hệ thống thực hiện kết xuất toán bộ<br>dữ liệu trên grid.<br>➢ Tên file: Danh sách KH khai báo<br>thanh toán hàng ngày|
|**5**|Khai báo mã KH|Button|Yes|Editable|Hiển thị button Khai báo mã KH. Click<br>button hiển thị popup Khai báo mã KH<br>chi tiết tại màn hình SCR 3. Màn hình<br>Khai báo thông tin mã KH|
|**Chi tiết thông tin cấu hình**||||||
|**6**|STT|Text|No|Read-only|Hiển thị số thứ tự|
|**7**|STT|Text|No|Read-only|Hiển thị số thứ tự|
|**8**|Mã cusid|Text|No|Editable|Hiển thị mã Cusid|
|**9**|Số điện thoại|Text|No|Read-only|Hiển thị số điện thoại KH|
|**10**|Tên KH|Text|No|Read-only|Hiển thị Tên KH|
|**11**|Loại kỳ thanh<br>toán|Text|No|Read-only|Hiển thị loại kỳ thanh toán theo HDDT|
|**12**|Email|Text|No|Read-only|Hiển thị email KH|
|**13**|Hình thức thanh<br>toán|Text|No|Read-only|Hiện thị hình thức thanh toán của KH|

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

Lần ban hành: 1 

|**No**|**Field Name**|**Control**<br>**Type**|**Mandatory**<br>**(Yes/No)**|**Editable/**<br>**Read-only**|**Description/Note**|
|---|---|---|---|---|---|
|**14**|Trạng thái|Text|No|Read-only|Hiển thị trạng thái tương ứng của yêu<br>cầu:<br>-<br>Chờ xác thực – Đã gửi yêu cầu<br>xác thực nhưng KH chưa xác thực<br>-<br>Đã xác thực – KH đã xác thực<br>OTP thành công<br>-<br>Xác thực thất bại – KH từ chối<br>xác thực hoặc xác thực tự động<br>hủy sau 72h<br>-<br>Không hoạt động – khi có cập<br>nhật kỳ thanh toán mới (KH ký<br>PL HĐ có thay đổi kỳ thanh toán<br>hoặc thay đổi kỳ thanh toán)|
|**15**|Người khai báo|Datetime|No|Read-only|Hiển thị tên người thực hiện khai báo|
|**16**|Thời gian khai<br>báo|Datetime|No|Read-only|Hiển thị thời gian thực hiện khai báo|
|**17**|Thời gian cập<br>nhật|Datetime|No|Read-only|Hiển thị thời gian cập nhật (thời gian xác<br>thực, hủy)|
|**18**|Thao tác|Button|Yes|Editable|Cho phép thao tác gửi lại yêu cầu xác thực<br>và xóa cấu hình.<br>- Click Button Gửi yêu cầu xác thực→chỉ<br>hiển thị với trạng thái Xác thực thất bại và<br>Không hoạt động.<br>- Click Xóa→Chỉ hiển thị với trạng thái<br>Chờ xác thực và Xác thực thất bại Hiển thị<br>thông báo Xác nhận xóa khai báo cấu<br>hình.<br>Hiển thị tooltip khi Hower chuột “Gửi<br>yêu cầu xác thực” và “Xóa”|

## **3.2.3 SCR3. Màn hình Khai báo thông tin mã KH** 

**==> picture [557 x 126] intentionally omitted <==**
**VIETTEL AI RACE** 

**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

|**No**|**Field Name**|**Control**<br>**Type**|**Mandatory**<br>**(Yes/No)**|**Editable/**<br>**Read-only**|**Description/Note**|
|---|---|---|---|---|---|
|**1**|Import file|Button|Yes|Editable|Cho phép user import file KH theo<br>template.<br>Nguyên tắc import:<br>-<br>Nếu KH đang có khai báo kỳ<br>thanh toán COD hàng ngày→<br>không cho phép import<br>-<br>Nếu KH đang không phải kỳ<br>thanh toán hàng ngày→cho<br>phép import<br>-<br>Dữ liệu import lên phải là mã<br>cusid|
|**2**|Tải xuống file<br>biểu mẫu|Button|No|Editable|Cho phép user tải xuống file biểu mẫu<br>Template file:|
|**3**|STT|Button|Yes|Editable|Hiển thị STT|
|**4**|Mã CusID|Texbox|Yes|Editable|Cho phép user nhập thông tin KH để<br>tìm kiếm.<br>Cho phép nhập các giá trị sau:<br>-<br>Mã CusID<br>-<br>Số điện thoại (sđt đăng nhập hệ<br>thống app/web)<br>-<br>Email (Email đăng nhập hệ<br>thống app/web)<br>Click enter hoặc click chuột→Hệ<br>thống tìm kiếm mã cus theo điều kiện<br>nhập.<br>Kiểm tra mã cus nhập vào hệ thống:<br>-<br>Nếu KH đang có khai báo kỳ<br>thanh toán COD hàng ngày→<br>Thông báo lỗi “KH đang có kỳ<br>thanh toán hàng ngày”<br>-<br>Nếu KH đang không phải kỳ<br>thanh toán hàng ngày→Hiển<br>thị thông tin KH tìm kiếm<br>-<br>Mã KH nhập bị trùng với mã<br>KH đã nhập→báo lỗi “Mã KH<br>đã được nhập”|
|**5**|Tên KH|Text|N/A|Readonly|Hiển thị tên KH theo cus đã tìm kiếm<br>Không có để trống|
**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

Lần ban hành: 1 

|**No**|**Field Name**|**Control**<br>**Type**|**Mandatory**<br>**(Yes/No)**|**Editable/**<br>**Read-only**|**Description/Note**|
|---|---|---|---|---|---|
|**6**|Số điện thoại|Text|N/A|Readonly|Hiển thị SĐT KH theo cus đã tìm kiếm<br>Không có để trống|
|**7**|Email|Text|N/A|Readonly|Hiển thị Email KH theo cus đã tìm kiếm<br>Không có để trống|
|**8**|Loại kỳ thanh<br>toán|Text|N/A|Readonly|Hiển thị loại kỳ thanh toán đang áp<br>dụng theo cus đã tìm kiếm<br>Không có để trống|
|**9**|Loại kỳ thanh<br>toán khai báo|Dropdownlist|Yes|Editable|Cho phép chọn loại kỳ thanh toán<br>Mặc định chọn: Hàng ngày|
|**10**|Thao tác|Button|Yes|Editable|Cho phép thao tác xóa mã KH đã nhập.<br>- Click Xóa→Hiển thị thông báo Xác<br>nhận xóa mã KH.<br>Hiển thị tooltip khi Hower chuột “Xóa”|
|**11**|Xác nhận|Button|Yes|Editable|Click Cập nhật để gửi yêu cầu xác thực<br>→đẩy yêu cầu xác thực sang hệ thống<br>App KH|
|**12**|Đóng|Button|Yes|Editable|Click “Đóng” để tắt nội dung thay đổi|
|**13**|Thêm dòng|Button|Yes|Editable|Cho phép user thêm dòng để nhập mã<br>KH khai báo|

## **3.3 Yêu cầu nghiệp vụ chi tiết** 

KH được xác thực thanh công sẽ có Kỳ thanh toán hàng ngày → hệ thống tự động cập nhật toàn bộ mã KH EVTP của mã CusID về kỳ thanh toán của cus 

Kỳ thanh toán sẽ thay đổi nếu KH thực hiện Ký PL thay đổi hình thức thanh toán hoặc thực hiện yêu cầu xác thực lại Kỳ thanh toán ➔ Kỳ thanh toán đã được khai báo sẽ được cập nhật về trạng thái Không hoạt động. 

Ảnh hưởng: 

- Màn hình quản lý KH chi nhánh trên HR thêm type "Thanh toán COD hàng ngày" 

- Màn hình quản lý KH FICO thêm type "Thanh toán COD hàng ngày" 

- Chức năng chi: hệ thống gom chi tự động theo đúng hình thức thanh toán của KH 

## **4. Chi tiết chức năng Xác thực OTP trên app KH** 

## **4.1 SCR1: Màn hình yêu cầu xác thực** 

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

Lần ban hành: 1 

## **4.1.1 Màn hình** 

**==> picture [99 x 362] intentionally omitted <==**

**==> picture [103 x 361] intentionally omitted <==**

**==> picture [102 x 354] intentionally omitted <==**

**==> picture [102 x 357] intentionally omitted <==**

**==> picture [421 x 21] intentionally omitted <==**

**----- Start of picture text -----**<br>
MH01  MH02  MH03  MH04<br>**----- End of picture text -----**<br>

## **4.1.2 Mô tả màn hình** 

- Hiển thị thông báo “Khách hàng có 1 yêu cầu xác thực thay đổi ngày thanh toán COD. Xác thực ngay.” → click thông báo hiển thị màn hình MH02: Xác nhận cập nhật ngày thanh toán → click Xác nhận → hiển thị màn hình MH03: nhập mã xác thực OTP → Xác thực thành công hiển thị màn hình MH04: thông báo cập nhật thành công, 

- MH01: Chi tiết tài khoản → Hiển thị cảnh báo “Khách hàng có 1 yêu cầu xác thực thay đổi ngày thanh toán COD. Xác thực ngay.” → Click Xác thực ngay → Chuyển sang màn MH02. 

- MH02: Xác nhận cập nhật ngày thanh toán. 

   - Hiển thị thông tin cập nhật 

   - Click Xác nhận → chuyển màn hình MH03 

   - Click Bỏ qua để từ chối cập nhật → Cập nhật trạng thái “Xác nhận thất bại” với lý do “KH từ chối xác nhận.” 
**VIETTEL AI RACE** TD278 **BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

- MH03: Xác thực OTP 

   - KH nhập mã xác thực qua tin nhắn gửi về. 

   - Xác thực thành công → chuyển màn hình MH04 

   - Xác thực không thành công → quay về màn hình MH01. 

MH04: Thông báo thành công → Hiển thị thông báo “Cập nhật thông tin thanh toán thành công” nếu KH xác thực OTP thành công