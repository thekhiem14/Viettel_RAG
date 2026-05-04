**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD280|
|---|---|---|
||**BÁO CÁO CÔNG NỢ COD**|Lần ban hành: 1|

## **1. Tổng quan** 

## **1.1 Mục đích tài liệu** 

Tài liệu này được xây dựng nhằm mục đích mô tả thiết kế của các chức năng đáp ứng yêu cầu nghiệp vụ theo quy trình tài liệu. 

## **1.2 Thuật ngữ và chữ viết tắt** 

|Thuật ngữ/ Từ viết tắt|Định nghĩa|
|---|---|
|LOG|Công ty TNHH MTV Logistics DHL|
|TCT|Tổng công ty|
|TTVH|Trung tâm Vận hành chuyển phát|

## **2. Nội dung** 

## **2.1 Báo cáo KPI Công nợ COD** 

## **2.1.1 Mô tả chức năng** 

|Mục đích|Cho phép người dùng theo dõi chỉ số KPI công nợ COD.|
|---|---|
|Hệ thống thực hiện|NOC: noc.dhl.vn|
|Đối tượng sử dụng|Cấp quyền truy cập cho các user thuộc các role sau:<br>•<br>Lãnh đạo TCT; Phòng tài chính: Xem toàn bộ dữ liệu của<br>báo cáo theo tất cả các cấp.<br>•<br>Cấp Chi nhánh: Lãnh đạo chi nhánh; Chuyên quản<br>chi nhánh; Nhân viên điều hành chất lượng: Xem<br>dữ liệu của chi nhánh quản lý và các bưu cục trực<br>thuộc.<br>•<br>Cấp Bưu cục: Lãnh đạo bưu cục: Xem dữ liệu của bưu<br>cụcquản lý.|
|Điều kiện đầu vào|Người dùng đăng nhập hệ thống thành công, truy cập mục Báo<br>cáo tài chính.<br>**Đăng nhập**→ **Báo cáo tài chính**→ **Báo cáo KPI công nợ**<br>**COD **|
|Điều kiện đầu ra|Hiển thị chỉ số KPI công nợ COD.|
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD280|
|---|---|---|
||**BÁO CÁO CÔNG NỢ COD**|Lần ban hành: 1|

## **2.1.2 Mô tả màn hình** 

