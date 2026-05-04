**VIETTEL AI RACE** 

**==> picture [38 x 46] intentionally omitted <==**

**Quy trình lựa chọn hạ tầng lưu trữ dữ liệu** 

Public 320 Lần ban hành: 1 

## **1. Quan điểm, mục đích** 

## **+ Quan điểm:** 

- ✓ Đơn vị cần tuân thủ việc đánh giá đầy đủ qua các bước với các tiêu chí được nêu và căn cứ vào kết quả đánh giá để ra quyết định lựa chọn công nghệ phù hợp với yêu cầu. 

- ✓ Quy trình này hỗ trợ đưa ra căn cứ lựa chọn công trong các chỉ tiêu kỹ thuật cho các dự án mua sắm, đầu tư tài nguyên lưu trữ mới. 

- ✓ Các đơn vị có trách nhiệm cung cấp use cases thường xuyên để quy trình này được cập nhật các tri thức mới. Đánh giá liên tục để đánh giá mức độ phù hợp với thực tế. 

**+ Mục đích:** Quy trình này nhằm quy định thống nhất phương pháp lựa chọn hạ tầng lưu trữ dữ liệu tại các đơn vị. 

## **2. Phạm vi, đối tượng áp dụng** 

- Phạm vi: Áp dụng cho hoạt động đánh giá, lựa chọn hạ tầng lưu trữ dữ liệu. 

- Đối tượng áp dụng: Các cơ quan, đơn vị trong Tập đoàn 

## **3. Tài liệu liên quan** 

|**TT**|**Tài liệu **|**Ngày ban hành**|
|---|---|---|
|1|Bộ tiêu chuẩn Lưu trữ và Vận hành dữ liệu<br>TC.CNVTQĐ.CNTT.40|3/2021|
|2|Quy định xây dựng và áp dụng chỉ tiêu kỹ thuật cho sản<br>phẩm hàng hóa phục vụ hoạt động của Tập đoàn CNVTQĐ<br>mã hiệu 3208/QyĐ-CNVTQĐ-VTNet|9/2020|
|3|Guideline định cỡ cấp phát tài nguyên CNTT mã hiệu<br>GL.CNVTQĐ.CNTT.18.514|09/2021|

## **4. Giải thích thuật ngữ và từ viết tắt** 

## - **Thuật ngữ** 

- **Dữ liệu (Data):** là thông tin được máy tính lưu trữ, xử lý hoặc truy xuất theo yêu cầu của người dùng hoặc theo tiến trình hoạt động của máy tính. 

**VIETTEL AI RACE** Public 320 **Quy trình lựa chọn hạ tầng lưu trữ dữ liệu** Lần ban hành: 1 

**==> picture [38 x 46] intentionally omitted <==**

   - **Hạ tầng lưu trữ dữ liệu:** gồm hệ thống vật lý và logic có nhiệm vụ quản lý và lưu trữ dữ liệu có thể bao gồm SAN (Storage Area Network), NAS (Network Attached Storage), DAS (Direct Attached System), Object Storage và (SDS) Software Define Storage. 

   - **Retention:** Lưu giữ dữ liệu đảm bảo luôn sẵn sàng phục vụ nhu cầu truy xuất của dữ liệu ngay khi có yêu cầu. 

   - **Archive:** Lưu trữ dữ liệu lâu dài. Khi lưu trữ lâu dài, dữ liệu được chuyển từ phân vùng lưu trữ tốc độ truy xuất cao sang phân vùng có hiệu năng thấp hơn. Khi dữ liệu chuyển từ giai đoạn “Retention” sang “Archive” được còn được gọi là “backup offline”. 

   - **Backup dự phòng:** Là việc sao lưu dữ liệu để dự phòng khi có sự cố xảy ra, dữ liệu vẫn đảm bảo tính sẵn sàng phục vụ cho nghiệp vụ. 

   - **Node:** Một máy tính/ máy chủ vật lý lưu trữ và xử lý dữ liệu như một phần của cơ sở dữ liệu phân tán. 

- **Từ viết tắt** 

