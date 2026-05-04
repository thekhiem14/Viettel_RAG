**VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN** Lần ban hành: 1 **CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**==> picture [39 x 47] intentionally omitted <==**

## **1. MỤC TIÊU CHUNG** 

Tiến hành nghiên cứu toàn diện về nhóm Lazarus Group, tập trung vào chiến thuật, kỹ thuật và thủ tục của họ. Sử dụng khung MITRE ATT&CK để vạch ra các hoạt động của nhóm và cung cấp những hiểu biết có thể hành động. [1] 

Phát hiện của bản báo cáo này đóng một vai trò quan trọng trong việc củng cố khả năng phòng thủ chống lại kẻ thù này. 

## **2. Lazarus Group** 

**Lazarus Group** là một trong những nhóm tin tặc nguy hiểm và nổi tiếng nhất hiện nay. Nhóm này được cho là có liên hệ chặt chẽ với chính phủ Bắc Triều Tiên, hoạt động ít nhất từ năm 2009 đến nay. Lazarus thường xuyên tiến hành các cuộc tấn công mạng quy mô lớn nhằm vào nhiều mục tiêu khác nhau, bao gồm cả lĩnh vực chính trị, quân sự và tài chính.[1] 

## **2.1 Nguồn gốc và tổ chức** 

Theo các báo cáo tình báo và phân tích an ninh mạng, Lazarus Group được điều hành bởi **Reconnaissance General Bureau (RGB)** – cơ quan tình báo quân sự của Triều Tiên. Bên trong Lazarus tồn tại nhiều nhánh phụ chuyên trách: [1] 

- **BlueNorOff / APT38** : Tập trung vào các cuộc tấn công tài chính, nhắm vào hệ thống ngân hàng và tiền mã hóa.[1] 

- **AndAriel** : Thực hiện các chiến dịch gián điệp mạng và tấn công vào hạ tầng quan trọng, đặc biệt tại Hàn Quốc.[1] 

- **Hidden Cobra, Guardians of Peace, ZINC, v.v.,** được dùng để che giấu dấu vết và tạo sự nhầm lẫn cho cơ quan điều tra .[1] 

## **2.2 Các vụ tấn công nổi bật** 

Một số sự kiện tiêu biểu do **Lazarus Group** thực hiện: 

- **2014 – Sony Pictures** : Tấn công, đánh cắp dữ liệu và làm rò rỉ thông tin mật, được cho là trả đũa bộ phim The Interview. [2] 

- **2016 – Ngân hàng Trung ương Bangladesh** : Lazarus đánh cắp 81 triệu USD qua hệ thống SWIFT. [3] 

- **2017 – WannaCry Ransomware** : Mã độc tống tiền toàn cầu, gây ảnh hưởng đến hơn 150 quốc gia. 

- **2022 – Ronin Network / Axie Infinity** : Đánh cắp hơn 620 triệu USD tiền mã hóa. 

- **2023 – Stake[.]com và Atomic Wallet** : Tổng cộng Lazarus đã lấy hơn 300 triệu USD từ các nền tảng crypto [4] 
**VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN** Lần ban hành: 1 **CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**==> picture [39 x 47] intentionally omitted <==**

Điểm đáng chú ý là Lazarus không chỉ triển khai Dream Job như một chiến dịch đơn lẻ. Nó còn liên kết với các hoạt động khác như **Operation North Star** và **Operation Interception** , thể hiện chiến lược lâu dài nhằm vào cá nhân trong lĩnh vực kỹ thuật và an ninh quốc phòng. [5] 

## **2.3 Operation Dream Job** 

Bài báo cáo này sẽ tập trung vào chiến dịch Operation Dream Job. 

**Operation Dream Job** là một trong những chiến dịch tấn công mạng phức tạp nhất do **Lazarus Group** tiến hành. Chiến dịch này lợi dụng các cơ hội nghề nghiệp giả mạo từ những công ty công nghệ và quốc phòng lớn để dụ dỗ nạn nhân tải về các tài liệu hoặc phần mềm chứa mã độc. Lần đầu tiên chiến dịch này được phát hiện là vào **tháng 9 năm 2019** theo dữ liệu từ MITRE ATT&CK. [5] 