|**STT**|**Trường dữ liệu**|**Kiểu dữ liệu**|**Mô tả**|
|---|---|---|---|
|**Bộ lọc**||||
|1|Bộ lọc thời gian|Datepicker|Cho phép lọc theo thời gian, chỉ cho phép chọn<br>từ ngày N-1 về trước. Bao gồm<br>+ Lũy kế ngày: cho phép lọc dữ liệu theo ngày.<br>Mặc định: ngày N-1|
|2|Bộ lọc theo<br>vùng|Dropdownlist|Cho phép lọc theo vùng phát (là vùng của chi<br>nhánh phát thực tế). Bao gồm: Theo cây tổ chức<br>NOC.<br>Chỉ cho phép chọn 1 lựa chọn. Mặc định: Tất cả|
|3|Bộ lọc theo chi<br>nhánh|Dropdownlist|Cho phép lọc và tìm kiếm theo chi nhánh phát<br>thực tế. Bao gồm: Theo cây tổ chức NOC.<br>Chỉ cho phép chọn 1 lựa chọn. Mặc định: Tất cả|
|4|Bộ lọc theo<br>vùng con|Dropdownlist|Cho phép lọc và tìm kiếm theo vùng con của chi<br>nhánh HNI/HCM. Bao gồm: Theo cây tổ chức<br>NOC.<br>Chỉ cho phép chọn 1 lựa chọn. Mặc định: Tất cả<br>Lưu ý:<br>+ Bộ lọc vùng con chỉ hiển thị khi đã chọn Bộ<br>lọc theo chi nhánh = HNI/HCM.<br>+ Cho phép lọc: Chi nhánh → Vùng con →<br>Bưu cục; Chi nhánh→Bưu cục.|
|5|Bộ lọc theo bưu<br>cục|Dropdownlist|Cho phép lọc và tìm kiếm theo bưu cục phát<br>thực tế, chỉ cho phép lọc theo bưu cục sau khi<br>đã chọn bộ lọc theo chi nhánh.<br>Bao gồm: Theo cây tổ chức NOC. Chỉ cho phép<br>chọn 1 lựa chọn.<br>Mặc định: Tất cả.|
|||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD280|
|---|---|---|---|---|---|---|
|||**BÁO CÁO CÔNG NỢ COD**||||Lần ban hành: 1|
||||||||
|6|Bộ lọc theo đánh<br>giá ngày||<br>Dropdownlist||Cho phép lọc và tìm kiếm theo đánh giá ngày.<br>Bao gồm:<br>+ Đạt<br>+ Không đạt<br>Chỉ cho phép chọn 1 lựa chọn. Mặc định: Tất<br>cả.||
|7|Xuất excel theo<br>màn||Button||Chọn → Tải xuống file excel theo báo cáo tổng<br>hợp đang hiển thị trên màn hình.<br>Tên file: kpicongnocodtonghop_ddmmyyyy||
|8|Xuất excel chi<br>tiết||Button||Chọn → Tải xuống file excel chi tiết bưu gửi<br>tính kpi công nợ theo điều kiện lọc đã chọn<br>(xuất chi tiết bưu gửi theo ngày).<br>Tên file:<br>kpicongnocodchitiettheongay_ddmmyyyy||
|**Báo cáo**<br>Thời gian cập nhật dữ liệu:<br>+ Ngày N cập nhật số liệu ngày N-1 tại 2 mốc 10h và 17h.<br>+Ngày 5 tháng N+1 chạy lại và chốt dữ liệu tháng N.|||||||
|Mô tả chung: Lấy toàn bộ bưu gửi đã phát sinh trạng thái 501 và có thời gian đến hạn<br>thu tiền nằm trong ngày được chọn tại bộ lọc thời gian (loại các đơn có tiền thu hộ = 0<br>hoặc null)<br>Lưu ý:<br>+ Nếu thời gian đến hạn thu tiền vào ngày chủ nhật, ngày Lễ, ngày Tết được loại trừ<br>và được tính vào ngày làm việc gần nhất (ví dụ: thời gian đến hạn thu tiền là 09:00:00<br>ngày 30/08 là chủ nhật, ngày 01/09 và 02/09 là ngày lễ => thời gian đến hạn thu tiền<br>được tính là 09:00:00 ngày 03/09)<br>+ Danh sách ngày Lễ, ngày Tết do phòng Chiến lược kinh doanh cung cấp:Quy đổi<br>chi tiết ngày 2023 2024 2025.xlsx|||||||
|1|Vùng||Text|Hiển thị vùng phát thực tế.|||
|2|Chi nhánh||Text|Hiển thị mã chi nhánh phát thực tế.|||

Mô tả chung: Lấy toàn bộ bưu gửi đã phát sinh trạng thái 501 và có thời gian đến hạn thu tiền nằm trong ngày được chọn tại bộ lọc thời gian (loại các đơn có tiền thu hộ = 0 hoặc null) 

+ Nếu thời gian đến hạn thu tiền vào ngày chủ nhật, ngày Lễ, ngày Tết được loại trừ và được tính vào ngày làm việc gần nhất (ví dụ: thời gian đến hạn thu tiền là 09:00:00 ngày 30/08 là chủ nhật, ngày 01/09 và 02/09 là ngày lễ => thời gian đến hạn thu tiền được tính là 09:00:00 ngày 03/09) 

+ Danh sách ngày Lễ, ngày Tết do phòng Chiến lược kinh doanh cung cấp: Quy đổi chi tiết ngày 2023 2024 2025.xlsx 

