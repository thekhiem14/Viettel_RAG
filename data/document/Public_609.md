Public 609 

**VIETTEL AI RACE** Public 609 **ỨNG DỤNG CÔNG NGHỆ ẢO HÓA TRONG VIỆCTỐI ƯU HÓA CƠ SỞ HẠ** Lần ban hành: 1 **TẦNG CÔNG NGHỆ THÔNG TIN** 

**==> picture [39 x 47] intentionally omitted <==**

## **1. YÊU CẦU ĐẶT RA** 

**==> picture [36 x 43] intentionally omitted <==**

- Đáp ứng việc quản lý máychủ và các ứng dụng một cách có hiệu quả, kinhtế hơn, cải thiệntính bảo mật và tính tuân thủ, mang lại sự linh hoạt và nhanh gọn cần thiết để thúc đẩy hiệu năng công việc. - Đơn giản hóa và hợp lý hóa việc quản lý các trang thiết bị phần cứng để giúp kiểm soát chip hí, tăng cường bảo mật và cải thiện khả năng linh hoạt của hệ thống với giải pháp tối ưu hóa hạ tầng CNTT. 

- Quản lý hiệu quả các máychủ ảo và máy chủ vật lý, làm giảm đi sự phức tạp của hệ thống, cải thiện hiệu quả hoạt động, giúp quản lý chi phí, và tăng khả năng thích nghi của hệ thống đối với các yêu cầu công việc luôn thay đổi. 

## **2. GIẢI PHÁP VÀ MÔ HÌNH ỨNG DỤNG** 

## **2.1 Giải pháp đề xuất** 

Xây dựng một hệ thống mạng ảo hóa máy chủ và trung tâm dữ liệu (Datacenter – Server Virtualization) với công nghệ ảo hóa của Vmware, bao gồm: 

   - Hợp nhất các máy chủ: tổng hợp nhiều máy chủ thành một nguồn tài nguyên hợp nhất và duy nhất. 

   - Hợp nhất hệ thống lưu trữ: Toàn bộ hệ thống lưu trữ của công ty có thể bao gồm nhiều thiết bị vật lý khác nhau, được ảo hóa thành một nguồn lưu trữ chung duy nhất từ góc nhìn của các máy chủ, ứng dụng trong hệ thống. Việc chia sẻ và phân chia nguồn lưu trữ này được quản lý tập trung. 

   - Ảo hóa kết nối mạng: ảo hóa các đường kết nối mạng, tạo ra một nguồn chung gồm các kết nối mạng có thể được gán một cách linh hoạt cho các máy tính, máy chủ và các thiết bị trong mạng mà không cần phải thay đổi các kết nối vật lý 

- **2.2 Mục tiêu Ảo hóa toàn bộ hệ thống máy chủ và ứng dụng để loại trừ:** 

- Thời gian trì trệ đầu tư thiết bị máy chủ mới khi triển khai một ứng dụng mới. 

- Thời gian chết (downtime) khi bảo trì hay nâng cấp phần cứng cho hệ thống máy chủ. 

- Tiết giảm không gian của phòng máy chủ, độ phức tạp của hệ thống cáp kết nối và chi phí hàng ngày cho hệ thống điện và làm mát. 

- Khai thác triệt để hiệu năng cũng như công năng của công nghệ và sức mạnh phần cứng máy chủ hiện nay. 

- Quản lý tập trung tại một điểm duy nhất và giảm thiểu các thao tác quản trị. 

- Dễ dàng và linh động triển khai các yêu cầu kinh doanh mới ngay lập tức và sao lưu dự phòng toàn bộ hệ thống. 
**VIETTEL AI RACE** Public 609 **ỨNG DỤNG CÔNG NGHỆ ẢO HÓA TRONG VIỆCTỐI ƯU HÓA CƠ SỞ HẠ** Lần ban hành: 1 **TẦNG CÔNG NGHỆ THÔNG TIN** 

**==> picture [39 x 47] intentionally omitted <==**

## **2.3 Mô hình cơ sở hạ tầng mạng ban đầu** 

Giả sử công ty đang có cơ sở hạ tầng mạng ban đầu chưa áp dụng công nghệ ảo hóa như hình 6 

**==> picture [277 x 227] intentionally omitted <==**

