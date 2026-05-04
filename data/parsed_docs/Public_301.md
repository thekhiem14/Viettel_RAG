Public 301 

**VIETTEL AI RACE Giáo Trình Cấu Hình QoS Trên Cisco Catalyst 9400 (Cisco IOS)** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

## **1. Mục lục** 

1. Giới Thiệu Và Mục Tiêu 

2. Kiến Trúc QoS Trên Catalyst 9400 

3. Thành Phần QoS: Classification, Marking, Shaping, Policing, Queuing 

4. Bảng Tra Cứu DSCP/PHB/CoS Và Mapping Queue (Bảng Phức Tạp) 

5. Triển Khai QoS Với MQC (Cisco IOS) 

6. Kịch Bản Thực Hành: Voice + Video + Data 

7. Giám Sát, Kiểm Chứng Và Xử Lý Sự Cố 

8. Lưu Ý, Hạn Chế, Best Practices 

9. Phụ Lục: Thuật Ngữ, Mẫu Cấu Hình 

## **2. Giới Thiệu Và Mục Tiêu** 

Chất lượng dịch vụ (QoS) là tập hợp các cơ chế nhằm ưu tiên lưu lượng quan trọng, đảm bảo độ trễ, jitter và mất gói nằm trong ngưỡng chấp nhận. Giáo trình hướng đến khả năng thiết kế và cấu hình QoS theo chuẩn Cisco IOS, áp dụng cho môi trường doanh nghiệp. 

## **3. Kiến Trúc QoS Trên Catalyst 9400** 

Catalyst 9400 sử dụng Modular QoS CLI (MQC) để định nghĩa class-map, policy-map và áp dụng service-policy vào interface/VLAN. Kiến trúc phần cứng hỗ trợ nhiều hàng đợi (queue) và thuật toán lập lịch. 

**Bảng 2.1 – Pipeline QoS (Heading Nằm Trong Bảng)** 

|**PIPELINE QOS TRÊN THIẾT BỊ (HEADING TRONG BẢNG)**|**PIPELINE QOS TRÊN THIẾT BỊ (HEADING TRONG BẢNG)**|**PIPELINE QOS TRÊN THIẾT BỊ (HEADING TRONG BẢNG)**|**PIPELINE QOS TRÊN THIẾT BỊ (HEADING TRONG BẢNG)**|**PIPELINE QOS TRÊN THIẾT BỊ (HEADING TRONG BẢNG)**|
|---|---|---|---|---|
|Bước|Thành Phần|Đầu Vào|Hành Động|Đầu Ra|
|1|Classification<br>Marking|ACL/DSCP/CoS/NBAR|Xác định lớp<br>lưu lượng|Lớp<br>dịch<br>vụ|
|2||Gói đã phân loại|Gán<br>DSCP/CoS/IP<br>Precedence|Nhãn QoS|
|3|Policing|Nhãn + tốc độ vào|Giới hạn/mark-down/drop<br>Lưu lượng phù hợp ngưỡng||
|4|Shaping|Hàng đợi đầu ra|Điều chỉnh tốc<br>độ, làm mượt|Luồng ổn<br>định|

## **4. Thành Phần QoS** 

Các thành phần chính gồm: Classification & Marking (xác định và gắn nhãn), Policing & Shaping (giới hạn và làm mượt), Queuing & Scheduling (ưu tiên khi nghẽn). 

**Bảng 3.1 – So Sánh Thành Phần QoS (Merge Nhiều Ô)** 

||**SO SÁNH CÁC THÀNH PHẦN QOS**|**SO SÁNH CÁC THÀNH PHẦN QOS**|**SO SÁNH CÁC THÀNH PHẦN QOS**|**SO SÁNH CÁC THÀNH PHẦN QOS**||
|---|---|---|---|---|---|
|Thành Phần|Mục Đích|Ưu Điểm|Nhược<br>Điểm|Tình Huống<br>Dùng|Lưu Ý|
Public 301 