|1|Vùng|Text|Hiển thị vùng phát thực tế.|
|---|---|---|---|
|2|Chi nhánh|Text|Hiển thị mã chi nhánh phát thực tế.|
|||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD280|
|---|---|---|---|---|---|
|||**BÁO CÁO CÔNG NỢ COD**|||Lần ban hành: 1|
|3|Vùng con||Text|Hiển thị mã vùng con phát thực tế.<br>Cột Vùng con chỉ hiển thị sau khi chọn chi nhánh<br>HNI/HCM tại bộ lọc chi nhánh.||
|4|Bưu cục||Text|Hiển thị bưu cục phát thực tế.<br>Cột Bưu cục chỉ hiển thị sau khi chọn chi nhánh<br>tại bộ lọc chi nhánh.||
|5|Tuyến bưu tá||Text|Hiển thị tuyến bưu tá phát thực tế. Định dạng: Họ<br>và tên (mã nhân viên) Nếu không có mã nhân<br>viên→Để (--)<br>Cột Tuyến bưu tá chỉ hiển thị sau khi chọn bưu<br>cục tại bộ lọc bưu cục.||
|**Ngày**||||||
|6|Số tiền phải thu||Number|Hiển thị tổng số tiền thu hộ. ĐVT: VNĐ||
|7|Số tiền thu đúng<br>hạn||<br>Number|Hiển thị tổng số tiền thu hộ có thời gian thu <=<br>thời gian đến hạn thu tiền. ĐVT: VNĐ||
|8|Tỷ lệ thu công<br>nợ||Number|Hiển thị tỷ lệ thu công nợ ngày.Công thức:<br>Tỷ lệ thu công nợ ngày = (Số tiền thu đúng hạn /<br>Số tiền phải thu) * 100 (%)Định dạng:%, làm<br>tròn đến 2 chữ số thập phân.<br>Chọn  Cho phép lọc giá trị của cột theo thứ tự.<br>+ Click : Lọc từ thấp lên cao.<br>+ Click : Lọc từ cao xuống thấp.||
|9|Đánh giá||Text|Hiển thị đánh giá.<br>+ Hiển thị Đạt: Nếu Tỷ lệ thu công nợ >= 99.9%<br>+ Hiển thị Không đạt: Nếu Tỷ lệ thu công nợ <<br>99.9% Hover<br> →Hiển thị “KPI thu công nợ =<br>99.9”||
|**Lũy kế tháng**||||||
||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD280|
|---|---|---|---|---|---|
||||**BÁO CÁO CÔNG NỢ COD**||Lần ban hành: 1|
|10|Số ngày kế<br>hoạch||Number|Hiển thị số ngày tính KPI lũy kế tháng đến ngày.<br>Trong đó: Số ngày tính KPI = Số ngày lũy kế từ<br>ngày 1 đến ngày được chọn - Số ngày chủ nhật,<br>ngày Lễ, ngày Tết trong khoảng thời gian xét.<br>Danh sách ngày Lễ, ngày Tết do phòng Chiến<br>lược kinh doanh cung cấp: Quy đổi chi tiết ngày<br>2023 2024 2025.xlsx||
|11|Số ngày đạt KPI||Number|Hiển thị số ngày đạt KPI trong tổng số ngày kế<br>hoạch.<br>Trong đó: Số ngày đạt KPI là những ngày có Tỷ<br>lệ thu công nợ ngày >= 99.9%||
|12|Số tiền phải thu||Number|Hiển thị tổng số tiền thu hộ lũy kế tháng. ĐVT:<br>VNĐ||
|13|Số tiền thu đúng<br>hạn||Number|Hiển thị tổng số tiền thu hộ có thời gian thu <=<br>thời gian đến hạn thu tiền lũy kế tháng.<br>ĐVT: VNĐ||
|14|Tỷ lệ thu công<br>nợ bình quân||Number|Hiển thị tỷ lệ thu công nợ bình quân tháng từ<br>ngày 1 đến ngày được chọn. Công thức:<br>Tỷ lệ thu công nợ bình quân tháng = (Tổng tỷ lệ<br>thu công nợ các ngày tính KPI<br>/ Số ngày tính KPI) * 100 (%)<br>Lưu ý: Số ngày tính KPI = Số ngày lũy kế từ<br>ngày 1 đến ngày được chọn - Số ngày chủ nhật,<br>ngày Lễ, ngày Tết trong khoảng thời gian xét.<br>Danh sách ngày Lễ, ngày Tết do phòng Chiến<br>lược kinh doanh cung cấp:Quy đổi chi tiết ngày<br>2023 2024 2025.xlsx<br>Định dạng: %, làm tròn đến 2 chữ số thập phân.<br>Chọn  Cho phép lọc giá trị của cột theo thứ tự.<br>+ Click : Lọc từ thấp lên cao.<br>+Click:Lọc từ caoxuống thấp.||
||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD280|
|---|---|---|---|---|---|
||||**BÁO CÁO CÔNG NỢ COD**||Lần ban hành: 1|
|15|Đánh giá||Text|Hiển thị đánh giá.<br>+ Hiển thị Đạt: Nếu Tỷ lệ thu công nợ bình quân<br>>= 99.9%<br>+ Hiển thị Không đạt: Nếu Tỷ lệ thu công nợ<br>bình quân < 99.9%<br>Hover<br>Hiển thị“KPI thu công nợ=99.9”||