Theo Hình 6, các server là các server vật lý và để tránh tình trạng xung đột giữa các dịch vụ, mỗi dịch vụ sẽ chạy trên một server vật lý riêng biệt (không tận dụng hết tài nguyên máy vật lý). Khi có sự cố xảy ra máy chủ vật lý sẽ ngưng hoạt động. Giải pháp khắc phục vấn đề này là cấp thêm server dự phòng cho mỗi dịch vụ, và như thế sẽ tạo ra sự phức tạp trong quản lý và chi phí đầu tư tốn kém. 

**2.4 Mô hình cơ sở hạ tầng mạng ứng dụng công nghệ ảo hóa** 

**==> picture [254 x 237] intentionally omitted <==**
**VIETTEL AI RACE** Public 609 **ỨNG DỤNG CÔNG NGHỆ ẢO HÓA TRONG VIỆCTỐI ƯU HÓA CƠ SỞ HẠ** Lần ban hành: 1 **TẦNG CÔNG NGHỆ THÔNG TIN** 

**==> picture [39 x 47] intentionally omitted <==**

Theo Hình 7, công ty xây dựng lại cơ sở hạ tầng CNTT bằng cách ứng dụng công nghệ ảo hóa, sử dụng phần mềm ảo hóa VmwareVsphere. Trong mô hình này có nhiều server ảo, thu hẹp số lượng server vật lý đáng kể, giảm chi phí đầu tư thiết bị kết nối mạng, giảm chi phí bảo trì bảo dưỡng, năng lượng, làm mát và các nguồn. tài nguyên khác có liên quan. Khi server vật lý này gặp sự cố, server ảo sẽ tự động được chuyển sang server vật lý khác mà không xuất hiện thời gian chết, tránh làm gián đoạn hệ thống, giúp doanh nghiệp tiết kiệm được chi phí, công tác quản lý đồng thời việc sao lưu dự phòng đơn giản và nhanh chóng hơn. 

**2.5 Phần mềm và thiết bị cần thiết cho triển khai hệ thống** 

**Phần mềm:** Sau đây liệt kê một số phần mềm 

_Bảng 1: Phần mềm cần thiết cho triển khai hệ thống_ 

|**STT**|**Tên phần mềm**|**Bản quyền**|
|---|---|---|
|1|OpenFiler OS|Miễn phí|
|2|Vmware Hypervisor ESXi|Có|
|3|Vmware vSphere Server||
|4|Vsphere Client||
|5|Windows Server 2008 r2||

Thiết bị: 

- Cần 2 máy chủ làm host ESXi Server, cấu hình tối thiểu của máy chủ như sau: CPU 

## _Bảng 2: Cấu hình tối thiểu máy chủ Host ESXi_ 

|_g_|_y_||
|---|---|---|
|STT|Thành phần|Mô tả kỹ thuật|
|1|CPU|CPU 64bit x86, hỗ trợ<br>công nghệ ảo hóa Intel<br>VT-x hoặc AMD RVI|
|2|RAM|2 GB|
|3|HDD|120 GB|
|4|RAID Controller|Có|
Public 609 

**VIETTEL AI RACE** Public 609 **ỨNG DỤNG CÔNG NGHỆ ẢO HÓA TRONG VIỆCTỐI ƯU HÓA CƠ SỞ HẠ** Lần ban hành: 1 **TẦNG CÔNG NGHỆ THÔNG TIN** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|
||SCSI||
||SATA||
|5|Network Interface|Tối thiểu 1|

- Cần 1 máy chủ vCenter Server, cấu hình tối thiểu như sau: 

## _Bảng 3: Cấu hình tối thiểu máy vCenter Server_ 

|STT|Thành phần|Mô tả kỹ thuật|
|---|---|---|
|1|CPU|CPU 64 bit|
|2|RAM|2 GB|
|3|HDD|120 GB|
|5|Network Interface|Tối thiểu a|

- Cần 1 máy giả lập SAN cho hệ thống ảo hóa, cấu hình tối thiểu như sau: 

## _Bảng 4: Cấu hình tối thiểu máy chủ SAN_ 

|STT|Thành phần|Mô tả kỹ thuật|
|---|---|---|
|1|CPU|CPU 32/64 bit|
|2|RAM|2 GB|
|3|HDD|80 GB|
|5|Network Interface|Tối thiểu 1|

## **2.6 Các bước triển khai hệ thống** 

Tiến hành cài đặt hệ thống theo trình tự các bước sau: 

**Bước 1:** Cài đặt Vmware ESXi lần lượt cho2 server ESXi. Đây là 2 host server chạy song songvới nhau, vận hành các máy ảo và khi host này ngưng hoạt động thì host kia sẽ tự động thay thế. 