**==> picture [26 x 10] intentionally omitted <==**

## **Phương thức tấn công** 

## _2.3.1.1. Kỹ thuật lợi dụng hệ thống hợp pháp_ 

Trong chiến dịch này, Lazarus đã khai thác các binary hợp pháp của Windows như **Regsvr32** và **Rundll32** để thực hiện proxy execution. Đây là kỹ thuật "Living off the Land" (LOLBin) thường thấy, giúp kẻ tấn công ngụy trang hoạt động của mình dưới lớp vỏ hợp pháp, khó bị phát hiện bởi các hệ thống phòng thủ truyền thống. [5] 

## _2.3.1.2. Kỹ thuật di chuyển ngang_ 

Sau khi xâm nhập ban đầu, Lazarus sử dụng kỹ thuật **Internal Spearphishing** để mở rộng phạm vi kiểm soát trong cùng một tổ chức. Kỹ thuật này được MITRE định danh là **T1534** . Điều này cho phép kẻ tấn công mở rộng quyền truy cập mà không cần phải khai thác thêm nhiều lỗ hổng. [5] 

## _2.3.1.3. Phần mềm độc hại_ 

Một RAT (Remote Access Trojan) quan trọng trong chiến dịch này là **DRATzarus** . Đây là công cụ giúp Lazarus duy trì truy cập từ xa, thực hiện các lệnh và đánh cắp dữ liệu. **DRATzarus** sử dụng **Native API** để thực thi trực tiếp trên hệ thống, đồng thời áp dụng kỹ thuật **Time-Based Evasion** nhằm tránh bị sandbox phân tích trong môi trường ảo. [6] [7] 
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL CYBER SECURITY**|Public 266|
|---|---|---|
||**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN**<br>**CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM**<br>**LAZARUS GROUP**|Lần ban hành: 1|

**==> picture [27 x 10] intentionally omitted <==**

## **Operation Dream Job Techniques Used [5]** 

|---|---|---|---|---|
|**Domain**|**ID**||**Name**|**Use**|
|**Enterprise**|T<br>10<br>87|.0<br>02|Account<br>Discovery:<br>Domain Account|During Operation Dream Job,<br>Lazarus Group queried<br>compromised victim's active<br>directory servers to obtain the list<br>of employees including<br>administrator accounts.|
|**Enterprise**|T<br>15<br>83|.0<br>01|Acquire<br>Infrastructure:<br>Domains|During Operation Dream Job,<br>Lazarus Group registered a domain<br>name identical to that of a<br>compromised company as part of<br>their BEC effort.|
|||.0<br>04|Acquire<br>Infrastructure:<br>Server|During Operation Dream Job,<br>Lazarus Group acquired servers to<br>host their malicious tools.|
|||.0<br>06|Acquire<br>Infrastructure:<br>Web Services|During Operation Dream Job,<br>Lazarus Group used file hosting<br>services like DropBox and<br>OneDrive.|
|**Enterprise**|T<br>10<br>71|.0<br>01|Application Layer<br>Protocol: Web<br>Protocols|During Operation Dream Job,<br>Lazarus Group uses HTTP and<br>HTTPS to contact actor-controlled<br>C2 servers.|
|**Enterprise**|T<br>15<br>60|.0<br>01|Archive Collected<br>Data: Archive via<br>Utility|During Operation Dream Job,<br>Lazarus Group uses HTTP and<br>HTTPS to contact actor-controlled<br>C2 servers.|
|**Enterprise**|T<br>15<br>47|.0<br>01|Boot or Logon<br>Autostart<br>Execution:<br>Registry Run<br>Keys / Startup<br>Folder|During Operation Dream Job,<br>Lazarus Group archived victim's<br>data into a RAR file.|
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL CYBER SECURITY**|Public 266|
|---|---|---|
||**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN**<br>**CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM**<br>**LAZARUS GROUP**|Lần ban hành: 1|