## **2.2. Báo cáo KPI công nợ COD theo tuyến bưu tá** 

|**STT**|**Trường dữ liệu**|**Kiểu dữ liệu**|<br>**Mô tả**|
|---|---|---|---|
|**Mô tả chung:**||||
|- Tần suất cấp nhật dữ liệu: Sau khi|||chốt số tháng tại ngày 5 ngày N+1, hiển thị|
|báo cáo KPI công nợ COD theo tuyến bưu tá tháng N (chọn bất kỳ ngày nào||||
|tháng N tại bộ lọc thời||gian đều xuất|báo cáo theo tháng từ ngày 1 đến ngày cuối|
|tháng N).||||
|Truy|cập: Đăng nhập → Truy xuất dữ liệu → Báo cáo KPI công nợ COD theo tuyến|||
|bưu tá (lũy kế)||||
|Tên file xuất: bckpicongnocodtheobuutaluyke_ddmmyyyy||||
|Tên báo cáo: Báo cáo KPI công nợ COD theo tuyến bưu tá (lũy kế)||||
|Loại báo cáo: Tài chính||||
|Phân|quyền: Chỉ phân quyền cho 1 vài user phòng Tài chính xuất toàn bộ dữ liệu.|||

|Phân|quyền: Chỉ phân quyền cho 1 vài user phòng Tài chính xuất toàn bộ dữ liệu.|quyền: Chỉ phân quyền cho 1 vài user phòng Tài chính xuất toàn bộ dữ liệu.|quyền: Chỉ phân quyền cho 1 vài user phòng Tài chính xuất toàn bộ dữ liệu.|
|---|---|---|---|
|1|Vùng|Text|Hiển thị vùng phát thực tế.|
|2|Chi nhánh|Text|Hiển thị mã chi nhánh phát thực tế.|
|3|Vùng con|Text|Hiển thị mã vùng con phát thực tế.|
|4|Bưu cục|Text|Hiển thị bưu cục phát thực tế.|
|5|Tuyến bưu tá|Text|Hiển thị họ và tên tuyến bưu tá phát thực tế.|
|6|Mã nhân viên|Text|Hiển thị mã nhân viên tuyến bưu tá phát thực tế.<br>Nếu không có mã nhân viên→Để trống|
|**Lũy**|**kế tháng**|||
|7|Số ngày kế|Number|Hiển thị số ngày tính KPI lũy kế tháng đến ngày.|
||hoạch|||
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD280|
|---|---|---|
||**BÁO CÁO CÔNG NỢ COD**|Lần ban hành: 1|

## **STT Trường dữ liệu Kiểu dữ liệu Mô tả** 

## **Mô tả chung:** 

- Tần suất cấp nhật dữ liệu: Sau khi chốt số tháng tại ngày 5 ngày N+1, hiển thị 

- báo cáo KPI công nợ COD theo tuyến bưu tá tháng N (chọn bất kỳ ngày nào tháng N tại bộ lọc thời gian đều xuất báo cáo theo tháng từ ngày 1 đến ngày cuối tháng N). 

- Truy cập: Đăng nhập → Truy xuất dữ liệu → Báo cáo KPI công nợ COD theo tuyến bưu tá (lũy kế) 

- Tên file xuất: bckpicongnocodtheobuutaluyke_ddmmyyyy 

- Tên báo cáo: Báo cáo KPI công nợ COD theo tuyến bưu tá (lũy kế) 

- Loại báo cáo: Tài chính 