|**STT**|**Thuật ngữ và từ viết tắt **|**Giải thích**|
|---|---|---|
|1.|CSDL|Cơ sở dữ liệu|
|2.|RDBMS|Relational Database Management System (Hệ quản<br>trịCSDLquan hệ)|
|3.|NoSQL|Non Relational hoặc Not Only SQL: Là loại DBMS<br>dành cho dữ liệu có cấu trúc linh hoạt|
|4.|CNTT|Côngnghệthôngtin|
|5.|QHĐC|Quyhoạch định cỡ|
|6.|VHKT|Vận hành khai thác|

**5. Nội dung quy trình lựa chọn Hạ tầng lưu trữ dữ liệu** 

   - Sự kiện bắt đầu và kết thúc 

      - Sự kiện bắt đầu: Khi có nhu cầu đầu tư hạ tầng lưu trữ dữ liệu mới. 

      - Sự kiện kết thúc: Lựa chọn được hạ tầng lưu trữ dữ liệu phù hợp cho nhu cầu, đưa vào CTKT phục vụ các dự án quy hoạch định cỡ và mua sắm tài nguyên hạ tầng lưu trữ dữ liệu mới. 

      - Đầu vào: Khi có yêu cầu mua sắm, đầu tư tài nguyên hạ tầng lưu trữ mới. 

Public 320 

**VIETTEL AI RACE** 

**Quy trình lựa chọn hạ tầng lưu trữ dữ liệu** 

**==> picture [38 x 46] intentionally omitted <==**

Lần ban hành: 1 

   - Đầu ra: Loại hạ tầng lưu trữ phù hợp với nhu cầu nghiệp vụ và tối ưu chi phí, tài nguyên và nỗ lực vận hành khai thác. 

- Lưu đồ tổng thể quy trình 

**==> picture [454 x 288] intentionally omitted <==**

- Diễn giải chi tiết 

|• Diễn|giải chi tiết|||||
|---|---|---|---|---|---|
|**Bước**|**Hoạt**<br>**động**<br>**chính**|**Công việc thực hiện**|**Phụ trách**<br>**thực hiện**|**Đầu vào**|**Đầu ra**|
|1.|Phân tích,<br>đánh<br>giá<br>các<br>tiêu<br>chí<br>công<br>nghệ<br>về<br>lựa<br>chọn|Khi có nhu cầu đầu tư tài<br>nguyên lưu trữ dữ liệu từ<br>các đơn vị có yêu cầu, đơn<br>vị QHĐC thực hiện phân<br>tích, đánh giá theo các tiêu<br>chí công nghệ sau:<br>-  Kiến trúc lưu trữ|Đơn vị<br>yêu cầu<br>Đơn vị<br>QHĐC|Phân<br>tích<br>yêu cầu về<br>hạ tầng cần<br>đầu tư|Các nhận<br>định  về<br>loại<br>hạ<br>tầng<br>phù<br>hợp<br>với<br>từng<br>tiêu<br>chí sau khi|

**VIETTEL AI RACE** 

**==> picture [38 x 46] intentionally omitted <==**

**Quy trình lựa chọn hạ tầng lưu trữ dữ liệu** 

Public 320 Lần ban hành: 1 

||hạ tầng lưu<br>trữ|- Nhu cầu lưu trữ<br>trong giai đoạn nào<br>của vòng đời dữ<br>liệu<br>(retention,<br>archiving, backup)<br>- Các yêu cầu tính<br>năng và phi tính<br>năng của hạ tầng<br>lưu trữ<br>Chi tiết về các tiêu chí<br>công nghệ cần phân tích,<br>đánh giá theo**Phụ lục 01**.|||đánh<br>giá<br>yêu cầu|
|---|---|---|---|---|---|
|2.|So   sánh<br>các  nhận<br>định<br>sau<br>đánh giá ở<br>Bước<br>1<br>với các<br>loại<br>hạ<br>tầng<br>lưu<br>trữ<br>phổ<br>biến|Sau khi đưa ra nhận định<br>về loại hạ tầng lưu trữ phù<br>hợp với các tiêu chí đánh<br>giá ở Bước 1, đơn vị<br>QHĐC đưa ra các đề xuất<br>về các sản phẩm hạ tầng<br>phù hợp với các ưu tiên<br>của đơn vị yêu cầu, đánh<br>giá dựa trên toàn bộ các<br>tiêu chí công nghệ.<br>Thông tin về các loại hạ<br>tầng lưu trữ phổ biến và<br>các trường hợp áp dụng<br>của chúng xem trong**Phụ**<br>**lục 02.**<br>Thông tin về use cases sử<br>dụng các loại hạ tầng lưu<br>trữ phổ biến tại Viettel<br>xem trong**Phụ lục 05**|ĐV<br>QHĐC|Các loai hạ<br>tầng<br>phù<br>hợp với các<br>tiêu<br>chí<br>công nghệ<br>riêng lẻ|Tổng hợp<br>các loại hạ<br>tầng lưu<br>trữ<br>phù<br>hợp với tất<br>cả các tiêu<br>chí của bài<br>toán.|
|3.|Đánh giá<br>tiêu<br>chí<br>tính<br>phổ<br>biến<br>của|Xem xét tiêu chí về tính<br>phổ biến, mức độ chín<br>muồi và có nhiều phản hồi<br>vềkhảnăng của sảnphẩm|ĐV<br>QHĐC|Các căn cứ<br>đánh<br>giá<br>lựa<br>chọn<br>trong<br>các|Danh sách<br>sản phẩm<br>đáp<br>ứng<br>được tiêu|