|---|---|---|---|---|
|**Enterprise**|T1110||Brute Force|During Operation Dream Job,<br>Lazarus Group placed LNK files<br>into the victims' startup folder for<br>persistence.|
|**Enterprise**|T<br>10<br>59|.0<br>01|Command and<br>Scripting<br>Interpreter:<br>PowerShell|During Operation Dream Job,<br>Lazarus Group used PowerShell<br>commands to explore the<br>environment of compromised<br>victims.|
|||.0<br>03|Command and<br>Scripting<br>Interpreter:<br>Windows<br>Command Shell|During Operation Dream Job,<br>Lazarus Group launched malicious<br>DLL files, created new folders,<br>and renamed folders with the use<br>of the Windows command shell.|
|||.0<br>05|Command and<br>Scripting<br>Interpreter:<br>Visual Basic|During Operation Dream Job,<br>Lazarus Group executed a VBA<br>written malicious macro after<br>victims download malicious<br>DOTM files; Lazarus Group also<br>used Visual Basic macro code to<br>extract a double Base64 encoded<br>DLL implant.|
|**Enterprise**|T<br>15<br>84|.0<br>01|Compromise<br>Infrastructure:<br>Domains|For Operation Dream Job, Lazarus<br>Group compromised domains in<br>Italy and other countries for their<br>C2 infrastructure.|
|||.0<br>04|Compromise<br>Infrastructure:<br>Server|For Operation Dream Job, Lazarus<br>Group compromised servers to<br>host their malicious tools|
|**Enterprise**|T1005||Data from Local<br>System|During Operation Dream Job,<br>Lazarus Group used malicious<br>Trojans and DLL files to exfiltrate<br>data from an infected host.|
|**Enterprise**|T1622||Debugger<br>Evasion|During Operation Dream Job,<br>Lazarus Group used tools that used<br>the IsDebuggerPresent call to<br>detect debuggers.|
**VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN** Lần ban hành: 1 **CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**Enterprise**|T<br>15<br>87|.0<br>01|Develop<br>Capabilities:<br>Malware|For Operation Dream Job, Lazarus<br>Group developed custom tools<br>such as Sumarta, DBLL Dropper,<br>Torisma, and DRATzarus for their<br>operations.|
|||.0<br>02|Develop<br>Capabilities:<br>Code Signing<br>Certificates|During Operation Dream Job,<br>Lazarus Group digitally signed<br>their malware and the dbxcli<br>utility.|
|**Enterprise**|T<br>15<br>73|.0<br>01|Encrypted<br>Channel:<br>Symmetric<br>Cryptography|During Operation Dream Job,<br>Lazarus Group used an AES key to<br>communicate with their C2 server.|
|**Enterprise**|T<br>15<br>85|.0<br>01|Establish<br>Accounts: Social<br>Media Accounts|For Operation Dream Job, Lazarus<br>Group created fake LinkedIn<br>accounts for their targeting efforts.|
|||.0<br>02|Establish<br>Accounts: Email<br>Accounts|During Operation Dream Job,<br>Lazarus Group created fake email<br>accounts to correspond with fake<br>LinkedIn personas; Lazarus Group<br>also established email accounts to<br>match those of the victim as part<br>of their BEC attempt.|
|**Enterprise**|T1041||Exfiltration Over<br>C2 Channel|During Operation Dream Job,<br>Lazarus Group exfiltrated data<br>from a compromised host to actor-<br>controlled C2 servers.|
|**Enterprise**|T<br>15<br>67|.0<br>02|Exfiltration Over<br>Web Service:<br>Exfiltration to<br>Cloud Storage|During Operation Dream Job,<br>Lazarus Group used a custom<br>build of open-source command-<br>line dbxcli to exfiltrate stolen data<br>to Dropbox.|
|**Enterprise**|T1083||File and<br>Directory<br>Discovery|During Operation Dream Job,<br>Lazarus Group conducted word<br>searches within documents on a<br>compromised host in search of<br>security and financial matters.|
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL CYBER SECURITY**|Public 266|
|---|---|---|
||**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN**<br>**CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM**<br>**LAZARUS GROUP**|Lần ban hành: 1|

