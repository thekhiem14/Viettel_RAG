**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

Lần ban hành: 1 

## **1. Nội dung nâng cấp** 

|**STT**|**Nội dung công việc**|**Chi tiết**|
|---|---|---|
|1|Hạn mức công nợ|Tất cả chức năng liên quan hạn mức công nợ<br>không thay đổi|
|2|Đề xuất hạn mức sản<br>lượng trên App/web|Cho phép người đề xuất nhập tỷ lệ đề xuất→<br>check tỷ lệ theo cấu hình để lấy luồng ký<br>Tự động tính ra sản lượng đề xuất theo mức tỷ lệ<br>nhập|

## **2. Nâng cấp chức năng trên web** 

## **2.1 Màn hình Danh sách Hạn mức bưu cục 2.1.1 Giao diện màn hình Tổng hạn mức bưu cục Mô tả chi tiết màn hình** 

- Màn hình danh sách hạn mức được theo dõi hạn mức công nợ/Hạn mức sản lượng theo Bưu cục. 

- Điều kiện lọc: 

 Chi nhánh 

   - Bưu cục 

   - Nhân viên 

- Phân quyền: 

   - Phân quyền chức năng cho GĐ chi nhánh, Phụ trách bưu cục. 

- User được phân quyền vào chi nhánh/bưu cục nào thì hiển thị thông tin chi 

- nhánh/bưu cục đó. 

- Thông tin hiển thị: 

   - Chi nhánh: Hiển thị thông tin chi nhánh 

   - Bưu cục: Hiên thị bưu cục theo chi nhánh 

- Hạn mức sản lượng: Tổng hạn mức sản lượng áp dụng của tất cả các tuyến thuộc 

- bưu cục 

 Hạn mức công nợ (1): Hạn mức công nợ tổng của bưu cục = Giá trị cố định được cấp + Giá trị đề xuất thêm 

- Hạn mức đã phân bổ (2): Hạn mức công nợ đã được phân bổ cho nhân viên trong 

- bưu cục 

   - Hạn mức còn lại = (1)-(2) 
**VIETTEL AI RACE** 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

- Thao tác: Xem chi tiết→ Gọi đến màn hình 3.2 

- Chức năng import: button Import 

**==> picture [352 x 191] intentionally omitted <==**

- Import hạn mức cố định của nhân viên trong bưu cục: Hạn mức sản lượng và Hạn mức công nợ 

- Phân quyền: phân quyền cho TTVH 

- Chọn loại hạn mức: Cho phép người dùng chọn loại hạn mức để import 

- Nguyên tắc import hạn mức công nợ: 

 Username phải tồn tại trên hệ thống và đang active 

 Nếu tổng hạn mức cố định import <>= Hạn mức cố định hiện tại của Bưu cục 

- ==> cho phép import 

 Nếu  tổng hạn mức cố định import < Hạn mức cố định hiện tại của bưu cục ==> gửi cảnh báo Noti vtman cho TBC  "TTVH đã cập nhật giảm hạn mức cố định của bưu cục, TBC đôn đốc tuyến hoàn thành công nợ để tiếp tục phân công" 

 Dữ liệu import mới được cập nhật lại vào dữ liệu hạn mức cố định hiện tại của bưu tá → cập nhật lại hạn mức của bưu cục → cập nhật lại hạn mức phân bổ = hạn mức cố định của bưu tá  → lưu log cập nhật 

 User có role chi nhánh chỉ được upload dữ liệu chi nhánh user đó quản lý, User có role TCT được upload dữ liệu cho toàn TCT. Nếu upload không đúng dữ liệu chi nhánh quản lý → trả ra lỗi tại các bưu cục chi nhánh không thuộc user đó quản lý. 

- Nguyên tắc import hạn mức sản lượng: 

   - Username phải tồn tại trên hệ thống và đang active 

 Dữ liệu import mới được cập nhật lại vào dữ liệu hạn mức cố định hiện tại của bưu tá → Cập nhật hạn mức áp dụng = hạn mức cố định của bưu tá + mức đề xuất thêm  → lưu log cập nhật 

- Chỉ user có Role TTVH mới thực hiện import. 
**VIETTEL AI RACE** 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

Lần ban hành: 1 

**==> picture [38 x 47] intentionally omitted <==**

**==> picture [189 x 189] intentionally omitted <==**

- Template import: 

- Cho phép xuất excel danh sách hạn mức bưu tá: Template như sau: 

**==> picture [352 x 46] intentionally omitted <==**

- Cho phép xuất excel danh sách hạn mức bưu cục: Template như sau: Hạn-mức-chinhanh 

**==> picture [352 x 83] intentionally omitted <==**

## **2.1.2. Màn hình Chi tiết hạn mức sản lượng của bưu cục** 

Mô tả màn hình: 

|---|---|---|---|---|
|STT|Field<br>Name|Control<br>Type|Editable/<br>Readonly|Description/Note|
|1|STT|Text|Readonly|Hiển thị STT|
|2|Chi nhánh|Text|Readonly|Hiển thị tên chi nhánh|
|3|Tên bưu<br>cục|Text|Readonly|Hiển thị tên bưu cục|
|4|User|Text|Readonly|HIển thị User|
|5|Tên nhân<br>viên|Text|Readonly|Hiển thị tên nhân viên|
**VIETTEL AI RACE** 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|STT|Field<br>Name|Control<br>Type|Editable/<br>Readonly|Description/Note|
|6|Trạng thái<br>hoạt động|Text|Readonly|Hiển thị trạng thái hoạt động|
|7|Hạn mức<br>cố định|Text|Readonly|HIển thị Hạn mức cố định được cấu hình<br>tự động hoặc TTVH cấu hình cho<br>đơn  vị|
|8|Hạn mức<br>áp dụng|Text|Readonly|Hiển thị hạn mức được áp dụng với tuyến<br>bưu tá → là hạn mức bưu tá được sử<br>dụng<br>Hạn mức áp dụng = Hạn mức cố định +<br>Mức phân bổ thêm hoặc Mức đề xuất<br>thêm|
|9|Sửa hạn<br>mức|Button|Editable|Click Sửa hạn mức để Chuyển sang màn<br>hình phân bổ hạn mức|
|10|Đóng|Button|Editable|Click Đóng để tắt popup|

