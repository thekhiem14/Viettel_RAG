Public 255 Lần ban hành: 1 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

## **1. Tổng quan** 

Credential Dumping là kỹ thuật mà kẻ tấn công sử dụng để trích xuất thông tin chứng thực (mật khẩu, hash, token) từ hệ thống bị xâm. Các nguồn dữ liệu điển hình bao gồm SAM, NTDS, /etc/shadow, hoặc trực tiếp từ bộ nhớ (process memory). Kỹ thuật này thường nhằm mục tiêu mở rộng truy cập trong mạng nội bộ và hỗ trợ lateral movement. 

Mục tiêu báo cáo: mô tả kỹ thuật, các biến thể, phương pháp phát hiện, mitigation, và cung cấp một bảng sự kiện mẫu lớn phục vụ cho bài lab / phân tích forensics. 

## **2. Chi tiết kỹ thuật** 

## **Các phương thức credential dumping phổ biến:** 

- Đọc trực tiếp tệp lưu trữ chứng thực: ví dụ /etc/shadow trên Linux, SAM/NTDS trên Windows. 

- Dump từ bộ nhớ: đọc process memory của tiến trình lưu giữ thông tin chứng thực (ví dụ LSASS trên Windows). 

- Sử dụng công cụ/tiện ích: mimikatz, gsecdump, pwdump, creddump, secretos. 

- Lấy thông tin từ file cấu hình, script hoặc backup không được mã hóa. 

Lưu ý về môi trường: hệ thống Windows thường lưu nhiều thông tin nhạy cảm trong memory của tiến trình LSASS hoặc trong AD database (NTDS.dit). Trên Linux, file /etc/shadow và các file cấu hình ứng dụng là mục tiêu. 

## **3. Kịch bản tấn công** 

Mô tả kịch bản: Kẻ tấn công xâm nhập một host công cộng (ví dụ quản trị từ xa), cài payload để thu thập hash từ LSASS, crack hoặc reuse hash để SSH sang host khác, từ đó truy cập database chứa dữ liệu nhạy cảm. 

Chi tiết bước: 

1) Recon - tìm host quản trị và các tài khoản có quyền cao. 

2) Initial Access - khai thác vuln hoặc sử dụng credential phishing để có foothold. 

3) Dump - sử dụng công cụ để dump memory/credential stores. 

4) Abuse - sử dụng credential để di chuyển ngang hoặc nâng quyền. 

- 5) Persistence & Exfil - cài backdoor và exfil dữ liệu. 

Public 255 Lần ban hành: 1 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

## **4. Phát hiện và biện pháp giảm thiểu** 

## **Phát hiện:** 

- Giám sát hoạt động tiến trình bất thường (lsass.exe memory read, procdump usage). 

- Tìm kiếm hành vi dump file, outbound connections sau khi dump. 

- Sử dụng YARA/Suricata để phát hiện chuỗi đặc trưng. 

## **Giảm thiểu:** 

- Bật LAPS / Credential Guard trên Windows, áp dụng EDR. 

- Hạn chế quyền: least privilege, segment network. 

- Bảo vệ tệp nhạy cảm (chặn truy cập /etc/shadow), áp dụng mật khẩu mạnh và 2FA. 

## **5. Hướng dẫn triển khai Lab** 

Phần này mô tả cách sử dụng bảng sự kiện mẫu trong quá trình lab: cách dựng môi trường, tạo activity mô phỏng, và cách dùng bảng sự kiện để thực hành phân tích. 

Mẹo: Sử dụng docker-compose để dựng mạng lab, seed file logs và script simulate_swipe.sh / simulate_lsass_dump.sh để tạo các sự kiện tương ứng. 

**VIETTEL AI RACE** Public 255 **BÁO CÁO CHI TIẾT: KỸ THUẬT** Lần ban hành: 1 **CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

## **Bảng sự kiện chi tiết (dùng cho phân tích forensic)** 

Bảng dưới đây liệt kê nhiều sự kiện liên quan đến credential dumping và hoạt động tấn công liên quan. Bảng có nhiều hàng để đảm bảo trải dài qua nhiều trang, thuận tiện cho bài tập phân tích log. 

**Bảng dữ liệu credential dump** 

|**Timesta**<br>**mp**|**Host**|**Event**|**Source**<br>**IP**|**File/Hash**|**Action**|
|---|---|---|---|---|---|
|2013-11-<br>29<br>00:00:00|ADMIN-01|LSASS<br>Dump<br>Detected|10.0.7.19<br>0|lsass.dmp /<br>SHA256:<br>b9c402da058212<br>77|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>00:05:00|STAGE-01|Suspicio<br>us<br>Process<br>Spawn|10.0.8.12<br>2|proc:<br>unknown_exec /<br>SHA256:<br>1f82ddeb7dc7c7<br>14|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>00:10:00|STAGE-01|Service<br>Installed|10.0.7.96|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>00:15:00|WEB-01|Config<br>File<br>Read|10.0.10.4<br>2|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>00:20:00|POS-01|SSH<br>Login|10.0.1.21<br>9|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>00:25:00|DB-01|LSASS<br>Dump<br>Detected|10.0.3.10<br>6|lsass.dmp /<br>SHA256:<br>d19684345abce8<br>19|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>00:30:00|POS-02|Process<br>Memory<br>Read|10.0.10.1<br>2|blackpos-lab.bin<br>/ SHA256:<br>99129601fa0661f<br>2|Credential<br>pattern found|
|2013-11-<br>29<br>00:35:00|WORKSTATI<br>ON-12|SSH<br>Login|10.0.8.60|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|

**VIETTEL AI RACE** Public 255 **BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>00:40:00|POS-01|Service<br>Installed|10.0.9.11<br>9|service:<br>backdoor_svc|Service<br>started at boot|
|---|---|---|---|---|---|
|2013-11-<br>29<br>00:45:00|POS-02|FTP<br>Upload<br>Attempt|10.0.9.11<br>4|cards-<br>20131129_part5.<br>csv / SHA256:<br>d0fef2e4262d8d2<br>5|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>00:50:00|WORKSTATI<br>ON-12|Schedul<br>ed Task<br>Creation|10.0.5.20<br>5|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>00:55:00|WEB-01|SSH<br>Login|10.0.7.58|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>01:00:00|ADMIN-01|SQL<br>Dump|10.0.2.96|db-dump-<br>20131129.sql /<br>SHA256:<br>e84fbab96c874f7<br>f|Sensitive data<br>exported|
|2013-11-<br>29<br>01:05:00||Config<br>File<br>Read|||Credentials<br>found in<br>config|
|2013-11-<br>29<br>01:10:00|WEB-01|Process<br>Memory<br>Read|10.0.2.22<br>8|blackpos-lab.bin<br>/ SHA256:<br>29bd38d37a50e1<br>5b|Credential<br>pattern found|
|2013-11-<br>29<br>01:15:00|ADMIN-01|Config<br>File<br>Read|10.0.9.22<br>3|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>01:20:00|VPN-01|SSH<br>Login|10.0.10.1<br>40|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>01:25:00|PROXY-01|SQL<br>Dump|10.0.10.8<br>0|db-dump-<br>20131129.sql /<br>SHA256:<br>0a377e6ab46b18<br>48|Sensitive data<br>exported|
|2013-11-<br>29<br>01:30:00|LSASS-BOX|FTP<br>Upload<br>Attempt|10.0.9.93|cards-<br>20131129_part3.<br>csv / SHA256:<br>9655ff022efeeab<br>0|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

Public 255 

**VIETTEL AI RACE** 

**BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>01:35:00|PROXY-01|SSH<br>Login|10.0.8.13|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|---|---|---|---|---|---|
|2013-11-<br>29<br>01:40:00|STAGE-01|Schedul<br>ed Task<br>Creation|10.0.4.11<br>8|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>01:45:00|WORKSTATI<br>ON-12|Config<br>File<br>Read|10.0.8.18<br>8|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>01:50:00|ADMIN-01|Config<br>File<br>Read|10.0.6.13<br>4|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>01:55:00|POS-01|Schedul<br>ed Task<br>Creation|10.0.7.53|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>02:00:00|LSASS-BOX|Schedul<br>ed Task<br>Creation|10.0.8.36|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>02:05:00|VPN-01|LSASS<br>Dump<br>Detected|10.0.4.22<br>0|lsass.dmp /<br>SHA256:<br>8bd952f21211d7<br>78|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>02:10:00|LSASS-BOX|Schedul<br>ed Task<br>Creation|10.0.8.10<br>4|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>02:15:00|STAGE-01|FTP<br>Upload<br>Attempt|10.0.4.18<br>8|cards-<br>20131129_part5.<br>csv / SHA256:<br>beddff63db8a35f<br>1|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>02:20:00|ADMIN-01|Config<br>File<br>Read|10.0.8.14<br>2|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>02:25:00|DB-01|SQL<br>Dump|10.0.9.23<br>4|db-dump-<br>20131129.sql /<br>SHA256:<br>1949c9ffcd5ea19<br>8|Sensitive data<br>exported|
|2013-11-<br>29<br>02:30:00|WORKSTATI<br>ON-12|LSASS<br>Dump<br>Detected|10.0.8.15<br>0|lsass.dmp /<br>SHA256:<br>31acd7e7fbd13b<br>07|Possible<br>credential<br>exfil from<br>memory|

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

Public 255 

Lần ban hành: 1 