**VIETTEL AI RACE Giáo Trình Cấu Hình QoS Trên Cisco Catalyst 9400 (Cisco IOS)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|Classification|Nhận<br>diện<br>lưu lượng|Chính xác theo ứng dụng<br>Phụ thuộc match|Chính xác theo ứng dụng<br>Phụ thuộc match|Biên mạng|Đồng<br>bộ<br>toàn mạng|
|---|---|---|---|---|---|
|Marking|Gán<br>DSCP/CoS|Ưu<br>tiên<br>xuyên miền|Sai<br>mark<br>gây lệch|Core/Distribution<br>Tuân thủ chính sách||
|Policing|Giới hạn tốc độ<br>Bảo vệ tài nguyên<br>Drop gói|||Biên,<br>ràng<br>buộc|Kết<br>hợp<br>remark-<br>down|
|Shaping<br>Làm mượt lưu|lượng|Giảm burst|Tăng trễ|WAN/Metro|Đặt tốc độ<br>hợp lý|
|Queuing|Xếp<br>hàng<br>theolớp|Đảm<br>bảo<br>ưu tiên|Cấu<br>hình<br>phức tạp|Tại<br>nơi<br>nghẽn|Kết<br>hợp<br>scheduling|

## **5. Bảng Tra Cứu DSCP/PHB/CoS Và Mapping Queue** 

**Bảng 4.1 – DSCP → PHB → CoS → Queue/Schedule (Bảng Vắt Trang)** 

|ST<br>T|Lớp Dịch Vụ|Ứng Dụng|DSC<br>P|PHB|Co<br>S|Queu<br>e|Schedule|
|---|---|---|---|---|---|---|---|
|1|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|2|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|3|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|4|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|5|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|6|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|7|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|8|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|9|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
||Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
**VIETTEL AI RACE** Public 301 

**Giáo Trình Cấu Hình QoS Trên Cisco Catalyst 9400 (Cisco IOS)** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

||Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|---|---|---|---|---|---|---|---|
||Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
||Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
||BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|10|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|11|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|12|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|13|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|14|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|15|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|16|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|17|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|18|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|19|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|20|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|21|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|22|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
**VIETTEL AI RACE** Public 301 

**Giáo Trình Cấu Hình QoS Trên Cisco Catalyst 9400 (Cisco IOS)** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|23|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|---|---|---|---|---|---|---|---|
|24|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|25|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|26|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|27|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|28|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|29|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|30|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|31|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|32|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|33|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|34|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|35|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|36|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|37|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|38|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|39|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
**VIETTEL AI RACE** Public 301 

**Giáo Trình Cấu Hình QoS Trên Cisco Catalyst 9400 (Cisco IOS)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|40|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|---|---|---|---|---|---|---|---|
|41|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|42|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|43|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|44|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|45|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|46|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|47|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|48|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|49|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|50|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|51|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|52|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|53|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|54|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|55|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|56|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
**VIETTEL AI RACE** Public 301 

**Giáo Trình Cấu Hình QoS Trên Cisco Catalyst 9400 (Cisco IOS)** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|57|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|---|---|---|---|---|---|---|---|
|58|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|59|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|60|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|61|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|62|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|63|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|64|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|65|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|66|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
|67|Video|Conf/Streamin<br>g|AF41<br>(34)|Assured<br>Forwardin<br>g|4-5|WFQ<br>Q4|Weighte<br>d|
|68|Control|OSPF/BGP|CS6<br>(48)|Network<br>Control|6|PQ|Strict<br>Priority|
|69|Signaling|SIP/H.323|CS3<br>(24)|Class<br>Selector|3|WFQ<br>Q3|Weighte<br>d|
|70|Transactiona<br>l|DB/ERP|AF31<br>(26)|Assured<br>Forwardin<br>g|3|WFQ<br>Q3|Weighte<br>d|
|71|Bulk|Backup/Sync|AF11<br>(10)|Assured<br>Forwardin<br>g|1|WFQ<br>Q2|Weighte<br>d|
|72|BestEffort|Web/Email|BE<br>(0)|Best Effort|0|WFQ<br>Q1|Weighte<br>d|
|73|Voice|VoIP/SIP|EF<br>(46)|Expedited<br>Forwardin<br>g|5-7|PQ|Strict<br>Priority|
**VIETTEL AI RACE** Public 301 

**Giáo Trình Cấu Hình QoS Trên Cisco** Lần ban hành: 1 **Catalyst 9400 (Cisco IOS)** 74 Video Conf/Streamin AF41 Assured 4-5 WFQ Weighte g (34) Forwardin Q4 d g