**Bước 2:** Cài đặt vCenter Server. Đây là máy chủ trung tâm quản lý toàn bộ hệ thống ảo hóa. Các dịch vụ chạy trên máy vCenter Server gồm có: Vsphere Web Client, vCenter Server, vCenter Update Manager. 

**Bước 3:** Cài đặt SAN Server. Đây là máy chủ giả lập hệ thống lưu trữ SANs được dung để hỗ trợ cho các chức năng nâng cao của hệ thống ảo hóa. SAN server chạy hệ điều hành OpenFiler (có thể dùng các ứng dụng khác để giả lập SAN Server). 

**Bước 4:** Cài đặt máy vSphere Client. Đây là một máy client bình thường sử dụng phần mềm vSphere Client dùng kết kết nối vào vCenter Server hoặc host để quản lý. 

**Bước 5:** Dùng vSphere Client kết nối vào vCenter Server sau đó thực hiện cấuhình. Tiến trình cấu hình hệ thống bao gồm các thao tác sau: 

- Liên kết máy ESXi vào vCenter Server(Add host) 

- Tạo Cluster 

- Đưa host vào trong Cluster 
Public 609 

**VIETTEL AI RACE** 

**ỨNG DỤNG CÔNG NGHỆ ẢO HÓA TRONG VIỆCTỐI ƯU HÓA CƠ SỞ HẠ** Lần ban hành: 1 **TẦNG CÔNG NGHỆ THÔNG TIN** 

**==> picture [39 x 47] intentionally omitted <==**

- Kết nối SAN vào hệ thống – 

Tạo máy ảo trên máy chủ ESXi 

**==> picture [36 x 43] intentionally omitted <==**

- Thực hiện kỹ thuật di chuyển máy ảo giữa các host và Datastore 

- Cấu hình Vmware DRS 

- Cấu hình Vmware HA 

- Thực hiện kỹ thuật sử dụngSnapshot 

- Tạo và cấu hình vNetwork Distributed Switch 

## **3. MÔ HÌNH TRIỂN KHAI HỆ THỐNG** 

**==> picture [292 x 214] intentionally omitted <==**

## Hình 8: Mô hình demo Vmware Vsphere 

Để đơn giản quá trình cài đặt, bài báo đưa ra mô hình cài đặt đơn giản và có tính demo như Hình 8, không trình bày chi tiết quá trình cài đặt. Các thành phần sử dụng trong Hình 8 bao gồm 

: - Hệ thống máy chủ host (dùng máy ảo giả lập máy vật lý ESXi Server), số lượng: 2 

- Máy chủ vCenter (dùng máy ảo giả lập máy vật lý), số lượng: 1 

- Máy chủ SAN Storage (dùng máy ảo giả lập máy vật lý), số lượng: 1 

- Máy dùng làm Vsphere Client (dùng máy ảo giả lập máy vật lý), số lượng: 1 

- Phần mềm sử dụng: 

**==> picture [53 x 37] intentionally omitted <==**

+ Microsoft Windows Server 2008 R2. 

+ Vmware Vsphere (Vmware Hypervisor ESXi, Vmware Vsphere) + Openfile OS. 

## **4. TRIỂN KHAI HỆ THỐNG** 

Các bước chính trong quá trình triển khai như sau: 

Bước 1: Quản lý ESXi Server với VM vSphere client 

- Liên kết máy ESXi vào vCenter Server (Add Host) 
Public 609 

**VIETTEL AI RACE** 

**==> picture [39 x 47] intentionally omitted <==**

**ỨNG DỤNG CÔNG NGHỆ ẢO HÓA TRONG VIỆCTỐI ƯU HÓA CƠ SỞ HẠ TẦNG CÔNG NGHỆ THÔNG TIN** 

Lần ban hành: 1 

- Tạo Cluster 

- Đưa host vào trong cluster 

- Sử dụng vSphere Client 

Bước 2: Kết nối SAN vào hệ thống (Add Networking và Add Storage) 

Bước 3: Tạo máy ảo trên máy chủ ESXi 

Bước 4: Di chuyển máy ảo giữa các Host và Datastore 

- Di chuyển máy ảo đã tắt nguồn 

- Di chuyển máy ảo đang chạy bằng StoragevMotion 

- Di chuyển máy ảo đang chạybằngvMotion 

Bước 5: Thực hiện Vmware DRS(Distributed Resource Scheduler) 

Bước 6: Thực hiện Vmware HA(HighAvailability) Bước 7: Sử dụng Snapshot 

Bước 8: Tạo và sử dụng vDS(vNetworkDistributed Switch) 

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**