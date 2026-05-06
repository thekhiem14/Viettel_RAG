**VIETTEL AI RACE** Public 258 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SALT TYPHOON** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

## **1. MỤC TIÊU CHUNG** 

Tiến hành nghiên cứu toàn diện về nhóm Salt Typhoon, tập trung vào chiến thuật, kỹ thuật và thủ tục của họ. Sử dụng khung MITRE ATT&CK để vạch ra các hoạt động của nhóm và cung cấp những hiểu biết có thể hành động. 

Phát hiện của bản báo cáo này đóng một vai trò quan trọng trong việc củng cố khả năng phòng thủ chống lại kẻ thù này. 

## **2. Salt Typhoon** 

Salt Typhoon là một nhóm do Nhà nước Cộng hòa Nhân dân Trung Hoa (PRC) hậu thuẫn, đã hoạt động ít nhất từ năm 2019 và chịu trách nhiệm cho nhiều vụ xâm nhập vào hạ tầng mạng của các nhà cung cấp dịch vụ internet (ISP) lớn tại Hoa Kỳ. [1] 

## **JumbledPath** 

Nhóm này custom nhiều loại mã độc khác nhau, một trong số đó là JumbledPath với ID S1206. [2] 

**JumbledPath** là một tiện ích (utility) được xây dựng tùy chỉnh bằng ngôn ngữ **GO** , đã được **Salt Typhoon** sử dụng ít nhất từ năm 2024 để thực hiện packet capture trên các thiết bị Cisco từ xa. **JumbledPath** được biên dịch dưới dạng ELF binary sử dụng kiến trúc x86-64, điều này khiến nó có khả năng được sử dụng trên các hệ điều hành Linux và các thiết bị mạng từ nhiều nhà cung cấp khác nhau.[3] 

Một trong các kỹ thuật mà **JumbledPath** thực hiện đó là hành vi xóa log tại ID **T1070.002.** [4] 

## JumbledPath Techniques Used 

|---|---|---|---|
|**Domain**|**ID**|**Name**|**Use**|
|**Enterprise**|T1560|Archive Collected<br>Data|JumbledPath can compress and<br>encrypt exfiltrated packet captures<br>from targeted devices.|
|**Enterprise**|T1665|Hide<br>Infrastructure|JumbledPath can use a chain of<br>jump hosts to communicate with<br>compromised devices to obscure<br>actor infrastructure.|
**VIETTEL AI RACE** Public 258 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SALT TYPHOON** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|
|**Enterprise**|T1562|Impair Defenses|JumbledPath can impair logging<br>on all devices used along its<br>connection path to compromised<br>hosts.|
|**Enterprise**|T1070|Indicator<br>Removal: Clear<br>Linux or Mac<br>System Logs|JumbledPath can clear logs on all<br>devices used along its connection<br>path to compromised network<br>infrastructure.|
|**Enterprise**|T1104|Multi-Stage<br>Channels|JumbledPath can communicate<br>over a unique series of connections<br>to send and retrieve data from<br>exploited devices.|
|**Enterprise**|T1040|Network Sniffing|JumbledPath has the ability to<br>perform packet capture on remote<br>devices via actor-defined jump-<br>hosts.|

## **GHOSTSPIDER** 

**GHOSTSPIDER** được xem như là một backdoor đa mô hình tinh vi được thiết kế với nhiều lớp để load các mô-đun khác nhau dựa trên các mục đích cụ thể. Backdoor này giao tiếp với C2 của mình bằng giao thức tùy chỉnh được bảo vệ bởi bảo mật lớp vận chuyển (TLS), đảm bảo giao tiếp an toàn. [5] 

Dưới đây là list domain mà **GHOSTSPIDER** kết nối về C2, có thể nói đa phần đều gửi về .com, đặc biệt tròn đó có 1 doamin đuôi .dev 
**VIETTEL AI RACE** Public 258 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SALT TYPHOON** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

**==> picture [319 x 403] intentionally omitted <==**

## **GHOSTSPIDER Techniques Used** 

Mặc dù đã có mã định danh là **FGS5008** trên MITRE nhưng chưa có nội dung chi tiết công khai [6] 

## **3. Salt Typhoon Techniques Used** 