|2013-11-<br>29<br>02:35:00|DB-01|Large<br>POST to<br>external|10.0.6.13<br>4|cards-<br>20131129_part8.<br>csv / SHA256:<br>1acef8425062d8<br>64|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|---|---|---|---|---|---|
|2013-11-<br>29<br>02:40:00|WORKSTATI<br>ON-12|FTP<br>Upload<br>Attempt|10.0.5.11<br>3|cards-<br>20131129_part2.<br>csv / SHA256:<br>3f95ad26ab1221<br>40|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>02:45:00|WEB-01|SSH<br>Login|10.0.2.60|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>02:50:00|WEB-01|SSH<br>Login|10.0.6.17<br>0|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>02:55:00|ADMIN-01|Config<br>File<br>Read|10.0.5.17<br>1|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>03:00:00|POS-01|Schedul<br>ed Task<br>Creation|10.0.7.19<br>5|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>03:05:00|POS-01|FTP<br>Upload<br>Attempt|10.0.4.41|cards-<br>20131129_part8.<br>csv / SHA256:<br>7d992b1dcda137<br>f9|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>03:10:00|PROXY-01|LSASS<br>Dump<br>Detected|10.0.7.20<br>7|lsass.dmp /<br>SHA256:<br>fbcecbaf2dd1066<br>f|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>03:15:00|WORKSTATI<br>ON-12|Large<br>POST to<br>external|10.0.4.14|cards-<br>20131129_part6.<br>csv / SHA256:<br>2bdcb8927f5057<br>92|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>03:20:00|VPN-01|SQL<br>Dump|10.0.5.18<br>1|db-dump-<br>20131129.sql /<br>SHA256:|Sensitive data<br>exported|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||||b26468dfed1782<br>5f||
|---|---|---|---|---|---|
|2013-11-<br>29<br>03:25:00|LSASS-BOX|SQL<br>Dump|10.0.10.1<br>77|db-dump-<br>20131129.sql /<br>SHA256:<br>70e075d63ddda7<br>ac|Sensitive data<br>exported|
|2013-11-<br>29<br>03:30:00|VPN-01|Process<br>Memory<br>Read|10.0.2.74|blackpos-lab.bin<br>/ SHA256:<br>8d6f97856397c9f<br>1|Credential<br>pattern found|
|2013-11-<br>29<br>03:35:00|ADMIN-01|LSASS<br>Dump<br>Detected|10.0.2.22<br>2|lsass.dmp /<br>SHA256:<br>43607084bb5a32<br>23|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>03:40:00|STAGE-01|LSASS<br>Dump<br>Detected|10.0.7.16<br>3|lsass.dmp /<br>SHA256:<br>8d6b20250bad1d<br>86|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>03:45:00|STAGE-01|SSH<br>Login|10.0.6.52|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>03:50:00|STAGE-01|Schedul<br>ed Task<br>Creation|10.0.7.25<br>2|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>03:55:00|DB-01|FTP<br>Upload<br>Attempt|10.0.7.17<br>3|cards-<br>20131129_part5.<br>csv / SHA256:<br>1d08a515d606ce<br>fa|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>04:00:00|VPN-01|Schedul<br>ed Task<br>Creation|10.0.2.23<br>8|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>04:05:00|PROXY-01|LSASS<br>Dump<br>Detected|10.0.9.67|lsass.dmp /<br>SHA256:<br>387249bd316e85<br>a7|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>04:10:00|STAGE-01|Large<br>POST to<br>external|10.0.5.18<br>0|cards-<br>20131129_part2.<br>csv / SHA256:<br>846147560642fc<br>8a|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>04:15:00|LSASS-BOX|FTP<br>Upload<br>Attempt|10.0.1.77|cards-<br>20131129_part4.<br>csv / SHA256:<br>2146c12be4da24<br>70|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|---|---|---|---|---|---|
|2013-11-<br>29<br>04:20:00|POS-02|LSASS<br>Dump<br>Detected|10.0.1.19<br>2|lsass.dmp /<br>SHA256:<br>a3a847cbfb46fee<br>c|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>04:25:00|POS-01|Suspicio<br>us<br>Process<br>Spawn|10.0.4.4|proc:<br>unknown_exec /<br>SHA256:<br>ca09f69ea5c9933<br>e|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>04:30:00|STAGE-01|FTP<br>Upload<br>Attempt|10.0.6.11<br>2|cards-<br>20131129_part10<br>.csv / SHA256:<br>b026418045dc86<br>e3|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>04:35:00|VPN-01|LSASS<br>Dump<br>Detected|10.0.7.12<br>5|lsass.dmp /<br>SHA256:<br>573e245a5953a2<br>c1|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>04:40:00|DB-01|SSH<br>Login|10.0.5.13|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>04:45:00|STAGE-01|Large<br>POST to<br>external|10.0.5.53|cards-<br>20131129_part2.<br>csv / SHA256:<br>990afed33020d1<br>a8|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>04:50:00|PROXY-01|Service<br>Installed|10.0.3.20<br>9|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>04:55:00|POS-01|Large<br>POST to<br>external|10.0.8.12<br>3|cards-<br>20131129_part7.<br>csv / SHA256:<br>8235dca3a59763<br>b6|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>05:00:00|DB-01|Process<br>Memory<br>Read|10.0.2.12<br>9|blackpos-lab.bin<br>/ SHA256:|Credential<br>pattern found|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||||3b6263199a0882<br>6e||
|---|---|---|---|---|---|
|2013-11-<br>29<br>05:05:00|VPN-01|Suspicio<br>us<br>Process<br>Spawn|10.0.5.23<br>9|proc:<br>unknown_exec /<br>SHA256:<br>27eed54ace1837<br>2e|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>05:10:00|POS-02|SSH<br>Login|10.0.6.15<br>8|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>05:15:00|LSASS-BOX|SSH<br>Login|10.0.10.1<br>47|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>05:20:00|DB-01|Process<br>Memory<br>Read|10.0.1.14<br>8|blackpos-lab.bin<br>/ SHA256:<br>96f82f754c9129f<br>a|Credential<br>pattern found|
|2013-11-<br>29<br>05:25:00|POS-01|Suspicio<br>us<br>Process<br>Spawn|10.0.9.18<br>0|proc:<br>unknown_exec /<br>SHA256:<br>c91dc4d99869a5<br>06|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>05:30:00|LSASS-BOX|Service<br>Installed|10.0.1.15<br>3|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>05:35:00|LSASS-BOX|FTP<br>Upload<br>Attempt|10.0.6.17|cards-<br>20131129_part7.<br>csv / SHA256:<br>1d4ed652ec76f9<br>95|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>05:40:00|LSASS-BOX|FTP<br>Upload<br>Attempt|10.0.2.18<br>0|cards-<br>20131129_part6.<br>csv / SHA256:<br>91b946a3f54dc6<br>2e|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>05:45:00|POS-02|Suspicio<br>us<br>Process<br>Spawn|10.0.5.14<br>6|proc:<br>unknown_exec /<br>SHA256:<br>373b6d8d4b25f9<br>cd|Spawned by<br>user<br>'svc_hvac'|

**VIETTEL AI RACE** Public 255 **BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>05:50:00|PROXY-01|Process<br>Memory<br>Read|10.0.3.39|blackpos-lab.bin<br>/ SHA256:<br>58f28fcd4ee3bc0<br>9|Credential<br>pattern found|
|---|---|---|---|---|---|
|2013-11-<br>29<br>05:55:00|PROXY-01|SSH<br>Login|10.0.3.47|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>06:00:00|WEB-01|LSASS<br>Dump<br>Detected|10.0.2.23<br>5|lsass.dmp /<br>SHA256:<br>667671af8708a7<br>0f|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>06:05:00|VPN-01|FTP<br>Upload<br>Attempt|10.0.10.6|cards-<br>20131129_part4.<br>csv / SHA256:<br>6591105b19efe5<br>58|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>06:10:00|WORKSTATI<br>ON-12|Config<br>File<br>Read|10.0.7.21<br>2|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>06:15:00|VPN-01|FTP<br>Upload<br>Attempt|10.0.4.90|cards-<br>20131129_part7.<br>csv / SHA256:<br>585f7d0ff19289d<br>5|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>06:20:00|DB-01|Config<br>File<br>Read|10.0.9.13<br>1|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>06:25:00|DB-01|Large<br>POST to<br>external|10.0.6.20<br>9|cards-<br>20131129_part4.<br>csv / SHA256:<br>12b770e02fcfde9<br>5|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>06:30:00|POS-01|FTP<br>Upload<br>Attempt|10.0.5.15<br>6|cards-<br>20131129_part7.<br>csv / SHA256:<br>45ddcac5ba8819<br>06|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>06:35:00|WORKSTATI<br>ON-12|Large<br>POST to<br>external|10.0.6.76|cards-<br>20131129_part9.<br>csv / SHA256:<br>d1eabd81c82a9b<br>d0|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

Public 255 

Lần ban hành: 1 

|2013-11-<br>29<br>06:40:00|LSASS-BOX|Suspicio<br>us<br>Process<br>Spawn|10.0.5.16<br>3|proc:<br>unknown_exec /<br>SHA256:<br>25ebe27973dec4<br>6f|Spawned by<br>user<br>'svc_hvac'|
|---|---|---|---|---|---|
|2013-11-<br>29<br>06:45:00|VPN-01|Large<br>POST to<br>external|10.0.9.2|cards-<br>20131129_part8.<br>csv / SHA256:<br>4c4eec07c64c6b<br>94|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>06:50:00|DB-01|Large<br>POST to<br>external|10.0.2.13<br>5|cards-<br>20131129_part5.<br>csv / SHA256:<br>cfe73d1ffe063ee<br>5|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>06:55:00|LSASS-BOX|SQL<br>Dump|10.0.10.1<br>99|db-dump-<br>20131129.sql /<br>SHA256:<br>2744b59f8584afe<br>b|Sensitive data<br>exported|
|2013-11-<br>29<br>07:00:00|POS-02|Suspicio<br>us<br>Process<br>Spawn|10.0.8.11<br>2|proc:<br>unknown_exec /<br>SHA256:<br>c7ad6e872c0a4c<br>9b|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>07:05:00|WEB-01|Large<br>POST to<br>external|10.0.10.9<br>4|cards-<br>20131129_part9.<br>csv / SHA256:<br>7d9314a396f205<br>70|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>07:10:00|STAGE-01|Service<br>Installed|10.0.6.90|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>07:15:00|ADMIN-01|Schedul<br>ed Task<br>Creation|10.0.10.2<br>43|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>07:20:00|STAGE-01|LSASS<br>Dump<br>Detected|10.0.8.12|lsass.dmp /<br>SHA256:<br>84193ae1a6dcfbc<br>d|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>07:25:00|POS-01|Service<br>Installed|10.0.9.56|service:<br>backdoor_svc|Service<br>started at boot|

