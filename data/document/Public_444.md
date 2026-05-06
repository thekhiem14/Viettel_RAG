**VIETTEL AI RACE** 

**DANH MỤC CHỨC NĂNG BCCS2** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

|Tên ứng dụng|Chức năng|API/Action|Mô tả|Kết<br>quả<br>mong<br>muốn|Ghi chú|
|---|---|---|---|---|---|
|BCCS2-Core|Validate<br>IVRPrompt|/ivrprompt/validate|Validate dữ liệu<br>IVRPrompt trong<br>BCCS2-Core.|Thông<br>báo<br>qua<br>SMS|Có cơ<br>chế<br>rollback|
|Infra-Server|Config QoS|/qos/config|Config dữ liệu QoS<br>trong Infra-Server.|Hiển<br>thị báo<br>cáo|Có cơ<br>chế<br>rollback|
|RPA-Engine|Delete<br>CustomerProfile|/customerprofile/delete|Delete dữ liệu<br>CustomerProfile<br>trong RPA-Engine.|Cảnh<br>báo|Kết nối<br>với hệ<br>thống<br>Billing|
|QA-<br>Automation|Generate<br>AgentStatus|/agentstatus/generate|Generate dữ liệu<br>AgentStatus trong<br>QA-Automation.|Lỗi<br>nghiêm<br>trọng|Dữ liệu<br>backup<br>mỗi<br>ngày|
|Security-<br>Firewall|Config<br>ClusterNode|/clusternode/config|Config dữ liệu<br>ClusterNode trong<br>Security-Firewall.|Không<br>lỗi|Tích<br>hợp với<br>CRM|
|Security-<br>Firewall|Update Queue|/queue/update|Update dữ liệu<br>Queue trong<br>Security-Firewall.|Ghi log<br>đầy đủ|Theo<br>quy<br>định<br>Viettel|
|IPCC-<br>ContactCenter|Insert<br>AccountLock|/accountlock/insert|Insert dữ liệu<br>AccountLock trong|Không<br>lỗi|Chỉ<br>dùng|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||||||IPCC-<br>ContactCenter.|||cho<br>admin|
||IVR-System||Monitor<br>ClusterNode|/clusternode/monitor|Monitor dữ liệu<br>ClusterNode trong<br>IVR-System.||Thông<br>báo<br>qua<br>email|Chạy<br>theo<br>lịch<br>cron|
||Infra-Server||Import Contact|/contact/import|Import dữ liệu<br>Contact trong Infra-<br>Server.||Hiển<br>thị báo<br>cáo|Có cơ<br>chế<br>rollback|
||IPCC-<br>ContactCenter||Insert Blacklist|/blacklist/insert|Insert dữ liệu<br>Blacklist trong<br>IPCC-<br>ContactCenter.||Thông<br>báo<br>qua<br>SMS|Kết nối<br>với hệ<br>thống<br>Billing|
||Security-<br>Firewall||Import Blacklist|/blacklist/import|Import dữ liệu<br>Blacklist trong<br>Security-Firewall.||Tự<br>động<br>retry|Dữ liệu<br>backup<br>mỗi<br>ngày|
||QA-<br>Automation||Schedule<br>PackagePlan|/packageplan/schedule|Schedule dữ liệu<br>PackagePlan trong<br>QA-Automation.||Thông<br>báo<br>qua<br>SMS|Chạy<br>theo<br>lịch<br>cron|
||RPA-Engine||Analyze<br>Blacklist|/blacklist/analyze|Analyze dữ liệu<br>Blacklist trong RPA-<br>Engine.||Ghi log<br>đầy đủ|Tích<br>hợp với<br>CRM|
||Infra-Server||Analyze VPN|/vpn/analyze|Analyze dữ liệu<br>VPN trong Infra-<br>Server.||Không<br>lỗi|Có cơ<br>chế<br>rollback|
||Infra-Network||Analyze<br>FirewallPolicy|/firewallpolicy/analyze|Analyze dữ liệu<br>FirewallPolicy trong<br>Infra-Network.||Thông<br>báo|Chạy<br>theo|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||||||||qua<br>SMS|lịch<br>cron|
||BCCS2-Core||Import<br>Opportunity|/opportunity/import|Import dữ liệu<br>Opportunity trong<br>BCCS2-Core.||Tự<br>động<br>retry|Kết nối<br>với hệ<br>thống<br>Billing|
||IPCC-<br>ContactCenter||Analyze<br>AgentStatus|/agentstatus/analyze|Analyze dữ liệu<br>AgentStatus trong<br>IPCC-<br>ContactCenter.||Cảnh<br>báo|Theo<br>chuẩn<br>ISO<br>27001|
||CRM-<br>Platform||Insert<br>IVRPrompt|/ivrprompt/insert|Insert dữ liệu<br>IVRPrompt trong<br>CRM-Platform.||Hiển<br>thị báo<br>cáo|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-Core||Import<br>CDRReport|/cdrreport/import|Import dữ liệu<br>CDRReport trong<br>BCCS2-Core.||Cảnh<br>báo|Chỉ<br>dùng<br>cho<br>admin|
||CRM-<br>Platform||Analyze QoS|/qos/analyze|Analyze dữ liệu QoS<br>trong CRM-<br>Platform.||Cảnh<br>báo|Tích<br>hợp với<br>CRM|
||BCCS2-Core||Update<br>Campaign|/campaign/update|Update dữ liệu<br>Campaign trong<br>BCCS2-Core.||Lỗi<br>nghiêm<br>trọng|Chạy<br>theo<br>lịch<br>cron|
||Infra-Network||Export<br>AccountLock|/accountlock/export|Export dữ liệu<br>AccountLock trong<br>Infra-Network.||Hiển<br>thị báo<br>cáo|Chạy<br>theo<br>lịch<br>cron|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||CRM-<br>Platform||Analyze<br>TransactionLog|/transactionlog/analyze|Analyze dữ liệu<br>TransactionLog<br>trong CRM-<br>Platform.||Không<br>lỗi|Tích<br>hợp với<br>CRM|
||CRM-<br>Platform||Config<br>KPIReport|/kpireport/config|Config dữ liệu<br>KPIReport trong<br>CRM-Platform.||Đồng<br>bộ dữ<br>liệu|Theo<br>chuẩn<br>ISO<br>27001|
||RPA-Engine||Optimize<br>Campaign|/campaign/optimize|Optimize dữ liệu<br>Campaign trong<br>RPA-Engine.||Thông<br>báo<br>qua<br>email|Chỉ<br>dùng<br>cho<br>admin|
||IVR-System||Delete Queue|/queue/delete|Delete dữ liệu Queue<br>trong IVR-System.||Tự<br>động<br>retry|Kết nối<br>với hệ<br>thống<br>Billing|
||RPA-Engine||Delete<br>AgentStatus|/agentstatus/delete|Delete dữ liệu<br>AgentStatus trong<br>RPA-Engine.||Thông<br>báo<br>qua<br>SMS|Tích<br>hợp với<br>CRM|
||BCCS2-<br>Billing||Schedule<br>AgentStatus|/agentstatus/schedule|Schedule dữ liệu<br>AgentStatus trong<br>BCCS2-Billing.||Đồng<br>bộ dữ<br>liệu|Dữ liệu<br>backup<br>mỗi<br>ngày|
||CRM-<br>Platform||Validate<br>CustomerProfile|/customerprofile/validate|Validate dữ liệu<br>CustomerProfile<br>trong CRM-<br>Platform.||Lỗi<br>nghiêm<br>trọng|Tích<br>hợp với<br>CRM|
||Security-<br>Firewall||Update VPN|/vpn/update|Update dữ liệu VPN<br>trong Security-<br>Firewall.||Ghi log<br>đầy đủ|Tích<br>hợp với<br>CRM|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||IVR-System||Schedule<br>Invoice|/invoice/schedule|Schedule dữ liệu<br>Invoice trong IVR-<br>System.||Không<br>lỗi|Tích<br>hợp với<br>CRM|
||BCCS2-Core||Search<br>Whitelist|/whitelist/search|Search dữ liệu<br>Whitelist trong<br>BCCS2-Core.||Ghi log<br>đầy đủ|Theo<br>chuẩn<br>ISO<br>27001|
||BCCS2-Core||Optimize<br>PackagePlan|/packageplan/optimize|Optimize dữ liệu<br>PackagePlan trong<br>BCCS2-Core.||Hiển<br>thị báo<br>cáo|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Server||Optimize VPN|/vpn/optimize|Optimize dữ liệu<br>VPN trong Infra-<br>Server.||Thông<br>báo<br>qua<br>email|Dữ liệu<br>backup<br>mỗi<br>ngày|
||IVR-System||Schedule QoS|/qos/schedule|Schedule dữ liệu<br>QoS trong IVR-<br>System.||Hiển<br>thị báo<br>cáo|Tích<br>hợp với<br>CRM|
||CRM-<br>Platform||Optimize<br>IVRPrompt|/ivrprompt/optimize|Optimize dữ liệu<br>IVRPrompt trong<br>CRM-Platform.||Thông<br>báo<br>qua<br>email|Bảo<br>mật 2<br>lớp|
||IPCC-<br>ContactCenter||Optimize<br>KPIReport|/kpireport/optimize|Optimize dữ liệu<br>KPIReport trong<br>IPCC-<br>ContactCenter.||Lỗi<br>nghiêm<br>trọng|Bảo<br>mật 2<br>lớp|
||Infra-Server||Schedule<br>FirewallPolicy|/firewallpolicy/schedule|Schedule dữ liệu<br>FirewallPolicy trong<br>Infra-Server.||Tự<br>động<br>retry|Có cơ<br>chế<br>rollback|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Security-<br>Firewall||Schedule QoS|/qos/schedule|Schedule dữ liệu<br>QoS trong Security-<br>Firewall.||Thông<br>báo<br>qua<br>SMS|Chạy<br>theo<br>lịch<br>cron|
||RPA-Engine||Optimize<br>KPIReport|/kpireport/optimize|Optimize dữ liệu<br>KPIReport trong<br>RPA-Engine.||Lỗi<br>nghiêm<br>trọng|Chạy<br>theo<br>lịch<br>cron|
||IPCC-<br>ContactCenter||Update<br>KPIReport|/kpireport/update|Update dữ liệu<br>KPIReport trong<br>IPCC-<br>ContactCenter.||Tự<br>động<br>retry|Kết nối<br>với hệ<br>thống<br>Billing|
||RPA-Engine||Config<br>FirewallPolicy|/firewallpolicy/config|Config dữ liệu<br>FirewallPolicy trong<br>RPA-Engine.||Thành<br>công|Theo<br>quy<br>định<br>Viettel|
||Security-<br>Firewall||Optimize<br>ClusterNode|/clusternode/optimize|Optimize dữ liệu<br>ClusterNode trong<br>Security-Firewall.||Ghi log<br>đầy đủ|Chỉ<br>dùng<br>cho<br>admin|
||Infra-Network||Schedule<br>SwitchConfig|/switchconfig/schedule|Schedule dữ liệu<br>SwitchConfig trong<br>Infra-Network.||Thông<br>báo<br>qua<br>email|Chạy<br>theo<br>lịch<br>cron|
||RPA-Engine||Analyze<br>KPIReport|/kpireport/analyze|Analyze dữ liệu<br>KPIReport trong<br>RPA-Engine.||Không<br>lỗi|Dữ liệu<br>backup<br>mỗi<br>ngày|
||QA-<br>Automation||Config<br>IVRPrompt|/ivrprompt/config|Config dữ liệu<br>IVRPrompt trong<br>QA-Automation.||Không<br>lỗi|Kết nối<br>với hệ|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
|||||||||thống<br>Billing|
||QA-<br>Automation||Monitor Invoice|/invoice/monitor|Monitor dữ liệu<br>Invoice trong QA-<br>Automation.||Cảnh<br>báo|Theo<br>chuẩn<br>ISO<br>27001|
||IVR-System||Insert<br>CustomerProfile|/customerprofile/insert|Insert dữ liệu<br>CustomerProfile<br>trong IVR-System.||Hiển<br>thị báo<br>cáo|Bảo<br>mật 2<br>lớp|
||IVR-System||Optimize QoS|/qos/optimize|Optimize dữ liệu<br>QoS trong IVR-<br>System.||Hiển<br>thị báo<br>cáo|Chỉ<br>dùng<br>cho<br>admin|
||BCCS2-<br>Billing||Schedule<br>Invoice|/invoice/schedule|Schedule dữ liệu<br>Invoice trong<br>BCCS2-Billing.||Đồng<br>bộ dữ<br>liệu|Dữ liệu<br>backup<br>mỗi<br>ngày|
||BCCS2-<br>Billing||Search<br>DebtControl|/debtcontrol/search|Search dữ liệu<br>DebtControl trong<br>BCCS2-Billing.||Cảnh<br>báo|Tích<br>hợp với<br>CRM|
||IVR-System||Optimize Lead|/lead/optimize|Optimize dữ liệu<br>Lead trong IVR-<br>System.||Không<br>lỗi|Chỉ<br>dùng<br>cho<br>admin|
||RPA-Engine||Config Lead|/lead/config|Config dữ liệu Lead<br>trong RPA-Engine.||Cảnh<br>báo|Chỉ<br>dùng<br>cho<br>admin|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Security-<br>Firewall||Monitor<br>ClusterNode|/clusternode/monitor|Monitor dữ liệu<br>ClusterNode trong<br>Security-Firewall.||Thông<br>báo<br>qua<br>SMS|Chạy<br>theo<br>lịch<br>cron|
||Security-<br>Firewall||Update QoS|/qos/update|Update dữ liệu QoS<br>trong Security-<br>Firewall.||Ghi log<br>đầy đủ|Theo<br>chuẩn<br>ISO<br>27001|
||RPA-Engine||Import Blacklist|/blacklist/import|Import dữ liệu<br>Blacklist trong RPA-<br>Engine.||Ghi log<br>đầy đủ|Tích<br>hợp với<br>CRM|
||RPA-Engine||Delete<br>StorageVolume|/storagevolume/delete|Delete dữ liệu<br>StorageVolume<br>trong RPA-Engine.||Tự<br>động<br>retry|Bảo<br>mật 2<br>lớp|
||RPA-Engine||Generate<br>Invoice|/invoice/generate|Generate dữ liệu<br>Invoice trong RPA-<br>Engine.||Không<br>lỗi|Chỉ<br>dùng<br>cho<br>admin|
||Infra-Network||Search<br>CDRReport|/cdrreport/search|Search dữ liệu<br>CDRReport trong<br>Infra-Network.||Đồng<br>bộ dữ<br>liệu|Chạy<br>theo<br>lịch<br>cron|
||BCCS2-Core||Optimize<br>DebtControl|/debtcontrol/optimize|Optimize dữ liệu<br>DebtControl trong<br>BCCS2-Core.||Thông<br>báo<br>qua<br>email|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Network||Delete<br>Campaign|/campaign/delete|Delete dữ liệu<br>Campaign trong<br>Infra-Network.||Thành<br>công|Kết nối<br>với hệ<br>thống<br>Billing|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Infra-Network||Delete<br>CustomerProfile|/customerprofile/delete|Delete dữ liệu<br>CustomerProfile<br>trong Infra-Network.||Không<br>lỗi|Chạy<br>theo<br>lịch<br>cron|
||BCCS2-Core||Monitor<br>TransactionLog|/transactionlog/monitor|Monitor dữ liệu<br>TransactionLog<br>trong BCCS2-Core.||Hiển<br>thị báo<br>cáo|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||QA-<br>Automation||Export Contact|/contact/export|Export dữ liệu<br>Contact trong QA-<br>Automation.||Hiển<br>thị báo<br>cáo|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Security-<br>Firewall||Delete Contact|/contact/delete|Delete dữ liệu<br>Contact trong<br>Security-Firewall.||Ghi log<br>đầy đủ|Theo<br>chuẩn<br>ISO<br>27001|
||Security-<br>Firewall||Search<br>Whitelist|/whitelist/search|Search dữ liệu<br>Whitelist trong<br>Security-Firewall.||Lỗi<br>nghiêm<br>trọng|Chỉ<br>dùng<br>cho<br>admin|
||BCCS2-<br>Billing||Import Contact|/contact/import|Import dữ liệu<br>Contact trong<br>BCCS2-Billing.||Cảnh<br>báo|Theo<br>quy<br>định<br>Viettel|
||Infra-Server||Insert<br>APIGateway|/apigateway/insert|Insert dữ liệu<br>APIGateway trong<br>Infra-Server.||Không<br>lỗi|Theo<br>quy<br>định<br>Viettel|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||QA-<br>Automation||Optimize<br>TransactionLog|/transactionlog/optimize|Optimize dữ liệu<br>TransactionLog<br>trong QA-<br>Automation.||Thành<br>công|Tích<br>hợp với<br>CRM|
||Infra-Network||Optimize<br>Opportunity|/opportunity/optimize|Optimize dữ liệu<br>Opportunity trong<br>Infra-Network.||Không<br>lỗi|Kết nối<br>với hệ<br>thống<br>Billing|
||RPA-Engine||Update<br>PackagePlan|/packageplan/update|Update dữ liệu<br>PackagePlan trong<br>RPA-Engine.||Lỗi<br>nghiêm<br>trọng|Theo<br>chuẩn<br>ISO<br>27001|
||BCCS2-Core||Generate<br>Invoice|/invoice/generate|Generate dữ liệu<br>Invoice trong<br>BCCS2-Core.||Thông<br>báo<br>qua<br>email|Kết nối<br>với hệ<br>thống<br>Billing|
||BCCS2-Core||Import<br>SwitchConfig|/switchconfig/import|Import dữ liệu<br>SwitchConfig trong<br>BCCS2-Core.||Không<br>lỗi|Theo<br>chuẩn<br>ISO<br>27001|
||Security-<br>Firewall||Schedule<br>Campaign|/campaign/schedule|Schedule dữ liệu<br>Campaign trong<br>Security-Firewall.||Tự<br>động<br>retry|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-<br>Billing||Update<br>Whitelist|/whitelist/update|Update dữ liệu<br>Whitelist trong<br>BCCS2-Billing.||Tự<br>động<br>retry|Theo<br>chuẩn<br>ISO<br>27001|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||QA-<br>Automation||Insert DataLake|/datalake/insert|Insert dữ liệu<br>DataLake trong QA-<br>Automation.||Ghi log<br>đầy đủ|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||CRM-<br>Platform||Import<br>CDRReport|/cdrreport/import|Import dữ liệu<br>CDRReport trong<br>CRM-Platform.||Tự<br>động<br>retry|Chạy<br>theo<br>lịch<br>cron|
||QA-<br>Automation||Config<br>AgentStatus|/agentstatus/config|Config dữ liệu<br>AgentStatus trong<br>QA-Automation.||Hiển<br>thị báo<br>cáo|Kết nối<br>với hệ<br>thống<br>Billing|
||IVR-System||Search<br>CDRReport|/cdrreport/search|Search dữ liệu<br>CDRReport trong<br>IVR-System.||Lỗi<br>nghiêm<br>trọng|Dữ liệu<br>backup<br>mỗi<br>ngày|
||Infra-Network||Validate<br>SwitchConfig|/switchconfig/validate|Validate dữ liệu<br>SwitchConfig trong<br>Infra-Network.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-<br>Billing||Monitor<br>ClusterNode|/clusternode/monitor|Monitor dữ liệu<br>ClusterNode trong<br>BCCS2-Billing.||Thông<br>báo<br>qua<br>SMS|Tích<br>hợp với<br>CRM|
||Security-<br>Firewall||Validate<br>Opportunity|/opportunity/validate|Validate dữ liệu<br>Opportunity trong<br>Security-Firewall.||Thông<br>báo<br>qua<br>SMS|Chỉ<br>dùng<br>cho<br>admin|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Security-<br>Firewall||Schedule<br>Whitelist|/whitelist/schedule|Schedule dữ liệu<br>Whitelist trong<br>Security-Firewall.||Đồng<br>bộ dữ<br>liệu|Tích<br>hợp với<br>CRM|
||BCCS2-<br>Billing||Delete<br>APIGateway|/apigateway/delete|Delete dữ liệu<br>APIGateway trong<br>BCCS2-Billing.||Thành<br>công|Theo<br>quy<br>định<br>Viettel|
||Infra-Network||Search<br>ClusterNode|/clusternode/search|Search dữ liệu<br>ClusterNode trong<br>Infra-Network.||Đồng<br>bộ dữ<br>liệu|Theo<br>quy<br>định<br>Viettel|
||BCCS2-Core||Config Contact|/contact/config|Config dữ liệu<br>Contact trong<br>BCCS2-Core.||Thông<br>báo<br>qua<br>email|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||IPCC-<br>ContactCenter||Config Contact|/contact/config|Config dữ liệu<br>Contact trong IPCC-<br>ContactCenter.||Thành<br>công|Chỉ<br>dùng<br>cho<br>admin|
||QA-<br>Automation||Config<br>CDRReport|/cdrreport/config|Config dữ liệu<br>CDRReport trong<br>QA-Automation.||Không<br>lỗi|Kết nối<br>với hệ<br>thống<br>Billing|
||BCCS2-Core||Schedule<br>KPIReport|/kpireport/schedule|Schedule dữ liệu<br>KPIReport trong<br>BCCS2-Core.||Thông<br>báo<br>qua<br>SMS|Chạy<br>theo<br>lịch<br>cron|
||Infra-Network||Delete<br>IVRPrompt|/ivrprompt/delete|Delete dữ liệu<br>IVRPrompt trong<br>Infra-Network.||Tự<br>động<br>retry|Dữ liệu<br>backup|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
|||||||||mỗi<br>ngày|
||Security-<br>Firewall||Validate<br>DebtControl|/debtcontrol/validate|Validate dữ liệu<br>DebtControl trong<br>Security-Firewall.||Thành<br>công|Có cơ<br>chế<br>rollback|
||BCCS2-Core||Optimize Lead|/lead/optimize|Optimize dữ liệu<br>Lead trong BCCS2-<br>Core.||Thông<br>báo<br>qua<br>SMS|Theo<br>quy<br>định<br>Viettel|
||RPA-Engine||Validate<br>Opportunity|/opportunity/validate|Validate dữ liệu<br>Opportunity trong<br>RPA-Engine.||Cảnh<br>báo|Có cơ<br>chế<br>rollback|
||IVR-System||Update<br>DataLake|/datalake/update|Update dữ liệu<br>DataLake trong<br>IVR-System.||Không<br>lỗi|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Server||Config<br>CustomerProfile|/customerprofile/config|Config dữ liệu<br>CustomerProfile<br>trong Infra-Server.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-<br>Billing||Validate<br>StorageVolume|/storagevolume/validate|Validate dữ liệu<br>StorageVolume<br>trong BCCS2-<br>Billing.||Thông<br>báo<br>qua<br>email|Theo<br>quy<br>định<br>Viettel|
||CRM-<br>Platform||Analyze<br>APIGateway|/apigateway/analyze|Analyze dữ liệu<br>APIGateway trong<br>CRM-Platform.||Tự<br>động<br>retry|Theo<br>quy<br>định<br>Viettel|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Infra-Network||Search Contact|/contact/search|Search dữ liệu<br>Contact trong Infra-<br>Network.||Hiển<br>thị báo<br>cáo|Theo<br>quy<br>định<br>Viettel|
||Infra-Network||Monitor QoS|/qos/monitor|Monitor dữ liệu QoS<br>trong Infra-Network.||Lỗi<br>nghiêm<br>trọng|Chạy<br>theo<br>lịch<br>cron|
||Security-<br>Firewall||Update<br>KPIReport|/kpireport/update|Update dữ liệu<br>KPIReport trong<br>Security-Firewall.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||RPA-Engine||Export<br>StorageVolume|/storagevolume/export|Export dữ liệu<br>StorageVolume<br>trong RPA-Engine.||Tự<br>động<br>retry|Dữ liệu<br>backup<br>mỗi<br>ngày|
||IVR-System||Config<br>PackagePlan|/packageplan/config|Config dữ liệu<br>PackagePlan trong<br>IVR-System.||Cảnh<br>báo|Theo<br>quy<br>định<br>Viettel|
||CRM-<br>Platform||Update<br>FirewallPolicy|/firewallpolicy/update|Update dữ liệu<br>FirewallPolicy trong<br>CRM-Platform.||Thành<br>công|Tích<br>hợp với<br>CRM|
||QA-<br>Automation||Analyze<br>Blacklist|/blacklist/analyze|Analyze dữ liệu<br>Blacklist trong QA-<br>Automation.||Không<br>lỗi|Dữ liệu<br>backup<br>mỗi<br>ngày|
||CRM-<br>Platform||Insert<br>AgentStatus|/agentstatus/insert|Insert dữ liệu<br>AgentStatus trong<br>CRM-Platform.||Tự<br>động<br>retry|Bảo<br>mật 2<br>lớp|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||BCCS2-Core||Config<br>DataLake|/datalake/config|Config dữ liệu<br>DataLake trong<br>BCCS2-Core.||Ghi log<br>đầy đủ|Kết nối<br>với hệ<br>thống<br>Billing|
||IPCC-<br>ContactCenter||Generate<br>Invoice|/invoice/generate|Generate dữ liệu<br>Invoice trong IPCC-<br>ContactCenter.||Thành<br>công|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-Core||Update<br>DebtControl|/debtcontrol/update|Update dữ liệu<br>DebtControl trong<br>BCCS2-Core.||Tự<br>động<br>retry|Tích<br>hợp với<br>CRM|
||BCCS2-<br>Billing||Optimize<br>IVRPrompt|/ivrprompt/optimize|Optimize dữ liệu<br>IVRPrompt trong<br>BCCS2-Billing.||Lỗi<br>nghiêm<br>trọng|Dữ liệu<br>backup<br>mỗi<br>ngày|
||BCCS2-Core||Update<br>IVRPrompt|/ivrprompt/update|Update dữ liệu<br>IVRPrompt trong<br>BCCS2-Core.||Thành<br>công|Bảo<br>mật 2<br>lớp|
||IVR-System||Validate<br>CDRReport|/cdrreport/validate|Validate dữ liệu<br>CDRReport trong<br>IVR-System.||Lỗi<br>nghiêm<br>trọng|Có cơ<br>chế<br>rollback|
||IPCC-<br>ContactCenter||Insert Blacklist|/blacklist/insert|Insert dữ liệu<br>Blacklist trong<br>IPCC-<br>ContactCenter.||Ghi log<br>đầy đủ|Có cơ<br>chế<br>rollback|
||BCCS2-Core||Import<br>PackagePlan|/packageplan/import|Import dữ liệu<br>PackagePlan trong<br>BCCS2-Core.||Lỗi<br>nghiêm<br>trọng|Theo<br>quy<br>định<br>Viettel|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||QA-<br>Automation||Delete<br>IVRPrompt|/ivrprompt/delete|Delete dữ liệu<br>IVRPrompt trong<br>QA-Automation.||Cảnh<br>báo|Theo<br>chuẩn<br>ISO<br>27001|
||QA-<br>Automation||Import<br>Opportunity|/opportunity/import|Import dữ liệu<br>Opportunity trong<br>QA-Automation.||Ghi log<br>đầy đủ|Dữ liệu<br>backup<br>mỗi<br>ngày|
||RPA-Engine||Delete<br>Promotion|/promotion/delete|Delete dữ liệu<br>Promotion trong<br>RPA-Engine.||Cảnh<br>báo|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||IVR-System||Update<br>Campaign|/campaign/update|Update dữ liệu<br>Campaign trong<br>IVR-System.||Không<br>lỗi|Tích<br>hợp với<br>CRM|
||IPCC-<br>ContactCenter||Optimize<br>CDRReport|/cdrreport/optimize|Optimize dữ liệu<br>CDRReport trong<br>IPCC-<br>ContactCenter.||Thông<br>báo<br>qua<br>email|Kết nối<br>với hệ<br>thống<br>Billing|
||Infra-Network||Monitor VPN|/vpn/monitor|Monitor dữ liệu<br>VPN trong Infra-<br>Network.||Thành<br>công|Tích<br>hợp với<br>CRM|
||RPA-Engine||Import<br>IVRPrompt|/ivrprompt/import|Import dữ liệu<br>IVRPrompt trong<br>RPA-Engine.||Không<br>lỗi|Theo<br>chuẩn<br>ISO<br>27001|
||BCCS2-<br>Billing||Validate<br>StorageVolume|/storagevolume/validate|Validate dữ liệu<br>StorageVolume<br>trong BCCS2-<br>Billing.||Đồng<br>bộ dữ<br>liệu|Chỉ<br>dùng<br>cho<br>admin|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||QA-<br>Automation||Delete Invoice|/invoice/delete|Delete dữ liệu<br>Invoice trong QA-<br>Automation.||Ghi log<br>đầy đủ|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-Core||Update<br>PackagePlan|/packageplan/update|Update dữ liệu<br>PackagePlan trong<br>BCCS2-Core.||Tự<br>động<br>retry|Chỉ<br>dùng<br>cho<br>admin|
||CRM-<br>Platform||Search<br>Campaign|/campaign/search|Search dữ liệu<br>Campaign trong<br>CRM-Platform.||Đồng<br>bộ dữ<br>liệu|Tích<br>hợp với<br>CRM|
||BCCS2-<br>Billing||Insert VPN|/vpn/insert|Insert dữ liệu VPN<br>trong BCCS2-<br>Billing.||Lỗi<br>nghiêm<br>trọng|Dữ liệu<br>backup<br>mỗi<br>ngày|
||IVR-System||Schedule<br>ClusterNode|/clusternode/schedule|Schedule dữ liệu<br>ClusterNode trong<br>IVR-System.||Thông<br>báo<br>qua<br>email|Kết nối<br>với hệ<br>thống<br>Billing|
||Security-<br>Firewall||Optimize<br>KPIReport|/kpireport/optimize|Optimize dữ liệu<br>KPIReport trong<br>Security-Firewall.||Cảnh<br>báo|Tích<br>hợp với<br>CRM|
||Infra-Server||Analyze<br>Promotion|/promotion/analyze|Analyze dữ liệu<br>Promotion trong<br>Infra-Server.||Tự<br>động<br>retry|Theo<br>chuẩn<br>ISO<br>27001|
||BCCS2-<br>Billing||Export<br>IVRPrompt|/ivrprompt/export|Export dữ liệu<br>IVRPrompt trong<br>BCCS2-Billing.||Thành<br>công|Chạy<br>theo<br>lịch<br>cron|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Security-<br>Firewall||Insert<br>DebtControl|/debtcontrol/insert|Insert dữ liệu<br>DebtControl trong<br>Security-Firewall.||Không<br>lỗi|Theo<br>quy<br>định<br>Viettel|
||QA-<br>Automation||Schedule<br>KPIReport|/kpireport/schedule|Schedule dữ liệu<br>KPIReport trong<br>QA-Automation.||Tự<br>động<br>retry|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Server||Monitor<br>Whitelist|/whitelist/monitor|Monitor dữ liệu<br>Whitelist trong<br>Infra-Server.||Thông<br>báo<br>qua<br>email|Chạy<br>theo<br>lịch<br>cron|
||Infra-Server||Config<br>FirewallPolicy|/firewallpolicy/config|Config dữ liệu<br>FirewallPolicy trong<br>Infra-Server.||Thông<br>báo<br>qua<br>SMS|Kết nối<br>với hệ<br>thống<br>Billing|
||Infra-Network||Monitor Lead|/lead/monitor|Monitor dữ liệu<br>Lead trong Infra-<br>Network.||Không<br>lỗi|Dữ liệu<br>backup<br>mỗi<br>ngày|
||IPCC-<br>ContactCenter||Delete<br>PackagePlan|/packageplan/delete|Delete dữ liệu<br>PackagePlan trong<br>IPCC-<br>ContactCenter.||Đồng<br>bộ dữ<br>liệu|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-Core||Generate<br>AccountLock|/accountlock/generate|Generate dữ liệu<br>AccountLock trong<br>BCCS2-Core.||Thông<br>báo<br>qua<br>email|Yêu<br>cầu xác<br>thực<br>người<br>dùng|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||IVR-System||Config<br>IVRPrompt|/ivrprompt/config|Config dữ liệu<br>IVRPrompt trong<br>IVR-System.||Ghi log<br>đầy đủ|Bảo<br>mật 2<br>lớp|
||Infra-Network||Optimize<br>Opportunity|/opportunity/optimize|Optimize dữ liệu<br>Opportunity trong<br>Infra-Network.||Đồng<br>bộ dữ<br>liệu|Chỉ<br>dùng<br>cho<br>admin|
||Infra-Network||Monitor<br>Contact|/contact/monitor|Monitor dữ liệu<br>Contact trong Infra-<br>Network.||Không<br>lỗi|Chạy<br>theo<br>lịch<br>cron|
||Security-<br>Firewall||Import<br>Campaign|/campaign/import|Import dữ liệu<br>Campaign trong<br>Security-Firewall.||Thành<br>công|Chỉ<br>dùng<br>cho<br>admin|
||Infra-Network||Schedule<br>AgentStatus|/agentstatus/schedule|Schedule dữ liệu<br>AgentStatus trong<br>Infra-Network.||Hiển<br>thị báo<br>cáo|Theo<br>chuẩn<br>ISO<br>27001|
||Security-<br>Firewall||Import<br>CustomerProfile|/customerprofile/import|Import dữ liệu<br>CustomerProfile<br>trong Security-<br>Firewall.||Thông<br>báo<br>qua<br>SMS|Theo<br>quy<br>định<br>Viettel|
||IPCC-<br>ContactCenter||Delete QoS|/qos/delete|Delete dữ liệu QoS<br>trong IPCC-<br>ContactCenter.||Ghi log<br>đầy đủ|Theo<br>quy<br>định<br>Viettel|
||Infra-Server||Validate Lead|/lead/validate|Validate dữ liệu<br>Lead trong Infra-<br>Server.||Đồng<br>bộ dữ<br>liệu|Có cơ<br>chế<br>rollback|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||BCCS2-<br>Billing||Delete<br>CustomerProfile|/customerprofile/delete|Delete dữ liệu<br>CustomerProfile<br>trong BCCS2-<br>Billing.||Hiển<br>thị báo<br>cáo|Có cơ<br>chế<br>rollback|
||BCCS2-<br>Billing||Generate<br>AccountLock|/accountlock/generate|Generate dữ liệu<br>AccountLock trong<br>BCCS2-Billing.||Thành<br>công|Kết nối<br>với hệ<br>thống<br>Billing|
||CRM-<br>Platform||Delete<br>PackagePlan|/packageplan/delete|Delete dữ liệu<br>PackagePlan trong<br>CRM-Platform.||Ghi log<br>đầy đủ|Chạy<br>theo<br>lịch<br>cron|
||CRM-<br>Platform||Validate<br>Opportunity|/opportunity/validate|Validate dữ liệu<br>Opportunity trong<br>CRM-Platform.||Ghi log<br>đầy đủ|Có cơ<br>chế<br>rollback|
||Infra-Network||Optimize<br>Promotion|/promotion/optimize|Optimize dữ liệu<br>Promotion trong<br>Infra-Network.||Không<br>lỗi|Bảo<br>mật 2<br>lớp|
||IPCC-<br>ContactCenter||Search<br>DebtControl|/debtcontrol/search|Search dữ liệu<br>DebtControl trong<br>IPCC-<br>ContactCenter.||Ghi log<br>đầy đủ|Tích<br>hợp với<br>CRM|
||RPA-Engine||Generate<br>AgentStatus|/agentstatus/generate|Generate dữ liệu<br>AgentStatus trong<br>RPA-Engine.||Không<br>lỗi|Tích<br>hợp với<br>CRM|
||Infra-Server||Config VPN|/vpn/config|Config dữ liệu VPN<br>trong Infra-Server.||Đồng<br>bộ dữ<br>liệu|Chỉ<br>dùng<br>cho<br>admin|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Security-<br>Firewall||Update<br>ClusterNode|/clusternode/update|Update dữ liệu<br>ClusterNode trong<br>Security-Firewall.||Không<br>lỗi|Theo<br>quy<br>định<br>Viettel|
||RPA-Engine||Config<br>IVRPrompt|/ivrprompt/config|Config dữ liệu<br>IVRPrompt trong<br>RPA-Engine.||Thông<br>báo<br>qua<br>SMS|Có cơ<br>chế<br>rollback|
||CRM-<br>Platform||Search<br>DataLake|/datalake/search|Search dữ liệu<br>DataLake trong<br>CRM-Platform.||Ghi log<br>đầy đủ|Chỉ<br>dùng<br>cho<br>admin|
||Security-<br>Firewall||Optimize<br>TransactionLog|/transactionlog/optimize|Optimize dữ liệu<br>TransactionLog<br>trong Security-<br>Firewall.||Thông<br>báo<br>qua<br>email|Dữ liệu<br>backup<br>mỗi<br>ngày|
||IPCC-<br>ContactCenter||Schedule<br>Invoice|/invoice/schedule|Schedule dữ liệu<br>Invoice trong IPCC-<br>ContactCenter.||Thành<br>công|Kết nối<br>với hệ<br>thống<br>Billing|
||BCCS2-Core||Update<br>TransactionLog|/transactionlog/update|Update dữ liệu<br>TransactionLog<br>trong BCCS2-Core.||Thông<br>báo<br>qua<br>SMS|Chỉ<br>dùng<br>cho<br>admin|
||BCCS2-Core||Delete<br>TransactionLog|/transactionlog/delete|Delete dữ liệu<br>TransactionLog<br>trong BCCS2-Core.||Ghi log<br>đầy đủ|Bảo<br>mật 2<br>lớp|
||IVR-System||Config VPN|/vpn/config|Config dữ liệu VPN<br>trong IVR-System.||Không<br>lỗi|Chỉ<br>dùng<br>cho<br>admin|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||CRM-<br>Platform||Generate<br>ClusterNode|/clusternode/generate|Generate dữ liệu<br>ClusterNode trong<br>CRM-Platform.||Không<br>lỗi|Bảo<br>mật 2<br>lớp|
||BCCS2-Core||Optimize Lead|/lead/optimize|Optimize dữ liệu<br>Lead trong BCCS2-<br>Core.||Lỗi<br>nghiêm<br>trọng|Kết nối<br>với hệ<br>thống<br>Billing|
||IVR-System||Update<br>CustomerProfile|/customerprofile/update|Update dữ liệu<br>CustomerProfile<br>trong IVR-System.||Thông<br>báo<br>qua<br>email|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Network||Schedule<br>AccountLock|/accountlock/schedule|Schedule dữ liệu<br>AccountLock trong<br>Infra-Network.||Lỗi<br>nghiêm<br>trọng|Chỉ<br>dùng<br>cho<br>admin|
||BCCS2-Core||Search<br>ClusterNode|/clusternode/search|Search dữ liệu<br>ClusterNode trong<br>BCCS2-Core.||Đồng<br>bộ dữ<br>liệu|Tích<br>hợp với<br>CRM|
||BCCS2-<br>Billing||Monitor<br>Opportunity|/opportunity/monitor|Monitor dữ liệu<br>Opportunity trong<br>BCCS2-Billing.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||RPA-Engine||Import<br>Campaign|/campaign/import|Import dữ liệu<br>Campaign trong<br>RPA-Engine.||Lỗi<br>nghiêm<br>trọng|Có cơ<br>chế<br>rollback|
||QA-<br>Automation||Search<br>SwitchConfig|/switchconfig/search|Search dữ liệu<br>SwitchConfig trong<br>QA-Automation.||Tự<br>động<br>retry|Có cơ<br>chế<br>rollback|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||BCCS2-<br>Billing||Export QoS|/qos/export|Export dữ liệu QoS<br>trong BCCS2-<br>Billing.||Đồng<br>bộ dữ<br>liệu|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Server||Update Invoice|/invoice/update|Update dữ liệu<br>Invoice trong Infra-<br>Server.||Ghi log<br>đầy đủ|Có cơ<br>chế<br>rollback|
||BCCS2-<br>Billing||Monitor VPN|/vpn/monitor|Monitor dữ liệu<br>VPN trong BCCS2-<br>Billing.||Thông<br>báo<br>qua<br>SMS|Dữ liệu<br>backup<br>mỗi<br>ngày|
||QA-<br>Automation||Search<br>SwitchConfig|/switchconfig/search|Search dữ liệu<br>SwitchConfig trong<br>QA-Automation.||Đồng<br>bộ dữ<br>liệu|Chạy<br>theo<br>lịch<br>cron|
||Security-<br>Firewall||Optimize<br>PackagePlan|/packageplan/optimize|Optimize dữ liệu<br>PackagePlan trong<br>Security-Firewall.||Thành<br>công|Theo<br>quy<br>định<br>Viettel|
||QA-<br>Automation||Delete Contact|/contact/delete|Delete dữ liệu<br>Contact trong QA-<br>Automation.||Tự<br>động<br>retry|Theo<br>chuẩn<br>ISO<br>27001|
||BCCS2-Core||Schedule<br>SwitchConfig|/switchconfig/schedule|Schedule dữ liệu<br>SwitchConfig trong<br>BCCS2-Core.||Thông<br>báo<br>qua<br>SMS|Có cơ<br>chế<br>rollback|
||IVR-System||Analyze<br>Promotion|/promotion/analyze|Analyze dữ liệu<br>Promotion trong<br>IVR-System.||Không<br>lỗi|Dữ liệu<br>backup<br>mỗi<br>ngày|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||QA-<br>Automation||Import Invoice|/invoice/import|Import dữ liệu<br>Invoice trong QA-<br>Automation.||Thành<br>công|Tích<br>hợp với<br>CRM|
||QA-<br>Automation||Import VPN|/vpn/import|Import dữ liệu VPN<br>trong QA-<br>Automation.||Thông<br>báo<br>qua<br>email|Theo<br>quy<br>định<br>Viettel|
||IVR-System||Update<br>SwitchConfig|/switchconfig/update|Update dữ liệu<br>SwitchConfig trong<br>IVR-System.||Thành<br>công|Chỉ<br>dùng<br>cho<br>admin|
||BCCS2-<br>Billing||Insert<br>CDRReport|/cdrreport/insert|Insert dữ liệu<br>CDRReport trong<br>BCCS2-Billing.||Thành<br>công|Theo<br>quy<br>định<br>Viettel|
||Security-<br>Firewall||Export<br>Whitelist|/whitelist/export|Export dữ liệu<br>Whitelist trong<br>Security-Firewall.||Cảnh<br>báo|Chỉ<br>dùng<br>cho<br>admin|
||CRM-<br>Platform||Search<br>DataLake|/datalake/search|Search dữ liệu<br>DataLake trong<br>CRM-Platform.||Cảnh<br>báo|Bảo<br>mật 2<br>lớp|
||Infra-Server||Schedule<br>IVRPrompt|/ivrprompt/schedule|Schedule dữ liệu<br>IVRPrompt trong<br>Infra-Server.||Thông<br>báo<br>qua<br>email|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Network||Analyze<br>Campaign|/campaign/analyze|Analyze dữ liệu<br>Campaign trong<br>Infra-Network.||Thông<br>báo<br>qua<br>SMS|Bảo<br>mật 2<br>lớp|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||BCCS2-<br>Billing||Delete<br>Opportunity|/opportunity/delete|Delete dữ liệu<br>Opportunity trong<br>BCCS2-Billing.||Hiển<br>thị báo<br>cáo|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||QA-<br>Automation||Monitor<br>AccountLock|/accountlock/monitor|Monitor dữ liệu<br>AccountLock trong<br>QA-Automation.||Ghi log<br>đầy đủ|Chạy<br>theo<br>lịch<br>cron|
||BCCS2-Core||Monitor<br>Campaign|/campaign/monitor|Monitor dữ liệu<br>Campaign trong<br>BCCS2-Core.||Không<br>lỗi|Chỉ<br>dùng<br>cho<br>admin|
||IVR-System||Export QoS|/qos/export|Export dữ liệu QoS<br>trong IVR-System.||Ghi log<br>đầy đủ|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Security-<br>Firewall||Config<br>KPIReport|/kpireport/config|Config dữ liệu<br>KPIReport trong<br>Security-Firewall.||Hiển<br>thị báo<br>cáo|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Server||Monitor<br>Blacklist|/blacklist/monitor|Monitor dữ liệu<br>Blacklist trong Infra-<br>Server.||Thông<br>báo<br>qua<br>SMS|Theo<br>quy<br>định<br>Viettel|
||BCCS2-Core||Optimize<br>FirewallPolicy|/firewallpolicy/optimize|Optimize dữ liệu<br>FirewallPolicy trong<br>BCCS2-Core.||Lỗi<br>nghiêm<br>trọng|Bảo<br>mật 2<br>lớp|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||IPCC-<br>ContactCenter||Search<br>PackagePlan|/packageplan/search|Search dữ liệu<br>PackagePlan trong<br>IPCC-<br>ContactCenter.||Tự<br>động<br>retry|Chỉ<br>dùng<br>cho<br>admin|
||IPCC-<br>ContactCenter||Delete<br>Promotion|/promotion/delete|Delete dữ liệu<br>Promotion trong<br>IPCC-<br>ContactCenter.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-Core||Monitor<br>SwitchConfig|/switchconfig/monitor|Monitor dữ liệu<br>SwitchConfig trong<br>BCCS2-Core.||Tự<br>động<br>retry|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||IPCC-<br>ContactCenter||Schedule<br>DataLake|/datalake/schedule|Schedule dữ liệu<br>DataLake trong<br>IPCC-<br>ContactCenter.||Ghi log<br>đầy đủ|Theo<br>chuẩn<br>ISO<br>27001|
||IPCC-<br>ContactCenter||Insert Queue|/queue/insert|Insert dữ liệu Queue<br>trong IPCC-<br>ContactCenter.||Thông<br>báo<br>qua<br>email|Tích<br>hợp với<br>CRM|
||RPA-Engine||Validate<br>APIGateway|/apigateway/validate|Validate dữ liệu<br>APIGateway trong<br>RPA-Engine.||Thông<br>báo<br>qua<br>SMS|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Server||Schedule<br>AgentStatus|/agentstatus/schedule|Schedule dữ liệu<br>AgentStatus trong<br>Infra-Server.||Đồng<br>bộ dữ<br>liệu|Theo<br>chuẩn<br>ISO<br>27001|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||IVR-System||Optimize Lead|/lead/optimize|Optimize dữ liệu<br>Lead trong IVR-<br>System.||Không<br>lỗi|Chỉ<br>dùng<br>cho<br>admin|
||BCCS2-Core||Optimize<br>Promotion|/promotion/optimize|Optimize dữ liệu<br>Promotion trong<br>BCCS2-Core.||Thông<br>báo<br>qua<br>SMS|Kết nối<br>với hệ<br>thống<br>Billing|
||BCCS2-<br>Billing||Generate Queue|/queue/generate|Generate dữ liệu<br>Queue trong<br>BCCS2-Billing.||Đồng<br>bộ dữ<br>liệu|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||BCCS2-Core||Monitor<br>PackagePlan|/packageplan/monitor|Monitor dữ liệu<br>PackagePlan trong<br>BCCS2-Core.||Hiển<br>thị báo<br>cáo|Kết nối<br>với hệ<br>thống<br>Billing|
||Security-<br>Firewall||Analyze<br>StorageVolume|/storagevolume/analyze|Analyze dữ liệu<br>StorageVolume<br>trong Security-<br>Firewall.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||IPCC-<br>ContactCenter||Export Contact|/contact/export|Export dữ liệu<br>Contact trong IPCC-<br>ContactCenter.||Đồng<br>bộ dữ<br>liệu|Chạy<br>theo<br>lịch<br>cron|
||Infra-Network||Validate QoS|/qos/validate|Validate dữ liệu QoS<br>trong Infra-Network.||Thành<br>công|Theo<br>quy<br>định<br>Viettel|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||RPA-Engine||Search Invoice|/invoice/search|Search dữ liệu<br>Invoice trong RPA-<br>Engine.||Thông<br>báo<br>qua<br>SMS|Tích<br>hợp với<br>CRM|
||IPCC-<br>ContactCenter||Update<br>FirewallPolicy|/firewallpolicy/update|Update dữ liệu<br>FirewallPolicy trong<br>IPCC-<br>ContactCenter.||Tự<br>động<br>retry|Theo<br>chuẩn<br>ISO<br>27001|
||QA-<br>Automation||Config<br>ClusterNode|/clusternode/config|Config dữ liệu<br>ClusterNode trong<br>QA-Automation.||Lỗi<br>nghiêm<br>trọng|Tích<br>hợp với<br>CRM|
||BCCS2-<br>Billing||Delete<br>FirewallPolicy|/firewallpolicy/delete|Delete dữ liệu<br>FirewallPolicy trong<br>BCCS2-Billing.||Cảnh<br>báo|Bảo<br>mật 2<br>lớp|
||IVR-System||Schedule<br>APIGateway|/apigateway/schedule|Schedule dữ liệu<br>APIGateway trong<br>IVR-System.||Hiển<br>thị báo<br>cáo|Có cơ<br>chế<br>rollback|
||BCCS2-Core||Config<br>DataLake|/datalake/config|Config dữ liệu<br>DataLake trong<br>BCCS2-Core.||Đồng<br>bộ dữ<br>liệu|Theo<br>quy<br>định<br>Viettel|
||BCCS2-<br>Billing||Optimize<br>Whitelist|/whitelist/optimize|Optimize dữ liệu<br>Whitelist trong<br>BCCS2-Billing.||Không<br>lỗi|Chạy<br>theo<br>lịch<br>cron|
||Infra-Network||Search<br>ClusterNode|/clusternode/search|Search dữ liệu<br>ClusterNode trong<br>Infra-Network.||Hiển<br>thị báo<br>cáo|Có cơ<br>chế<br>rollback|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||IPCC-<br>ContactCenter||Search Blacklist|/blacklist/search|Search dữ liệu<br>Blacklist trong<br>IPCC-<br>ContactCenter.||Hiển<br>thị báo<br>cáo|Bảo<br>mật 2<br>lớp|
||IPCC-<br>ContactCenter||Optimize Queue|/queue/optimize|Optimize dữ liệu<br>Queue trong IPCC-<br>ContactCenter.||Lỗi<br>nghiêm<br>trọng|Có cơ<br>chế<br>rollback|
||Infra-Network||Schedule<br>IVRPrompt|/ivrprompt/schedule|Schedule dữ liệu<br>IVRPrompt trong<br>Infra-Network.||Tự<br>động<br>retry|Theo<br>quy<br>định<br>Viettel|
||RPA-Engine||Schedule<br>CustomerProfile|/customerprofile/schedule|Schedule dữ liệu<br>CustomerProfile<br>trong RPA-Engine.||Thông<br>báo<br>qua<br>email|Tích<br>hợp với<br>CRM|
||Infra-Network||Analyze Queue|/queue/analyze|Analyze dữ liệu<br>Queue trong Infra-<br>Network.||Không<br>lỗi|Theo<br>chuẩn<br>ISO<br>27001|
||CRM-<br>Platform||Update<br>DataLake|/datalake/update|Update dữ liệu<br>DataLake trong<br>CRM-Platform.||Thông<br>báo<br>qua<br>SMS|Chỉ<br>dùng<br>cho<br>admin|
||QA-<br>Automation||Export<br>AgentStatus|/agentstatus/export|Export dữ liệu<br>AgentStatus trong<br>QA-Automation.||Đồng<br>bộ dữ<br>liệu|Kết nối<br>với hệ<br>thống<br>Billing|
||BCCS2-<br>Billing||Schedule<br>SwitchConfig|/switchconfig/schedule|Schedule dữ liệu<br>SwitchConfig trong<br>BCCS2-Billing.||Lỗi<br>nghiêm<br>trọng|Tích<br>hợp với<br>CRM|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||IVR-System||Update Contact|/contact/update|Update dữ liệu<br>Contact trong IVR-<br>System.||Hiển<br>thị báo<br>cáo|Kết nối<br>với hệ<br>thống<br>Billing|
||IVR-System||Insert<br>ClusterNode|/clusternode/insert|Insert dữ liệu<br>ClusterNode trong<br>IVR-System.||Thông<br>báo<br>qua<br>SMS|Chạy<br>theo<br>lịch<br>cron|
||Security-<br>Firewall||Validate<br>Campaign|/campaign/validate|Validate dữ liệu<br>Campaign trong<br>Security-Firewall.||Hiển<br>thị báo<br>cáo|Theo<br>chuẩn<br>ISO<br>27001|
||IPCC-<br>ContactCenter||Search Queue|/queue/search|Search dữ liệu<br>Queue trong IPCC-<br>ContactCenter.||Tự<br>động<br>retry|Chạy<br>theo<br>lịch<br>cron|
||IPCC-<br>ContactCenter||Search<br>Whitelist|/whitelist/search|Search dữ liệu<br>Whitelist trong<br>IPCC-<br>ContactCenter.||Ghi log<br>đầy đủ|Theo<br>quy<br>định<br>Viettel|
||IVR-System||Config<br>FirewallPolicy|/firewallpolicy/config|Config dữ liệu<br>FirewallPolicy trong<br>IVR-System.||Hiển<br>thị báo<br>cáo|Bảo<br>mật 2<br>lớp|
||QA-<br>Automation||Validate<br>AccountLock|/accountlock/validate|Validate dữ liệu<br>AccountLock trong<br>QA-Automation.||Tự<br>động<br>retry|Tích<br>hợp với<br>CRM|
||RPA-Engine||Insert<br>AccountLock|/accountlock/insert|Insert dữ liệu<br>AccountLock trong<br>RPA-Engine.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Infra-Network||Insert Invoice|/invoice/insert|Insert dữ liệu<br>Invoice trong Infra-<br>Network.||Thông<br>báo<br>qua<br>SMS|Chỉ<br>dùng<br>cho<br>admin|
||RPA-Engine||Generate<br>Whitelist|/whitelist/generate|Generate dữ liệu<br>Whitelist trong<br>RPA-Engine.||Tự<br>động<br>retry|Theo<br>quy<br>định<br>Viettel|
||BCCS2-Core||Analyze Invoice|/invoice/analyze|Analyze dữ liệu<br>Invoice trong<br>BCCS2-Core.||Thông<br>báo<br>qua<br>email|Kết nối<br>với hệ<br>thống<br>Billing|
||QA-<br>Automation||Generate<br>FirewallPolicy|/firewallpolicy/generate|Generate dữ liệu<br>FirewallPolicy trong<br>QA-Automation.||Tự<br>động<br>retry|Theo<br>quy<br>định<br>Viettel|
||Infra-Server||Analyze<br>AgentStatus|/agentstatus/analyze|Analyze dữ liệu<br>AgentStatus trong<br>Infra-Server.||Đồng<br>bộ dữ<br>liệu|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Server||Export<br>DataLake|/datalake/export|Export dữ liệu<br>DataLake trong<br>Infra-Server.||Thành<br>công|Kết nối<br>với hệ<br>thống<br>Billing|
||BCCS2-Core||Insert<br>PackagePlan|/packageplan/insert|Insert dữ liệu<br>PackagePlan trong<br>BCCS2-Core.||Ghi log<br>đầy đủ|Dữ liệu<br>backup<br>mỗi<br>ngày|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||BCCS2-Core||Delete<br>DataLake|/datalake/delete|Delete dữ liệu<br>DataLake trong<br>BCCS2-Core.||Ghi log<br>đầy đủ|Dữ liệu<br>backup<br>mỗi<br>ngày|
||Infra-Server||Validate<br>DataLake|/datalake/validate|Validate dữ liệu<br>DataLake trong<br>Infra-Server.||Không<br>lỗi|Chạy<br>theo<br>lịch<br>cron|
||Infra-Server||Schedule QoS|/qos/schedule|Schedule dữ liệu<br>QoS trong Infra-<br>Server.||Tự<br>động<br>retry|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||RPA-Engine||Search<br>CustomerProfile|/customerprofile/search|Search dữ liệu<br>CustomerProfile<br>trong RPA-Engine.||Hiển<br>thị báo<br>cáo|Dữ liệu<br>backup<br>mỗi<br>ngày|
||Infra-Server||Update Lead|/lead/update|Update dữ liệu Lead<br>trong Infra-Server.||Không<br>lỗi|Có cơ<br>chế<br>rollback|
||Security-<br>Firewall||Generate<br>CDRReport|/cdrreport/generate|Generate dữ liệu<br>CDRReport trong<br>Security-Firewall.||Đồng<br>bộ dữ<br>liệu|Chỉ<br>dùng<br>cho<br>admin|
||Security-<br>Firewall||Monitor<br>PackagePlan|/packageplan/monitor|Monitor dữ liệu<br>PackagePlan trong<br>Security-Firewall.||Cảnh<br>báo|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||IPCC-<br>ContactCenter||Export<br>FirewallPolicy|/firewallpolicy/export|Export dữ liệu<br>FirewallPolicy trong||Thông<br>báo|Theo<br>chuẩn|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||||||IPCC-<br>ContactCenter.||qua<br>SMS|ISO<br>27001|
||Security-<br>Firewall||Import<br>Promotion|/promotion/import|Import dữ liệu<br>Promotion trong<br>Security-Firewall.||Ghi log<br>đầy đủ|Dữ liệu<br>backup<br>mỗi<br>ngày|
||BCCS2-<br>Billing||Delete<br>KPIReport|/kpireport/delete|Delete dữ liệu<br>KPIReport trong<br>BCCS2-Billing.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||IPCC-<br>ContactCenter||Import VPN|/vpn/import|Import dữ liệu VPN<br>trong IPCC-<br>ContactCenter.||Cảnh<br>báo|Tích<br>hợp với<br>CRM|
||IPCC-<br>ContactCenter||Monitor<br>Whitelist|/whitelist/monitor|Monitor dữ liệu<br>Whitelist trong<br>IPCC-<br>ContactCenter.||Ghi log<br>đầy đủ|Kết nối<br>với hệ<br>thống<br>Billing|
||QA-<br>Automation||Optimize<br>DebtControl|/debtcontrol/optimize|Optimize dữ liệu<br>DebtControl trong<br>QA-Automation.||Lỗi<br>nghiêm<br>trọng|Kết nối<br>với hệ<br>thống<br>Billing|
||IPCC-<br>ContactCenter||Insert<br>SwitchConfig|/switchconfig/insert|Insert dữ liệu<br>SwitchConfig trong<br>IPCC-<br>ContactCenter.||Tự<br>động<br>retry|Kết nối<br>với hệ<br>thống<br>Billing|
||IPCC-<br>ContactCenter||Config<br>CDRReport|/cdrreport/config|Config dữ liệu<br>CDRReport trong<br>IPCC-<br>ContactCenter.||Lỗi<br>nghiêm<br>trọng|Theo<br>quy<br>định<br>Viettel|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||IPCC-<br>ContactCenter||Config<br>PackagePlan|/packageplan/config|Config dữ liệu<br>PackagePlan trong<br>IPCC-<br>ContactCenter.||Ghi log<br>đầy đủ|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||IPCC-<br>ContactCenter||Config<br>AgentStatus|/agentstatus/config|Config dữ liệu<br>AgentStatus trong<br>IPCC-<br>ContactCenter.||Cảnh<br>báo|Có cơ<br>chế<br>rollback|
||Security-<br>Firewall||Monitor<br>IVRPrompt|/ivrprompt/monitor|Monitor dữ liệu<br>IVRPrompt trong<br>Security-Firewall.||Ghi log<br>đầy đủ|Dữ liệu<br>backup<br>mỗi<br>ngày|
||RPA-Engine||Update<br>FirewallPolicy|/firewallpolicy/update|Update dữ liệu<br>FirewallPolicy trong<br>RPA-Engine.||Hiển<br>thị báo<br>cáo|Chạy<br>theo<br>lịch<br>cron|
||Infra-Server||Delete Contact|/contact/delete|Delete dữ liệu<br>Contact trong Infra-<br>Server.||Thông<br>báo<br>qua<br>SMS|Theo<br>quy<br>định<br>Viettel|
||Infra-Network||Insert Invoice|/invoice/insert|Insert dữ liệu<br>Invoice trong Infra-<br>Network.||Đồng<br>bộ dữ<br>liệu|Tích<br>hợp với<br>CRM|
||QA-<br>Automation||Schedule<br>Campaign|/campaign/schedule|Schedule dữ liệu<br>Campaign trong QA-<br>Automation.||Ghi log<br>đầy đủ|Yêu<br>cầu xác<br>thực<br>người<br>dùng|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||BCCS2-<br>Billing||Analyze<br>Whitelist|/whitelist/analyze|Analyze dữ liệu<br>Whitelist trong<br>BCCS2-Billing.||Thông<br>báo<br>qua<br>SMS|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Security-<br>Firewall||Generate<br>CDRReport|/cdrreport/generate|Generate dữ liệu<br>CDRReport trong<br>Security-Firewall.||Thành<br>công|Có cơ<br>chế<br>rollback|
||IPCC-<br>ContactCenter||Analyze<br>Whitelist|/whitelist/analyze|Analyze dữ liệu<br>Whitelist trong<br>IPCC-<br>ContactCenter.||Không<br>lỗi|Dữ liệu<br>backup<br>mỗi<br>ngày|
||QA-<br>Automation||Export Invoice|/invoice/export|Export dữ liệu<br>Invoice trong QA-<br>Automation.||Hiển<br>thị báo<br>cáo|Theo<br>chuẩn<br>ISO<br>27001|
||IPCC-<br>ContactCenter||Export QoS|/qos/export|Export dữ liệu QoS<br>trong IPCC-<br>ContactCenter.||Cảnh<br>báo|Dữ liệu<br>backup<br>mỗi<br>ngày|
||BCCS2-Core||Insert<br>CDRReport|/cdrreport/insert|Insert dữ liệu<br>CDRReport trong<br>BCCS2-Core.||Lỗi<br>nghiêm<br>trọng|Kết nối<br>với hệ<br>thống<br>Billing|
||BCCS2-Core||Update<br>APIGateway|/apigateway/update|Update dữ liệu<br>APIGateway trong<br>BCCS2-Core.||Tự<br>động<br>retry|Chỉ<br>dùng<br>cho<br>admin|
||Infra-Server||Export<br>TransactionLog|/transactionlog/export|Export dữ liệu<br>TransactionLog<br>trong Infra-Server.||Cảnh<br>báo|Theo<br>chuẩn|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
|||||||||ISO<br>27001|
||Infra-Server||Update Contact|/contact/update|Update dữ liệu<br>Contact trong Infra-<br>Server.||Cảnh<br>báo|Theo<br>quy<br>định<br>Viettel|
||CRM-<br>Platform||Insert<br>CDRReport|/cdrreport/insert|Insert dữ liệu<br>CDRReport trong<br>CRM-Platform.||Thành<br>công|Bảo<br>mật 2<br>lớp|
||BCCS2-Core||Export<br>KPIReport|/kpireport/export|Export dữ liệu<br>KPIReport trong<br>BCCS2-Core.||Hiển<br>thị báo<br>cáo|Tích<br>hợp với<br>CRM|
||IVR-System||Monitor<br>APIGateway|/apigateway/monitor|Monitor dữ liệu<br>APIGateway trong<br>IVR-System.||Ghi log<br>đầy đủ|Theo<br>quy<br>định<br>Viettel|
||Security-<br>Firewall||Import Queue|/queue/import|Import dữ liệu<br>Queue trong<br>Security-Firewall.||Cảnh<br>báo|Bảo<br>mật 2<br>lớp|
||BCCS2-Core||Import Queue|/queue/import|Import dữ liệu<br>Queue trong<br>BCCS2-Core.||Đồng<br>bộ dữ<br>liệu|Chạy<br>theo<br>lịch<br>cron|
||IVR-System||Analyze<br>Campaign|/campaign/analyze|Analyze dữ liệu<br>Campaign trong<br>IVR-System.||Ghi log<br>đầy đủ|Chỉ<br>dùng<br>cho<br>admin|
||Security-<br>Firewall||Generate<br>APIGateway|/apigateway/generate|Generate dữ liệu<br>APIGateway trong<br>Security-Firewall.||Đồng<br>bộ dữ<br>liệu|Kết nối<br>với hệ|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
|||||||||thống<br>Billing|
||CRM-<br>Platform||Monitor<br>Promotion|/promotion/monitor|Monitor dữ liệu<br>Promotion trong<br>CRM-Platform.||Cảnh<br>báo|Tích<br>hợp với<br>CRM|
||Security-<br>Firewall||Monitor<br>Whitelist|/whitelist/monitor|Monitor dữ liệu<br>Whitelist trong<br>Security-Firewall.||Thông<br>báo<br>qua<br>SMS|Theo<br>chuẩn<br>ISO<br>27001|
||IPCC-<br>ContactCenter||Delete<br>PackagePlan|/packageplan/delete|Delete dữ liệu<br>PackagePlan trong<br>IPCC-<br>ContactCenter.||Thành<br>công|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||IVR-System||Insert<br>DebtControl|/debtcontrol/insert|Insert dữ liệu<br>DebtControl trong<br>IVR-System.||Lỗi<br>nghiêm<br>trọng|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Server||Optimize<br>Whitelist|/whitelist/optimize|Optimize dữ liệu<br>Whitelist trong<br>Infra-Server.||Tự<br>động<br>retry|Dữ liệu<br>backup<br>mỗi<br>ngày|
||Infra-Network||Monitor<br>Promotion|/promotion/monitor|Monitor dữ liệu<br>Promotion trong<br>Infra-Network.||Hiển<br>thị báo<br>cáo|Kết nối<br>với hệ<br>thống<br>Billing|
||BCCS2-Core||Import<br>IVRPrompt|/ivrprompt/import|Import dữ liệu<br>IVRPrompt trong<br>BCCS2-Core.||Không<br>lỗi|Theo<br>chuẩn<br>ISO<br>27001|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||IVR-System||Validate<br>TransactionLog|/transactionlog/validate|Validate dữ liệu<br>TransactionLog<br>trong IVR-System.||Ghi log<br>đầy đủ|Chạy<br>theo<br>lịch<br>cron|
||BCCS2-Core||Import<br>CustomerProfile|/customerprofile/import|Import dữ liệu<br>CustomerProfile<br>trong BCCS2-Core.||Lỗi<br>nghiêm<br>trọng|Dữ liệu<br>backup<br>mỗi<br>ngày|
||BCCS2-<br>Billing||Optimize QoS|/qos/optimize|Optimize dữ liệu<br>QoS trong BCCS2-<br>Billing.||Cảnh<br>báo|Theo<br>quy<br>định<br>Viettel|
||BCCS2-Core||Schedule Queue|/queue/schedule|Schedule dữ liệu<br>Queue trong<br>BCCS2-Core.||Cảnh<br>báo|Có cơ<br>chế<br>rollback|
||CRM-<br>Platform||Optimize<br>ClusterNode|/clusternode/optimize|Optimize dữ liệu<br>ClusterNode trong<br>CRM-Platform.||Lỗi<br>nghiêm<br>trọng|Chạy<br>theo<br>lịch<br>cron|
||CRM-<br>Platform||Delete<br>FirewallPolicy|/firewallpolicy/delete|Delete dữ liệu<br>FirewallPolicy trong<br>CRM-Platform.||Tự<br>động<br>retry|Chỉ<br>dùng<br>cho<br>admin|
||Infra-Server||Export<br>Whitelist|/whitelist/export|Export dữ liệu<br>Whitelist trong<br>Infra-Server.||Thành<br>công|Chạy<br>theo<br>lịch<br>cron|
||Infra-Server||Import<br>CDRReport|/cdrreport/import|Import dữ liệu<br>CDRReport trong<br>Infra-Server.||Đồng<br>bộ dữ<br>liệu|Tích<br>hợp với<br>CRM|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Infra-Server||Update<br>KPIReport|/kpireport/update|Update dữ liệu<br>KPIReport trong<br>Infra-Server.||Tự<br>động<br>retry|Có cơ<br>chế<br>rollback|
||BCCS2-<br>Billing||Config Lead|/lead/config|Config dữ liệu Lead<br>trong BCCS2-<br>Billing.||Đồng<br>bộ dữ<br>liệu|Có cơ<br>chế<br>rollback|
||CRM-<br>Platform||Analyze<br>Blacklist|/blacklist/analyze|Analyze dữ liệu<br>Blacklist trong<br>CRM-Platform.||Cảnh<br>báo|Chạy<br>theo<br>lịch<br>cron|
||QA-<br>Automation||Update<br>Whitelist|/whitelist/update|Update dữ liệu<br>Whitelist trong QA-<br>Automation.||Thông<br>báo<br>qua<br>SMS|Tích<br>hợp với<br>CRM|
||IPCC-<br>ContactCenter||Monitor Invoice|/invoice/monitor|Monitor dữ liệu<br>Invoice trong IPCC-<br>ContactCenter.||Ghi log<br>đầy đủ|Bảo<br>mật 2<br>lớp|
||CRM-<br>Platform||Export Invoice|/invoice/export|Export dữ liệu<br>Invoice trong CRM-<br>Platform.||Lỗi<br>nghiêm<br>trọng|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Server||Import<br>KPIReport|/kpireport/import|Import dữ liệu<br>KPIReport trong<br>Infra-Server.||Tự<br>động<br>retry|Chạy<br>theo<br>lịch<br>cron|
||QA-<br>Automation||Validate Lead|/lead/validate|Validate dữ liệu<br>Lead trong QA-<br>Automation.||Thành<br>công|Chỉ<br>dùng<br>cho<br>admin|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Infra-Server||Update VPN|/vpn/update|Update dữ liệu VPN<br>trong Infra-Server.||Thông<br>báo<br>qua<br>email|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Network||Search VPN|/vpn/search|Search dữ liệu VPN<br>trong Infra-Network.||Thông<br>báo<br>qua<br>email|Chạy<br>theo<br>lịch<br>cron|
||BCCS2-<br>Billing||Export<br>APIGateway|/apigateway/export|Export dữ liệu<br>APIGateway trong<br>BCCS2-Billing.||Đồng<br>bộ dữ<br>liệu|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Network||Import<br>KPIReport|/kpireport/import|Import dữ liệu<br>KPIReport trong<br>Infra-Network.||Thông<br>báo<br>qua<br>email|Kết nối<br>với hệ<br>thống<br>Billing|
||Security-<br>Firewall||Export<br>APIGateway|/apigateway/export|Export dữ liệu<br>APIGateway trong<br>Security-Firewall.||Tự<br>động<br>retry|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Server||Schedule<br>Blacklist|/blacklist/schedule|Schedule dữ liệu<br>Blacklist trong Infra-<br>Server.||Hiển<br>thị báo<br>cáo|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||QA-<br>Automation||Schedule<br>Blacklist|/blacklist/schedule|Schedule dữ liệu<br>Blacklist trong QA-<br>Automation.||Tự<br>động<br>retry|Tích<br>hợp với<br>CRM|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||Infra-Server||Monitor<br>CustomerProfile|/customerprofile/monitor|Monitor dữ liệu<br>CustomerProfile<br>trong Infra-Server.||Đồng<br>bộ dữ<br>liệu|Chỉ<br>dùng<br>cho<br>admin|
||IVR-System||Generate<br>PackagePlan|/packageplan/generate|Generate dữ liệu<br>PackagePlan trong<br>IVR-System.||Thông<br>báo<br>qua<br>SMS|Có cơ<br>chế<br>rollback|
||BCCS2-Core||Optimize<br>IVRPrompt|/ivrprompt/optimize|Optimize dữ liệu<br>IVRPrompt trong<br>BCCS2-Core.||Đồng<br>bộ dữ<br>liệu|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Network||Delete Whitelist|/whitelist/delete|Delete dữ liệu<br>Whitelist trong<br>Infra-Network.||Lỗi<br>nghiêm<br>trọng|Theo<br>chuẩn<br>ISO<br>27001|
||Infra-Server||Delete<br>PackagePlan|/packageplan/delete|Delete dữ liệu<br>PackagePlan trong<br>Infra-Server.||Không<br>lỗi|Theo<br>chuẩn<br>ISO<br>27001|
||RPA-Engine||Update<br>IVRPrompt|/ivrprompt/update|Update dữ liệu<br>IVRPrompt trong<br>RPA-Engine.||Thông<br>báo<br>qua<br>SMS|Theo<br>quy<br>định<br>Viettel|
||IVR-System||Generate<br>Blacklist|/blacklist/generate|Generate dữ liệu<br>Blacklist trong IVR-<br>System.||Thành<br>công|Kết nối<br>với hệ<br>thống<br>Billing|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||RPA-Engine||Analyze<br>CDRReport|/cdrreport/analyze|Analyze dữ liệu<br>CDRReport trong<br>RPA-Engine.||Hiển<br>thị báo<br>cáo|Tích<br>hợp với<br>CRM|
||IPCC-<br>ContactCenter||Search Contact|/contact/search|Search dữ liệu<br>Contact trong IPCC-<br>ContactCenter.||Thành<br>công|Chỉ<br>dùng<br>cho<br>admin|
||IVR-System||Analyze<br>FirewallPolicy|/firewallpolicy/analyze|Analyze dữ liệu<br>FirewallPolicy trong<br>IVR-System.||Không<br>lỗi|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Network||Search<br>IVRPrompt|/ivrprompt/search|Search dữ liệu<br>IVRPrompt trong<br>Infra-Network.||Thông<br>báo<br>qua<br>email|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||Infra-Network||Schedule VPN|/vpn/schedule|Schedule dữ liệu<br>VPN trong Infra-<br>Network.||Hiển<br>thị báo<br>cáo|Chỉ<br>dùng<br>cho<br>admin|
||IVR-System||Monitor<br>TransactionLog|/transactionlog/monitor|Monitor dữ liệu<br>TransactionLog<br>trong IVR-System.||Tự<br>động<br>retry|Yêu<br>cầu xác<br>thực<br>người<br>dùng|
||QA-<br>Automation||Monitor<br>StorageVolume|/storagevolume/monitor|Monitor dữ liệu<br>StorageVolume<br>trong QA-<br>Automation.||Thông<br>báo<br>qua<br>email|Tích<br>hợp với<br>CRM|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD444|TD444|TD444|
|---|---|---|---|---|---|---|---|---|
||||**DANH**|**MỤC CHỨC NĂNG BCCS2**||Lần ban hành: 1|||
||||||||||
||BCCS2-<br>Billing||Insert<br>FirewallPolicy|/firewallpolicy/insert|Insert dữ liệu<br>FirewallPolicy trong<br>BCCS2-Billing.||Thông<br>báo<br>qua<br>email|Dữ liệu<br>backup<br>mỗi<br>ngày|
||RPA-Engine||Optimize<br>Campaign|/campaign/optimize|Optimize dữ liệu<br>Campaign trong<br>RPA-Engine.||Tự<br>động<br>retry|Dữ liệu<br>backup<br>mỗi<br>ngày|