|---|---|---|---|---|
|**Domain**|**ID**||**Name**|**Use**|
|**Enterprise**|T10<br>98|.004|Account<br>Manipulation:<br>SSH<br>Authorized<br>Keys|Salt Typhoon has added SSH<br>authorized_keys under root or<br>other users at the Linux level on<br>compromised network devices.|
|**Enterprise**|T11|.002|Brute Force:|Salt Typhoon has cracked|
**VIETTEL AI RACE** Public 258 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SALT TYPHOON** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
||10||Password<br>Cracking|passwords for accounts with weak<br>encryption obtained from the<br>configuration files of<br>compromised network devices.|
|**Enterprise**|T1136||Create<br>Account|Salt Typhoon has created Linux-<br>level users on compromised<br>network devices through<br>modification of /etc/shadow and<br>/etc/passwd.|
|**Enterprise**|T16<br>02|.002|Data from<br>Configuration<br>Repository:<br>Network<br>Device<br>Configuration<br>Dump|Salt Typhoon has attempted to<br>acquire credentials by dumping<br>network device configurations.[|
|**Enterprise**|T15<br>87|.001|Develop<br>Capabilities:<br>Malware|Salt Typhoon has used custom<br>tooling including JumbledPath.|
|**Enterprise**|T10<br>48|.003|Exfiltration<br>Over<br>Alternative<br>Protocol:<br>Exfiltration<br>Over<br>Unencrypted<br>Non-C2<br>Protocol|Salt Typhoon has exfiltrated<br>configuration files from exploited<br>network devices over FTP and<br>TFTP.|
|**Enterprise**|T1190||Exploit<br>Public-Facing<br>Application|Salt Typhoon has exploited CVE-<br>2018-0171 in the Smart Install<br>feature of Cisco IOS and Cisco<br>IOS XE software for initial access.|
|**Enterprise**|T15<br>90|.004|Gather Victim<br>Network<br>Information:<br>Network<br>Topology|Salt Typhoon has used<br>configuration files from exploited<br>network devices to help discover<br>upstream and downstream network<br>segments.|
Public 258 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SALT TYPHOON** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|**Enterprise**|T15<br>62|.004|Impair<br>Defenses:<br>Disable or<br>Modify<br>System<br>Firewall|Salt Typhoon has made changes to<br>the Access Control List (ACL) and<br>loopback interface address on<br>compromised devices.|
|**Enterprise**|T10<br>70|.002|Indicator<br>Removal:<br>Clear Linux or<br>Mac System<br>Logs|Salt Typhoon has cleared logs<br>including .bash_history, auth.log,<br>lastlog, wtmp, and btmp.|
|**Enterprise**|T1040||Network<br>Sniffing|Salt Typhoon has used a variety of<br>tools and techniques to capture<br>packet data between network<br>interfaces.|
|**Enterprise**|T15<br>88|.002|Obtain<br>Capabilities:<br>Tool|Salt Typhoon has used publicly<br>available tooling to exploit<br>vulnerabilities.|
|**Enterprise**|T1572||Protocol<br>Tunneling|Salt Typhoon has modified device<br>configurations to create and use<br>Generic Routing Encapsulation<br>(GRE) tunnels.|
|**Enterprise**|T10<br>21|.004|Remote<br>Services: SSH|Salt Typhoon has modified the<br>loopback address on compromised<br>switches and used them as the<br>source of SSH connections to<br>additional devices within the target<br>environment, allowing them to<br>bypass access control lists (ACLs).|

## **4. References** 

**[1] Salt Typhoon. https://attack.mitre.org/groups/G1045/** 

**[2] JumbledPath. https://attack.mitre.org/software/S1206/** 

**[3] Weathering the storm: In the midst of a Typhoon. - - https://blog.talosintelligence.com/salt typhoon analysis/** 
**VIETTEL AI RACE** Public 258 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SALT TYPHOON** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

**[4] Indicator Removal: Clear Linux or Mac System Logs. https://attack.mitre.org/techniques/T1070/002/** 

**[5] Game of Emperor: Unveiling Long Term Earth Estries Cyber Intrusions. https://www.trendmicro.com/en_vn/research/24/k/earthestries.html** 

**[6] Ghost Spider. https://fight.mitre.org/software/FGS5008/**