**==> picture [39 x 47] intentionally omitted <==**

Public 255 

**VIETTEL AI RACE** Public 255 **BÁO CÁO CHI TIẾT: KỸ THUẬT** Lần ban hành: 1 **CREDENTIAL DUMPING (MITRE T1003)** 

|2013-11-<br>29<br>07:30:00|DB-01|SSH<br>Login|10.0.8.20<br>7|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|---|---|---|---|---|---|
|2013-11-<br>29<br>07:35:00|LSASS-BOX|Config<br>File<br>Read|10.0.3.86|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>07:40:00|DB-01|SSH<br>Login|10.0.6.19|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>07:45:00|POS-01|SQL<br>Dump|10.0.5.23<br>9|db-dump-<br>20131129.sql /<br>SHA256:<br>a8b8817bf3d761f<br>7|Sensitive data<br>exported|
|2013-11-<br>29<br>07:50:00|ADMIN-01|Service<br>Installed|10.0.2.50|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>07:55:00|WORKSTATI<br>ON-12|Suspicio<br>us<br>Process<br>Spawn|10.0.2.83|proc:<br>unknown_exec /<br>SHA256:<br>51402279fa6e9e<br>2a|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>08:00:00|STAGE-01|Schedul<br>ed Task<br>Creation|10.0.9.12<br>7|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>08:05:00|WORKSTATI<br>ON-12|FTP<br>Upload<br>Attempt|10.0.5.14<br>6|cards-<br>20131129_part8.<br>csv / SHA256:<br>58364e3a8790ad<br>c5|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>08:10:00|POS-02|SQL<br>Dump|10.0.6.21<br>9|db-dump-<br>20131129.sql /<br>SHA256:<br>950481b02b5e06<br>f3|Sensitive data<br>exported|
|2013-11-<br>29<br>08:15:00|POS-01|FTP<br>Upload<br>Attempt|10.0.4.21<br>3|cards-<br>20131129_part3.<br>csv / SHA256:<br>597ba5041e013a<br>b6|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

Public 255 

Lần ban hành: 1 

|2013-11-<br>29<br>08:20:00|DB-01|LSASS<br>Dump<br>Detected|10.0.7.14<br>8|lsass.dmp /<br>SHA256:<br>d7154c4a606252<br>56|Possible<br>credential<br>exfil from<br>memory|
|---|---|---|---|---|---|
|2013-11-<br>29<br>08:25:00|STAGE-01|Large<br>POST to<br>external|10.0.4.14<br>1|cards-<br>20131129_part2.<br>csv / SHA256:<br>10003b7a20751e<br>a1|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>08:30:00|STAGE-01|Schedul<br>ed Task<br>Creation|10.0.10.1<br>98|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>08:35:00|DB-01|SQL<br>Dump|10.0.2.10<br>7|db-dump-<br>20131129.sql /<br>SHA256:<br>6818c26f1fbd7ed<br>7|Sensitive data<br>exported|
|2013-11-<br>29<br>08:40:00|VPN-01|FTP<br>Upload<br>Attempt|10.0.5.13<br>5|cards-<br>20131129_part1.<br>csv / SHA256:<br>966b0e15f7e1ca1<br>4|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>08:45:00|VPN-01|Process<br>Memory<br>Read|10.0.8.10<br>3|blackpos-lab.bin<br>/ SHA256:<br>3d7430fe33854c<br>22|Credential<br>pattern found|
|2013-11-<br>29<br>08:50:00|STAGE-01|FTP<br>Upload<br>Attempt|10.0.1.13<br>6|cards-<br>20131129_part4.<br>csv / SHA256:<br>908deb054564c7<br>83|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>08:55:00|PROXY-01|SQL<br>Dump|10.0.2.17|db-dump-<br>20131129.sql /<br>SHA256:<br>c7b145ea7431a2<br>d5|Sensitive data<br>exported|
|2013-11-<br>29<br>09:00:00|LSASS-BOX|Large<br>POST to<br>external|10.0.3.22<br>1|cards-<br>20131129_part7.<br>csv / SHA256:<br>7500829e888145<br>d0|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>09:05:00|ADMIN-01|SSH<br>Login|10.0.7.23<br>3|n/a|Login<br>successful<br>(possible|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

||||||credential<br>reuse)|
|---|---|---|---|---|---|
|2013-11-<br>29<br>09:10:00|STAGE-01|Service<br>Installed|10.0.10.1<br>07|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>09:15:00|STAGE-01|Service<br>Installed|10.0.9.24<br>9|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>09:20:00|WORKSTATI<br>ON-12|Service<br>Installed|10.0.4.19|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>09:25:00|LSASS-BOX|FTP<br>Upload<br>Attempt|10.0.4.7|cards-<br>20131129_part6.<br>csv / SHA256:<br>45b0cda00ff4359<br>5|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>09:30:00|STAGE-01|Schedul<br>ed Task<br>Creation|10.0.7.31|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>09:35:00|ADMIN-01|Service<br>Installed|10.0.8.20|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>09:40:00|POS-01|Suspicio<br>us<br>Process<br>Spawn|10.0.8.16<br>2|proc:<br>unknown_exec /<br>SHA256:<br>dc79ec93132944<br>07|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>09:45:00|PROXY-01|FTP<br>Upload<br>Attempt|10.0.1.12<br>2|cards-<br>20131129_part10<br>.csv / SHA256:<br>15262acad16be8<br>9d|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>09:50:00|WORKSTATI<br>ON-12|SQL<br>Dump|10.0.9.20<br>3|db-dump-<br>20131129.sql /<br>SHA256:<br>ca3aaf4cde2695d<br>7|Sensitive data<br>exported|
|2013-11-<br>29<br>09:55:00|STAGE-01|Config<br>File<br>Read|10.0.10.7<br>9|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>10:00:00|WEB-01|Suspicio<br>us<br>Process<br>Spawn|10.0.1.17<br>4|proc:<br>unknown_exec /<br>SHA256:|Spawned by<br>user<br>'svc_hvac'|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||||2a5243398731c6<br>d6||
|---|---|---|---|---|---|
|2013-11-<br>29<br>10:05:00|ADMIN-01|Config<br>File<br>Read|10.0.1.81|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>10:10:00|STAGE-01|SQL<br>Dump|10.0.3.72|db-dump-<br>20131129.sql /<br>SHA256:<br>84acea8d005cb2<br>c4|Sensitive data<br>exported|
|2013-11-<br>29<br>10:15:00|VPN-01|FTP<br>Upload<br>Attempt|10.0.10.2<br>07|cards-<br>20131129_part2.<br>csv / SHA256:<br>e9532cd3e5928e<br>ae|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>10:20:00|WEB-01|Schedul<br>ed Task<br>Creation|10.0.2.18<br>9|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>10:25:00|PROXY-01|Config<br>File<br>Read|10.0.5.71|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>10:30:00|STAGE-01|SSH<br>Login|10.0.5.88|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>10:35:00|VPN-01|LSASS<br>Dump<br>Detected|10.0.10.5|lsass.dmp /<br>SHA256:<br>b0290303a758bb<br>13|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>10:40:00|WEB-01|SSH<br>Login|10.0.7.23<br>7|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>10:45:00|DB-01|Schedul<br>ed Task<br>Creation|10.0.3.14<br>6|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>10:50:00|PROXY-01|Service<br>Installed|10.0.8.23<br>9|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>10:55:00|WEB-01|Schedul<br>ed Task<br>Creation|10.0.5.14<br>6|task:<br>persist_worker|Persistence<br>scheduled|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>11:00:00|VPN-01|Schedul<br>ed Task<br>Creation|10.0.3.12<br>8|task:<br>persist_worker|Persistence<br>scheduled|
|---|---|---|---|---|---|
|2013-11-<br>29<br>11:05:00|DB-01|Suspicio<br>us<br>Process<br>Spawn|10.0.4.20<br>1|proc:<br>unknown_exec /<br>SHA256:<br>106068704ee01d<br>df|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>11:10:00|WEB-01|Suspicio<br>us<br>Process<br>Spawn|10.0.2.24<br>0|proc:<br>unknown_exec /<br>SHA256:<br>7a64edd274697a<br>16|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>11:15:00|DB-01|Process<br>Memory<br>Read|10.0.7.68|blackpos-lab.bin<br>/ SHA256:<br>e2bbaa394a53f99<br>9|Credential<br>pattern found|
|2013-11-<br>29<br>11:20:00|WEB-01|Schedul<br>ed Task<br>Creation|10.0.3.16<br>0|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>11:25:00|WEB-01|Config<br>File<br>Read|10.0.6.20<br>8|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>11:30:00|POS-02|LSASS<br>Dump<br>Detected|10.0.8.13<br>0|lsass.dmp /<br>SHA256:<br>6028a6f0e67a98<br>d7|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>11:35:00|DB-01|Config<br>File<br>Read|10.0.10.1<br>9|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>11:40:00|POS-02|Schedul<br>ed Task<br>Creation|10.0.9.11<br>6|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>11:45:00|VPN-01|LSASS<br>Dump<br>Detected|10.0.3.19<br>8|lsass.dmp /<br>SHA256:<br>b2c011a3fb3165<br>92|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>11:50:00|ADMIN-01|Large<br>POST to<br>external|10.0.4.22<br>9|cards-<br>20131129_part5.<br>csv / SHA256:<br>57502ba5380a93<br>20|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

Public 255 

**VIETTEL AI RACE** 

**BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>11:55:00|STAGE-01|LSASS<br>Dump<br>Detected|10.0.8.20<br>2|lsass.dmp /<br>SHA256:<br>c9bc765f12bf3e4<br>c|Possible<br>credential<br>exfil from<br>memory|
|---|---|---|---|---|---|
|2013-11-<br>29<br>12:00:00|WORKSTATI<br>ON-12|Schedul<br>ed Task<br>Creation|10.0.3.36|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>12:05:00|VPN-01|Schedul<br>ed Task<br>Creation|10.0.3.16<br>0|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>12:10:00|POS-02|Schedul<br>ed Task<br>Creation|10.0.5.20<br>1|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>12:15:00|STAGE-01|Process<br>Memory<br>Read|10.0.10.3|blackpos-lab.bin<br>/ SHA256:<br>b6c8cdc8def6cbc<br>8|Credential<br>pattern found|
|2013-11-<br>29<br>12:20:00|ADMIN-01|Config<br>File<br>Read|10.0.4.11<br>5|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>12:25:00|POS-02|Service<br>Installed|10.0.6.89|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>12:30:00|POS-01|SQL<br>Dump|10.0.5.22<br>9|db-dump-<br>20131129.sql /<br>SHA256:<br>84e1da2ce2801e<br>21|Sensitive data<br>exported|
|2013-11-<br>29<br>12:35:00|DB-01|SSH<br>Login|10.0.10.3<br>8|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>12:40:00|WEB-01|Large<br>POST to<br>external|10.0.6.43|cards-<br>20131129_part8.<br>csv / SHA256:<br>4fe7dd1b54e639<br>41|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>12:45:00|POS-02|Config<br>File<br>Read|10.0.8.1|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>12:50:00|POS-01|Config<br>File<br>Read|10.0.2.13<br>4|config.ini|Credentials<br>found in<br>config|

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

Public 255 

Lần ban hành: 1 

|2013-11-<br>29<br>12:55:00|PROXY-01|Suspicio<br>us<br>Process<br>Spawn|10.0.10.1<br>73|proc:<br>unknown_exec /<br>SHA256:<br>26001ad2132cc6<br>67|Spawned by<br>user<br>'svc_hvac'|
|---|---|---|---|---|---|
|2013-11-<br>29<br>13:00:00|WEB-01|LSASS<br>Dump<br>Detected|10.0.7.21<br>9|lsass.dmp /<br>SHA256:<br>8ec4b6adfd72ecd<br>9|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>13:05:00|VPN-01|Schedul<br>ed Task<br>Creation|10.0.8.71|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>13:10:00|ADMIN-01|SQL<br>Dump|10.0.3.15<br>5|db-dump-<br>20131129.sql /<br>SHA256:<br>c4dcbc4456165b<br>7c|Sensitive data<br>exported|
|2013-11-<br>29<br>13:15:00|ADMIN-01|Process<br>Memory<br>Read|10.0.8.79|blackpos-lab.bin<br>/ SHA256:<br>529c19335be452<br>15|Credential<br>pattern found|
|2013-11-<br>29<br>13:20:00|DB-01|Config<br>File<br>Read|10.0.3.10<br>6|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>13:25:00|PROXY-01|Schedul<br>ed Task<br>Creation|10.0.1.14<br>9|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>13:30:00|WEB-01|Schedul<br>ed Task<br>Creation|10.0.1.64|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>13:35:00|POS-01|Schedul<br>ed Task<br>Creation|10.0.3.24<br>8|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>13:40:00|STAGE-01|Schedul<br>ed Task<br>Creation|10.0.4.16<br>7|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>13:45:00|PROXY-01|Schedul<br>ed Task<br>Creation|10.0.4.24<br>5|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>13:50:00|POS-01|Suspicio<br>us<br>Process<br>Spawn|10.0.10.1<br>45|proc:<br>unknown_exec /<br>SHA256:<br>26219d625a3e27<br>50|Spawned by<br>user<br>'svc_hvac'|

**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|Public 255|
|---|---|---|
||**BÁO CÁO CHI TIẾT: KỸ THUẬT**<br>**CREDENTIAL DUMPING(MITRE T1003)**|Lần ban hành: 1|

|2013-11-<br>29<br>13:55:00|STAGE-01|SQL<br>Dump|10.0.3.21<br>0|db-dump-<br>20131129.sql /<br>SHA256:<br>453b1ebbce3746<br>66|Sensitive data<br>exported|
|---|---|---|---|---|---|
|2013-11-<br>29<br>14:00:00|LSASS-BOX|Service<br>Installed|10.0.6.24<br>1|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>14:05:00|DB-01|SQL<br>Dump|10.0.1.99|db-dump-<br>20131129.sql /<br>SHA256:<br>826caffdc1af946<br>b|Sensitive data<br>exported|
|2013-11-<br>29<br>14:10:00|PROXY-01|Schedul<br>ed Task<br>Creation|10.0.3.68|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>14:15:00|WORKSTATI<br>ON-12|SQL<br>Dump|10.0.4.20<br>4|db-dump-<br>20131129.sql /<br>SHA256:<br>c64dfe06934c4d<br>de|Sensitive data<br>exported|
|2013-11-<br>29<br>14:20:00|STAGE-01|Process<br>Memory<br>Read|10.0.10.1<br>98|blackpos-lab.bin<br>/ SHA256:<br>35444b0e72b756<br>9e|Credential<br>pattern found|
|2013-11-<br>29<br>14:25:00|WEB-01|Process<br>Memory<br>Read|10.0.3.16<br>6|blackpos-lab.bin<br>/ SHA256:<br>c163460646b55e<br>90|Credential<br>pattern found|
|2013-11-<br>29<br>14:30:00|POS-02|Schedul<br>ed Task<br>Creation|10.0.1.19<br>9|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>14:35:00|POS-02|Large<br>POST to<br>external|10.0.1.25<br>1|cards-<br>20131129_part4.<br>csv / SHA256:<br>702046f0a58605<br>05|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>14:40:00|WEB-01|SSH<br>Login|10.0.2.13<br>5|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|

**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|Public 255|
|---|---|---|
||**BÁO CÁO CHI TIẾT: KỸ THUẬT**<br>**CREDENTIAL DUMPING(MITRE T1003)**|Lần ban hành: 1|

|2013-11-<br>29<br>14:45:00|VPN-01|Large<br>POST to<br>external|10.0.7.13<br>6|cards-<br>20131129_part10<br>.csv / SHA256:<br>e95768a19f1ceef<br>0|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|---|---|---|---|---|---|
|2013-11-<br>29<br>14:50:00|ADMIN-01|Suspicio<br>us<br>Process<br>Spawn|10.0.9.10<br>1|proc:<br>unknown_exec /<br>SHA256:<br>6130b47147e15e<br>c2|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>14:55:00|WORKSTATI<br>ON-12|SQL<br>Dump|10.0.7.13<br>3|db-dump-<br>20131129.sql /<br>SHA256:<br>526252effea0ab5<br>6|Sensitive data<br>exported|
|2013-11-<br>29<br>15:00:00|DB-01|SQL<br>Dump|10.0.8.70|db-dump-<br>20131129.sql /<br>SHA256:<br>b8283af3567af33<br>b|Sensitive data<br>exported|
|2013-11-<br>29<br>15:05:00|POS-01|LSASS<br>Dump<br>Detected|10.0.3.72|lsass.dmp /<br>SHA256:<br>f8e1a86a0450ace<br>2|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>15:10:00|POS-01|SSH<br>Login|10.0.4.25<br>2|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>15:15:00|VPN-01|Service<br>Installed|10.0.4.19<br>6|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>15:20:00|POS-01|Suspicio<br>us<br>Process<br>Spawn|10.0.3.23<br>9|proc:<br>unknown_exec /<br>SHA256:<br>4b7e9d4b497ab1<br>47|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>15:25:00|POS-02|Suspicio<br>us<br>Process<br>Spawn|10.0.4.21<br>3|proc:<br>unknown_exec /<br>SHA256:<br>0451dd1f5ffb670<br>6|Spawned by<br>user<br>'svc_hvac'|

**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|Public 255|
|---|---|---|
||**BÁO CÁO CHI TIẾT: KỸ THUẬT**<br>**CREDENTIAL DUMPING(MITRE T1003)**|Lần ban hành: 1|

|2013-11-<br>29<br>15:30:00|WEB-01|FTP<br>Upload<br>Attempt|10.0.2.18|cards-<br>20131129_part9.<br>csv / SHA256:<br>11788df4eecba9a<br>d|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|---|---|---|---|---|---|
|2013-11-<br>29<br>15:35:00|PROXY-01|Suspicio<br>us<br>Process<br>Spawn|10.0.8.76|proc:<br>unknown_exec /<br>SHA256:<br>869c918ff18a36a<br>9|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>15:40:00|STAGE-01|Config<br>File<br>Read|10.0.2.89|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>15:45:00|STAGE-01|Large<br>POST to<br>external|10.0.10.2<br>24|cards-<br>20131129_part8.<br>csv / SHA256:<br>17faa7a766be738<br>2|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>15:50:00|POS-01|FTP<br>Upload<br>Attempt|10.0.3.16<br>7|cards-<br>20131129_part6.<br>csv / SHA256:<br>ef9167aa8bd0d1f<br>c|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>15:55:00|POS-01|SSH<br>Login|10.0.6.41|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>16:00:00|LSASS-BOX|Process<br>Memory<br>Read|10.0.9.21<br>5|blackpos-lab.bin<br>/ SHA256:<br>928e13cd34af72<br>45|Credential<br>pattern found|
|2013-11-<br>29<br>16:05:00|VPN-01|LSASS<br>Dump<br>Detected|10.0.2.12<br>4|lsass.dmp /<br>SHA256:<br>111134e298d34d<br>3e|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>16:10:00|WORKSTATI<br>ON-12|Large<br>POST to<br>external|10.0.2.16<br>1|cards-<br>20131129_part1.<br>csv / SHA256:<br>110484162d8f2a<br>8c|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>16:15:00|STAGE-01|Large<br>POST to<br>external|10.0.10.1<br>69|cards-<br>20131129_part1.<br>csv / SHA256:|Outbound to<br>ftp-exfil-|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||||2f8c4bfca67590a<br>d|targetlab.exa<br>mple|
|---|---|---|---|---|---|
|2013-11-<br>29<br>16:20:00|ADMIN-01|FTP<br>Upload<br>Attempt|10.0.4.16<br>5|cards-<br>20131129_part3.<br>csv / SHA256:<br>842334f65f9079<br>b5|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>16:25:00|DB-01|Suspicio<br>us<br>Process<br>Spawn|10.0.10.2<br>17|proc:<br>unknown_exec /<br>SHA256:<br>65ee7734a85a03<br>b7|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>16:30:00|STAGE-01|FTP<br>Upload<br>Attempt|10.0.9.17<br>9|cards-<br>20131129_part2.<br>csv / SHA256:<br>6b6973dcf8cd4b<br>02|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>16:35:00|POS-01|SQL<br>Dump|10.0.2.21|db-dump-<br>20131129.sql /<br>SHA256:<br>1a05d69b723c4c<br>93|Sensitive data<br>exported|
|2013-11-<br>29<br>16:40:00|POS-01|Process<br>Memory<br>Read|10.0.4.18<br>6|blackpos-lab.bin<br>/ SHA256:<br>632528ddc08195<br>bb|Credential<br>pattern found|
|2013-11-<br>29<br>16:45:00|WEB-01|Service<br>Installed|10.0.10.1<br>00|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>16:50:00|STAGE-01|Service<br>Installed|10.0.7.86|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>16:55:00|WORKSTATI<br>ON-12|SQL<br>Dump|10.0.6.27|db-dump-<br>20131129.sql /<br>SHA256:<br>d870d52a4a1afe6<br>2|Sensitive data<br>exported|
|2013-11-<br>29<br>17:00:00|DB-01|Suspicio<br>us<br>Process<br>Spawn|10.0.3.11|proc:<br>unknown_exec /<br>SHA256:<br>3ad51277bc207f<br>81|Spawned by<br>user<br>'svc_hvac'|