Public 320 

**VIETTEL AI RACE** 

**==> picture [38 x 46] intentionally omitted <==**

**Quy trình lựa chọn hạ tầng lưu trữ dữ liệu** 

Lần ban hành: 1 

|||sản phẩm<br>và chi phí|tại các cộng đồng công<br>nghệ trên thế giới.<br>Xem xét chi phí cho 1 đơn<br>vị lưu trữ trên từng loại hạ<br>tầng để chọn loại tối ưu về<br>TCO.|tại các cộng đồng công<br>nghệ trên thế giới.<br>Xem xét chi phí cho 1 đơn<br>vị lưu trữ trên từng loại hạ<br>tầng để chọn loại tối ưu về<br>TCO.|||báo<br>cáo<br>công nghệ<br>của đơn vị<br>và<br>Tập<br>đoàn.<br>Các nguồn<br>thông tin<br>đáng<br>tin<br>cậy.|báo<br>cáo<br>công nghệ<br>của đơn vị<br>và<br>Tập<br>đoàn.<br>Các nguồn<br>thông tin<br>đáng<br>tin<br>cậy.|chí về chi<br>phí<br>và<br>mức<br>độ<br>phổ<br>biến<br>của<br>sản<br>phẩm.|
|---|---|---|---|---|---|---|---|---|---|
|4||Đánh giá<br>năng<br>lực<br>làm<br>chủ<br>sản phẩm,<br>các<br>sản<br>phẩm<br>DBMS và<br>hệ<br>điều<br>hành<br>hỗ<br>trợ|Đơn vị triển khai cài đặt và<br>Đơn vị vận hành hạ tầng<br>lưu trữ đánh giá năng lực<br>làm chủ sản phẩm. Ưu tiên<br>chọn sản phẩm mà đội dự<br>án am hiểu và thành thạo<br>nhất và vận hành đơn giản,<br>ít lỗi.<br>Trường hợp là hạ tầng lưu<br>trữ mới thì cần phải có<br>đánh giá thử nghiệp trước<br>khi ra quyết định lựa chọn.<br>Biểu mẫu đánh giá lựa<br>chọn từ Bước 1,2,3,4 xem<br>trong**Phụ lục 04.**||ĐV<br>QHĐC||Các use<br>cases<br>đội<br>dự án đã<br>triển<br>khai<br>hoặc tham<br>khảo từ các<br>đơn vị<br>khác.<br>Biên<br>bản<br>đánh<br>giá<br>kết quả thử<br>nghiệp theo<br>các tiêu chí<br>công  nghệ<br>được<br>ưu<br>tiên.||Kết<br>quả<br>lựa<br>chọn<br>hạ<br>tầng<br>lưu<br>trữ<br>được Lãnh<br>đạo đơn vị<br>QHĐC và<br>Lãnh đạo<br>đơn vị vận<br>hành   hạ<br>tầng lưu<br>trữ<br>phê<br>duyệt.|
|5||Xây dựng<br>CTKT về<br>Hạ<br>tầng<br>lưu trữ|Đội dự án đưa đưa kết quả<br>lựa chọn hạ tầng lưu trữ ở<br>Bước 4 vào CTKT mua<br>sắm đầu tư mới hạ tầng lưu<br>trữ theo QĐ 3208/QyĐ-<br>CNVTQĐ-VTNet.||ĐV<br>QHĐC||Căn cứ vào<br>kết quả phê<br>duyệt lựa<br>chọn<br>hạ<br>tầng lưu trữ||CTKT hạ<br>tầng<br>lưu<br>trữ|
|• Vai trò của các bên liênquan||||||||||
|**STT**|**Hoạt động chính**|||**ĐV**|**yêu cầu**||**ĐV**<br>**QHĐC**|**ĐV VHKT**<br>**hạ tầng lưu**<br>**trữ**||