|---|---|---|---|---|
|**Enterprise**|T1589||Gather Victim<br>Identity<br>Information|For Operation Dream Job, Lazarus<br>Group conducted extensive<br>reconnaissance research on<br>potential targets.|
|**Enterprise**|T<br>15<br>91||Gather Victim<br>Org Information|For Operation Dream Job, Lazarus<br>Group gathered victim<br>organization information to<br>identify specific targets.|
|||.0<br>04|Identify Roles|During Operation Dream Job,<br>Lazarus Group targeted specific<br>individuals within an organization<br>with tailored job vacancy<br>announcements.|
|**Enterprise**|T1656||Impersonation|During Operation Dream Job,<br>Lazarus Group impersonated HR<br>hiring personnel through LinkedIn<br>messages and conducted<br>interviews with victims in order to<br>deceive them into downloading<br>malware.|
|**Enterprise**|T<br>10<br>70|.0<br>04|Indicator<br>Removal: File<br>Deletion|During Operation Dream Job,<br>Lazarus Group removed all<br>previously delivered files from a<br>compromised computer.|
|**Enterprise**|T1105||Ingress Tool<br>Transfer|During Operation Dream Job,<br>Lazarus Group downloaded<br>multistage malware and tools onto<br>a compromised host.|
|**Enterprise**|T1534||Internal<br>Spearphishing|During Operation Dream Job,<br>Lazarus Group conducted internal<br>spearphishing from within a<br>compromised organization.|
|**Enterprise**|T<br>10<br>36|.0<br>08|Masquerading:<br>Masquerade File<br>Type|During Operation Dream Job,<br>Lazarus Group disguised<br>malicious template files as JPEG<br>files to avoid detection.|
|**Enterprise**|T1106||Native API|During Operation Dream Job,|
**VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN** Lần ban hành: 1 **CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|||||Lazarus Group used Windows API<br>ObtainUserAgentString to obtain<br>the victim's User-Agent and used<br>the value to connect to their C2<br>server.|
|**Enterprise**|T<br>10<br>27|.0<br>02|Obfuscated Files<br>or Information:<br>Software Packing|During Operation Dream Job,<br>Lazarus Group packed malicious<br>.db files with Themida to evade<br>detection.|
|||.0<br>13|Obfuscated Files<br>or Information:<br>Encrypted/Encod<br>ed File|During Operation Dream Job,<br>Lazarus Group encrypted malware<br>such as DRATzarus with XOR and<br>DLL files with base64.|
|**Enterprise**|T<br>15<br>88|.0<br>02|Obtain<br>Capabilities: Tool|For Operation Dream Job, Lazarus<br>Group obtained tools such as<br>Wake-On-Lan, Responder,<br>ChromePass, and dbxcli.|
|||.0<br>03|Obtain<br>Capabilities:<br>Code Signing<br>Certificates|During Operation Dream Job,<br>Lazarus Group used code signing<br>certificates issued by Sectigo RSA<br>for some of its malware and tools.|
|**Enterprise**|T<br>15<br>66|.0<br>01|Phishing:<br>Spearphishing<br>Attachment|During Operation Dream Job,<br>Lazarus Group sent emails with<br>malicious attachments to gain<br>unauthorized access to targets'<br>computers.|
|||.0<br>02|Phishing:<br>Spearphishing<br>Link|During Operation Dream Job,<br>Lazarus Group sent malicious<br>OneDrive links with fictitious job<br>offer advertisements via email.|
|||.0<br>03|Phishing:<br>Spearphishing via<br>Service|During Operation Dream Job,<br>Lazarus Group sent victims<br>spearphishing messages via<br>LinkedIn concerning fictitious<br>jobs.|
|**Enterprise**|T<br>10|.0<br>05|Scheduled<br>Task/Job:|During Operation Dream Job,<br>Lazarus Group created scheduled|
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL CYBER SECURITY**|Public 266|
|---|---|---|
||**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN**<br>**CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM**<br>**LAZARUS GROUP**|Lần ban hành: 1|