Public 255 

**VIETTEL AI RACE** 

**BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>17:05:00|LSASS-BOX|SSH<br>Login|10.0.5.22<br>5|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|---|---|---|---|---|---|
|2013-11-<br>29<br>17:10:00|STAGE-01|Config<br>File<br>Read|10.0.6.11<br>5|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>17:15:00|STAGE-01|Config<br>File<br>Read|10.0.2.21<br>1|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>17:20:00|ADMIN-01|Process<br>Memory<br>Read|10.0.4.10<br>8|blackpos-lab.bin<br>/ SHA256:<br>ca25ef44c184bb5<br>6|Credential<br>pattern found|
|2013-11-<br>29<br>17:25:00|POS-01|Schedul<br>ed Task<br>Creation|10.0.3.13<br>9|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>17:30:00|DB-01|Config<br>File<br>Read|10.0.9.60|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>17:35:00|DB-01|Schedul<br>ed Task<br>Creation|10.0.2.55|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>17:40:00|STAGE-01|SQL<br>Dump|10.0.1.13<br>8|db-dump-<br>20131129.sql /<br>SHA256:<br>81363fd4e9606a<br>d8|Sensitive data<br>exported|
|2013-11-<br>29<br>17:45:00|VPN-01|Suspicio<br>us<br>Process<br>Spawn|10.0.7.13|proc:<br>unknown_exec /<br>SHA256:<br>ce14fb490fc3d9e<br>d|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>17:50:00|ADMIN-01|LSASS<br>Dump<br>Detected|10.0.6.43|lsass.dmp /<br>SHA256:<br>6569453d4aa21d<br>34|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>17:55:00|VPN-01|Process<br>Memory<br>Read|10.0.8.16<br>3|blackpos-lab.bin<br>/ SHA256:<br>b1ab4dafd469b1<br>5d|Credential<br>pattern found|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>18:00:00|PROXY-01|Large<br>POST to<br>external|10.0.6.47|cards-<br>20131129_part5.<br>csv / SHA256:<br>c4196950302f44<br>e0|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|---|---|---|---|---|---|
|2013-11-<br>29<br>18:05:00|WORKSTATI<br>ON-12|Service<br>Installed|10.0.2.30|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>18:10:00|VPN-01|Large<br>POST to<br>external|10.0.2.16<br>5|cards-<br>20131129_part1.<br>csv / SHA256:<br>cc0873a374d47a<br>46|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>18:15:00|POS-01|Config<br>File<br>Read|10.0.9.99|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>18:20:00|ADMIN-01|LSASS<br>Dump<br>Detected|10.0.4.20<br>0|lsass.dmp /<br>SHA256:<br>3e54fd25802542<br>db|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>18:25:00|POS-02|Process<br>Memory<br>Read|10.0.5.21<br>5|blackpos-lab.bin<br>/ SHA256:<br>4d245ca39b8d46<br>fc|Credential<br>pattern found|
|2013-11-<br>29<br>18:30:00|LSASS-BOX|Schedul<br>ed Task<br>Creation|10.0.9.25<br>0|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>18:35:00|WORKSTATI<br>ON-12|Schedul<br>ed Task<br>Creation|10.0.10.2<br>25|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>18:40:00|POS-01|LSASS<br>Dump<br>Detected|10.0.5.77|lsass.dmp /<br>SHA256:<br>8145218b75e3e8<br>5a|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>18:45:00|ADMIN-01|Suspicio<br>us<br>Process<br>Spawn|10.0.5.10<br>7|proc:<br>unknown_exec /<br>SHA256:<br>40e5ba94438b7e<br>4a|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>18:50:00|STAGE-01|Suspicio<br>us<br>Process<br>Spawn|10.0.7.38|proc:<br>unknown_exec /<br>SHA256:<br>d6eb1d9665cb91<br>08|Spawned by<br>user<br>'svc_hvac'|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>18:55:00|STAGE-01|Process<br>Memory<br>Read|10.0.9.18<br>7|blackpos-lab.bin<br>/ SHA256:<br>4f606210092eec<br>6f|Credential<br>pattern found|
|---|---|---|---|---|---|
|2013-11-<br>29<br>19:00:00|WORKSTATI<br>ON-12|SQL<br>Dump|10.0.6.11<br>6|db-dump-<br>20131129.sql /<br>SHA256:<br>f0989cb9998b19<br>8d|Sensitive data<br>exported|
|2013-11-<br>29<br>19:05:00|STAGE-01|FTP<br>Upload<br>Attempt|10.0.7.21<br>3|cards-<br>20131129_part2.<br>csv / SHA256:<br>7160c1f013e299<br>4a|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>19:10:00|DB-01|SSH<br>Login|10.0.5.33|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>19:15:00|STAGE-01|Suspicio<br>us<br>Process<br>Spawn|10.0.4.70|proc:<br>unknown_exec /<br>SHA256:<br>2079ecc29900d1<br>21|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>19:20:00|ADMIN-01|Large<br>POST to<br>external|10.0.10.8<br>9|cards-<br>20131129_part2.<br>csv / SHA256:<br>9b953ffd5bf3bc1<br>6|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>19:25:00|POS-02|Schedul<br>ed Task<br>Creation|10.0.4.22<br>0|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>19:30:00|POS-01|LSASS<br>Dump<br>Detected|10.0.10.1<br>10|lsass.dmp /<br>SHA256:<br>f305109b0d0e15<br>13|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>19:35:00|PROXY-01|Large<br>POST to<br>external|10.0.4.25<br>2|cards-<br>20131129_part6.<br>csv / SHA256:<br>bf6e8c3e5357c30<br>f|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>19:40:00|WORKSTATI<br>ON-12|Suspicio<br>us|10.0.9.11<br>2|proc:<br>unknown_exec /<br>SHA256:|Spawned by<br>user<br>'svc_hvac'|

**VIETTEL AI RACE** Public 255 **BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||Process<br>Spawn||ef7fbc5ac20c4b4<br>7||
|---|---|---|---|---|---|
|2013-11-<br>29<br>19:45:00|LSASS-BOX|LSASS<br>Dump<br>Detected|10.0.10.7<br>3|lsass.dmp /<br>SHA256:<br>2de904cf75fd589<br>a|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>19:50:00|PROXY-01|Process<br>Memory<br>Read|10.0.8.83|blackpos-lab.bin<br>/ SHA256:<br>30848b2006bf81<br>83|Credential<br>pattern found|
|2013-11-<br>29<br>19:55:00|POS-02|FTP<br>Upload<br>Attempt|10.0.6.10<br>8|cards-<br>20131129_part6.<br>csv / SHA256:<br>5f707ce3c67177<br>d6|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>20:00:00|STAGE-01|LSASS<br>Dump<br>Detected|10.0.6.31|lsass.dmp /<br>SHA256:<br>5a50e6ea7f58673<br>8|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>20:05:00|STAGE-01|Large<br>POST to<br>external|10.0.4.11<br>7|cards-<br>20131129_part1.<br>csv / SHA256:<br>d25c9c748a29c0<br>6c|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>20:10:00|VPN-01|LSASS<br>Dump<br>Detected|10.0.7.17<br>9|lsass.dmp /<br>SHA256:<br>de68c9046c1372<br>b4|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>20:15:00|VPN-01|SQL<br>Dump|10.0.6.21<br>5|db-dump-<br>20131129.sql /<br>SHA256:<br>bbce0fd8fae8128<br>9|Sensitive data<br>exported|
|2013-11-<br>29<br>20:20:00|STAGE-01|FTP<br>Upload<br>Attempt|10.0.3.17<br>0|cards-<br>20131129_part9.<br>csv / SHA256:<br>01df0fb9353637<br>96|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>20:25:00|PROXY-01|SQL<br>Dump|10.0.8.89|db-dump-<br>20131129.sql /<br>SHA256:<br>a2f34fbdc5aed32<br>5|Sensitive data<br>exported|

Public 255 

**VIETTEL AI RACE** 

**BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>20:30:00|ADMIN-01|Schedul<br>ed Task<br>Creation|10.0.2.13<br>5|task:<br>persist_worker|Persistence<br>scheduled|
|---|---|---|---|---|---|
|2013-11-<br>29<br>20:35:00|POS-02|LSASS<br>Dump<br>Detected|10.0.3.82|lsass.dmp /<br>SHA256:<br>7e66d3dd7f3b9f2<br>0|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>20:40:00|POS-01|Process<br>Memory<br>Read|10.0.8.24<br>9|blackpos-lab.bin<br>/ SHA256:<br>1cc9fa732a42c01<br>4|Credential<br>pattern found|
|2013-11-<br>29<br>20:45:00|POS-01|Suspicio<br>us<br>Process<br>Spawn|10.0.4.94|proc:<br>unknown_exec /<br>SHA256:<br>20cb34e7883a79<br>dc|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>20:50:00|LSASS-BOX|Service<br>Installed|10.0.1.27|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>20:55:00|POS-01|SQL<br>Dump|10.0.5.23|db-dump-<br>20131129.sql /<br>SHA256:<br>a6b8d8fc4ab89ba<br>b|Sensitive data<br>exported|
|2013-11-<br>29<br>21:00:00|DB-01|Service<br>Installed|10.0.7.35|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>21:05:00|STAGE-01|FTP<br>Upload<br>Attempt|10.0.8.82|cards-<br>20131129_part5.<br>csv / SHA256:<br>a46d359a7adcdb<br>61|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>21:10:00|PROXY-01|Service<br>Installed|10.0.7.12<br>3|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>21:15:00|DB-01|Schedul<br>ed Task<br>Creation|10.0.5.20|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>21:20:00|ADMIN-01|Config<br>File<br>Read|10.0.2.50|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>21:25:00|WORKSTATI<br>ON-12|Suspicio<br>us|10.0.4.10<br>7|proc:<br>unknown_exec /<br>SHA256:|Spawned by<br>user<br>'svc_hvac'|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||Process<br>Spawn||2c997e95134de8<br>01||
|---|---|---|---|---|---|
|2013-11-<br>29<br>21:30:00|LSASS-BOX|Schedul<br>ed Task<br>Creation|10.0.5.36|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>21:35:00|WORKSTATI<br>ON-12|Schedul<br>ed Task<br>Creation|10.0.7.16<br>6|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>21:40:00|LSASS-BOX|Process<br>Memory<br>Read|10.0.4.13<br>8|blackpos-lab.bin<br>/ SHA256:<br>35601431cedc4a<br>3a|Credential<br>pattern found|
|2013-11-<br>29<br>21:45:00|LSASS-BOX|SQL<br>Dump|10.0.7.38|db-dump-<br>20131129.sql /<br>SHA256:<br>0d6b2f9d90cb0b<br>38|Sensitive data<br>exported|
|2013-11-<br>29<br>21:50:00|VPN-01|Process<br>Memory<br>Read|10.0.5.24<br>5|blackpos-lab.bin<br>/ SHA256:<br>3f3e4dafb4993e6<br>7|Credential<br>pattern found|
|2013-11-<br>29<br>21:55:00|DB-01|SQL<br>Dump|10.0.3.15<br>0|db-dump-<br>20131129.sql /<br>SHA256:<br>e451c6f9d9488b<br>ae|Sensitive data<br>exported|
|2013-11-<br>29<br>22:00:00|LSASS-BOX|Schedul<br>ed Task<br>Creation|10.0.8.13<br>9|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>22:05:00|POS-01|SSH<br>Login|10.0.9.24<br>0|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>22:10:00|DB-01|Config<br>File<br>Read|10.0.5.10<br>9|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>22:15:00|POS-01|Config<br>File<br>Read|10.0.10.2<br>04|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>22:20:00|STAGE-01|Suspicio<br>us<br>Process<br>Spawn|10.0.10.1<br>7|proc:<br>unknown_exec /<br>SHA256:|Spawned by<br>user<br>'svc_hvac'|

Public 255 

**VIETTEL AI RACE** 

**BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||||59f82b34988e94<br>dd||
|---|---|---|---|---|---|
|2013-11-<br>29<br>22:25:00|POS-01|Suspicio<br>us<br>Process<br>Spawn|10.0.7.13<br>5|proc:<br>unknown_exec /<br>SHA256:<br>8fa8a4f7533d237<br>7|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>29<br>22:30:00|POS-02|LSASS<br>Dump<br>Detected|10.0.9.19<br>5|lsass.dmp /<br>SHA256:<br>292eef2d19b786<br>b9|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>22:35:00|VPN-01|Service<br>Installed|10.0.4.58|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>29<br>22:40:00|POS-01|Config<br>File<br>Read|10.0.7.99|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>22:45:00|WORKSTATI<br>ON-12|FTP<br>Upload<br>Attempt|10.0.2.19<br>1|cards-<br>20131129_part9.<br>csv / SHA256:<br>dac3b27bd0cecd<br>a2|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>22:50:00|DB-01|Config<br>File<br>Read|10.0.9.21<br>5|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>29<br>22:55:00|WEB-01|LSASS<br>Dump<br>Detected|10.0.10.1<br>84|lsass.dmp /<br>SHA256:<br>761cfe9de6c1f2b<br>2|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>23:00:00|DB-01|SQL<br>Dump|10.0.7.49|db-dump-<br>20131129.sql /<br>SHA256:<br>d9c4371d04ea36<br>96|Sensitive data<br>exported|
|2013-11-<br>29<br>23:05:00|ADMIN-01|FTP<br>Upload<br>Attempt|10.0.1.25<br>3|cards-<br>20131129_part6.<br>csv / SHA256:<br>b7b91e61bdf1c6<br>7e|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>23:10:00|POS-02|FTP<br>Upload<br>Attempt|10.0.6.50|cards-<br>20131129_part4.<br>csv / SHA256:<br>c5847f3ab670ae6<br>f|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>29<br>23:15:00|WORKSTATI<br>ON-12|Service<br>Installed|10.0.5.27|service:<br>backdoor_svc|Service<br>started at boot|
|---|---|---|---|---|---|
|2013-11-<br>29<br>23:20:00|POS-02|LSASS<br>Dump<br>Detected|10.0.7.85|lsass.dmp /<br>SHA256:<br>64f63ce5369037<br>5e|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>29<br>23:25:00|PROXY-01|Schedul<br>ed Task<br>Creation|10.0.1.22<br>2|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>23:30:00|VPN-01|SSH<br>Login|10.0.6.19<br>8|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>29<br>23:35:00|VPN-01|SQL<br>Dump|10.0.1.37|db-dump-<br>20131129.sql /<br>SHA256:<br>bab203e457e261<br>92|Sensitive data<br>exported|
|2013-11-<br>29<br>23:40:00|POS-01|FTP<br>Upload<br>Attempt|10.0.7.25<br>4|cards-<br>20131129_part3.<br>csv / SHA256:<br>62583c52cbffb0f<br>6|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>23:45:00|PROXY-01|Schedul<br>ed Task<br>Creation|10.0.2.23<br>0|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>29<br>23:50:00|WORKSTATI<br>ON-12|Large<br>POST to<br>external|10.0.9.78|cards-<br>20131129_part10<br>.csv / SHA256:<br>858109f8d8c4ebf<br>7|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>29<br>23:55:00|DB-01|SQL<br>Dump|10.0.4.32|db-dump-<br>20131129.sql /<br>SHA256:<br>58a332dd1c6493<br>e3|Sensitive data<br>exported|
|2013-11-<br>30<br>00:00:00|PROXY-01|FTP<br>Upload<br>Attempt|10.0.7.21<br>7|cards-<br>20131129_part6.<br>csv / SHA256:<br>521ffb2bd0e9b31<br>b|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

Public 255 

Lần ban hành: 1 

|2013-11-<br>30<br>00:05:00|POS-01|Config<br>File<br>Read|10.0.5.97|config.ini|Credentials<br>found in<br>config|
|---|---|---|---|---|---|
|2013-11-<br>30<br>00:10:00|POS-02|SSH<br>Login|10.0.4.76|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>30<br>00:15:00|POS-01|Config<br>File<br>Read|10.0.3.15<br>6|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>30<br>00:20:00|WEB-01|Large<br>POST to<br>external|10.0.7.11<br>5|cards-<br>20131129_part5.<br>csv / SHA256:<br>df97d92dd82d71<br>60|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>00:25:00|WORKSTATI<br>ON-12|Schedul<br>ed Task<br>Creation|10.0.10.2<br>15|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>00:30:00|LSASS-BOX|Suspicio<br>us<br>Process<br>Spawn|10.0.8.25<br>4|proc:<br>unknown_exec /<br>SHA256:<br>9c3e6af6f6180c6<br>4|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>30<br>00:35:00|WORKSTATI<br>ON-12|LSASS<br>Dump<br>Detected|10.0.8.90|lsass.dmp /<br>SHA256:<br>b70bd341ed530b<br>35|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>00:40:00|DB-01|LSASS<br>Dump<br>Detected|10.0.2.24<br>5|lsass.dmp /<br>SHA256:<br>be0cb2bc67eb9b<br>43|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>00:45:00|ADMIN-01|Large<br>POST to<br>external|10.0.9.17<br>0|cards-<br>20131129_part1.<br>csv / SHA256:<br>75e2a66da079b9<br>32|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>00:50:00|LSASS-BOX|Large<br>POST to<br>external|10.0.7.56|cards-<br>20131129_part8.<br>csv / SHA256:<br>d41b8af1da968ca<br>2|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Public 255 

Lần ban hành: 1 

