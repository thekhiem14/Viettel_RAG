Public 274 

**VIETTEL AI RACE** 

**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

## **1. MỤC TIÊU CHUNG** 

Tiến hành nghiên cứu toàn diện về nhóm Sandworm, tập trung vào chiến thuật, kỹ thuật và thủ tục của họ. Sử dụng khung MITRE ATT&CK để vạch ra các hoạt động của nhóm và cung cấp những hiểu biết có thể hành động. 

Phát hiện của bản báo cáo này đóng một vai trò quan trọng trong việc củng cố khả năng phòng thủ chống lại kẻ thù này. 

## **2. Sandworm Team** 

**Sandworm** là một nhóm APT có liên hệ rộng rãi với các chiến dịch phá hoại nhắm vào hạ tầng trọng yếu (điện lực, viễn thông, chính phủ). Theo Mitre, nhóm bắt đầu hoạt động từ năm 2009. Sandworm Team thể hiện năng lực tấn công có hệ thống, từ xâm nhập – duy trì – điều khiển – phá hoại trên cả IT và OT 

Một fun fact thú vị là tên gọi “ **Sandworm** ” không phải do họ tự đặt mà xuất phát từ các nhà nghiên cứu phương Tây, lấy cảm hứng từ loài sinh vật khổng lồ trong tiểu thuyết Dune – sống ẩn mình dưới cát rồi bất ngờ tấn công dữ dội. 

## **2.1 Nguồn gốc và tổ chức** 

**Sandworm** là một nhóm do nhà nước bảo trợ được liên kết với Nga. Nhiều tổ chức an ninh mạng và cơ quan chính phủ quốc tế đã gán nhóm này cho **Cơ quan Tình báo Quân đội Nga (GRU)** , cụ thể là một đơn vị tác chiến mạng thuộc Main Centre for Special Technologies (được ghi nhận là Unit 74455). 

**Sandworm** được mô tả không phải là một nhóm “tội phạm mạng” độc lập mà là một đơn vị quân sự/tác chiến mạng có mục tiêu chiến lược, do đó hoạt động theo chỉ đạo, mục tiêu và năng lực của cơ quan nhà nước ( **GRU** ). Sự vận hành theo mô hình đơn vị quân đội giải thích việc nhóm sử dụng các chiến lược nhắm mục tiêu lớn (critical infrastructure), sự phối hợp giữa nhiều chiến dịch, và khả năng triển khai mã độc có tầm phá hoại cao. 

## **2.2 Các vụ tấn công nổi bật** 

Một số sự kiện tiêu biểu do **Sandworm** thực hiện: 

- **2009–2014: Hình thành, trinh sát và cắm chốt trong mạng mục tiêu (persistence đa lớp).** 

- **2015–2016: Chiến dịch tại Ukraine:** lạm dụng công cụ quản trị, thu thập thông tin xác thực, dùng script ufn.vbs, quan sát điều khiển SCADA gây mất điện. 
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

- **2017:** Phát tán NotPetya với khả năng lây lan kiểu worm, khai thác MS17‑010, sử dụng chứng thực nội bộ để di chuyển ngang. 

- **2022:** Chuỗi tấn công nhắm vào SCADA/ICS, duy trì hiện diện thông qua web‑shell bằng Neo‑REGEORG; thực thi tác vụ qua scilc.exe; phá hoại bằng CaddyWiper với khả năng Native API (T1106). Tấn công vào modem bằng AcidRain. 

## **2.3 Ukraine Power Grid** 

## **2.3.1 Mục tiêu & Tác động** 

Nhóm này nhắm vào doanh nghiệp điện lực và hệ thống SCADA/DMS/EMS phụ trợ vận hành lưới. Gây ra gián đoạn cấp điện cục bộ, thao túng vận hành từ xa; gây mất dịch vụ và ảnh hưởng xã hội. 

## **2.3.2 Kỹ thuật & Công cụ đã ghi nhận** 

- Credential Access 

- LSASS Memory (T1003.001) – trích xuất hash/creds từ tiến trình LSASS để leo thang đặc quyền nội bộ. 

- Brute Force (T1110) – thử mật khẩu/khớp tài khoản trên nhiều host để mở rộng kiểm soát. 

- Execution/Automation: Sử dụng script VBS ufn.vbs trong chuỗi tự động hoá hành động (kiểm soát, duy trì, hoặc dàn lệnh). 

- Lateral Movement: Khai thác thông tin xác thực thu được để di chuyển ngang qua mạng OT/IT; lạm dụng công cụ quản trị hợp lệ. 

Khái quát lại: 

Phishing/khai thác điểm yếu -> Cắm chốt + thu thập creds (T1003.001, T1110) -> Tự động hoá điều khiển (VBS ufn.vbs) -> Di chuyển vào tầng OT -> Thao túng SCADA -> Che giấu & rút lui. 

## **2.4 NotPetya** 

## **2.4.1 Mục tiêu & Tác động** 