|---|---|---|---|---|
||53||Scheduled Task|tasks to set a periodic execution of<br>a remote XSL script.|
|**Enterprise**|T<br>15<br>93|.0<br>01|Search Open<br>Websites/Domain<br>s: Social Media|For Operation Dream Job, Lazarus<br>Group used LinkedIn to identify<br>and target employees within a<br>chosen organization.|
|**Enterprise**|T<br>15<br>05|.0<br>04|Server Software<br>Component: IIS<br>Components|During Operation Dream Job,<br>Lazarus Group targeted Windows<br>servers running Internet<br>Information Systems (IIS) to<br>install C2 components.|
|**Enterprise**|T<br>16<br>08|.0<br>01|Stage<br>Capabilities:<br>Upload Malware|For Operation Dream Job, Lazarus<br>Group used compromised servers<br>to host malware.|
|||.0<br>02|Stage<br>Capabilities:<br>Upload Tool|For Operation Dream Job, Lazarus<br>Group used multiple servers to<br>host malicious tools.|
|**Enterprise**|T<br>15<br>53|.0<br>02|Subvert Trust<br>Controls: Code<br>Signing|During Operation Dream Job,<br>Lazarus Group digitally signed<br>their own malware to evade<br>detection.|
|**Enterprise**|T<br>12<br>18|.0<br>10|System Binary<br>Proxy Execution:<br>Regsvr32|During Operation Dream Job,<br>Lazarus Group used regsvr32 to<br>execute malware.|
|||.0<br>11|System Binary<br>Proxy Execution:<br>Rundll32|During Operation Dream Job,<br>Lazarus Group executed malware<br>with<br>C:\\windows\system32\rundll32.ex<br>e<br>"C:\ProgramData\ThumbNail\thu<br>mbnail.db", CtrlPanel S-6-81-<br>3811-75432205-060098-6872 0 0<br>905.|
|**Enterprise**|T<br>16<br>14|.0<br>01|System Location<br>Discovery:<br>System Language<br>Discovery|During Operation Dream Job,<br>Lazarus Group deployed malware<br>designed not to run on computers<br>set to Korean, Japanese, or|
**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN** Lần ban hành: 1 **CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

|---|---|---|---|---|
|||||Chinese in Windows language<br>preferences.|
|**Enterprise**|T1221||Template<br>Injection|During Operation Dream Job,<br>Lazarus Group used DOCX files<br>to retrieve a malicious document<br>template/DOTM file.|
|**Enterprise**|T<br>12<br>04||User Execution:<br>Malicious Link|During Operation Dream Job,<br>Lazarus Group lured users into<br>executing a malicious link to<br>disclose private account<br>information or provide initial<br>access.|
||||User Execution:<br>Malicious File|During Operation Dream Job,<br>Lazarus Group lured victims into<br>executing malicious documents<br>that contained "dream job"<br>descriptions from defense,<br>aerospace, and other sectors.|
|**Enterprise**|T<br>14<br>97|.0<br>01|Virtualization/Sa<br>ndbox Evasion:<br>System Checks|During Operation Dream Job,<br>Lazarus Group used tools that<br>conducted a variety of system<br>checks to detect sandboxes or<br>VMware services.|
||||Virtualization/Sa<br>ndbox Evasion:<br>Time Based<br>Evasion|During Operation Dream Job,<br>Lazarus Group used tools that<br>collected GetTickCount and<br>GetSystemTimeAsFileTime data<br>to detect sandbox or VMware<br>services.|
|||.0<br>03|||
|**Enterprise**|T1047||Windows<br>Management<br>Instrumentation|During Operation Dream Job,<br>Lazarus Group used WMIC to<br>executed a remote XSL script.|
**VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN** Lần ban hành: 1 **CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**==> picture [39 x 47] intentionally omitted <==**

|**Enterprise**||||
|---|---|---|---|
||T1220|XSL Script<br>Processing|During Operation Dream Job,<br>Lazarus Group used a remote XSL<br>script to download a Base64-<br>encoded DLL custom downloader.|

## **3. Lazarus Group Techniques Used [1]** 

