**VIETTEL AI RACE** Public 319 

**Quy trình lựa chọn DBMS** 

**==> picture [38 x 46] intentionally omitted <==**

Lần ban hành: 1 

## **NỘI DUNG QUY TRÌNH** 

## **1. Quan điểm. mục đích** 

## **+ Quan điểm:** 

- ✓ Quy trình chỉ ra các bước và các tiêu chí đánh giá, nguồn tri thức và thông tin đáng tin cậy để đơn vị làm căn cứ đánh giá, lựa chọn hệ quản trị cơ sở dữ liệu (DBMS). 

- ✓ Đơn vị cần tuân thủ việc đánh giá đầy đủ qua các bước với các tiêu chí được nêu và căn cứ vào kết quả đánh giá để ra quyết định lựa chọn công nghệ phù hợp với dự án. 

- ✓ Quy trình này nằm trong bước phân tích nghiệp vụ trong Quy trình phát triển phần mềm của Tập đoàn, đầu ra của quy trình này sẽ giúp cho đơn vị đưa ra quyết định lựa chọn DBMS một cách đúng đắn, là cơ sở để xây dựng chỉ tiêu về hệ quản trị CSDL trong CTKT và tài liệu giải pháp. 

- ✓ Các đơn vị có trách nhiệm cung cấp use cases thường xuyên để quy trình này được cập nhật các tri thức mới. Đánh giá liên tục để xem có phù hợp với thực tế hay không. 

**+ Mục đích:** Quy trình này nhằm quy định thống nhất phương pháp lựa chọn hệ quản trị CSDL cho các dự án xây mới và nâng cấp phát triển phần mềm. 

## **2. Phạm vi, đối tượng áp dụng** 

- Phạm vi: Áp dụng cho hoạt động đánh giá, lựa chọn hệ quản trị CSDL cho các dự án phần mềm. 

- Đối tượng áp dụng: Các cơ quan, đơn vị trong Tập đoàn 

## **3. Tài liệu liên quan** 

||**3. Tài liệu liên quan**||
|---|---|---|
|**TT**|**Tài liệu**|**Thời gian ban**<br>**hành**|
|1|Bộ tiêu chuẩn Lưu trữ và Vận hành dữ liệu<br>TC.CNVTQĐ.CNTT.40|09/2022|
|2|Quy định thiết lập, quản lý, lưu trữ, khai thác log hệ thống<br>CNTT số 4137/QĐ-CNVTQĐ-CNTT.|9/2021|
|3|Quy định xây dựng, nâng cấp, bảo trì các sản phẩm phần<br>mềm trong Tập đoàn Công nghiệp – Viễn thông Quân đội<br>(3388/QĐ-CNVQTĐ-CNTT)|7/2021|
|4|Bộ tiêu chuẩn lưu trữ và vận hành dữ liệu<br>(TC.CNVTQĐ.CNTT.40)|9/2022|

## **4. Giải thích thuật ngữ và từ viết tắt** 

## - **Thuật ngữ** 

- **Dữ liệu (Data):** là thông tin được máy tính lưu trữ, xử lý hoặc truy xuất theo yêu cầu của người dùng hoặc theo tiến trình hoạt động của máy tính. 

- **Cơ sở dữ liệu:** Chỉ mọi tập hợp dữ liệu được lưu trữ, bất kể cấu trúc hoặc nội dung. Trong một số cơ sở dữ liệu lớn CSDL được nhắc đến như là instances và schema. 

**VIETTEL AI RACE** Public 319 

**Quy trình lựa chọn DBMS** 

**==> picture [38 x 46] intentionally omitted <==**

Lần ban hành: 1 

   - **Instance** : Là một triển khai phần mềm cơ sở dữ liệu (DBMS) có nhiệm vụ kiểm soát quyền truy cập vào một khu vực lưu trữ nhất định. Thường tổ chức có nhiều instance chạy đồng thời, độc lập nhau và mỗi instance kiểm soát truy cập vào các khu vực lưu trữ khác nhau. 

   - **Hệ quản trị CSDL hay DBMS (Database Management System):** Là phần mềm tương tác với người dùng cuối, ứng dụng và chính cơ sở dữ liệu để thu thập và phân tích dữ liệu. Phần mềm DBMS bao gồm các tiện ích cốt lõi được cung cấp để quản trị cơ sở dữ liệu. 

   - **Node:** Một máy tính/ máy chủ vật lý lưu trữ và xử lý dữ liệu như một phần của cơ sở dữ liệu phân tán. 