Về bản chất **NotPetya** có hành vi ransomware nhưng thực chất phá hoại (wiper‑like) với khả năng tự lan truyền kiểu worm. Thông qua khai thác lỗ hổng SMBv1 MS17‑010, đồng thời lạm dụng chứng thực nội bộ (công cụ hợp lệ như PsExec/WMIC) để di chuyển ngang tốc độ cao. 
**VIETTEL AI RACE** Public 274 

**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

Cuộc tấn công đã lan toàn cầu, gây gián đoạn chuỗi cung ứng, thiệt hại lớn về tài chính/vận hành. 

## **2.5 AcidRain** 

## **2.5.1 Mục tiêu & Tác động** 

**AcidRain** nhắm vào firmware/thành phần lưu trữ của modem/thiết bị mạng, gây mất kết nối diện rộng – đặc biệt nguy hiểm với hạ tầng vệ tinh/viễn thông khi bị đồng loạt tác động. 

## **3. Sandworm Team Techniques Used** 

|---|---|---|---|---|
|**Do**<br>**mai**<br>**n**|**ID**||**Name**|**Use**|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>0<br>8<br>7|.<br>0<br>0<br>2|<br>Account<br>Discovery:<br>Domain<br>Account|Sandworm Team has used a tool to query<br>Active Directory using LDAP, discovering<br>information about usernames listed in AD.|
|||.<br>0<br>0<br>3|<br>Account<br>Discovery:<br>Email<br>Account|Sandworm Team used malware to enumerate<br>email settings, including usernames and<br>passwords, from the M.E.Doc application.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>098||Account<br>Manipulation|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used the sp_addlinkedsrvlogin<br>command in MS-SQL to create a link between a<br>created account and other servers in the<br>network.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>583||Acquire<br>Infrastructure|Sandworm Team used various third-party email<br>campaign management services to deliver<br>phishing emails.|
||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|Public 274|
|---|---|---|---|---|---|
||||**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN**<br>**CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM**<br>**SANDWORM TEAM**||Lần ban hành: 1|
|||.<br>0<br>0<br>1|<br>Domains|Sandworm Team has registered domain names<br>and created URLs that are often designed to<br>mimic or spoof legitimate websites, such as<br>email login pages, online file sharing and<br>storage websites, and password reset pages,<br>while also hosting these items on legitimate,<br>compromised network infrastructure.||
|||.<br>0<br>0<br>4|<br>Server|Sandworm Team has leased servers from<br>resellers instead of leasing infrastructure<br>directly from hosting companies to enable its<br>operations.||
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>9<br>5|.<br>0<br>0<br>2|<br>Active<br>Scanning:<br>Vulnerability<br>Scanning|Sandworm Team has scanned network<br>infrastructure for vulnerabilities as part of its<br>operational planning.||
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>0<br>7<br>1|.<br>0<br>0<br>1|<br>Application<br>Layer<br>Protocol:<br>Web<br>Protocols|Sandworm Team's BCS-server tool connects to<br>the designated C2 server via HTTP.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team used BlackEnergy to<br>communicate between compromised hosts and<br>their command-and-control servers via HTTP<br>post requests.||
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>110||Brute Force|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used a script to attempt RPC<br>authentication against a number of hosts.||
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|**En**<br>**ter**<br>**pr**<br>**ise**|**En**<br>**ter**<br>**pr**<br>**ise**|||||
|---|---|---|---|---|---|
||**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>0<br>5<br>9|.<br>0<br>0<br>1|<br>Command<br>and Scripting<br>Interpreter:<br>PowerShell|Sandworm Team has used PowerShell scripts to<br>run a credential harvesting tool in memory to<br>evade defenses.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used PowerShell scripts to run<br>a credential harvesting tool in memory to evade<br>defenses.<br>During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team utilized a PowerShell utility<br>called TANKTRAP to spread and launch a<br>wiper using Windows Group Policy.|
||||.<br>0<br>0<br>3|<br>Command<br>and Scripting<br>Interpreter:<br>Windows<br>Command<br>Shell|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used the xp_cmdshell<br>command in MS-SQL.|
||||.<br>0<br>0<br>5|<br>Command<br>and Scripting<br>Interpreter:<br>Visual Basic|Sandworm Team has created VBScripts to run<br>an SSH server.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team installed a VBA script called<br>vba_macro.exe. This macro dropped<br>FONTCACHE.DAT, the primary BlackEnergy<br>implant; rundll32.exe, for executing the<br>malware; NTUSER.log, an empty file; and<br>desktop.ini, the default file used to determine<br>folder displays on Windows machines.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team created VBScripts to run on<br>an SSH server.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>8<br>6|.<br>0<br>0<br>1|<br>Compromise<br>Accounts:<br>Social Media<br>Accounts|Sandworm Team creates credential capture<br>webpages to compromise existing, legitimate<br>social media accounts.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>554||Compromise<br>Host<br>Software<br>Binary|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used a trojanized version of<br>Windows Notepad to add a layer of persistence<br>for Industroyer.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>8<br>4|.<br>0<br>0<br>4|<br>Compromise<br>Infrastructure<br>: Server|Sandworm Team compromised legitimate Linux<br>servers running the EXIM mail transfer agent<br>for use in subsequent campaigns.|
|||.<br>0<br>0<br>5|<br>Compromise<br>Infrastructure<br>: Botnet|Sandworm Team has used a large-scale botnet<br>to target Small Office/Home Office (SOHO)<br>network devices.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>1<br>3<br>6|.<br>0<br>0<br>2|<br>Create<br>Account:<br>Domain<br>Account|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team created privileged domain<br>accounts to be used for further exploitation and<br>lateral movement.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team created two new accounts,<br>"admin" and "система" (System). The accounts<br>were then assigned to a domain matching local<br>operation and were delegated new privileges.|
|**En**<br>**ter**|T<br>1<br>5|.<br>0|Create or<br>Modify<br>System<br>Process:|During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team configured Systemd to<br>maintain persistence of GOGETTER,<br>specifying the WantedBy=multi-user.target|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**pr**<br>**ise**|4<br>3|0<br>2|<br>Systemd<br>Service|configuration to run GOGETTER when the<br>system begins accepting user logins.|
|||.<br>0<br>0<br>3|<br>Create or<br>Modify<br>System<br>Process:<br>Windows<br>Service|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used an arbitrary system<br>service to load at system boot for persistence for<br>Industroyer. They also replaced the ImagePath<br>registry value of a Windows service with a new<br>backdoor binary.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>5<br>5|.<br>0<br>0<br>3|<br>Credentials<br>from<br>Password<br>Stores:<br>Credentials<br>from Web<br>Browsers|Sandworm Team's CredRaptor tool can collect<br>saved passwords from various internet<br>browsers.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>485||Data<br>Destruction|Sandworm Team has used CaddyWiper,<br>SDelete, and the BlackEnergy KillDisk<br>component to overwrite files on victim systems.<br>Additionally, Sandworm Team has used the<br>JUNKMAIL tool to overwrite files with null<br>bytes.<br>During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team deployed CaddyWiper on the<br>victim’s IT environment systems to wipe files<br>related to the OT capabilities, along with<br>mapped drives, and physical drive partitions.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>1<br>3<br>2|.<br>0<br>0<br>1|<br>Data<br>Encoding:<br>Standard<br>Encoding|Sandworm Team's BCS-server tool uses base64<br>encoding and HTML tags for the<br>communication traffic between the C2 server.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>486||Data<br>Encrypted<br>for Impact|Sandworm Team has used Prestige ransomware<br>to encrypt data at targeted organizations in<br>transportation and related logistics industries in<br>Ukraine and Poland.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>213||Data from<br>Information<br>Repositories|Sandworm Team exfiltrates data of interest<br>from enterprise databases using Adminer.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>005||Data from<br>Local<br>System|Sandworm Team has exfiltrated internal<br>documents, files, and other data from<br>compromised hosts.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>4<br>9<br>1|.<br>0<br>0<br>2|<br>Defacement:<br>External<br>Defacement|Sandworm Team defaced approximately 15,000<br>websites belonging to Georgian government,<br>non-government, and private sector<br>organizations in 2019.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>140||Deobfuscate/<br>Decode Files<br>or<br>Information|Sandworm Team's VBS backdoor can decode<br>Base64-encoded data and save it to the<br>%TEMP% folder. The group also decrypted<br>received information using the Triple DES<br>algorithm and decompresses it using GZip.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>8<br>7|.<br>0<br>0<br>1|<br>Develop<br>Capabilities:<br>Malware|Sandworm Team has developed malware for its<br>operations, including malicious mobile<br>applications and destructive malware such as<br>NotPetya and Olympic Destroyer.|
|**En**<br>**ter**|T<br>1<br>5|.<br>0|Disk Wipe:<br>Disk|Sandworm Team has used the BlackEnergy<br>KillDisk component to corrupt the infected<br>system's master boot record.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**pr**<br>**ise**|6<br>1|0<br>2|<br>Structure<br>Wipe||
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>4<br>8<br>4|.<br>0<br>0<br>1|<br>Domain or<br>Tenant<br>Policy<br>Modification<br>: Group<br>Policy<br>Modification|During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team leveraged Group Policy<br>Objects (GPOs) to deploy and execute malware.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>499||Endpoint<br>Denial of<br>Service|Sandworm Team temporarily disrupted service<br>to Georgian government, non-government, and<br>private sector websites after compromising a<br>Georgian web hosting provider in 2019.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>8<br>5|.<br>0<br>0<br>1|<br>Establish<br>Accounts:<br>Social Media<br>Accounts|Sandworm Team has established social media<br>accounts to disseminate victim internal-only<br>documents and other sensitive data.|
|||.<br>0<br>0<br>2|<br>Establish<br>Accounts:<br>Email<br>Accounts|Sandworm Team has created email accounts<br>that mimic legitimate organizations for its<br>spearphishing operations.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>041||Exfiltration<br>Over C2<br>Channel|Sandworm Team has sent system information to<br>its C2 server using HTTP.|
|**En**<br>**ter**|T1<br>190||Exploit<br>Public-|Sandworm Team exploits public-facing<br>applications for initial access and to acquire<br>infrastructure, such as exploitation of the EXIM<br>mail transfer agent in Linux systems.|
Public 274 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|**pr**<br>**ise**|||Facing<br>Application||
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>203||Exploitation<br>for Client<br>Execution|Sandworm Team has exploited vulnerabilities in<br>Microsoft PowerPoint via OLE objects (CVE-<br>2014-4114) and Microsoft Word via crafted<br>TIFF images (CVE-2013-3906).|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>133||External<br>Remote<br>Services|Sandworm Team has used Dropbear SSH with a<br>hardcoded backdoor password to maintain<br>persistence within the target network.<br>Sandworm Team has also used VPN tunnels<br>established in legitimate software company<br>infrastructure to gain access to internal networks<br>of that software company's users.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team installed a modified Dropbear<br>SSH client as the backdoor to target systems.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>083||File and<br>Directory<br>Discovery|Sandworm Team has enumerated files on a<br>compromised host.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>9<br>2|.<br>0<br>0<br>2|<br>Gather<br>Victim Host<br>Information:<br>Software|Sandworm Team has researched software code<br>to enable supply-chain operations, most notably<br>for the 2017 NotPetya attack. Sandworm Team<br>also collected a list of computers using specific<br>software as part of its targeting efforts.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>8<br>9|.<br>0<br>0<br>2|<br>Gather<br>Victim<br>Identity<br>Information:|Sandworm Team has obtained valid emails<br>addresses while conducting research against<br>target organizations that were subsequently used<br>in spearphishing campaigns.|
Public 274 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
||||Email<br>Addresses||
|||.<br>0<br>0<br>3|<br>Gather<br>Victim<br>Identity<br>Information:<br>Employee<br>Names|Sandworm Team's research of potential victim<br>organizations included the identification and<br>collection of employee information.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>9<br>0|.<br>0<br>0<br>1|<br>Gather<br>Victim<br>Network<br>Information:<br>Domain<br>Properties|Sandworm Team conducted technical<br>reconnaissance of the Parliament of Georgia's<br>official internet domain prior to its 2019 attack.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>9<br>1|.<br>0<br>0<br>2|<br>Gather<br>Victim Org<br>Information:<br>Business<br>Relationships|In preparation for its attack against the 2018<br>Winter Olympics, Sandworm Team conducted<br>online research of partner organizations listed<br>on an official PyeongChang Olympics<br>partnership site.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>6<br>2|.<br>0<br>0<br>1|<br>Impair<br>Defenses:<br>Disable or<br>Modify<br>Tools|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team modified in-registry internet<br>settings to lower internet security.|
|||.<br>0<br>0<br>2|<br>Impair<br>Defenses:<br>Disable<br>Windows<br>Event<br>Logging|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team disabled event logging on<br>compromised systems.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>0<br>7<br>0|.<br>0<br>0<br>4|<br>Indicator<br>Removal:<br>File Deletion|Sandworm Team has used backdoors that can<br>delete files used in an attack from an infected<br>system.<br>During the 2015 Ukraine Electric Power Attack,<br>vba_macro.exe deletes itself after<br>FONTCACHE.DAT, rundll32.exe, and the<br>associated .lnk file is delivered.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>105||Ingress Tool<br>Transfer|Sandworm Team has pushed additional<br>malicious tools onto an infected system to steal<br>user credentials, move laterally, and destroy<br>data.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team pushed additional malicious<br>tools onto an infected system to steal user<br>credentials, move laterally, and destroy data.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>490||Inhibit<br>System<br>Recovery|Sandworm Team uses Prestige to delete the<br>backup catalog from the target system using:<br>C:\Windows\System32\wbadmin.exe delete<br>catalog -quiet and to delete volume shadow<br>copies using:<br>C:\Windows\System32\vssadmin.exe delete<br>shadows /all /quiet.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>0<br>5<br>6|.<br>0<br>0<br>1|<br>Input<br>Capture:<br>Keylogging|Sandworm Team has used a keylogger to<br>capture keystrokes by using the<br>SetWindowsHookEx function.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team gathered account credentials<br>via a BlackEnergy keylogger plugin.|
Public 274 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>570||Lateral Tool<br>Transfer|Sandworm Team has used move to transfer files<br>to a network share and has copied payloads--<br>such as Prestige ransomware--to an Active<br>Directory Domain Controller and distributed via<br>the Default Domain Group Policy Object.<br>Additionally, Sandworm Team has transferred<br>an ISO file into the OT network to gain initial<br>access.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team moved their tools laterally<br>within the corporate network and between the<br>ICS and corporate network.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used move to transfer files to a<br>network share.<br>During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team used a Group Policy Object<br>(GPO) to copy CaddyWiper's executable<br>msserver.exe from a staging server to a local<br>hard drive before deployment.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>036<br>.<br>0<br>0<br>4||Masqueradin<br>g|Sandworm Team masqueraded malicious<br>installers as Windows update packages to evade<br>defense and entice users to execute binaries.|
|||.<br>0<br>0<br>4|<br>Masquerade<br>Task or<br>Service|During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team leveraged Systemd service<br>units to masquerade GOGETTER malware as<br>legitimate or seemingly legitimate services.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|||.<br>0<br>0<br>5|<br>Match<br>Legitimate<br>Resource<br>Name or<br>Location|Sandworm Team has avoided detection by<br>naming a malicious binary explorer.exe.<br>During the 2016 Ukraine Electric Power Attack,<br>DLLs and EXEs with filenames associated with<br>common electric power sector protocols were<br>used to masquerade files.|
|||.<br>0<br>0<br>8|<br>Masquerade<br>File Type|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team masqueraded executables as<br>.txt files.|
|||.<br>0<br>1<br>0|<br>Masquerade<br>Account<br>Name|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team created two new accounts,<br>"admin" and "система" (System).|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>112||Modify<br>Registry|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team modified in-registry Internet<br>settings to lower internet security before<br>launching rundll32.exe, which in-turn launches<br>the malware and communicates with C2 servers<br>over the Internet. .|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>106||Native API|Sandworm Team uses Prestige to disable and<br>restore file system redirection by using the<br>following functions:<br>Wow64DisableWow64FsRedirection() and<br>Wow64RevertWow64FsRedirection().|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>040||Network<br>Sniffing|Sandworm Team has used intercepter-NG to<br>sniff passwords in network traffic.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team used BlackEnergy’s network<br>sniffer module to discover user credentials<br>being sent over the network between the local|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|||||LAN and the power grid’s industrial control<br>systems.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>095||Non-<br>Application<br>Layer<br>Protocol|During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team proxied C2 communications<br>within a TLS-based tunnel.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>571||Non-<br>Standard<br>Port|Sandworm Team has used port 6789 to accept<br>connections on the group's SSH server.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>027<br>.<br>0<br>0<br>2<br>.<br>0<br>1<br>0||Obfuscated<br>Files or<br>Information|Sandworm Team has used Base64 encoding<br>within malware variants.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used heavily obfuscated code<br>with Industroyer in its Windows Notepad<br>backdoor.|
|||.<br>0<br>0<br>2|<br>Software<br>Packing|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used UPX to pack a copy of<br>Mimikatz.|
|||.<br>0<br>1<br>0|<br>Command<br>Obfuscation|Sandworm Team has used ROT13 encoding,<br>AES encryption and compression with the zlib<br>library for their Python-based backdoor.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>8<br>8|.<br>0<br>0<br>2|<br>Obtain<br>Capabilities:<br>Tool|Sandworm Team has acquired open-source<br>tools for their operations, including Invoke-<br>PSImage, which was used to establish an<br>encrypted channel from a compromised host to<br>Sandworm Team's C2 server in preparation for<br>the 2018 Winter Olympics attack, as well as<br>Impacket and RemoteExec, which were used in<br>their 2022 Prestige operations. Additionally,<br>Sandworm Team has used Empire, Cobalt<br>Strike and PoshC2.|
|||.<br>0<br>0<br>6|<br>Obtain<br>Capabilities:<br>Vulnerabiliti<br>es|In 2017, Sandworm Team conducted technical<br>research related to vulnerabilities associated<br>with websites used by the Korean Sport and<br>Olympic Committee, a Korean power company,<br>and a Korean airport.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>0<br>0<br>3|.<br>0<br>0<br>1|<br>OS<br>Credential<br>Dumping:<br>LSASS<br>Memory|Sandworm Team has used its plainpwd tool, a<br>modified version of Mimikatz, and comsvcs.dll<br>to dump Windows credentials from system<br>memory.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used Mimikatz to capture and<br>use legitimate credentials.|
|||.<br>0<br>0<br>3|<br>OS<br>Credential<br>Dumping:<br>NTDS|Sandworm Team has used ntdsutil.exe to back<br>up the Active Directory database, likely for<br>credential access.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>6<br>6|.<br>0<br>0<br>1|<br>Phishing:<br>Spearphishin<br>g Attachment|Sandworm Team has delivered malicious<br>Microsoft Office and ZIP file attachments via<br>spearphishing emails.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team obtained their initial foothold|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|||||into many IT systems using Microsoft Office<br>attachments delivered through phishing emails.|
|||.<br>0<br>0<br>2|<br>Phishing:<br>Spearphishin<br>g Link|Sandworm Team has crafted phishing emails<br>containing malicious hyperlinks.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>9<br>8|.<br>0<br>0<br>3|<br>Phishing for<br>Information:<br>Spearphishin<br>g Link|Sandworm Team has crafted spearphishing<br>emails with hyperlinks designed to trick<br>unwitting recipients into revealing their account<br>credentials.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>055||Process<br>Injection|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team loaded BlackEnergy into<br>svchost.exe, which then launched iexplore.exe<br>for their C2.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>572||Protocol<br>Tunneling|During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team deployed the GOGETTER<br>tunneler software to establish a "Yamux" TLS-<br>based C2 channel with an external server(s).|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>090||Proxy|Sandworm Team's BCS-server tool can create<br>an internal proxy server to redirect traffic from<br>the adversary-controlled C2 to internal servers<br>which may not be connected to the internet, but<br>are interconnected locally.|
|**En**<br>**ter**|T1<br>219||Remote<br>Access Tools|Sandworm Team has used remote<br>administration tools or remote industrial control<br>system client software for execution and to<br>maliciously release electricity breakers.|
Public 274 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|**pr**<br>**ise**|||||
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>0<br>2<br>1|.<br>0<br>0<br>2|<br>Remote<br>Services:<br>SMB/Windo<br>ws Admin<br>Shares|Sandworm Team has copied payloads to the<br>ADMIN$ share of remote systems and run net<br>use to connect to network shares.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team utilized net use to connect to<br>network shares.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>018||Remote<br>System<br>Discovery|Sandworm Team has used a tool to query<br>Active Directory using LDAP, discovering<br>information about computers listed in AD.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team remotely discovered systems<br>over LAN connections. OT systems were<br>visible from the IT network as well, giving<br>adversaries the ability to discover operational<br>assets.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team checked for connectivity to<br>resources within the network and used LDAP to<br>query Active Directory, discovering information<br>about computers listed in AD.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>0<br>5<br>3|.<br>0<br>0<br>5|<br>Scheduled<br>Task/Job:<br>Scheduled<br>Task|Sandworm Team leveraged SHARPIVORY, a<br>.NET dropper that writes embedded payload to<br>disk and uses scheduled tasks to persist on<br>victim machines.<br>During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team leveraged Scheduled Tasks<br>through a Group Policy Object (GPO) to<br>execute CaddyWiper at a predetermined time.|
Public 274 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>593||Search Open<br>Websites/Do<br>mains|Sandworm Team researched Ukraine's unique<br>legal entity identifier (called an "EDRPOU"<br>number), including running queries on the<br>EDRPOU website, in preparation for the<br>NotPetya attack. Sandworm Team has also<br>researched third-party websites to help it craft<br>credible spearphishing emails.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>594||Search<br>Victim-<br>Owned<br>Websites|Sandworm Team has conducted research<br>against potential victim websites as part of its<br>operational planning.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>5<br>0<br>5|.<br>0<br>0<br>1|<br>Server<br>Software<br>Component:<br>SQL Stored<br>Procedures|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used various MS-SQL stored<br>procedures.|
|||.<br>0<br>0<br>3|<br>Server<br>Software<br>Component:<br>Web Shell|Sandworm Team has used webshells including<br>P.A.S. Webshell to maintain access to victim<br>networks.<br>During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team deployed the Neo-<br>REGEORG webshell on an internet-facing<br>server.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>489||Service Stop|Sandworm Team attempts to stop the MSSQL<br>Windows service to ensure successful<br>encryption of locked files.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>072||Software<br>Deployment<br>Tools|Sandworm Team has used the commercially<br>available tool RemoteExec for agentless remote<br>code execution.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>6<br>0<br>8|.<br>0<br>0<br>1|<br>Stage<br>Capabilities:<br>Upload<br>Malware|Sandworm Team staged compromised versions<br>of legitimate software installers in forums to<br>enable initial access to executing user.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>539||Steal Web<br>Session<br>Cookie|Sandworm Team used information stealer<br>malware to collect browser session cookies.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>195<br>.<br>0<br>0<br>2||Supply<br>Chain<br>Compromise|Sandworm Team staged compromised versions<br>of legitimate software installers on forums to<br>achieve initial, untargetetd access in victim<br>environments.|
|||.<br>0<br>0<br>2|<br>Compromise<br>Software<br>Supply<br>Chain|Sandworm Team has distributed NotPetya by<br>compromising the legitimate Ukrainian<br>accounting software M.E.Doc and replacing a<br>legitimate software update with a malicious one.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>2<br>1<br>8|.<br>0<br>1<br>1|<br>System<br>Binary Proxy<br>Execution:<br>Rundll32|Sandworm Team used a backdoor which could<br>execute a supplied DLL using rundll32.exe.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team used a backdoor which could<br>execute a supplied DLL using rundll32.exe.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>082||System<br>Information<br>Discovery|Sandworm Team used a backdoor to enumerate<br>information about the infected system's<br>operating system.|
|**En**<br>**ter**|T1<br>049||System<br>Network|Sandworm Team had gathered user, IP address,<br>and server data related to RDP sessions on a<br>compromised host. It has also accessed network|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|**pr**<br>**ise**|||Connections<br>Discovery|diagram files useful for understanding how a<br>host's network was configured.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>033||System<br>Owner/User<br>Discovery|Sandworm Team has collected the username<br>from a compromised host.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>199||Trusted<br>Relationship|Sandworm Team has used dedicated network<br>connections from one victim organization to<br>gain unauthorized access to a separate<br>organization. Additionally, Sandworm Team<br>has accessed Internet service providers and<br>telecommunication entities that provide mobile<br>connectivity.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>2<br>0<br>4|.<br>0<br>0<br>1|<br>User<br>Execution:<br>Malicious<br>Link|Sandworm Team has tricked unwitting<br>recipients into clicking on malicious hyperlinks<br>within emails crafted to resemble trustworthy<br>senders.|
|||.<br>0<br>0<br>2|<br>User<br>Execution:<br>Malicious<br>File|Sandworm Team has tricked unwitting<br>recipients into clicking on spearphishing<br>attachments and enabling malicious macros<br>embedded within files.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team leveraged Microsoft Office<br>attachments which contained malicious macros<br>that were automatically executed once the user<br>permitted them.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>078<br>.<br>0<br>0<br>2||Valid<br>Accounts|Sandworm Team have used previously acquired<br>legitimate credentials prior to attacks.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team used valid accounts on the<br>corporate network to escalate privileges, move<br>laterally, and establish persistence within the<br>corporate network.|
|||.<br>0<br>0<br>2|<br>Domain<br>Accounts|Sandworm Team has used stolen credentials to<br>access administrative accounts within the<br>domain.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T<br>1<br>1<br>0<br>2|.<br>0<br>0<br>2|<br>Web Service:<br>Bidirectional<br>Communicati<br>on|Sandworm Team has used the Telegram Bot<br>API from Telegram Messenger to send and<br>receive commands to its Python backdoor.<br>Sandworm Team also used legitimate M.E.Doc<br>software update check requests for sending and<br>receiving commands and hosted malicious<br>payloads on putdrive.com.|
|**En**<br>**ter**<br>**pr**<br>**ise**|T1<br>047||Windows<br>Management<br>Instrumentati<br>on|Sandworm Team has used Impacket’s<br>WMIexec module for remote code execution<br>and VBScript to run WMI queries.<br>During the 2016 Ukraine Electric Power Attack,<br>WMI in scripts were used for remote execution<br>and system surveys.|
|**M**<br>**ob**<br>**ile**|T1<br>660||Phishing|Sandworm Team used SMS-based phishing to<br>target victims with malicious links.|
|**M**<br>**ob**<br>**ile**|T1<br>409||Stored<br>Application<br>Data|Sandworm Team can collect encrypted<br>Telegram and Signal communications.|
Public 274 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|
|**IC**<br>**S**|T0<br>895|Autorun<br>Image|During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team used existing hypervisor<br>access to map an ISO image named a.iso to a<br>virtual machine running a SCADA server. The<br>SCADA server’s operating system was<br>configured to autorun CD-ROM images, and as<br>a result, a malicious VBS script on the ISO<br>image was automatically executed.|
|**IC**<br>**S**|T0<br>803|Block<br>Command<br>Message|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team blocked command messages<br>by using malicious firmware to render serial-to-<br>ethernet converters inoperable.|
|**IC**<br>**S**|T0<br>804|Block<br>Reporting<br>Message|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team blocked reporting messages<br>by using malicious firmware to render serial-to-<br>ethernet converters inoperable.|
|**IC**<br>**S**|T0<br>805|Block Serial<br>COM|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team overwrote the serial-to-<br>ethernet converter firmware, rendering the<br>devices not operational. This meant that<br>communication to the downstream serial<br>devices was either not possible or more<br>difficult.|
|**IC**<br>**S**|T0<br>807|Command-<br>Line<br>Interface|Sandworm Team uses the MS-SQL server<br>xp_cmdshell command, and PowerShell to<br>execute commands.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team supplied the name of the<br>payload DLL to Industroyer via a command line<br>parameter.<br>During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team leveraged the SCIL-API on|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|
||||the MicroSCADA platform to execute<br>commands through the scilc.exe binary.|
|**IC**<br>**S**|T0<br>885|Commonly<br>Used Port|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team used port 443 to communicate<br>with their C2 servers.|
|**IC**<br>**S**|T0<br>884|Connection<br>Proxy|Sandworm Team establishes an internal proxy<br>prior to the installation of backdoors within the<br>network.<br>During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team established an internal proxy<br>prior to the installation of backdoors within the<br>network.|
|**IC**<br>**S**|T0<br>813|Denial of<br>Control|During the 2015 Ukraine Electric Power Attack,<br>KillDisk rendered devices that were necessary<br>for remote recovery unusable, including at least<br>one RTU. Additionally, Sandworm Team<br>overwrote the firmware for serial-to-ethernet<br>converters, denying operators control of the<br>downstream devices.|
|**IC**<br>**S**|T0<br>814|Denial of<br>Service|During the 2015 Ukraine Electric Power Attack,<br>power company phone line operators were hit<br>with a denial of service attack so that they<br>couldn’t field customers’ calls about outages.<br>Operators were also denied service to their<br>downstream devices when their serial-to-<br>ethernet converters had their firmware<br>overwritten, which bricked the devices.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|
|**IC**<br>**S**|T0<br>816|Device<br>Restart/Shutd<br>own|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team scheduled the uninterruptable<br>power supplies (UPS) to shutdown data and<br>telephone servers via the UPS management<br>interface.|
|**IC**<br>**S**|T0<br>819|Exploit<br>Public-<br>Facing<br>Application|Sandworm Team actors exploited vulnerabilities<br>in GE's Cimplicity HMI and<br>Advantech/Broadwin WebAccess HMI software<br>which had been directly exposed to the internet.|
|**IC**<br>**S**|T0<br>822|External<br>Remote<br>Services|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team used Valid Accounts taken<br>from the Windows Domain Controller to access<br>the control system Virtual Private Network<br>(VPN) used by grid operators.|
|**IC**<br>**S**|T0<br>823|Graphical<br>User<br>Interface|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team utilized HMI GUIs in the<br>SCADA environment to open breakers.|
|**IC**<br>**S**|T0<br>867|Lateral Tool<br>Transfer|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team moved their tools laterally<br>within the ICS network.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used a VBS script to facilitate<br>lateral tool transfer. The VBS script was used to<br>copy ICS-specific payloads with the following<br>command: cscript C:\Backinfo\ufn.vbs<br>C:\Backinfo\101.dll C:\Delta\101.dll|
|**IC**<br>**S**|T0<br>826|Loss of<br>Availability|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team opened the breakers at the<br>infected sites, shutting the power off for<br>thousands of businesses and households for<br>around 6 hours.|
Public 274 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|
|**IC**<br>**S**|T0<br>827|Loss of<br>Control|During the 2015 Ukraine Electric Power Attack,<br>operators were shut out of their equipment<br>either through the denial of peripheral use or the<br>degradation of equipment. Operators were<br>therefore unable to recover from the incident<br>through their traditional means. Much of the<br>power was restored manually.|
|**IC**<br>**S**|T0<br>828|Loss of<br>Productivity<br>and Revenue|During the 2015 Ukraine Electric Power Attack,<br>power breakers were opened which caused the<br>operating companies to be unable to deliver<br>power, and left thousands of businesses and<br>households without power for around 6 hours.|
|**IC**<br>**S**|T0<br>831|Manipulation<br>of Control|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team opened live breakers via<br>remote commands to the HMI, causing<br>blackouts.|
|**IC**<br>**S**|T0<br>849|Masqueradin<br>g|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team transferred executable files as<br>.txt and then renamed them to .exe, likely to<br>avoid detection through extension tracking.|
|**IC**<br>**S**|T0<br>886|Remote<br>Services|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team used an IT helpdesk software<br>to move the mouse on ICS control devices to<br>maliciously release electricity breakers.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used MS-SQL access to a<br>pivot machine, allowing code execution<br>throughout the ICS network.|
|**IC**<br>**S**|T0<br>846|Remote<br>System<br>Discovery|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team remotely discovered<br>operational assets once on the OT network.|
Public 274 