|2013-11-<br>30<br>00:55:00|VPN-01|Service<br>Installed|10.0.1.17<br>7|service:<br>backdoor_svc|Service<br>started at boot|
|---|---|---|---|---|---|
|2013-11-<br>30<br>01:00:00|DB-01|Process<br>Memory<br>Read|10.0.10.2<br>29|blackpos-lab.bin<br>/ SHA256:<br>f74636c9a6dec5b<br>f|Credential<br>pattern found|
|2013-11-<br>30<br>01:05:00|LSASS-BOX|Service<br>Installed|10.0.2.17<br>3|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>01:10:00|WEB-01|FTP<br>Upload<br>Attempt|10.0.4.1|cards-<br>20131129_part1.<br>csv / SHA256:<br>3dd47b1e739c1d<br>1d|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>01:15:00|WEB-01|LSASS<br>Dump<br>Detected|10.0.8.92|lsass.dmp /<br>SHA256:<br>276dca0ba7eb16<br>a0|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>01:20:00|STAGE-01|SSH<br>Login|10.0.4.19<br>5|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>30<br>01:25:00|ADMIN-01|Service<br>Installed|10.0.6.14<br>1|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>01:30:00|WEB-01|Suspicio<br>us<br>Process<br>Spawn|10.0.8.10<br>1|proc:<br>unknown_exec /<br>SHA256:<br>9e4d12485cb51e<br>1b|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>30<br>01:35:00|WORKSTATI<br>ON-12|Schedul<br>ed Task<br>Creation|10.0.9.19<br>3|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>01:40:00|POS-01|SSH<br>Login|10.0.2.13<br>2|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>30<br>01:45:00|WORKSTATI<br>ON-12|SSH<br>Login|10.0.4.23<br>1|n/a|Login<br>successful<br>(possible|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

||||||credential<br>reuse)|
|---|---|---|---|---|---|
|2013-11-<br>30<br>01:50:00|POS-02|SQL<br>Dump|10.0.7.2|db-dump-<br>20131129.sql /<br>SHA256:<br>438b187127484d<br>78|Sensitive data<br>exported|
|2013-11-<br>30<br>01:55:00|WORKSTATI<br>ON-12|Service<br>Installed|10.0.3.3|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>02:00:00|PROXY-01|Service<br>Installed|10.0.2.10<br>9|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>02:05:00|DB-01|Large<br>POST to<br>external|10.0.6.21<br>3|cards-<br>20131129_part10<br>.csv / SHA256:<br>5001178f875605<br>03|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>02:10:00|DB-01|Process<br>Memory<br>Read|10.0.2.19<br>1|blackpos-lab.bin<br>/ SHA256:<br>24f6a192035f864<br>d|Credential<br>pattern found|
|2013-11-<br>30<br>02:15:00|VPN-01|Schedul<br>ed Task<br>Creation|10.0.8.17|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>02:20:00|ADMIN-01|FTP<br>Upload<br>Attempt|10.0.6.23<br>7|cards-<br>20131129_part4.<br>csv / SHA256:<br>ce01ff4245df446<br>6|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>02:25:00|PROXY-01|SQL<br>Dump|10.0.6.18<br>0|db-dump-<br>20131129.sql /<br>SHA256:<br>e813f6085dc2b9<br>db|Sensitive data<br>exported|
|2013-11-<br>30<br>02:30:00|WORKSTATI<br>ON-12|Service<br>Installed|10.0.3.37|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>02:35:00|VPN-01|Large<br>POST to<br>external|10.0.10.1<br>17|cards-<br>20131129_part10<br>.csv / SHA256:<br>400fb171f4347ee<br>9|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>30<br>02:40:00|WEB-01|Process<br>Memory<br>Read|10.0.7.13<br>3|blackpos-lab.bin<br>/ SHA256:<br>e2bda3e62f3dec5<br>3|Credential<br>pattern found|
|---|---|---|---|---|---|
|2013-11-<br>30<br>02:45:00|LSASS-BOX|SQL<br>Dump|10.0.3.10<br>5|db-dump-<br>20131129.sql /<br>SHA256:<br>f9cb407a44838a<br>45|Sensitive data<br>exported|
|2013-11-<br>30<br>02:50:00|POS-02|Suspicio<br>us<br>Process<br>Spawn|10.0.5.2|proc:<br>unknown_exec /<br>SHA256:<br>be05a3d196aef8c<br>8|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>30<br>02:55:00|POS-02|Schedul<br>ed Task<br>Creation|10.0.6.4|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>03:00:00|POS-02|Schedul<br>ed Task<br>Creation|10.0.10.2<br>44|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>03:05:00|LSASS-BOX|SSH<br>Login|10.0.5.15<br>1|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>30<br>03:10:00|ADMIN-01|Config<br>File<br>Read|10.0.4.24<br>8|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>30<br>03:15:00|STAGE-01|Large<br>POST to<br>external|10.0.6.63|cards-<br>20131129_part8.<br>csv / SHA256:<br>c0e80997db5043<br>5b|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>03:20:00|STAGE-01|SSH<br>Login|10.0.10.2<br>42|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>30<br>03:25:00|STAGE-01|Process<br>Memory<br>Read|10.0.8.10<br>8|blackpos-lab.bin<br>/ SHA256:<br>e869cc6ac1fc629<br>c|Credential<br>pattern found|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>30<br>03:30:00|ADMIN-01|LSASS<br>Dump<br>Detected|10.0.4.16<br>0|lsass.dmp /<br>SHA256:<br>d81942dbed9c3a<br>28|Possible<br>credential<br>exfil from<br>memory|
|---|---|---|---|---|---|
|2013-11-<br>30<br>03:35:00|VPN-01|Service<br>Installed|10.0.2.58|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>03:40:00|VPN-01|Large<br>POST to<br>external|10.0.9.72|cards-<br>20131129_part1.<br>csv / SHA256:<br>2f25ef8892a937e<br>b|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>03:45:00|PROXY-01|SSH<br>Login|10.0.5.11<br>4|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>30<br>03:50:00|VPN-01|Schedul<br>ed Task<br>Creation|10.0.6.24<br>0|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>03:55:00|WORKSTATI<br>ON-12|Schedul<br>ed Task<br>Creation|10.0.4.14<br>2|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>04:00:00|WEB-01|Large<br>POST to<br>external|10.0.5.24<br>9|cards-<br>20131129_part1.<br>csv / SHA256:<br>2adf79bd592249<br>8a|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>04:05:00|WORKSTATI<br>ON-12|SQL<br>Dump|10.0.4.55|db-dump-<br>20131129.sql /<br>SHA256:<br>4f1dff19803cf84<br>5|Sensitive data<br>exported|
|2013-11-<br>30<br>04:10:00|STAGE-01|Service<br>Installed|10.0.2.76|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>04:15:00|POS-01|Process<br>Memory<br>Read|10.0.1.78|blackpos-lab.bin<br>/ SHA256:<br>236fa33cdfa4a93<br>e|Credential<br>pattern found|
|2013-11-<br>30<br>04:20:00|PROXY-01|Suspicio<br>us<br>Process<br>Spawn|10.0.1.62|proc:<br>unknown_exec /<br>SHA256:|Spawned by<br>user<br>'svc_hvac'|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||||60aae3a070e6c5<br>06||
|---|---|---|---|---|---|
|2013-11-<br>30<br>04:25:00|POS-01|FTP<br>Upload<br>Attempt|10.0.9.19<br>9|cards-<br>20131129_part8.<br>csv / SHA256:<br>2b7760c699c070<br>3f|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>04:30:00|STAGE-01|LSASS<br>Dump<br>Detected|10.0.10.1<br>1|lsass.dmp /<br>SHA256:<br>c7da6e58e2bf9bd<br>0|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>04:35:00|POS-02|Schedul<br>ed Task<br>Creation|10.0.10.1<br>38|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>04:40:00|POS-02|LSASS<br>Dump<br>Detected|10.0.5.60|lsass.dmp /<br>SHA256:<br>dc6ecb759e708c<br>a8|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>04:45:00|WORKSTATI<br>ON-12|Process<br>Memory<br>Read|10.0.8.99|blackpos-lab.bin<br>/ SHA256:<br>71bc5cec3daf47f<br>5|Credential<br>pattern found|
|2013-11-<br>30<br>04:50:00|WORKSTATI<br>ON-12|FTP<br>Upload<br>Attempt|10.0.1.14<br>7|cards-<br>20131129_part1.<br>csv / SHA256:<br>e3977a9f3dc426e<br>e|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>04:55:00|POS-02|FTP<br>Upload<br>Attempt|10.0.9.18<br>1|cards-<br>20131129_part2.<br>csv / SHA256:<br>899dd387a12448<br>6e|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>05:00:00|POS-01|SQL<br>Dump|10.0.1.15<br>3|db-dump-<br>20131129.sql /<br>SHA256:<br>c6bc506c73aa0f7<br>6|Sensitive data<br>exported|
|2013-11-<br>30<br>05:05:00|POS-02|Process<br>Memory<br>Read|10.0.4.94|blackpos-lab.bin<br>/ SHA256:<br>0e4c9632e0e478<br>4c|Credential<br>pattern found|
|2013-11-<br>30<br>05:10:00|PROXY-01|Suspicio<br>us|10.0.9.10<br>1|proc:<br>unknown_exec /<br>SHA256:|Spawned by<br>user<br>'svc_hvac'|

**VIETTEL AI RACE** Public 255 

**BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||Process<br>Spawn||99458975f221c7<br>69||
|---|---|---|---|---|---|
|2013-11-<br>30<br>05:15:00|WEB-01|Service<br>Installed|10.0.6.66|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>05:20:00|WORKSTATI<br>ON-12|FTP<br>Upload<br>Attempt|10.0.9.20<br>6|cards-<br>20131129_part1.<br>csv / SHA256:<br>84c714c3ea65f48<br>6|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>05:25:00|WORKSTATI<br>ON-12|Process<br>Memory<br>Read|10.0.9.11<br>7|blackpos-lab.bin<br>/ SHA256:<br>7d8ba738839f90<br>6c|Credential<br>pattern found|
|2013-11-<br>30<br>05:30:00|STAGE-01|Process<br>Memory<br>Read|10.0.9.27|blackpos-lab.bin<br>/ SHA256:<br>cfe7e5b9a80458a<br>9|Credential<br>pattern found|
|2013-11-<br>30<br>05:35:00|PROXY-01|Config<br>File<br>Read|10.0.6.89|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>30<br>05:40:00|VPN-01|FTP<br>Upload<br>Attempt|10.0.8.10|cards-<br>20131129_part8.<br>csv / SHA256:<br>e249ea2439fb1b<br>b1|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>05:45:00|LSASS-BOX|Large<br>POST to<br>external|10.0.4.16<br>0|cards-<br>20131129_part4.<br>csv / SHA256:<br>bfaf5cdef585a56<br>e|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>05:50:00|DB-01|Schedul<br>ed Task<br>Creation|10.0.10.1<br>55|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>05:55:00|WORKSTATI<br>ON-12|SSH<br>Login|10.0.10.1<br>9|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>30<br>06:00:00|WEB-01|Schedul<br>ed Task<br>Creation|10.0.3.19<br>5|task:<br>persist_worker|Persistence<br>scheduled|