**VIETTEL AI RACE** 

**==> picture [38 x 46] intentionally omitted <==**

**Quy trình lựa chọn hạ tầng lưu trữ dữ liệu** 

Public 320 

Lần ban hành: 1 

|1.|Đưa rayêu cầu vềtài nguyên lưu trữ|A/R|||
|---|---|---|---|---|
|2.|Đánh giá, phân tích các tiêu chí về<br>công nghệ, chi phí, và khả năng làm<br>chủ côngnghệ|I|A/R|R|
|3.|Thẩm định và phê duyệt lựa chọn hạ<br>tầnglưu trữ|R|A|R|
|4.|Đưa kết quả lựa chọn hạ tầng lưu trữ<br>vào CTKTphần mềm|I|A/R|C|

## **Giải thích:** 

|**Chữ viết tắt **<br>A<br>R<br>S<br>C<br>I|**Ý nghĩa**<br>|
|---|---|
||Đơn vị/vai trò chịụtrách nhiệmgiải trình kếtquả của hoạt động|
||Đơn vị/vai trò chịu trách nhiệm thực hiện hoạt động<br>|
||Đơn vị/vai trò cungcấpnguồn lực và hỗ trợthực hiện hoạt động|
||Đơn vị/vai trò cung cấp thông tin và tư vấn hỗ trợ trước và trong quá<br>trình thực hiện hoạt động|
||Đơn vị/vai trò được thông báo/cung cấp thông tin sau khi hoạt động<br>được thực hiện|
|**iêu chí, chỉ số**||
|Miêu tả KPI|Công thức tính:_Tỉ lệ tuân thủ quy trình = Tổng số dự án có báo cáo lựa_<br>_chọn hạ tầng lưu trữ đúng quy trình trước khi xây dựng CTKT/ Tổng số_<br>_dự án._<br>Cách tính: Hàng quý đơn vị chịu trách nhiệm rà soát và lấy số lượng trên<br>hệ thống để tínhtỉ lệ.|
|Mục đích KPI|Quản lýviệc tuân thủquytrình.|
|Ngưỡng KPI<br>mục tiêu|<br>>=90% (Kiểm tra thử nghiệm sau 3 tháng sau đó sẽ điều chỉnh ngưỡng<br>KPI theo thực tế)|
|Đơn vị chịu<br>trách<br>nhiệm<br>thực hiện KPI|<br>ĐV QHĐC|

## **6. Tiêu chí, chỉ số đánh giá việc thực hiện quy trình** 

Public 320 Lần ban hành: 1 

**VIETTEL AI RACE Quy trình lựa chọn hạ tầng lưu trữ dữ liệu** 

**==> picture [38 x 46] intentionally omitted <==**

|Đơn vị rà soát<br>việc thực hiện<br>KPI|Đơn vị rà soát<br>việc thực hiện<br>KPI|Bộ phận Quản trị dữ liệu||
|---|---|---|---|
|**Phụ lục đính kèm**<br>||||
|**TT**|**Tênphục lục/ biểu mẫu**<br>||**Mã số**|
|1|Phụlục 01_Các tiêu chí lựa chọn hạtầnglưu trữ<br>||PL01|
|2|Phụlục 02 Các loại hạtầnglưu trữphổbiến||PL02|
|3|Phụ lục 03 So sánh về giá cả và hiệu năng giữa các<br>loại hạtầnglưu trữphổ biến<br>||PL03|
|4|Phụlục 04 Biểu mẫu đánhgiá tổnghợp||PL04|
|5|Phụ lục 05 Danh sách Use cases các hạ tầng lưu trữ<br>phổ biến tại Viettel||PL05|

## **7. Phụ lục đính kèm**