|**STT**|**Trường dữ liệu**|**Kiểu dữ liệu**|<br>**Mô tả**|
|---|---|---|---|
|**Mô tả chung:**<br>- Tần suất cấp nhật dữ liệu: Sau khi chốt số tháng tại ngày 5 ngày N+1, hiển thị<br>báo cáo KPI công nợ COD theo tuyến bưu tá tháng N (chọn bất kỳ ngày nào<br>tháng N tại bộ lọc thời gian đều xuất báo cáo theo tháng từ ngày 1 đến ngày cuối<br>tháng N).<br>- Truy cập: Đăng nhập → Truy xuất dữ liệu → Báo cáo KPI công nợ COD theo tuyến<br>bưu tá (lũy kế)<br>- Tên file xuất: bckpicongnocodtheobuutaluyke_ddmmyyyy<br>- Tên báo cáo: Báo cáo KPI công nợ COD theo tuyến bưu tá (lũy kế)<br>- Loại báo cáo: Tài chính||||
|- Phân quyền: Chỉ phân quyền cho 1 vài user phòng Tài chính xuất toàn bộ dữ liệu.||||
|1|Vùng|Text|Hiển thị vùng phát thực tế.|
|2|Chi nhánh|Text|Hiển thị mã chi nhánh phát thực tế.|
|3|Vùng con|Text|Hiển thị mã vùng con phát thực tế.|
|4|Bưu cục|Text|Hiển thị bưu cục phát thực tế.|
|5|Tuyến bưu tá|Text|Hiển thị họ và tên tuyến bưu tá phát thực tế.|
|6|Mã nhân viên|Text|Hiển thị mã nhân viên tuyến bưu tá phát thực tế.<br>Nếu không có mã nhân viên→Để trống|
|**Lũy kế tháng**||||
|7|Số ngày kế<br>hoạch|Number|Hiển thị số ngày tính KPI lũy kế tháng đến ngày.<br>Trong đó: Số ngày tính KPI = Số ngày lũy kế từ<br>ngày 1 đến ngày được chọn - Số ngày chủ nhật,<br>ngày Lễ, ngày Tết trong khoảng thời gian xét.<br>Danh sách ngày Lễ, ngày Tết do phòng Chiến<br>lược kinh doanh cung cấp: Quy đổi chi tiết ngày<br>2023 2024 2025.xlsx|
|8|Số ngày đạt KPI|Number|Hiển thị số ngày đạt KPI trong tổng số ngày kế<br>hoạch.<br>Trong đó: Sốngày đạtKPI lànhữngngày cóTỷ|
||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD280|
|---|---|---|---|---|---|
||||**BÁO CÁO CÔNG NỢ COD**||Lần ban hành: 1|
|||||lệ thu công nợ ngày >= 99.9%||
|9|Số tiền phải thu||Number|Hiển thị tổng số tiền thu hộ lũy kế tháng. ĐVT:<br>VNĐ||
|10|Số tiền thu đúng<br>hạn||<br>Number|Hiển thị tổng số tiền thu hộ có thời gian thu <=<br>thời gian đến hạn thu tiền lũy kế tháng.<br>ĐVT: VNĐ||
|11|Tỷ lệ thu công nợ<br>bình quân||<br>Number|Hiển thị tỷ lệ thu công nợ bình quân tháng từ<br>ngày 1 đến ngày được chọn.Công thức:<br>Tỷ lệ thu công nợ bình quân tháng = (Tổng tỷ lệ<br>thu công nợ các ngày tính KPI / Số ngày tính<br>KPI) * 100 (%)<br>Lưu ý:Số ngày tính KPI = Số ngày lũy kế từ<br>ngày 1 đến ngày được chọn - Số ngày chủ nhật,<br>ngày Lễ, ngày Tết trong khoảng thời gian xét.<br>Danh sách ngày Lễ, ngày Tết do phòng Chiến<br>lược kinh doanh cung cấp: Quy đổi chi tiết<br>ngày 2023 2024 2025.xlsx<br>Định dạng:%, làm tròn đến 2 chữ số thập phân.||
|12|Đánh giá||Number|Hiển thị đánh giá.<br>+ Hiển thị Đạt: Nếu Tỷ lệ thu công nợ bình quân<br>>= 99.9%<br>+ Hiển thị Không đạt: Nếu Tỷ lệ thu công nợ bình<br>quân < 99.9%||