|---|---|---|---|---|
|**Domain**|**ID**||**Name**|**Use**|
|**Enterprise**|T11<br>34|.002|Access Token<br>Manipulation:<br>Create Process<br>with Token|Lazarus Group keylogger KiloAlfa<br>obtains user tokens from<br>interactive sessions to execute<br>itself with API call<br>CreateProcessAsUserA under that<br>user's context.|
|**Enterprise**|T10<br>87|.002|Account<br>Discovery:<br>Domain<br>Account|During Operation Dream Job,<br>Lazarus Group queried<br>compromised victim's active<br>directory servers to obtain the list<br>of employees including<br>administrator accounts.|
|**Enterprise**|T1098||Account<br>Manipulation|Lazarus Group malware<br>WhiskeyDelta-Two contains a<br>function that attempts to rename<br>the administrator’s account.|
|**Enterprise**|T15<br>83|.001|Acquire<br>Infrastructure:<br>Domains|Lazarus Group has acquired<br>domains related to their campaigns<br>to act as distribution points and C2<br>channels.<br>During Operation Dream Job,<br>Lazarus Group registered a<br>domain name identical to that of a<br>compromised company as part of<br>their BEC effort.|
|||.004|Acquire<br>Infrastructure:<br>Server|During Operation Dream Job,<br>Lazarus Group acquired servers to<br>host their malicious tools.|
**VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|---|---|---|---|---|
|||.006|Acquire<br>Infrastructure:<br>Web Services|Lazarus Group has hosted<br>malicious downloads on Github.<br>During Operation Dream Job,<br>Lazarus Group used file hosting<br>services like DropBox and<br>OneDrive.|
|**Enterprise**|T15<br>57|.001|Adversary-in-<br>the-Middle:<br>LLMNR/NBT<br>-NS Poisoning<br>and SMB<br>Relay|Lazarus Group executed<br>Responder using the command<br>[Responder file path] -i [IP<br>address] -rPv on a compromised<br>host to harvest credentials and<br>move laterally.|
|**Enterprise**|T10<br>71|.001|Application<br>Layer<br>Protocol: Web<br>Protocols|Lazarus Group has conducted C2<br>over HTTP and HTTPS.<br>During Operation Dream Job,<br>Lazarus Group uses HTTP and<br>HTTPS to contact actor-controlled<br>C2 servers.|
|**Enterprise**|T1010||Application<br>Window<br>Discovery|Lazarus Group malware IndiaIndia<br>obtains and sends to its C2 server<br>the title of the window for each<br>running process. The KilaAlfa<br>keylogger also reports the title of<br>the window in the foreground.|
|**Enterprise**|T15<br>60||Archive<br>Collected<br>Data|Lazarus Group has compressed<br>exfiltrated data with RAR and<br>used RomeoDelta malware to<br>archive specified directories in .zip<br>format, encrypt the .zip file, and<br>upload it to C2.|
|||.001|Archive via<br>Utility|During Operation Dream Job,<br>Lazarus Group archived victim's<br>data into a RAR file.|
|||.002|Archive via<br>Library|Lazarus Group malware IndiaIndia<br>saves information gathered about<br>the victim to a file that is<br>compressed with Zlib, encrypted,|
**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL CYBER SECURITY**|Public 266|
|---|---|---|
||**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN**<br>**CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM**<br>**LAZARUS GROUP**|Lần ban hành: 1|