- **Từ viết tắt:** 

|**STT**|**Thuật ngữ và từ viết tắt **|**Giải thích**|
|---|---|---|
|1.|CSDL|Cơ sở dữ liệu|
|2.|RDBMS|Relational Database Management System (Hệ quản<br>trịCSDLquan hệ)|
|3.|NoSQL|NonRelational hoặc Not Only SQL: Là loại DBMS<br>dành cho dữ liệu có cấu trúc linh hoạt, không cố<br>định.<br>|
|4.|ĐV PTPM|Đơn vịPhát triểnphần mềm|
|5.|ĐV Nghiệp vụ|Đơn vị đặt hàng xây dựng phần mềm, am hiểu về<br>nghiệpvụ.|
|6.|ĐV VHKT|Đơn vịvận hành khai thác cơ sở dữ liệu|

**5. Nội dung quy trình lựa chọn Hệ quản trị cơ sở dữ liệu cho các dự án xây mới, nâng cấp phần mềm** 

## • **Sự kiện bắt đầu và kết thúc** 

   - Sự kiện bắt đầu: Khi có nhu cầu lựa chọn DBMS cho các dự án xây mới, nâng cấp phần mềm. 

   - Sự kiện kết thúc: Lựa chọn được DBMS phù hợp với yêu cầu của bài toán nghiệp vụ, đưa vào CTKT và tài liệu giải pháp của phần mềm được xây mới hoặc nâng cấp. 

   - Đầu vào: Khi có yêu cầu xây mới/ nâng cấp phần mềm. 

   - Đầu ra: DBMS được lựa chọn trong CTKT phần mềm và tài liệu giải pháp. 

- **Lưu đồ tổng thể quy trình** 

**VIETTEL AI RACE** Public 319 

**==> picture [38 x 46] intentionally omitted <==**

**Quy trình lựa chọn DBMS** 

Lần ban hành: 1 

**==> picture [454 x 233] intentionally omitted <==**

- **Diễn giải chi tiết** 

|**Bước**|**Hoạt**<br>**động**<br>**chính**|**Công việc thực hiện**|**Phụ trách**<br>**thực hiện**|**Đầu vào**|**Đầu ra**|
|---|---|---|---|---|---|

|||||**VIETTEL AI RACE**||Public 319|Public 319||
|---|---|---|---|---|---|---|---|---|
|||||**Quy trình lựa chọn DBMS**||Lần ban hành:||1|
||||||||||
|||Đưa ra yêu<br>cầu về dữ<br>liệu||Khi đơn vị nghiệp vụ đưa<br>ra yêu cầu về xây dựng,<br>nâng cấp phần mềm (theo<br>biểu mẫu được quy định<br>trong**Phụ lục 01**), đơn vị<br>PTPM phối hợp với đơn vị<br>nghiệp vụ phân tích, làm<br>rõ các yêu cầu về quản lý,<br>lưu trữ và xử lý dữ liệu của<br>ứng dụng theo các tiêu chí<br>sau:<br>- Cấu trúc dữ liệu<br>- Kiểu tổ chức dữ<br>liệu<br>- Kiểu xử lý dữ liệu<br>- Yêu cầu đảm bảo<br>tính ACID/BASE,<br>các ưu tiên trong<br>định luật CAP<br>- Nhu cầu đọc ghi dữ<br>liệu<br>- Quy mô dữ liệu<br>Chi tiết về các tiêu chí<br>công nghệ cần phân tích,<br>đánhgiá theo**Phụ lục 02**.|ĐV<br>nghiệp vụ;<br>ĐV PTPM||Phân<br>tích<br>yêu cầu xây<br>dựng, nâng<br>cấp<br>phần<br>mềm|Các nhận<br>định  về<br>loại<br>DBMS<br>phù<br>hợp<br>với<br>từng<br>tiêu<br>chí<br>sau<br>khi<br>đánh<br>giá<br>yêu cầu|
||2.|So   sánh<br>các  nhận<br>định<br>sau<br>đánh giá ở<br>Bước<br>1<br>với các<br>loại||Sau khi đưa ra nhận định<br>về loại DBMS phù hợp với<br>các tiêu chí đánh giá ở<br>Bước 1, đơn vị PTPM đưa<br>ra các đề xuất về các sản<br>phẩm DBMS có khả năng<br>đápứng yêu cầu bài toán|ĐV PTPM||Các<br>loai<br>DBMS phù<br>hợp với các<br>tiêu<br>chí<br>công nghệ<br>riêng lẻ|Tổng hợp<br>các<br>DBMS<br>phù<br>hợp<br>với tất cả<br>các   tiêu|