**VIETTEL AI RACE BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM SANDWORM TEAM** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|
|**IC**<br>**S**|T0<br>853|Scripting|During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team utilized VBS and batch scripts<br>for file movement and as wrappers for<br>PowerShell execution.<br>During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team utilizes a Visual Basic script<br>lun.vbs to execute n.bat which then executed the<br>MicroSCADA scilc.exe command.|
|**IC**<br>**S**|T0<br>894|System<br>Binary Proxy<br>Execution|During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team executed a MicroSCADA<br>application binary scilc.exe to send a predefined<br>list of SCADA instructions specified in a file<br>defined by the adversary, s1.txt. The executed<br>command C:\sc\prog\exec\scilc.exe -do<br>pack\scil\s1.txt leverages the SCADA software<br>to send unauthorized command messages to<br>remote substations.|
|**IC**<br>**S**|T0<br>857|System<br>Firmware|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team overwrote the serial-to-<br>ethernet gateways with custom firmware to<br>make systems either disabled, shutdown, and/or<br>unrecoverable.|
|**IC**<br>**S**|T0<br>855|Unauthorized<br>Command<br>Message|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team issued unauthorized<br>commands to substation breaks after gaining<br>control of operator workstations and accessing a<br>distribution management system (DMS)<br>application.<br>During the 2022 Ukraine Electric Power Attack,<br>Sandworm Team used the MicroSCADA SCIL-<br>API to specify a set of SCADA instructions,<br>including the sending of unauthorized<br>commands to substation devices.|
**VIETTEL AI RACE** Public 274 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM** Lần ban hành: 1 **SANDWORM TEAM** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|
|**IC**<br>**S**|T0<br>859|Valid<br>Accounts|During the 2015 Ukraine Electric Power Attack,<br>Sandworm Team used valid accounts to<br>laterally move through VPN connections and<br>dual-homed systems. Sandworm Team used the<br>credentials of valid accounts to interact with<br>client applications and access employee<br>workstations hosting HMI applications.<br>During the 2016 Ukraine Electric Power Attack,<br>Sandworm Team used valid accounts to<br>laterally move through VPN connections and<br>dual-homed systems.|