Public 255 

**VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>30<br>06:05:00|POS-02|SSH<br>Login|10.0.9.15<br>4|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|---|---|---|---|---|---|
|2013-11-<br>30<br>06:10:00|STAGE-01|Suspicio<br>us<br>Process<br>Spawn|10.0.7.12<br>2|proc:<br>unknown_exec /<br>SHA256:<br>f88f46ab20ae03b<br>5|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>30<br>06:15:00|VPN-01|Suspicio<br>us<br>Process<br>Spawn|10.0.6.12<br>4|proc:<br>unknown_exec /<br>SHA256:<br>c62af96724fac63<br>b|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>30<br>06:20:00|DB-01|Service<br>Installed|10.0.5.14<br>8|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>06:25:00|POS-01|LSASS<br>Dump<br>Detected|10.0.4.16<br>3|lsass.dmp /<br>SHA256:<br>42048aa9748407<br>65|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>06:30:00|PROXY-01|Process<br>Memory<br>Read|10.0.9.21<br>2|blackpos-lab.bin<br>/ SHA256:<br>5c2f395426b296<br>ec|Credential<br>pattern found|
|2013-11-<br>30<br>06:35:00|PROXY-01|Large<br>POST to<br>external|10.0.8.73|cards-<br>20131129_part4.<br>csv / SHA256:<br>b844a46ef03936<br>16|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>06:40:00|LSASS-BOX|Process<br>Memory<br>Read|10.0.7.13<br>4|blackpos-lab.bin<br>/ SHA256:<br>19cb008c900a81<br>22|Credential<br>pattern found|
|2013-11-<br>30<br>06:45:00|STAGE-01|SQL<br>Dump|10.0.5.90|db-dump-<br>20131129.sql /<br>SHA256:<br>a5d4c8e7c9a0eb<br>7f|Sensitive data<br>exported|
|2013-11-<br>30<br>06:50:00|WORKSTATI<br>ON-12|Schedul<br>ed Task<br>Creation|10.0.3.20<br>1|task:<br>persist_worker|Persistence<br>scheduled|

**VIETTEL AI RACE** Public 255 **BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|2013-11-<br>30<br>06:55:00|ADMIN-01|Process<br>Memory<br>Read|10.0.3.13<br>6|blackpos-lab.bin<br>/ SHA256:<br>c0652ae67d0ef92<br>4|Credential<br>pattern found|
|---|---|---|---|---|---|
|2013-11-<br>30<br>07:00:00|STAGE-01|Service<br>Installed|10.0.4.94|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>07:05:00|DB-01|FTP<br>Upload<br>Attempt|10.0.1.91|cards-<br>20131129_part1.<br>csv / SHA256:<br>06cf0b882ef6dff<br>a|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>07:10:00|DB-01|SQL<br>Dump|10.0.7.24<br>1|db-dump-<br>20131129.sql /<br>SHA256:<br>b5b5d2863976af<br>7a|Sensitive data<br>exported|
|2013-11-<br>30<br>07:15:00|POS-01|Service<br>Installed|10.0.4.81|service:<br>backdoor_svc|Service<br>started at boot|
|2013-11-<br>30<br>07:20:00|WEB-01|LSASS<br>Dump<br>Detected|10.0.6.12<br>7|lsass.dmp /<br>SHA256:<br>e86ff55df7e8d24<br>d|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>07:25:00|VPN-01|SSH<br>Login|10.0.5.22|n/a|Login<br>successful<br>(possible<br>credential<br>reuse)|
|2013-11-<br>30<br>07:30:00|WEB-01|FTP<br>Upload<br>Attempt|10.0.10.2<br>16|cards-<br>20131129_part7.<br>csv / SHA256:<br>92c2315b8e64eb<br>fb|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>07:35:00|POS-01|Schedul<br>ed Task<br>Creation|10.0.5.12<br>2|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>07:40:00|DB-01|LSASS<br>Dump<br>Detected|10.0.3.17<br>3|lsass.dmp /<br>SHA256:<br>1c00cb07f6cdc30<br>4|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>07:45:00|WEB-01|Process<br>Memory<br>Read|10.0.5.11<br>6|blackpos-lab.bin<br>/ SHA256:|Credential<br>pattern found|

Public 255 

**VIETTEL AI RACE** 

**BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|||||0e3fd56f5d59fe5<br>c||
|---|---|---|---|---|---|
|2013-11-<br>30<br>07:50:00|WORKSTATI<br>ON-12|Suspicio<br>us<br>Process<br>Spawn|10.0.2.25<br>3|proc:<br>unknown_exec /<br>SHA256:<br>a284aa86f4c2da3<br>4|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>30<br>07:55:00|ADMIN-01|Config<br>File<br>Read|10.0.6.11<br>7|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>30<br>08:00:00|WEB-01|SQL<br>Dump|10.0.6.25<br>3|db-dump-<br>20131129.sql /<br>SHA256:<br>ae3a5a8ab3bf844<br>8|Sensitive data<br>exported|
|2013-11-<br>30<br>08:05:00|PROXY-01|FTP<br>Upload<br>Attempt|10.0.1.17|cards-<br>20131129_part2.<br>csv / SHA256:<br>b43c3900be5f5f5<br>0|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>08:10:00|VPN-01|LSASS<br>Dump<br>Detected|10.0.3.25<br>1|lsass.dmp /<br>SHA256:<br>b68e9e59e0240e<br>dc|Possible<br>credential<br>exfil from<br>memory|
|2013-11-<br>30<br>08:15:00|PROXY-01|FTP<br>Upload<br>Attempt|10.0.8.23<br>9|cards-<br>20131129_part5.<br>csv / SHA256:<br>338d2f32d1d3a0<br>71|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>08:20:00|STAGE-01|Process<br>Memory<br>Read|10.0.1.17<br>0|blackpos-lab.bin<br>/ SHA256:<br>722efe12b0b810<br>a8|Credential<br>pattern found|
|2013-11-<br>30<br>08:25:00|PROXY-01|Large<br>POST to<br>external|10.0.1.10<br>7|cards-<br>20131129_part1.<br>csv / SHA256:<br>97bcacd1078ebe<br>26|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>08:30:00|POS-02|Suspicio<br>us<br>Process<br>Spawn|10.0.1.17|proc:<br>unknown_exec /<br>SHA256:<br>490f82df73a8eea<br>d|Spawned by<br>user<br>'svc_hvac'|

Public 255 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE BÁO CÁO CHI TIẾT: KỸ THUẬT CREDENTIAL DUMPING (MITRE T1003)** 

Lần ban hành: 1 

|2013-11-<br>30<br>08:35:00|POS-02|LSASS<br>Dump<br>Detected|10.0.3.58|lsass.dmp /<br>SHA256:<br>a10d1426dcbb25<br>b2|Possible<br>credential<br>exfil from<br>memory|
|---|---|---|---|---|---|
|2013-11-<br>30<br>08:40:00|LSASS-BOX|Large<br>POST to<br>external|10.0.7.20<br>1|cards-<br>20131129_part9.<br>csv / SHA256:<br>865b2dd49c9253<br>b2|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>08:45:00|LSASS-BOX|Large<br>POST to<br>external|10.0.1.13<br>8|cards-<br>20131129_part2.<br>csv / SHA256:<br>e7149c9aea07d4f<br>8|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>08:50:00|PROXY-01|Config<br>File<br>Read|10.0.8.20<br>9|config.ini|Credentials<br>found in<br>config|
|2013-11-<br>30<br>08:55:00|POS-01|Schedul<br>ed Task<br>Creation|10.0.5.19<br>8|task:<br>persist_worker|Persistence<br>scheduled|
|2013-11-<br>30<br>09:00:00|VPN-01|FTP<br>Upload<br>Attempt|10.0.7.14|cards-<br>20131129_part5.<br>csv / SHA256:<br>b13ccbd23b0894<br>a3|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>09:05:00|WORKSTATI<br>ON-12|Suspicio<br>us<br>Process<br>Spawn|10.0.5.16<br>8|proc:<br>unknown_exec /<br>SHA256:<br>9a73dff0d8ef5fa<br>0|Spawned by<br>user<br>'svc_hvac'|
|2013-11-<br>30<br>09:10:00|POS-02|Large<br>POST to<br>external|10.0.8.11<br>6|cards-<br>20131129_part4.<br>csv / SHA256:<br>ce02838f65efe81<br>7|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|
|2013-11-<br>30<br>09:15:00|POS-02|FTP<br>Upload<br>Attempt|10.0.9.10<br>4|cards-<br>20131129_part9.<br>csv / SHA256:<br>a24e1365964acd<br>ce|Outbound to<br>ftp-exfil-<br>targetlab.exa<br>mple|

**VIETTEL AI RACE** Public 255 **BÁO CÁO CHI TIẾT: KỸ THUẬT** Lần ban hành: 1 **CREDENTIAL DUMPING (MITRE T1003)** 

**==> picture [39 x 47] intentionally omitted <==**

- Các dữ liệu, hash và domain trong tài liệu này đều đã được giả hóa cho mục đích đào tạo. 

- Không bao gồm mã độc thật; chỉ mô phỏng hành vi để phục vụ lab và phân tích. 

Tài liệu tham khảo (gợi ý): 

- Báo cáo điều tra vụ Target Breach (2013) 

- Bài viết phân tích BlackPOS / memory-scraper 

- MITRE ATT&CK: T1003 Credential Dumping