Public 319 

**VIETTEL AI RACE** 

**Quy trình lựa chọn DBMS** 

**==> picture [39 x 46] intentionally omitted <==**

Lần ban hành: 1 

||DBMS<br>phổ<br>biến<br>trên<br>thị<br>trường|về mặt công nghệ, các ưu<br>tiên cần đáp ứng cho bài<br>toán.<br>Thông tin về đặc trưng, so<br>sánh các loại DBMS phổ<br>biến xem trong**Phụ lục**<br>**03.**|||chí của bài<br>toán.|
|---|---|---|---|---|---|
|3.|Đánh giá<br>vấn đề chi<br>phí và bản<br>quyền|Chọn DBMS thương mại<br>khi: Khách hàng có yêu<br>cầu chọn 1 hoặc loại<br>DBMS và đảm bảo có<br>ngân sách của dự án đủ chi<br>trả, hiệu quả kinh doanh<br>vượt trội so với chi phí bỏ<br>ra.<br>Các trường hợp còn lại:<br>Phải ưu tiên chọn DBMS<br>mã nguồn mở và tuân theo<br>HD về sử dụng mã nguồn<br>mở của Tập đoàn.<br>Các lưu ý về chi phí và<br>license cho DBMS xem<br>trong **Phụ lục 04**.|ĐV PTPM|Các căn cứ<br>lựa<br>chọn<br>sản<br>phẩm<br>thương mại|Danh sách<br>sản phẩm<br>đáp<br>ứng<br>được tiêu<br>chí về chi<br>phí/<br>bản<br>quyền.|
|4|Đánh  giá<br>năng lực<br>làm<br>chủ<br>sản phẩm<br>của đội dự<br>án|Đội dự án của ĐV PTPM<br>và Đơn vị VHKT dữ liệu<br>(dự kiến) đánh giá năng<br>lực làm chủ của mình đối<br>với sản phẩm được chọn<br>qua 3 bước trên. Ưu tiên<br>chọn sản phẩm mà đội dự<br>án am hiểu và thành thạo<br>nhất và vận hành đơn giản,<br>ít lỗi.<br>Trường hợp là DBMS mới<br>đốivớiđơnvị thìcầnphải|ĐV PTPM<br>ĐV<br>VHKT|Các use<br>cases<br>đội<br>dự án đã<br>triển<br>khai<br>hoặc tham<br>khảo từ các<br>đơn vị<br>khác.<br>Biên<br>bản<br>đánh<br>giá<br>kết quả thử<br>nghiệptheo|Kết   quả<br>lựa<br>chọn<br>sản phẩm<br>DBMS tối<br>ưu cho dự<br>án<br>được<br>Trưởng dự<br>án và Lãnh<br>đạo đơn vị<br>vận hành<br>CSDL.|

Public 319 

**VIETTEL AI RACE** 

**Quy trình lựa chọn DBMS** 

**==> picture [39 x 46] intentionally omitted <==**

Lần ban hành: 1 

