**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD279|
|---|---|---|
||**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE**|Lần ban hành: 1|

## **1. Tổng quan** 

## **1.1 Quy trình** 
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD279|
|---|---|---|
||**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE**|Lần ban hành: 1|

**==> picture [376 x 669] intentionally omitted <==**
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD279|
|---|---|---|
||**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE**|Lần ban hành: 1|

**==> picture [376 x 366] intentionally omitted <==**

## **1.2 Mô tả** 

Tại bước 4 và 7, Fico check những điều kiện sau: 

|STT|Điều kiện check|Mô tả|
|---|---|---|
|1|Kiểm tra trùng lặp|Đơn hàng đã được xử lý/phát hàng trước đó hay<br>chưa?|
|2|Check tổng chi tiết mặt<br>hàng của đơn = Tổng số<br>lượng mặt hàng của đơn<br>hàng||
|3|Check thông tin đơn hàng<br>và chi tiết (tạm thời chưa<br>che4ck)|Tổng SL mặt hàng trên đơn = Tổng dl chi tiết<br>Tổng tiền trước thuế trên đơn = Tổng tiền trước<br>thuế chi tiết (loại 1+3+4+5+6)<br>Tổng thuế trên đơn = Tổng thuế chi tiết ((loại<br>1+3+4+5+6)|
|||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD279|
|---|---|---|---|---|
|||**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE**||Lần ban hành: 1|
||||Tổng tiền sau thuế = Tổng tiền sau thuế chi tiết<br>((1+3+4+5+6))||
|4|Check tiên trên chi tiết mặt<br>hàng<br>(tạm<br>thời<br>chưa<br>check)||Các bước check<br>1 – Tính từng loại tiền theo công thức dưới đây<br>2 – Làm tròn số tiền sau khi tính được theo cấu<br>hình Vinvoice<br>3 – So sánh số tiền đã làm tròn với số hệ thống<br>nguồn gửi sang<br>Tổng tiền trước thuế = Đơn giá * SL<br>Tiền thuế = Tiền trước thuế *% thuế<br>Tiền sau thế=Tiền trước thuế+Tiền thuế||
|5|Check tiền chiết khấu||Chiết khấu truyền sang như 1 mặt hàng, tính tiền<br>như 1 mặt hàng||
|6|Check các trường bắt buộc<br>theo API||Tiền hàng hóa: max 500<br>Mã hàng hóa: max 50<br>Tên đơn vị tính: max 300<br>Số lượng: sau dấu phẩy max 4 số, không nhận số<br>âm||
|7|Check dữ liệu các đường<br>truyền sang đúng số thập<br>phân chưa?||Theo cấu hình Vinvoice yêu cầu||

## **1.3 Danh sách tính năng** 

Danh sách tính năng và API 

- Danh sách API 

   - + API tra cứu hóa đơn 

   - + API gửi thông tin đơn hàng 

   - + API Callback trả kết quả hóa đơn 

   - + API đồng bộ thông tin khách hàng 

- Quản lý danh sách đơn hàng 

## **2. Sơ đồ trạng thái** 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE** Lần ban hành: 1 

**==> picture [428 x 423] intentionally omitted <==**

Bảng mapping trạng thái 

|TT<br>FMCG<br>Show cho<br>user|Sub TT<br>FMCG|Action|Fico|Action|Bảng kê hóa<br>đơn|Action|
|---|---|---|---|---|---|---|
|Chưa xuất<br>HĐ|Chưa yc<br>xuất HĐ|Sửa TT xuất<br>HĐ/Đẩy lại|||||
|Chưa xuất<br>HĐ|Lỗi TT<br>xuất HĐ|Sửa TT xuất<br>HĐ/Đẩy lại|||||
|||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD279|TD279|
|---|---|---|---|---|---|---|---|---|
|||**BỔ SUNG LUỒNG TRÌNH KÝ VOFFICE**|||||Lần ban hành: 1||
||||||||||
|Đang phát<br>hành||Đang xuất<br>HĐ|Tra cứu TT<br>của HĐ|Đã gom<br>bảng kê|Không||Tạo mới||
||||||||Chốt bảng<br>kê||
||||||||Chờ phát<br>hành||
||||||||Đã phát<br>hành||
|Đã xuất<br>HĐ||Đã xuất<br>HĐ|Gửi lại HĐ<br>cho khách|Đã xuất<br>HĐ|||Đã phát<br>hành||
|Xuất HĐ<br>thất bại||Xuất HĐ<br>thất bại|Sửa lại TT<br>xuất<br>HĐ/Đẩy lại|Xuất HĐ<br>thất bại|||Lỗi xuất HĐ|Gỡ bill<br>bảng kê,<br>sửa<br>thông<br>tin|