|---|---|---|---|---|
|||||and uploaded to a C2 server.|
|||.003|Archive via<br>Custom<br>Method|A Lazarus Group malware sample<br>encrypts data using a simple byte<br>based XOR operation prior to<br>exfiltration.|
|**Enterprise**|T15<br>47|.001|Boot or Logon<br>Autostart<br>Execution:<br>Registry Run<br>Keys / Startup<br>Folder|Lazarus Group has maintained<br>persistence by loading malicious<br>code into a startup folder or by<br>adding a Registry Run.<br>During Operation Dream Job,<br>Lazarus Group placed LNK files<br>into the victims' startup folder for<br>persistence.|
|||.009|Boot or Logon<br>Autostart<br>Execution:<br>Shortcut<br>Modification|Lazarus Group malware has<br>maintained persistence on a<br>system by creating a LNK shortcut<br>in the user’s Startup folder.|
|**Enterprise**|T11<br>10|.003|Brute Force:<br>Password<br>Spraying|Lazarus Group malware attempts<br>to connect to Windows shares for<br>lateral movement by using a<br>generated list of usernames, which<br>center around permutations of the<br>username Administrator, and weak<br>passwords.|
|**Enterprise**|T10<br>59|.001|Command and<br>Scripting<br>Interpreter:<br>PowerShell|Lazarus Group has used<br>PowerShell to execute commands<br>and malicious code.<br>During Operation Dream Job,<br>Lazarus Group used PowerShell<br>commands to explore the<br>environment of compromised<br>victims.|
|||.003|Command and<br>Scripting<br>Interpreter:|Lazarus Group malware uses<br>cmd.exe to execute commands on<br>a compromised host. A Destover-|
**VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN** Lần ban hành: 1 **CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
||||Windows<br>Command<br>Shell|like variant used by Lazarus<br>Group uses a batch file mechanism<br>to delete its binaries from the<br>system.<br>During Operation Dream Job,<br>Lazarus Group launched malicious<br>DLL files, created new folders,<br>and renamed folders with the use<br>of the Windows command shell.|
|||.005|Command and<br>Scripting<br>Interpreter:<br>Visual Basic|Lazarus Group has used VBA and<br>embedded macros in Word<br>documents to execute malicious<br>code.<br>During Operation Dream Job,<br>Lazarus Group executed a VBA<br>written malicious macro after<br>victims download malicious<br>DOTM files; Lazarus Group also<br>used Visual Basic macro code to<br>extract a double Base64 encoded<br>DLL implant.|
|**Enterprise**|T15<br>84|.001|Compromise<br>Infrastructure:<br>Domains|For Operation Dream Job, Lazarus<br>Group compromised domains in<br>Italy and other countries for their<br>C2 infrastructure.|
|||.004|Compromise<br>Infrastructure:<br>Server|Lazarus Group has compromised<br>servers to stage malicious tools.<br>For Operation Dream Job, Lazarus<br>Group compromised servers to<br>host their malicious tools.|
|**Enterprise**|T15<br>43|.003|Create or<br>Modify<br>System<br>Process:<br>Windows<br>Service|Several Lazarus Group malware<br>families install themselves as new<br>services.|
**VIETTEL CYBER SECURITY** Public 266 **BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN** Lần ban hành: 1 **CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|---|---|
|**Enterprise**|T1485||Data<br>Destruction|Lazarus Group has used a custom<br>secure delete function to overwrite<br>file contents with data from heap<br>memory.|
|**Enterprise**|T11<br>32|.001|Data<br>Encoding:<br>Standard<br>Encoding|A Lazarus Group malware sample<br>encodes data with base64.|
|**Enterprise**|T1005||Data from<br>Local System|Lazarus Group has collected data<br>and files from compromised<br>networks.<br>During Operation Dream Job,<br>Lazarus Group used malicious<br>Trojans and DLL files to exfiltrate<br>data from an infected host.|
|**Enterprise**|T10<br>01|.003|Data<br>Obfuscation:<br>Protocol or<br>Service<br>Impersonation|Lazarus Group malware also uses<br>a unique form of communication<br>encryption known as FakeTLS that<br>mimics TLS but uses a different<br>encryption method, potentially<br>evading SSL traffic<br>inspection/decryption.|
|**Enterprise**|T10<br>74|.001|Data Staged:<br>Local Data<br>Staging|Lazarus Group malware IndiaIndia<br>saves information gathered about<br>the victim to a file that is saved in<br>the %TEMP% directory, then<br>compressed, encrypted, and<br>uploaded to a C2 server.|

## **4. References** 

**[1] Lazarus Group. https://attack.mitre.org/groups/G0032/** 

**[2] Cyber Security NCC Group Resource Hub articles, The Lazarus group: - North Korean scourge for +10 years. https://www.nccgroup.com/the lazarus-group-north-korean-scourge-for-plus10-years** 
**VIETTEL CYBER SECURITY** Public 266 Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

**BÁO CÁO ĐIỀU TRA CHIẾN DỊCH TẤN CÔNG MẠNG LIÊN QUAN ĐẾN NHÓM LAZARUS GROUP** 

**- [3] Lazarus Group, The APT with countless lives. https://eurepoc.eu/wp content/uploads/2024/02/Advanced-Persistent-Threat-Profile-Lazarus- February 2024.pdf** 

**[4] Inside Lazarus Group: Analyzing North Korea's Most Infamous Crypto Hacks. https://hacken.io/discover/lazarus-group/** 

**[5] Operation Dream Job. https://attack.mitre.org/campaigns/C0022/** 

**[6] Native API. https://attack.mitre.org/techniques/T1106/** 

**[7] Virtualization/Sandbox Evasion: Time Based Evasion. https://attack.mitre.org/techniques/T1497/003/**