||||có đánh giá thử nghiệp<br>trước khi ra quyết định lựa<br>chọn.<br>Biểu mẫu đánh giá lựa<br>chọn từ Bước 1,2,3,4 xem<br>trong**Phụ lục 05.**<br>Các đơn vị tham khảo<br>thêm kinh nghiệm sử dụng<br>các DBMS phổ biến tại<br>Viettel theo**Phụ lục 06.**|có đánh giá thử nghiệp<br>trước khi ra quyết định lựa<br>chọn.<br>Biểu mẫu đánh giá lựa<br>chọn từ Bước 1,2,3,4 xem<br>trong**Phụ lục 05.**<br>Các đơn vị tham khảo<br>thêm kinh nghiệm sử dụng<br>các DBMS phổ biến tại<br>Viettel theo**Phụ lục 06.**|||các tiêu chí<br>công nghệ<br>được<br>ưu<br>tiên.|các tiêu chí<br>công nghệ<br>được<br>ưu<br>tiên.||
|---|---|---|---|---|---|---|---|---|---|
|5||Xây dựng<br>CTKT về<br>DBMS<br>cho<br>ứng<br>dụng phần<br>mềm|Đội dự án đưa kết quả lựa<br>chọn DBMS ở Bước 4 vào<br>CTKT phần mềm.<br>Xem hướng dẫn xây dựng<br>CTKT cho phần mềm theo<br>**42/HD.00.CNTT.17.**||ĐV PTPM||Căn cứ vào<br>kết quả phê<br>duyệt<br>lựa<br>chọn<br>DMBS||CTKT<br>phần mềm|
|• **Vai trò của các bên liênquan**||||||||||
|**STT**|**Hoạt động chính**<br>|||**ĐV Nghiệp**<br>**vụ**||**ĐV PTPM**||**ĐV VHKT**||
|1.|Đưa rayêu cầu vềdữ liệu|||A/R||S||||
|2.|Lựa chọn sản phẩm có khả năng đáp<br>ứng yêu cầu theo các tiêu chí công<br>nghệ|||R||A/R||I||
|3.|Đánh giá vấn đề chi phí và bản<br>quyền|||I||A/R||R||
|4.|Đánh giá khả năng làm chủ công<br>nghệ|||R||A||R||
|5.|Báo cáo, phê duyệt, thẩm định và<br>đưa vào CTKT|||I||A/R||I||

## **Giải thích:** 

|**Giải thích:**||
|---|---|
|**Chữ viết tắt **|**Ý nghĩa**<br>|
|A|Đơn vị/vai trò chịu trách nhiệmgiải trình kếtquả của hoạt động|
|R|Đơn vị/vai trò chịu trách nhiệm thực hiện hoạt động<br>|
|S|Đơn vị/vai trò cungcấpnguồn lực và hỗ trợthực hiện hoạt động|

**VIETTEL AI RACE** Public 319 

**Quy trình lựa chọn DBMS** 

**==> picture [38 x 46] intentionally omitted <==**

Lần ban hành: 1 

Đơn vị/vai trò cung cấp thông tin và tư vấn hỗ trợ trước và trong quá C trình thực hiện hoạt động Đơn vị/vai trò được thông báo/cung cấp thông tin sau khi hoạt động I được thực hiện 

## **6. Tiêu chí, chỉ số đánh giá việc thực hiện quy trình** 

|Miêu tả KPI|Công thức tính:_Tỉ lệ tuân thủ quy trình = Tổng số dự án có báo cáo lựa_<br>_chọn DBMS đúng quy trình trước khi xây dựng CTKT/ Tổng số dự án._<br>Cách tính: Hàng quý đơn vị chịu trách nhiệm rà soát và lấy số lượng trên<br>hệthốngđể tính tỉ lệ.|
|---|---|
|Mục đích KPI|Quản lýviệc tuân thủquytrình.|
|Ngưỡng KPI<br>mục tiêu|>=90% (Kiểm tra thử nghiệm sau 3 tháng sau đó sẽ điều chỉnh ngưỡng<br>KPI theo thực tế)|
|Đơn  vị  chịu<br>trách<br>nhiệm<br>thực hiện KPI|ĐV PTPM|
|Đơn vị rà soát<br>việc thực hiện<br>KPI|Bộ phận Quản trị dữ liệu|

## **7. Phụ lục đính kèm** 

||**7. Phụ lục đính kèm**||
|---|---|---|
|**TT**|**Tênphục lục/ biểu mẫu**<br>|**Mã số**|
|1|Phụlục 01 Biểu mẫu PYC xâymới,nângcấp phàn mềm|PL01|
|2|Phụlục 02 Các tiêu chí côngnghệ<br>|PL01|
|3|Phụlục 03 Các loại DBMSphổbiến<br>|PL02|
|4|Phụluc 04 Hướngdẫn đánhgiá chiphí và bảnquyền<br>|PL03|
|5|Phụlục 05 Biểu mẫu đánhgiá tổnghợp|PL05|
|6|Phụlục 06 DS Usecase sử dụngDBMS tại Viettel|PL06|