**Màn hình TBC phân bổ hạn mức thêm cho tuyến** 

|---|---|---|---|---|
|**STT**|**Field Name**|**Control**<br>**Type**|**Editable/**<br>**Readonly**|**Description/Note**|
|**Thông tin tổng hợp**|||||
|1|Bưu cục|Text|Readonly|Hiển thị tên bưu cục|
|2|Tổng hạn<br>mức cố định|Text|Readonly|Hiển thị tổng hạn mức cố định của<br>bưu cục =  Tổng hạn mức cố định<br>của tất cả các tuyến thuộc bưu cục|
|3|Tổng hạn<br>mức áp dụng|Text|Readonly|Hiển thị tổng hạn mức áp dụng của<br>tuyến|
|4|Tổng hạn<br>mức đã phân<br>bổ/đề xuất<br>thêm|Text|Readonly|Hiển thị Tổng hạn mức đã phân bổ =<br>Tổng hạn mức áp dụng – Tổng hạn<br>mức cố định|
|**Thông tin chi tiết**|||||
**VIETTEL AI RACE** 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|1|STT|Text|Readonly|Hiển thị STT|
|2|Chi nhánh|Text|Readonly|Hiển thị tên chi nhánh|
|3|Tên bưu cục|Text|Readonly|Hiển thị tên bưu cục|
|4|User|Text|Readonly|HIển thị User|
|5|Tên nhân<br>viên|Text|Readonly|Hiển thị tên nhân viên|
|6|Trạng thái<br>hoạt động|Button|Editable|Cho phép người dùng on/off trạng<br>thái của bưu tá|
|7|Hạn mức cố<br>định|Text|Readonly|HIển thị Hạn mức cố định được cấu<br>hình tự động hoặc TTVH cấu hình<br>cho đơn  vị|
|8|Hạn mức áp<br>dụng|Text|Readonly|Hiển thị hạn mức áp dụng của từng<br>tuyến bưu tá.<br>Hạn mức áp dụng được tính theo<br>nguyên tắc sau:<br>Hạn mức áp dụng = Hạn mức cố định<br>của tuyến + Hạn mức phân bổ thêm<br>hoặc hạn mức đề xuất thêm<br>Lưu ý:<br>- Hạn mức áp dụng không cộng đồng<br>thời với hạn mức phân bổ và Hạn<br>mức đề xuất thêm<br>- Nếu có hạn mức đề xuất thêm→thì<br>hạn mức phân bổ = 0<br>- Nếu không có hạn mức đề xuất<br>thêm→Hạn mức phân bổ = Hạn<br>mức mà TBC phân bổ thêm|
|9|Hạn mức<br>phân bổ|Textbox|Editable|Cho phép TBC phân bổ hạn mức cho<br>các tuyến.<br>Giá trị phân bổ không được lớn hơn<br>25% so với hạn mức cố định của<br>tuyến đó, Nếu lớn hơn hiện thị cảnh<br>báo lỗi "Hạn mức thay đổi không<br>được quá 25% so với Hạn mức cố<br>định của bưu tá"|

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

Lần ban hành: 1 

|---|---|---|---|---|
|||||Lưu ý:<br>- Disable textbox với các tuyến có<br>Hạn mức áp dụng – Hạn mức cố định<br>lớn hơn hoặc bằng 25%<br>- Disable textbox với các tuyến off|
|10|Cập nhật|Button|Editable|Click Cập nhật để lưu trạng thái hoạt<br>động và Hạn mức áp dụng của từng<br>tuyến.|
|11|Đóng|Button|Editable|Click Đóng để tắt popup|

## **2.2 Màn hình Báo cáo tổng hợp hạn mức** 

## **Mô tả chi tiết màn hình** 

## *** Hạn mức sản lượng:** 

- Hạn mức áp dụng: là hạn mức được áp dụng trong ngày của tuyến bưu tá đó 

- Đã sử dụng: là tổng sản lượng đơn đã phân công vào tuyến (đã loại trừ các loại vận đơn không tính hạn mức) + đơn đã PTC trong ngày 

- Còn lại = Hạn mức áp dụng - Đã sử  dụng 

- ➔ Loại trừ các loại bưu gửi sau không trừ hạn mức sản lượng bưu tá: Bill chuyển hoàn (mã dịch vụ - GCH), Bill giao hàng 1 phần (Mã DV – G1P), Bill Báo phát (Mã DV – GBP), Bill đổi hàng (mã DV – GBH) 

Chi tiết Bưu tá: Cho phép xem chi tiết danh sách hạn mức đơn đã phân công và Công nợ của từng tuyến bưu tá 

- Chi tiết phân công: 

Hiển thị danh sách đơn đã phân công nhưng chưa gạch phát 

- Chi tiết công nợ: 

Hiển thị danh sách chi tiết công nợ của tuyến bưu tá, bao gồm: Nợ quá hạn, Nợ sắp quá hạn và Nợ trong hạn. 

## **2.3 [WEB] TRÌNH KÝ ĐỀ XUẤT** 

## **2.3.1 Mô tả chức năng** 

Chức năng cho phép người dùng trình ký lên VOFFICE các đề xuất có trạng thái Chờ trình ký. 
**VIETTEL AI RACE** TD276 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

Chức năng phân quyền cho đối tượng có role tương ứng với vài trò trình ký theo cấu hình ở chức năng _FICO_ → _Quản trị hệ thống à Công nợ nội bộ - Khai báo danh mục._ User có vai trò trình ký, thao tác với dữ liệu tại đơn vị mà user được phân quyền. 

Ngoài ra chức năng được phân quyền cho role TCT để xem dữ liệu và hỗ trợ khi có khiếu nại. User role TCT chỉ được phép xem dữ liệu, không có quyền tác động (trình ký). 

## **2.3.2 Màn hình** 

- _2.3.2.1. Trình ký đề xuất_ 

**==> picture [352 x 142] intentionally omitted <==**

## _2.3.2.2. Chi tiết đề xuất_ 

**==> picture [352 x 60] intentionally omitted <==**

Chi tiết gia hạn  theo bảng kê 

**==> picture [352 x 162] intentionally omitted <==**
**VIETTEL AI RACE** 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

Lần ban hành: 1 

**==> picture [38 x 47] intentionally omitted <==**

Chi tiết gia hạn thời hạn nộp tiền 

## **2.3.3 Mô tả màn hình** 

## _2.3.3.3. Trình ký đề xuất_ 

|**STT**|**Thông tin**|**Kiểu DL**|**Bắt**<br>**buộc**|**Mặc**<br>**định**|**Mô tả**|
|---|---|---|---|---|---|
|**1**|Chọn bưu cục|Combobox|Không|Tất cả|Cho phép chọn bưu cục mà user<br>được phép truy cập, thuộc chi<br>nhánh của bưu cục đang đăng<br>nhập, bao gồm:<br>-        Tất cả: Lấy dữ liệu thuộc<br>tất cả bưu cục mà user đc phép<br>truy cập, theo chi nhánh đang<br>đăng nhập<br>-        Danh sách bưu cục mà<br>user được phép truy cập thuộc<br>chi nhánh đang đăng nhập. Định<br>dạng: [Tên bưu cục] – [Mã bưu<br>cục]<br>Cho phép nhập text tìm kiếm<br>theo tên/mã bưu cục|
|**2**|Chọn loại đề<br>xuất|Combobox|Có|Không|Cho phép chọn loại đề xuất, bao<br>gồm:<br>-        Tất cả: Lấy dữ liệu tất cả<br>các loại đề xuất<br>-        Đề xuất tăng hạn mức<br>(công nợ/sản lượng)<br>-        Đề xuất thay đổi thời hạn<br>nộp tiền<br>-        Đề xuất gia hạn theo đơn-<br>bảng kê<br>Chỉ chọn 1 trong 4 lựa chọn.|

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

## Lần ban hành: 1 

|**STT**|**Thông tin**|**Kiểu DL**|**Bắt**<br>**buộc**|**Mặc**<br>**định**|**Mô tả**|
|---|---|---|---|---|---|
|**3**|Chọn cấp trình<br>ký|Combobox|Không|Không|Chọn cấp trình ký, bao gồm:<br>-        Tất cả<br>-        Danh sách cấp trình ký:<br>Xác định theo danh mục đối<br>tượng được cấu hình tại chức<br>năng_Công nợ nội bộ - Khai báo_<br>_danh mục_. VD: V_GDCN|
|**4**|Chọn trạng thái|Combobox|Không|Không|Cho phép chọn trạng thái trình<br>ký:<br>-        Chờ trình ký: Là các đề<br>xuất chờ trình ký<br>-        Chờ ký duyệt: Là các đề<br>xuất đã trình ký Vof, chờ các<br>cấp ký duyệt<br>-        Đã duyệt: đề xuất được<br>các cấp ký duyệt nhưng chưa<br>đến thời gian hiệu lực<br>-        Đang sử dụng: đề xuất<br>được các cấp ký duyệt và đang<br>trong thời gian hiệu lực<br>-        Hết hạn: đề xuất được các<br>cấp ký duyệt và đã qua thời gian<br>hiệu lực<br>-        Từ chối: đề xuất bị từ chối<br>ký duyệt|
|**5**|Tìm kiếm|Button|Không|Không|Cho phép tìm kiếm đề xuất theo<br>các mục đã chọn|
**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

## Lần ban hành: 1 

|**STT**|**Thông tin**|**Kiểu DL**|**Bắt**<br>**buộc**|**Mặc**<br>**định**|**Mô tả**|
|---|---|---|---|---|---|
|**6**|Trình ký|Button|Không|Không|Cho phép gom trình ký lên<br>Voffice các đề xuất có cùng cấp<br>trình ký.<br>Chỉ enable button khi NSD chọn<br>ít nhất 1 đề xuất và các đề xuất<br>có cùng cấp trình ký<br>Click button à Hiển thị màn<br>hình cho phép nhập các thông<br>tin trính ký (mục 19-22)|
|**7**|Checkbox|Checkbox|Không|Không|Cho phép chọn 1 hoặc nhiều đề<br>xuất|
|**8**|STT|Text|Không|Không|Hiển thị số thứ tự|
|**9**|Chi nhánh|Text|Không|Không|Hiển thị tên chi nhánh|
|**10**|Bưu cục|Text|Không|Không|Hiển thị thông tin bưu cục:<br>Bưu cục [tên bưu cục] – [Mã<br>bưu cục]|
|**11**|Loại đề xuất|Text|Không|Không|Hiển thị loại đề xuất|
|**12**|User|Text|Không|Không|Hiển thị user|
|**13**|Tên nhân viên|Text|Không|Không|Hiển thị tên user|
|**14**|Lý do đề xuất|Text|Không|Không|Hiển thị lý do đề xuất đã chọn|
|**15**|Ghi chú|Text|Không|Không|Hiển thị nội dung Ghi chú đã<br>nhập (nếu có)|
|**16**|Đối tượng phê<br>duyệt|Text|Không|Không|Hiển thị đối tượng phê duyệt<br>cấp tiếp theo mà đối tượng phê<br>duyệt trước đó đã chọn|
|**17**|Thời gian đề<br>xuất|Text|Không|Không|Hiển thị thời gian đề xuất<br>Dd/mm/yyyy<br>Hh:mm:ss|
|**18**|Thời gian cập<br>nhật|Text|Không|Không|Hiển thị thời gian cập nhật: thời<br>gian cập nhật vào danh sách chờ<br>tổng hợp trình ký.|
**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

Lần ban hành: 1 

|**STT**|**Thông tin**|**Kiểu DL**|**Bắt**<br>**buộc**|**Mặc**<br>**định**|**Mô tả**|
|---|---|---|---|---|---|
|**19**|Thao tác|Button|Không|Không|Cho phép xem chi tiết đề xuất<br>Màn hình:**_3.4.3.2_** **_Chi tiết đề_**<br>**_xuất_**|
|**Trình ký đề xuất**||||||
|**20**|Nhập nội dung<br>thực trạng|TextInput|Không|Không|Cho phép nhập nội dung thực<br>trạng, nội dung này sẽ hiển thị<br>trong file mẫu trình ký<br>Maxlength: 1000|
|**21**|Chọn người phê<br>duyệt|Combobox|Không|Không|Cho phép chọn đối tượng phê<br>duyệt theo luồng phê duyệt đã<br>cấu hình.<br>Hiển thị danh sách đối tượng<br>theo luồng phê duyệt.<br>Riêng chân ký TCT-Kế toán<br>trưởng hệ thống sẽ tự động hiển<br>thị đối tượng và không cho phép<br>chọn lại. Đối tượng được lấy<br>theo role TCT – Kế toán trưởng<br>(trường hợp trên hệ thống có<br>nhiều hơn 1 đối tượng có role<br>này, hiển thị ngẫu nhiên 1 đối<br>tượng).<br>Trường hợp không có đối tượng<br>phê duyệt à hiển thị thông báo<br>Message lỗi: "Không xác định<br>được đối tượng [tên role] tại đơn<br>vị, yêu cầu kiểm tra lại ", không<br>cho tạo Trình ký.|
|**22**|Hiển thị chân ký|Radio<br>button|Không|Không|Cho phép người dùng lựa chọn<br>hiển thị (click button) hoặc<br>không hiển thị (không click<br>button) chữ ký trong file trình<br>ký.|
|**23**|Hủy|Button|Không|Không|Cho phép hủy trình ký|
|**24**|Xác nhận|Button|Không|Không|Cho phép xác nhận các thông tin<br>trình ký vừa chọn|
**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

Lần ban hành: 1 

|**STT**|**Thông tin**|**Kiểu DL**|**Bắt**<br>**buộc**|**Mặc**<br>**định**|**Mô tả**|
|---|---|---|---|---|---|
|**Mẫu**|**trình ký**|||||
|**25**|File trình ký|Button|Không|Không|Hiển thị file trình ký mẫu|
|**26**|Phụ lục|Button|Không|Không|Hiển thị file đính kèm của các<br>đề xuất<br>Chỉ hiển thị các file định dạng<br>PDF|
|**27**|Tên chi nhánh|Text|Không|Không|Hiển thị tên chi nhánh trình ký<br>Với các chi nhánh đặc biệt, hiển<br>thị tên theo file phụ lục PTC<br>cung cấp|
|**28**|Mã chi nhánh|Text|Không|Không|Hiển thị mã chi nhánh trình ký|
|**29**|Tỉnh/TP|Text|Không|Không|Hiển thị tên tỉnh, thành phố =<br>tên chi nhánh<br>Với các chi nhánh đặc biệt, hiển<br>thị tên theo file phụ lục|
|**30**|Ngày/tháng/năm|Text|Không|Không|Hiển thị thông tin ngày trính ký|
|**31**|Kính gửi|Text|Không|Không|Tên role của cấp phê duyệt cao<br>nhất|
|**32**|Đề nghị|Text|Không|Không|Tên role của cấp phê duyệt cao<br>nhất|
|**33**|Thực trạng|Text|Không|Không|Hiển thị nội dung thực trạng đã<br>nhập|
|**34**|Chi tiết đề xuất|Text|Không|Không|Hiển thị nội dung chi tiết đề<br>xuất|
|**35**|Kính đề nghị|Text|Không|Không|Tên role của cấp phê duyệt cao<br>nhất|

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

## Lần ban hành: 1 

|**36**|Chân ký|Text|Không|Không|Gắn chân ký theo luồng trình<br>ký.<br>Chân ký Người đề xuất: Hiển thị<br>họ tên người yêu cầu đề xuất (ko<br>gắn chữ ký VOF)<br>Chân ký Trưởng bưu cục:<br>comment số 1, gắn chân ký theo<br>mã nhân viên của người trình ký<br>– cố định hiển thị.<br>Các chân ký sau sẽ phụ thuộc<br>vào luồng ký và cấu hình trình<br>ký có hiển thị chân ký hay ko.<br>Người phê duyệt có hiển thị chữ<br>ký tương ứng với các comment<br>(gắn chân ký): 2, 3, 4.<br>Chân ký GĐCN : Comment số 2<br>Chân ký Trưởng nhóm đối soát:<br>Comment số 3<br>Chân ký P.Tài chính: Comment<br>số 4<br>Chân ký nào ko đc gắn chân ký<br>à ko hiển thị trên file trình ký<br>VD: Luồng ký bao gồm:<br>1.     Phó GĐCN: Chọn ko hiển<br>thị chữ ký<br>2.     GĐCN: Chọn hiển thị chữ<br>ký<br>3.     TCT – Kế toán đối soát:<br>Chọn ko hiển thị chữ ký<br>4.     TCT – Kế toán trưởng:<br>Chọn hiển thị chữ ký|
|---|---|---|---|---|---|

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

## Lần ban hành: 1 

|**STT**|**Thông tin**|**Kiểu DL**|**Bắt**<br>**buộc**|**Mặc**<br>**định**|**Mô tả**|
|---|---|---|---|---|---|
||||||è Comment 1: Gắn tại chân ký<br>Trưởng bưu cục, Hiển thị chữ<br>ký của người trình ký<br>è Comment 2: Gắn tại chân ký<br>Giám đốc chi nhánh, hiển thị<br>chữ ký của role GĐCN<br>è Comment 3: Gắn tại chân ký<br>Trưởng nhóm đối soát, hiển thị<br>chữ ký của role Kế toán trưởng.<br>è Comment 4: Ko đc khai báo<br>nên ko hiển thị chân ký P.TC<br>trong file trình ký|
|**37**|Hủy|Button|Không|Không|Cho phép hủy thao tác trình ký|
|**38**|Trình ký|Button|Không|Không|Cho phép trình ký theo cài đặt<br>đã chọn. Click button hệ thống<br>gọi đến màn hình đăng nhập<br>VOF, yêu cầu NSD nhập thông<br>tin user, pass để đăng nhập trình<br>ký VOF|

## **2.3.4 Yêu cầu nghiệp vụ chi tiết** 

Chức năng cho phép người dùng – đối tượng được cấu hình vai trò trình ký trong luồng phê duyệt liên quan đến thời hạn nộp tiền hoặc hạn mức (cấu hình vai trò tại chức năng  ( _FICO_ à _Quản trị hệ thống_ à _Công nợ nội bộ - Khai báo danh mục_ à _Khai báo danh mục thời hạn nộp tiền_ và _Cấu hình luồng phê duyệt_ ) 

Sau khi khai báo, hệ thống sẽ xác định luồng phê duyệt, đối tượng có vai trò trình ký tương ứng với thông tin đề xuất (so sánh với thông tin cấu hình luồng phê duyệt). Khi đến chân phê duyệt của đối tượng có vai trò trình ký, đề xuất sẽ được cập nhật trạng thái Chờ trình ký, hiển thị tại màn hình đề xuất trình ký của đối tượng. 

Chỉ thực hiện trình ký được với các đề xuất trạng thái Chờ trình ký, có thể chọn nhiều đề xuất, nhưng phải cùng loại đề xuất (thời hạn nộp tiền/hạn mức/gia hạn đơn-bảng kê) thì mới cho trình ký trong cùng 1 lượt  (do luồng ký của các loại đề xuất có thể khác nhau). 

Các bước trình ký: 
**VIETTEL AI RACE** TD276 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU** Lần ban hành: 1 **TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

**Bước 1** : Người dùng chọn các đề xuất cùng loại, trạng thái Chờ trình ký để thực hiện trình ký. Hệ thống hiển thị màn hình trính ký, hiển thị role trong luồng phê duyệt (theo cấu hình) lần lượt từ trên xuống, cho phép chọn đối tượng ký duyệt, chỉ hiển thị danh sách đối tượng có role tương ứng với luồng phê duyệt đã cấu hình. Đồng thời chọn xem đối tượng có hiển thị chữ ký trong luồng phê duyệt hay không. Khi chọn đối tượng, hệ thống kiểm tra đối tượng có thông tin trên VOF hay không, thông qua mã nhân viên của đối tượng được chọn, nếu không có thông tin trên VOF, hệ thống hiển thị cảnh báo: ”Người dùng không có thông tin ký Voffice. Vui lòng kiểm tra lại mã nhân viên”, và không cho tạo trình ký. 

**Bước 2:** Sau khi xác nhận thông tin cấu hình trình ký (xác định đối tượng, có hiển thị chữ ký hay ko). Hệ thống lần lượt xác định hiển thị chữ ký tại các chân ký (comment). Chân ký (comment) sẽ tương ứng với số lượng đối tượng phê duyệt 

- Comment 1: Tương ứng chân ký của Người trình ký – tên chân ký Trưởng bưu cục (theo quy định hiện tại) 

- Comment 2: Tương ứng chân ký của đối tượng phê duyệt thứ 2 trong luồng ký - Tên chân ký lấy theo Chức danh phê duyệt trong cấu hình 

- Comment 3: Tương ứng chân ký của đối tượng phê duyệt thứ 3 trong luồng ký - Tên chân ký lấy theo Chức danh phê duyệt trong cấu hình 

- Comment n: Tương ứng chân ký của đối tượng phê duyệt thứ n trong luồng ký - Tên chân ký lấy theo Chức danh phê duyệt trong cấu hình 

Căn cứ vào cấu hình hiển thị chữ ký, hệ thống sẽ gán tương ứng từ comment số 2, 3, 4 với các đối tượng được cấu hình hiển thị chữ ký từ trên xuống dưới. Comment nào ko có đối tượng hiển thị chữ ký sẽ được ẩn khỏi file trình ký. 

VD1: Cấu hình luồng ký bao gồm: 

1. Role Phó GĐCN: Chọn ko hiển thị chữ ký 

2. Role GĐCN: Chọn hiển thị chữ ký 

3. Role TCT – Kế toán đối soát: Chọn ko hiển thị chữ ký 

4. Role TCT – Kế toán trưởng: Chọn hiển thị chữ ký 

- Comment 1: Gắn tại chân ký Trưởng bưu cục, Hiển thị chữ ký của người trình ký 

- Comment 2: Gắn tại chân ký Giám đốc chi nhánh, hiển thị chữ ký của role GĐCN 

- Comment 3: Gắn tại chân ký Trưởng nhóm đối soát, hiển thị chữ ký của role Kế toán trưởng. 

- Comment 4: Ko đc khai báo nên ko hiển thị chân ký P.TC trong file trình ký 

VD2: Cấu hình luồng ký bao gồm: 

1. Role Phó GĐCN: Chọn ko hiển thị chữ ký 

2. Role GĐCN: Chọn hiển thị chữ ký 
**VIETTEL AI RACE** TD276 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU** Lần ban hành: 1 **TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

- Comment 1: Gắn tại chân ký Trưởng bưu cục, Hiển thị chữ ký của người trình ký 

- Comment 2: Gắn tại chân ký Giám đốc chi nhánh, hiển thị chữ ký của role GĐCN 

- Comment 3, 4: Ko đc khai báo chữ ký nên ko hiển thị chân ký Trưởng nhóm đối soát và Kế toán trưởng trong tờ trình. 

**Bước 3:** Sau khi xác nhận nội dung trong file trình ký, người dùng chọn Trình ký, hệ thống hiển thị màn hình cho phép nhập thông tin user, pass tài khoản Voffice để đăng nhập trình ký. 

Đăng nhập thành công, hiển thị màn hình các thông tin trình ký: 

- Trích yếu nội dung: Đề xuất nâng hạn mức/tăng thời hạn nộp tiền/gia hạn thời gian nộp tiền - Chi nhánh:[Tên chi nhánh thực hiện trình ký] -Bưu cục: [Tên bưu cục thực hiện trình ký] 

- Nội dung: Đề xuất nâng hạn mức/tăng thời hạn nộp tiền/gia hạn thời gian nộp tiền - Chi nhánh:[Tên chi nhánh thực hiện trình ký] -Bưu cục: [Tên bưu cục thực hiện trình ký] 

- Hình thức văn bản: Đề xuất 

- Độ khẩn: Khẩn 

- Danh sách người ký: Hiển thị danh sách người ký đã chọn và cấu hình tại màn hình Trình ký đề xuất dựa theo mã nhân viên của đối tượng được chọn để xác định người ký tương ứng trên hệ thống VOF. 

- Văn bản trình ký: là file mẫu trình ký 

- Văn bản đính kèm: Hiển thị các file đính kèm (dạng PDF) của các đề xuất có trong lượt trình ký. (Các file đính kèm khác định dạng PDF không thể hiển thị lên lượt trình ký) 

Trình ký thành công, hệ thống cập nhật trạng thái đề xuất thành Chờ ký duyệt. Tờ trình đc các cấp phê duyệt, hệ thống trạng thái đề xuất Đã duyệt/Đang sử dụng/Hết hạn phụ thuộc vào thời gian áp dụng. Tờ trình bị từ chối, hệ thống cập nhật trạng thái đề xuất thành Từ chối. Với các đề xuất trạng thái từ chối, người đề xuất phải đề xuất lại từ đầu. 

Vận hành: Để đảm bảo thông tin trình ký, có đối tượng để chọn phê duyệt theo luồng cấu hình, P.TC yêu cầu đơn vị khai báo đủ các role theo luồng ký tại tất cả các đơn vị. 

## **Chức năng ảnh hưởng** : 

- Thêm trường thông tin Vai trò phê duyệt cho các đối tượng tại chức năng: _FICO_ à _Quản trị hệ thống_ à _Công nợ nội bộ - Khai báo danh mục_ à _Khai báo danh mục thời hạn nộp tiền_ và _Cấu hình luồng phê duyệt_ 

Cho phép chọn các Vai trò: 

- Phê duyệt: Đối tượng thực hiện phê duyệt trên app Vtman/web Fico 

- Trình ký: Đối tượng thực hiện phê duyệt trên app Vtman/web Fico, sau đó tổng hợp trình ký các đề xuất lên Voffice để các cấp tiếp theo ký duyệt trên Vofice 
**VIETTEL AI RACE** TD276 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU** Lần ban hành: 1 **TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

- Ký duyệt: Đối tượng thực hiện phê duyệt (ký duyệt) trên Voffice. 

- Bổ sung trạng thái đề xuất: 2 trạng thái Chờ trình ký, Chờ ký duyệt. Áp dụng cho tất cả các loại đề xuất. 

- **Chờ trình ký:** đề xuất đã qua 1 hoặc nhiều cấp phê duyệt trên app VTMan/web fico, đang chờ được tổng hợp trình ký lên Voffice. Đối tượng tổng hợp trình ký sẽ được P.TC khai báo vai trò tại chức năng _FICO_ à _Quản trị hệ thống_ à _Công nợ nội bộ - Khai báo danh mục_ à _Khai báo danh mục thời hạn nộp tiền_ và _Cấu hình luồng phê duyệt_ 

- **Chờ ký duyệt:** đề xuất đã được trình ký lên Voffice, đang chờ các cấp ký duyệt. 

## **2.4 [WEB] Danh sách đề xuất Hạn mức bưu cục 2.4.1 Màn hình danh sách đề xuất** 

Mô tả Màn hình danh sách đề xuất 

|---|---|---|---|---|
|**STT**|**Field**<br>**Name**|**Control**<br>**Type**|**Editable/**<br>**Readonly**|**Description/Note**|
|**Tra cứu**|||||
|1|Thời<br>gian đề<br>xuất|Calendar|Editable|Cho phép người dùng chọn khoảng thời gian<br>đề xuất.<br>Giới hạn chọn tới ngày hiện tại|
|2|Chi<br>nhánh|Dropdown<br>list|Editable|Hiển thị danh sách chi nhánh cho người dùng<br>chọn<br>Mặc định theo phân quyền<br>Nếu role TCT → hiển thị tất cả chi nhánh cho<br>người dùng chọn<br>Nếu role chi nhánh → mặc định chi nhánh  mà<br>user quản lý - không cho phép chọn<br>Nếu role Bưu cục → Hiện thị mặc định chi<br>nhánh quản lý bưu cục - không cho phép chọn|
**VIETTEL AI RACE** 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|**STT**|**Field**<br>**Name**|**Control**<br>**Type**|**Editable/**<br>**Readonly**|**Description/Note**|
|3|Bưu cục|Dropdown<br>list|Editable|Hiển thị danh sách bưu cục cho người dùng<br>chọn<br>Mặc định theo phân quyền<br>Nếu role TCT → hiển thị tất cả bưu cục thuộc<br>chi nhánh đã chọn cho người dùng chọn<br>Nếu role chi nhánh → hiển thị danh sách bưu<br>cục mà user quản lý<br>Nếu role Bưu cục → Hiện thị mặc định bưu<br>cục- không cho phép chọn|
|4|Nhân<br>viên|Dropdown<br>list|Editable|Hiển thị danh sách mã nhân viên thuộc bưu<br>cục quản lý khi chọn Buu cục.<br>Nếu không chọn bưu cục → không cho phép<br>chọn  Nhân viên|
|5|Trạng<br>thái|Dropdown<br>list|Editable|Hiển thị danh sách trạng thái của đề xuất<br>▪<br>Chờ trình ký → TBC tạo đề xuất thành<br>công và chờ trình ký Voff<br>▪<br>Chờ ký duyệt → đã trình ký voff và<br>đang chờ kết quả trình ký<br>▪<br>Hủy → TBC đã hủy đề xuất<br>▪<br>Từ chối → đề xuất đã bị từ chối Voff<br>▪<br>Đã duyệt → Đề xuất đã được phê<br>duyệt voff nhưng chưa đến thời gian<br>áp dụng<br>▪<br>Đang sử dụng → Đề xuất đã được phê<br>duyệt và đến thời gian áp dụng<br>▪<br>Hết hạn → là đề xuất đã hết hạn áp<br>dụng|
|6|Tìm<br>kiếm|Button|Editable|Click Tìm kiếm đề lọc dữ liệu theo điều kiện<br>tìm kiếm|
|**Dữ liệu chi tiết**|||||
|1|STT|Text|Readonly|Hiển thị STT → click vào dòng STT hiển thị<br>danh sách đề xuất thuộc bưu cục hiển thị|
**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

Lần ban hành: 1 

|---|---|---|---|---|
|**STT**|**Field**<br>**Name**|**Control**<br>**Type**|**Editable/**<br>**Readonly**|**Description/Note**|
|2|Chi<br>nhánh|Text|Readonly|Hiển thị chi nhánh|
|3|Bưu cục|Text|Readonly|Hiển thị tên bưu cục|
|4|Tài<br>khoản<br>đề xuất|Text|Readonly|Hiển thị tài khoản đề xuất (username)|
|5|Nhân<br>viên đề<br>xuất|Text|Readonly|Hiển thị  tên nhân viên  đề xuất|
|6|Loại đề<br>xuất|Text|Readonly|Hiển thị  tên loại đề xuất|
|7|Hạn<br>mức<br>bưu cục<br>cũ|Text|Readonly|Hiển thị hạn mức hiện tại của bưu cục|
|8|Hạn<br>mức đề<br>xuất bổ<br>sung<br>thêm|Text|Readonly|Hiển thị hạn mức bổ sung thêm|
|9|Áp<br>dụng từ<br>ngày|Text|Readonly|Hiển thị thời gian bắt đầu áp dụng|
|10|Áp<br>dụng<br>đến<br>ngày|Text|Readonly|Hiển thị thời gian hết hạn|
|11|Lý<br>do<br>đề xuất|Text|Readonly|Hiển thị lý do đề xuất|
|12|Ghi chú|Text|Readonly|Hiển thị ghi chú theo lý do đề xuất|
|13|File<br>đính<br>kèm|Hyperlink|Editable|Hiển thị file đính kèm|
**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

## Lần ban hành: 1 

|---|---|---|---|---|
|**STT**|**Field**<br>**Name**|**Control**<br>**Type**|**Editable/**<br>**Readonly**|**Description/Note**|
|14|Đối<br>tượng<br>phê<br>duyệt|Text|Readonly|Hiển thị đối tượng phê duyệt cuối cùng theo<br>luồng ký|
|15|Trạng<br>thái|Text|Readonly|Hiển thị trạng thái của đề xuất|
|16|Lý<br>do<br>từ chối|Text|Readonly|Hiển thị lý do từ chối  trên Voff (Nếu lấy được)|
|17|File tờ<br>trình|Hyperlink|Editable|Hiển thị tên file tờ trình đã ký trên voff. Hiển<br>thì khi luồng ký được phê duyệt ban hành.<br>Click Tên file cho phép tải về file|
|18|Thời<br>gian đề<br>xuất|Text|Readonly|Hiển thị thời gian tạo đề xuất thành công|
|19|Thời<br>gian<br>cập<br>nhật|Text|Readonly|Hiển thị thời gian đề xuất được phê duyệt thành<br>công. Ký duyệt ban hành.|
|20|Thao<br>tác|Text|Editable|Cho phép người dùng thao tác với các trạng<br>thái.<br>▪<br>Sửa: cho phép sửa lại đề xuất với trạng<br>thái chờ trình ký của loại đề xuất Hạn<br>mức công nợ, ko cho phép sửa với loại<br>Hạn mức sản lượng<br>▪<br>Xóa: cho phép xóa đề xuất có các<br>trạng thái Chờ trình ký, Đang sử<br>dụng → Cập nhật về trạng thái Hủy.<br>TH với trạng thái Đang sử dụng khi<br>hủy sẽ trừ hạn  mức đã đề xuất.|
|21|Đề xuất|Button|Editable|Click button đề xuất → Chuyển màn hình 3.8.2|

Nghiệp  vụ chi tiết: 

*** Loại đề xuất Hạn mức công nợ:** 
**VIETTEL AI RACE** TD276 **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU** Lần ban hành: 1 **TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

- User được phép trình ký nhiều đề xuất cùng loại và cùng luồng ký 

- Sau khi ký duyệt thành công → Cộng hạn mức vào tổng hạn mức của bưu cục 

- ▪ TH đề xuất hết hạn → Cấp nhật về trạng thái Hết hạn → Cập nhật hạn mức phân bổ của tuyến = Hạn mức cố định của tuyến đó 

- TH hủy đề xuất Đang sử dụng → Cập nhật về trạng thái Hủy → Cập nhật hạn mức phân bổ của tuyến = Hạn mức cố định của tuyến đó 

## *** Loại đề xuất Hạn mức Sản lượng:** 

- User được phép trình ký nhiều đề xuất cùng loại và cùng luồng ký 

- Sau khi ký duyệt thành công → Cộng hạn mức vào hạn mức của tuyến đề xuất 

- • TH đề xuất hết hạn → Cấp nhật về trạng thái Hết hạn → Cập nhật hạn mức cố định của tuyến về hạn mức cố định ban đầu → cập nhật lại Hạn mức áp dụng cho các tuyến 

- TH hủy đề xuất Đang sử dụng → Cập nhật về trạng thái Hủy → Cập nhật hạn mức cố định của tuyến về hạn mức cố định ban đầu → cập nhật lại Hạn mức áp dụng cho các tuyến 

## **2.4.2 Màn hình thêm mới đề xuất** 

**==> picture [445 x 138] intentionally omitted <==**

Màn hình nếu chọn Hạn mức sản lượng 

**==> picture [469 x 145] intentionally omitted <==**

Mô tả Màn hình thêm mới đề xuất: 
**VIETTEL AI RACE** 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|**STT**|**Field**<br>**Name**|**Control**<br>**Type**|**Editable/**<br>**Readonly**|**Description/Note**|
|1|Loại<br>đề<br>xuất|Dropdown<br>list|Editable|Hiển thị danh sách loại đề xuất cho người<br>dùng chọn<br>•<br>Loại đề xuất: Hiển thị theo phân<br>quyền.<br>Giá trị hiển thị:<br>Hạn mức sản lượng: Hiển thị với<br>tất cả các role kể cả TBC<br>Hạn mức công nợ: Chỉ hiển thị nếu<br>là role TBC|
|2|Hạn mức<br>đề xuất|Textbox|Editable|Cho phép người dùng nhập giá trị. Giá trị<br>nhập là số nguyên dương và lớn hơn mức<br>cấu hình nhỏ nhất<br>Hower chuột vào icon<br>hiển thị tooltip:<br>“Nhập mức tỷ lệ lớn hơn 25%”<br>Sau khi nhập tỷ lệ→Click Enter hoặc nhấp<br>chuột→Hệ thống tính giá trị đề xuất thêm<br>theo công thức:<br>Hạn mức đề xuất thêm = Hạn mức cố định *<br>tỷ lệ đã nhập.|
|3|Lý do đề<br>xuất|Dropdown<br>list|Editable|Hiển thị danh sách lý do đề xuất (lấy theo<br>cấu hình)|
|4|Người<br>phê duyệt|Dropdown<br>list|Editable|Hiển thị danh sách Chọn người duyệt cấp<br>phê duyệt đầu tiên, lấy danh sách theo cấu<br>hình luồng ký.<br>Chỉ hiển thị nếu chọn loại đề xuất là Hạn<br>mức sản lượng|
|5|Thời gian<br>áp dụng|Calendar|Editable|Cho phép chọn thời gian áp dụng. chỉ cho<br>phép chọn trong khoảng thời gian 7 ngày<br>Giá trị mặc định: 7 ngày tính từ ngày hiện<br>tại|
**VIETTEL AI RACE** 

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|6|File đính<br>kèm|File|Editable|Cho phép import lên file đính kèm|
|7|Lưu|Button|Editable|Click Lưu để lưu cấu hình<br>Nguyên tắc lưu  cấu hình: tạo đề xuất thành<br>công nếu đạt đủ các yêu cầu sau:<br>1. Bưu cục không tồn tại đề xuất có 1<br>trong các trạng thái trạng thái Đang<br>sử dụng, chờ trình ký, Đã duyệt, Chờ<br>ký duyệt<br>2. Nếu tồn tại mục 1 thì check thời gian<br>áp dụng ko trùng với khoảng áp<br>dụng của các đề xuất đã tồn tại với<br>trạng thái Đang sử dụng, chờ trình<br>ký, Đã duyệt, Chờ ký duyệt|
|8|Đóng|Button|Editable|Click Đóng để tắt popup cập nhật|

Nếu là đề xuất Hạn mức sản lượng→ cập nhật đề xuất trạng thái Chờ duyệt → TBC phê duyệt và trình ký 

Nếu là đề xuất Hạn mức công nợ → Cập nhật đề xuất trạng thái Chờ trình ký → TBC thực hiện trình ký 

|---|---|---|---|---|---|
|**5.**|Thời<br>gian<br>cập<br>nhật|Text|N/A|Readonly|Hiển thị thời gian<br>cập nhật|
|**6.**|Người<br>cập<br>nhật|Text|N/A|Readonly|Hiển thị thông tin<br>người cập nhật|

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

## Lần ban hành: 1 

|**7.**|Thao<br>tác|Button|N/A|Editable|Hiển thị icon cho<br>người dùng chọn.<br>Hiển thị tooltip<br>tương ứng khi<br>hower icon:<br>- Sửa : Cho phép<br>người dùng sửa<br>cấu hình.<br>- Xem lịch sử:<br>Cho phép người<br>dùng xem lịch sử<br>chỉnh sửa|
|---|---|---|---|---|---|
|**II.**|Màn hình cập nhật cấu hình|||||
|**8**|Chọn<br>Kỳ<br>đánh<br>giá|Texbox|Yes|Editable|Cho phép người<br>dùng chọn số<br>ngày. Giá trị nhập<br>vào là số nguyên<br>dương lớn hơn<br>hoặc = 0|
|**9**|Loại<br>đánh<br>giá|Dropdownlist|Yes|Editable|Cho phép người<br>dùng chọn kỳ<br>đánh giá:<br>Giá trị hiển thị:<br>- Không tính T7,<br>CN<br>- Tính T7, CN<br>Giá trị mặc định:<br>Không tính T7,<br>CN|
**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

## Lần ban hành: 1 

|---|---|---|---|---|---|
|**10**|Trạng<br>thái<br>hoạt<br>động|Button|N/A|Readonly|Cho phép người<br>dùng on/off cấu<br>hình. Áp dụng<br>cho cấu hình mới<br>nhất.<br>Nếu cấu hình mới<br>nhật = off→tức<br>là không có cấu<br>hình kỳ đánh giá<br>→hạn mức cố<br>định = kỳ đánh<br>giá gần nhất|
|**11**|Đóng|Button|N/A|Editable|Đóng<br>yêu<br>cầu<br>chỉnh<br>sửa<br>cấu<br>hình|
|**12**|Lưu|Button|N/A|Editable|Click Lưu để lưu<br>thông tin cấu hình<br>cảnh báo.<br>Cập nhật toàn bộ<br>cấu hình cũ về<br>trạng thái Không<br>hoạt động.|
|**III.**|Lịch sử cập nhật cấu hình<br>Hiển thị danh sách lịch sử cấu hình|||||
|**13**|STT|Text|N/A|Readonly|Hiển thị STT|
|**14**|Kỳ<br>đánh<br>giá|Text|N/A|Readonly|Hiển thị kỳ đánh<br>giá theo cấu hình|
|**15**|Loại<br>đánh<br>giá|Text|N/A|Readonly|Hiển thị loại đánh<br>giá theo cấu hình|
|**16**|Trạng<br>thái<br>hoạt<br>động|Lable|N/A|Readonly|Hiển thị trạng<br>thái hoạt động<br>của cấu hình|
**VIETTEL AI RACE** TD276 

**==> picture [38 x 47] intentionally omitted <==**

**NÂNG CẤP HẠN MỨC CÔNG NỢ BƯU TÁ** 

Lần ban hành: 1 

|---|---|---|---|---|---|
|**17**|Thời<br>gian<br>cập<br>nhật|Text|N/A|Readonly|Hiển thị thời gian<br>cập nhật|
|**18**|Người<br>cập<br>nhật|Text|N/A|Readonly|Hiển thị thông tin<br>người cập nhật|