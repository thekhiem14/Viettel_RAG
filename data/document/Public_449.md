**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|Module|Loại log|Mức độ|Hành<br>động|Mô tả chi tiết|Kết quả|Ghi chú|
|---|---|---|---|---|---|---|
|RPA|TransactionLog|Critical|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Gửi log sang<br>ELK|
|CRM|TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Theo chuẩn<br>syslog<br>RFC5424|
|Billing|PerformanceLog|Error|Phân<br>tích<br>log|Hệ thống Billing<br>Phân tích log loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Có dashboard<br>Grafana|
|Infra|TransactionLog|Critical|Xóa<br>log|Hệ thống Infra Xóa<br>log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Theo chuẩn<br>syslog<br>RFC5424|
|QA|AuditLog|Warning|Xuất|Hệ thống QA Xuất|Không|Có dashboard|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Grafana<br>Có dashboard<br>Grafana<br>Có dashboard<br>Grafana<br>Tự động xóa<br>log sau 180<br>ngày<br>Theo chuẩn<br>syslog<br>RFC5424<br>Theo chuẩn<br>syslog|
||||||log|log loại AuditLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|mất mát<br>dữ liệu||Grafana|
||IPCC||PerformanceLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Có dashboard<br>Grafana|
||IPCC||ErrorLog|Info|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>ErrorLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Có dashboard<br>Grafana|
||Billing||ErrorLog|Warning|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần||Tự động xóa<br>log sau 180<br>ngày|
||CRM||AuditLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống CRM<br>Gửi log sang SIEM<br>loại AuditLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Theo chuẩn<br>syslog<br>RFC5424|
||Infra||AuditLog|Error|Gửi<br>log|Hệ thống Infra Gửi<br>logsangSIEM loại|Không<br>mất mát||Theo chuẩn<br>syslog|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||RFC5424<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết<br>Phân quyền chi<br>tiết<br>Gửi log sang<br>ELK|
||||||sang<br>SIEM|AuditLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|dữ liệu||RFC5424|
||RPA||PerformanceLog|Fatal|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Tự động xóa<br>log sau 180<br>ngày|
||QA||AccessLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>AccessLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Tự động xóa<br>log sau 180<br>ngày|
||Billing||ErrorLog|Info|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>ErrorLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Phân quyền chi<br>tiết|
||IVR||TransactionLog|Fatal|Xóa<br>log|Hệ thống IVR Xóa<br>log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Phân quyền chi<br>tiết|
||IVR||PerformanceLog|Error|Xóa<br>log|Hệ thống IVR Xóa<br>log loại<br>PerformanceLog|Có chỉ<br>số<br>thống||Gửi log sang<br>ELK|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Theo chuẩn<br>syslog<br>RFC5424<br>Gửi log sang<br>ELK<br>Phân quyền chi<br>tiết<br>Gửi log sang<br>ELK<br>Phân quyền chi<br>tiết|
|||||||với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|kê|||
||IPCC||AuditLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại AuditLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần||Theo chuẩn<br>syslog<br>RFC5424|
||Infra||AccessLog|Warning|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||QA||AccessLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Phân quyền chi<br>tiết|
||Infra||ErrorLog|Critical|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần||Gửi log sang<br>ELK|
||QA||AuditLog|Error|Xóa<br>log|Hệ thống QA Xóa<br>log loại AuditLog<br>với mức Error, dữ<br>liệu lưu trữ tối|Tích<br>hợp<br>cảnh<br>báo||Phân quyền chi<br>tiết|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|||||thiểu 90 ngày.|realtime||
|---|---|---|---|---|---|---|
|CRM|AuditLog|Fatal|Xóa<br>log|Hệ thống CRM<br>Xóa log loại<br>AuditLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê|Phân quyền chi<br>tiết|
|CRM|PerformanceLog|Warning|Xuất<br>log|Hệ thống CRM<br>Xuất log loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Theo chuẩn<br>syslog<br>RFC5424|
|Infra|TransactionLog|Critical|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Tự động xóa<br>log sau 180<br>ngày|
|IPCC|TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Phân quyền chi<br>tiết|
|IPCC|PerformanceLog|Fatal|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối|Có chỉ<br>số<br>thống<br>kê|Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424<br>Có dashboard<br>Grafana<br>Tự động xóa<br>log sau 180<br>ngày<br>Theo chuẩn|
|||||||thiểu 90 ngày.||||
||Billing||AccessLog|Fatal|Phân<br>tích<br>log|Hệ thống Billing<br>Phân tích log loại<br>AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Tự động xóa<br>log sau 180<br>ngày|
||RPA||ErrorLog|Fatal|Xóa<br>log|Hệ thống RPA Xóa<br>log loại ErrorLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Có dashboard<br>Grafana|
||Infra||TransactionLog|Info|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Theo chuẩn<br>syslog<br>RFC5424|
||IVR||ErrorLog|Warning|Xuất<br>log|Hệ thống IVR Xuất<br>log loại ErrorLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Có dashboard<br>Grafana|
||QA||AuditLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>AuditLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||Infra||PerformanceLog|Critical|Phân|Hệ thống Infra|Có chỉ||Theo chuẩn|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

||||tích<br>log|Phân tích log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|số<br>thống<br>kê|syslog<br>RFC5424|
|---|---|---|---|---|---|---|
|QA|AuditLog|Critical|Xuất<br>log|Hệ thống QA Xuất<br>log loại AuditLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Gửi log sang<br>ELK|
|IPCC|TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Gửi log sang<br>ELK|
|RPA|PerformanceLog|Critical|Phân<br>tích<br>log|Hệ thống RPA<br>Phân tích log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Có dashboard<br>Grafana|
|Infra|AuditLog|Info|Xóa<br>log|Hệ thống Infra Xóa<br>log loại AuditLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Có dashboard<br>Grafana|
|RPA|ErrorLog|Fatal|Xóa<br>log|Hệ thống RPA Xóa<br>log loại ErrorLog<br>với mức Fatal,dữ|Tích<br>hợp<br>cảnh|Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Phân quyền chi<br>tiết<br>Gửi log sang<br>ELK<br>Gửi log sang<br>ELK<br>Theo chuẩn<br>syslog<br>RFC5424<br>Gửi log sang<br>ELK|
|||||||liệu lưu trữ tối<br>thiểu 90 ngày.|báo<br>realtime|||
||Billing||ErrorLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống Billing<br>Gửi log sang SIEM<br>loại ErrorLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Phân quyền chi<br>tiết|
||CRM||PerformanceLog|Critical|Gửi<br>log<br>sang<br>SIEM|Hệ thống CRM<br>Gửi log sang SIEM<br>loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||Billing||TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||CRM||TransactionLog|Error|Phân<br>tích<br>log|Hệ thống CRM<br>Phân tích log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Theo chuẩn<br>syslog<br>RFC5424|
||IVR||AuditLog|Critical|Xuất<br>log|Hệ thống IVR Xuất<br>log loại AuditLog<br>với mức Critical,|Không<br>mất mát||Gửi log sang<br>ELK|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Theo chuẩn<br>syslog<br>RFC5424|
|||||||dữ liệu lưu trữ tối<br>thiểu 90 ngày.|dữ liệu|||
||CRM||ErrorLog|Info|Xuất<br>log|Hệ thống CRM<br>Xuất log loại<br>ErrorLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||IPCC||ErrorLog|Fatal|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>ErrorLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||QA||AuditLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>AuditLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Tự động xóa<br>log sau 180<br>ngày|
||CRM||TransactionLog|Critical|Gửi<br>log<br>sang<br>SIEM|Hệ thống CRM<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Tự động xóa<br>log sau 180<br>ngày|
||Infra||ErrorLog|Warning|Nén<br>và<br>lưu<br>trữ|Hệ thống Infra Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Warning,dữ liệu|Log<br>được<br>mã hóa<br>AES-||Theo chuẩn<br>syslog<br>RFC5424|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Theo chuẩn<br>syslog<br>RFC5424<br>Gửi log sang<br>ELK<br>Phân quyền chi<br>tiết<br>Theo chuẩn<br>syslog<br>RFC5424<br>Có dashboard<br>Grafana|
||||||log|lưu trữ tối thiểu 90<br>ngày.|256|||
||RPA||TransactionLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Theo chuẩn<br>syslog<br>RFC5424|
||QA||ErrorLog|Error|Xuất<br>log|Hệ thống QA Xuất<br>log loại ErrorLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Gửi log sang<br>ELK|
||QA||AccessLog|Info|Xuất<br>log|Hệ thống QA Xuất<br>log loại AccessLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Phân quyền chi<br>tiết|
||CRM||AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống CRM<br>Gửi log sang SIEM<br>loại AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Theo chuẩn<br>syslog<br>RFC5424|
||Billing||PerformanceLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Có dashboard<br>Grafana|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Có dashboard<br>Grafana<br>Có dashboard<br>Grafana<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày|
|||||||thiểu 90 ngày.||||
||IPCC||AccessLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại AccessLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Có dashboard<br>Grafana|
||Billing||AuditLog|Warning|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>AuditLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Có dashboard<br>Grafana|
||Billing||AuditLog|Error|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>AuditLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||Billing||AccessLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||CRM||AccessLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|||||thiểu 90 ngày.|||
|---|---|---|---|---|---|---|
|Infra|AccessLog|Fatal|Phân<br>tích<br>log|Hệ thống Infra<br>Phân tích log loại<br>AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Có dashboard<br>Grafana|
|IPCC|TransactionLog|Info|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Tự động xóa<br>log sau 180<br>ngày|
|QA|AccessLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>AccessLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê|Có dashboard<br>Grafana|
|IPCC|ErrorLog|Error|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>ErrorLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Gửi log sang<br>ELK|
|Infra|ErrorLog|Critical|Phân<br>tích<br>log|Hệ thống Infra<br>Phân tích log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90|Không<br>mất mát<br>dữ liệu|Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424<br>Gửi log sang<br>ELK<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày|
|||||||ngày.||||
||IVR||AccessLog|Warning|Phân<br>tích<br>log|Hệ thống IVR<br>Phân tích log loại<br>AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Có dashboard<br>Grafana|
||IVR||TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IVR Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Theo chuẩn<br>syslog<br>RFC5424|
||QA||ErrorLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>ErrorLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||RPA||TransactionLog|Fatal|Phân<br>tích<br>log|Hệ thống RPA<br>Phân tích log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||Billing||AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống Billing<br>Gửi log sang SIEM<br>loại AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|||||ngày.|||
|---|---|---|---|---|---|---|
|CRM|TransactionLog|Info|Phân<br>tích<br>log|Hệ thống CRM<br>Phân tích log loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Gửi log sang<br>ELK|
|Billing|ErrorLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại ErrorLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê|Theo chuẩn<br>syslog<br>RFC5424|
|RPA|TransactionLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống RPA Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Gửi log sang<br>ELK|
|Infra|ErrorLog|Info|Xóa<br>log|Hệ thống Infra Xóa<br>log loại ErrorLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Có dashboard<br>Grafana|
|IVR|ErrorLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IVR Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Theo chuẩn<br>syslog<br>RFC5424|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Phân quyền chi<br>tiết<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424<br>Theo chuẩn<br>syslog<br>RFC5424<br>Có dashboard<br>Grafana<br>Phân quyền chi<br>tiết|
||IPCC||AuditLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại AuditLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Phân quyền chi<br>tiết|
||QA||TransactionLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Có dashboard<br>Grafana|
||Infra||AuditLog|Warning|Xóa<br>log|Hệ thống Infra Xóa<br>log loại AuditLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Theo chuẩn<br>syslog<br>RFC5424|
||IVR||ErrorLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống IVR Gửi<br>log sang SIEM loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Theo chuẩn<br>syslog<br>RFC5424|
||IVR||AuditLog|Fatal|Xuất<br>log|Hệ thống IVR Xuất<br>log loại AuditLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Có dashboard<br>Grafana|
||Infra||PerformanceLog|Info|Nén<br>và<br>lưu|Hệ thống Infra Nén<br>và lưu trữ log loại<br>PerformanceLog|Không<br>mất mát||Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Gửi log sang<br>ELK<br>Có dashboard<br>Grafana<br>Phân quyền chi<br>tiết<br>Tự động xóa<br>log sau 180<br>ngày<br>Theo chuẩn<br>syslog|
||||||trữ<br>log|với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|dữ liệu|||
||Billing||PerformanceLog|Error|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||CRM||TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Có dashboard<br>Grafana|
||QA||TransactionLog|Fatal|Xuất<br>log|Hệ thống QA Xuất<br>log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Phân quyền chi<br>tiết|
||RPA||TransactionLog|Critical|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||QA||TransactionLog|Critical|Phân<br>tích|Hệ thống QA Phân<br>tích log loại<br>TransactionLog|Có chỉ<br>số<br>thống||Theo chuẩn<br>syslog|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||RFC5424<br>Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết<br>Gửi log sang<br>ELK<br>Có dashboard<br>Grafana<br>Phân quyền chi<br>tiết|
||||||log|với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|kê||RFC5424|
||CRM||AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống CRM<br>Gửi log sang SIEM<br>loại AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Tự động xóa<br>log sau 180<br>ngày|
||Billing||PerformanceLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Phân quyền chi<br>tiết|
||QA||TransactionLog|Error|Xuất<br>log|Hệ thống QA Xuất<br>log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||Billing||AccessLog|Info|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>AccessLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Có dashboard<br>Grafana|
||CRM||AuditLog|Warning|Nén<br>và<br>lưu|Hệ thống CRM<br>Nén và lưu trữ log<br>loại AuditLogvới|Có chỉ<br>số<br>thống||Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Gửi log sang<br>ELK<br>Gửi log sang<br>ELK<br>Phân quyền chi<br>tiết|
||||||trữ<br>log|mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|kê|||
||Billing||AccessLog|Info|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>AccessLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||IVR||AccessLog|Error|Xóa<br>log|Hệ thống IVR Xóa<br>log loại AccessLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||IVR||AccessLog|Error|Xóa<br>log|Hệ thống IVR Xóa<br>log loại AccessLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Gửi log sang<br>ELK|
||Billing||TransactionLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Gửi log sang<br>ELK|
||Billing||TransactionLog|Error|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối|Log<br>được<br>mã hóa<br>AES-||Phân quyền chi<br>tiết|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|||||thiểu 90 ngày.|256||
|---|---|---|---|---|---|---|
|Infra|AccessLog|Info|Xóa<br>log|Hệ thống Infra Xóa<br>log loại AccessLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Gửi log sang<br>ELK|
|RPA|ErrorLog|Critical|Xóa<br>log|Hệ thống RPA Xóa<br>log loại ErrorLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Gửi log sang<br>ELK|
|Billing|TransactionLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Theo chuẩn<br>syslog<br>RFC5424|
|Infra|PerformanceLog|Fatal|Xóa<br>log|Hệ thống Infra Xóa<br>log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Có dashboard<br>Grafana|
|Infra|TransactionLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống Infra Gửi<br>log sang SIEM loại<br>TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Phân quyền chi<br>tiết|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|IPCC|PerformanceLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Phân quyền chi<br>tiết|
|---|---|---|---|---|---|---|
|IPCC|TransactionLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Có dashboard<br>Grafana|
|RPA|AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê|Gửi log sang<br>ELK|
|IVR|AccessLog|Critical|Phân<br>tích<br>log|Hệ thống IVR<br>Phân tích log loại<br>AccessLog với<br>mức Critical, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Phân quyền chi<br>tiết|
|Billing|AuditLog|Critical|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>AuditLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90|Có chỉ<br>số<br>thống<br>kê|Gửi log sang<br>ELK|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Có dashboard<br>Grafana<br>Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết<br>Tự động xóa<br>log sau 180<br>ngày<br>Gửi log sang<br>ELK|
|||||||ngày.||||
||QA||AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Có dashboard<br>Grafana|
||Billing||TransactionLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống Billing<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Tự động xóa<br>log sau 180<br>ngày|
||Billing||AccessLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Phân quyền chi<br>tiết|
||IPCC||ErrorLog|Error|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>ErrorLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||RPA||TransactionLog|Critical|Phân<br>tích<br>log|Hệ thống RPA<br>Phân tích log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối|Có thể<br>truy<br>xuất khi<br>cần||Gửi log sang<br>ELK|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|||||thiểu 90 ngày.|||
|---|---|---|---|---|---|---|
|Billing|AuditLog|Error|Phân<br>tích<br>log|Hệ thống Billing<br>Phân tích log loại<br>AuditLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê|Phân quyền chi<br>tiết|
|QA|TransactionLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Tự động xóa<br>log sau 180<br>ngày|
|CRM|AuditLog|Info|Phân<br>tích<br>log|Hệ thống CRM<br>Phân tích log loại<br>AuditLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Có dashboard<br>Grafana|
|QA|TransactionLog|Warning|Phân<br>tích<br>log|Hệ thống QA Phân<br>tích log loại<br>TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Phân quyền chi<br>tiết|
|Billing|TransactionLog|Fatal|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Gửi log sang<br>ELK|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày|
|||||||thiểu 90 ngày.||||
||Infra||AccessLog|Warning|Xóa<br>log|Hệ thống Infra Xóa<br>log loại AccessLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||Billing||TransactionLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống Billing<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Phân quyền chi<br>tiết|
||CRM||AccessLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại AccessLog với<br>mức Critical, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||QA||ErrorLog|Warning|Xóa<br>log|Hệ thống QA Xóa<br>log loại ErrorLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||Infra||TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Infra Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|IPCC|AuditLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại AuditLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Gửi log sang<br>ELK|
|---|---|---|---|---|---|---|
|QA|AccessLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê|Gửi log sang<br>ELK|
|CRM|PerformanceLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống CRM<br>Gửi log sang SIEM<br>loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Theo chuẩn<br>syslog<br>RFC5424|
|RPA|TransactionLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống RPA Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Có dashboard<br>Grafana|
|CRM|AuditLog|Warning|Phân<br>tích<br>log|Hệ thống CRM<br>Phân tích log loại<br>AuditLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Tự động xóa<br>log sau 180<br>ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|Infra|ErrorLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Infra Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Gửi log sang<br>ELK|
|---|---|---|---|---|---|---|
|RPA|PerformanceLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống RPA Nén<br>và lưu trữ log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Có dashboard<br>Grafana|
|IPCC|AuditLog|Warning|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>AuditLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Theo chuẩn<br>syslog<br>RFC5424|
|Billing|AccessLog|Info|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>AccessLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Theo chuẩn<br>syslog<br>RFC5424|
|Billing|AccessLog|Warning|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Theo chuẩn<br>syslog<br>RFC5424|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết<br>Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Phân quyền chi<br>tiết<br>Theo chuẩn<br>syslog|
||QA||TransactionLog|Warning|Xuất<br>log|Hệ thống QA Xuất<br>log loại<br>TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||IVR||AccessLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống IVR Gửi<br>log sang SIEM loại<br>AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Phân quyền chi<br>tiết|
||IVR||ErrorLog|Warning|Xóa<br>log|Hệ thống IVR Xóa<br>log loại ErrorLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Tự động xóa<br>log sau 180<br>ngày|
||IPCC||AuditLog|Fatal|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>AuditLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần||Có dashboard<br>Grafana|
||Infra||TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Infra Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Phân quyền chi<br>tiết|
||Infra||AuditLog|Error|Nén<br>và|Hệ thống Infra Nén<br>và lưu trữ logloại|Tích<br>hợp||Theo chuẩn<br>syslog|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||RFC5424<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424<br>Theo chuẩn<br>syslog|
||||||lưu<br>trữ<br>log|AuditLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|cảnh<br>báo<br>realtime||RFC5424|
||IPCC||PerformanceLog|Critical|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Tự động xóa<br>log sau 180<br>ngày|
||Infra||PerformanceLog|Warning|Phân<br>tích<br>log|Hệ thống Infra<br>Phân tích log loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||Infra||AccessLog|Fatal|Xóa<br>log|Hệ thống Infra Xóa<br>log loại AccessLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Có dashboard<br>Grafana|
||QA||PerformanceLog|Critical|Phân<br>tích<br>log|Hệ thống QA Phân<br>tích log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Theo chuẩn<br>syslog<br>RFC5424|
||Infra||PerformanceLog|Critical|Xóa<br>log|Hệ thống Infra Xóa<br>log loại<br>PerformanceLog|Có thể<br>truy<br>xuất khi||Theo chuẩn<br>syslog|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||RFC5424<br>Gửi log sang<br>ELK<br>Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết<br>Theo chuẩn<br>syslog<br>RFC5424<br>Theo chuẩn<br>syslog<br>RFC5424|
|||||||với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|cần||RFC5424|
||QA||PerformanceLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||RPA||ErrorLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống RPA Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||IPCC||ErrorLog|Critical|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần||Phân quyền chi<br>tiết|
||QA||AccessLog|Fatal|Xóa<br>log|Hệ thống QA Xóa<br>log loại AccessLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Theo chuẩn<br>syslog<br>RFC5424|
||RPA||AuditLog|Warning|Nén<br>và<br>lưu<br>trữ|Hệ thống RPA Nén<br>và lưu trữ log loại<br>AuditLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90|Log<br>được<br>mã hóa<br>AES-||Theo chuẩn<br>syslog<br>RFC5424|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

||||log|ngày.|256||
|---|---|---|---|---|---|---|
|QA|AuditLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>AuditLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Có dashboard<br>Grafana|
|CRM|PerformanceLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống CRM<br>Gửi log sang SIEM<br>loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Có dashboard<br>Grafana|
|RPA|TransactionLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Tự động xóa<br>log sau 180<br>ngày|
|Billing|AuditLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại AuditLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Tự động xóa<br>log sau 180<br>ngày|
|IPCC|AuditLog|Error|Nén<br>và<br>lưu<br>trữ|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại AuditLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90|Log<br>được<br>mã hóa<br>AES-|Gửi log sang<br>ELK|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

||||log|ngày.|256||
|---|---|---|---|---|---|---|
|IPCC|PerformanceLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Có dashboard<br>Grafana|
|IPCC|TransactionLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Gửi log sang<br>ELK|
|IVR|PerformanceLog|Warning|Phân<br>tích<br>log|Hệ thống IVR<br>Phân tích log loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Có dashboard<br>Grafana|
|Infra|AccessLog|Critical|Phân<br>tích<br>log|Hệ thống Infra<br>Phân tích log loại<br>AccessLog với<br>mức Critical, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Theo chuẩn<br>syslog<br>RFC5424|
|Billing|PerformanceLog|Warning|Nén<br>và<br>lưu<br>trữ|Hệ thống Billing<br>Nén và lưu trữ log<br>loại<br>PerformanceLog|Có thể<br>truy<br>xuất khi|Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Theo chuẩn<br>syslog<br>RFC5424<br>Có dashboard<br>Grafana<br>Tự động xóa<br>log sau 180<br>ngày<br>Gửi log sang<br>ELK<br>Tự động xóa<br>log sau 180<br>ngày|
||||||log|với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|cần|||
||QA||AccessLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Theo chuẩn<br>syslog<br>RFC5424|
||QA||PerformanceLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Có dashboard<br>Grafana|
||IPCC||PerformanceLog|Fatal|Xuất<br>log|Hệ thống IPCC<br>Xuất log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||Infra||AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống Infra Gửi<br>log sang SIEM loại<br>AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||IPCC||ErrorLog|Error|Gửi<br>log<br>sang|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại ErrorLog với<br>mức Error,dữ liệu|Có thể<br>truy<br>xuất khi||Tự động xóa<br>log sau 180<br>ngày|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Có dashboard<br>Grafana<br>Gửi log sang<br>ELK<br>Theo chuẩn<br>syslog<br>RFC5424<br>Phân quyền chi<br>tiết<br>Tự động xóa<br>log sau 180<br>ngày|
||||||SIEM|lưu trữ tối thiểu 90<br>ngày.|cần|||
||IVR||AuditLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IVR Nén<br>và lưu trữ log loại<br>AuditLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Có dashboard<br>Grafana|
||Billing||TransactionLog|Critical|Gửi<br>log<br>sang<br>SIEM|Hệ thống Billing<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||RPA||PerformanceLog|Critical|Phân<br>tích<br>log|Hệ thống RPA<br>Phân tích log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Theo chuẩn<br>syslog<br>RFC5424|
||IPCC||AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Phân quyền chi<br>tiết|
||Infra||AuditLog|Critical|Nén<br>và<br>lưu<br>trữ|Hệ thống Infra Nén<br>và lưu trữ log loại<br>AuditLog với mức<br>Critical,dữ liệu lưu|Tích<br>hợp<br>cảnh<br>báo||Tự động xóa<br>log sau 180<br>ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

||||log|trữ tối thiểu 90<br>ngày.|realtime||
|---|---|---|---|---|---|---|
|Billing|AccessLog|Error|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>AccessLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Phân quyền chi<br>tiết|
|QA|AuditLog|Critical|Xuất<br>log|Hệ thống QA Xuất<br>log loại AuditLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Theo chuẩn<br>syslog<br>RFC5424|
|QA|PerformanceLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Phân quyền chi<br>tiết|
|Infra|ErrorLog|Error|Xóa<br>log|Hệ thống Infra Xóa<br>log loại ErrorLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Tự động xóa<br>log sau 180<br>ngày|
|CRM|AccessLog|Info|Xóa<br>log|Hệ thống CRM<br>Xóa log loại<br>AccessLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Tự động xóa<br>log sau 180<br>ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|IPCC|AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Gửi log sang<br>ELK|
|---|---|---|---|---|---|---|
|QA|AuditLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>AuditLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Tự động xóa<br>log sau 180<br>ngày|
|RPA|ErrorLog|Fatal|Xóa<br>log|Hệ thống RPA Xóa<br>log loại ErrorLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Theo chuẩn<br>syslog<br>RFC5424|
|CRM|TransactionLog|Info|Xuất<br>log|Hệ thống CRM<br>Xuất log loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Gửi log sang<br>ELK|
|Infra|PerformanceLog|Info|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>PerformanceLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Theo chuẩn<br>syslog<br>RFC5424|
|Infra|TransactionLog|Warning|Gửi<br>log|Hệ thống Infra Gửi<br>logsangSIEM loại|Tích<br>hợp|Theo chuẩn<br>syslog|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

||||sang<br>SIEM|TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|cảnh<br>báo<br>realtime|RFC5424|
|---|---|---|---|---|---|---|
|IVR|AuditLog|Warning|Xuất<br>log|Hệ thống IVR Xuất<br>log loại AuditLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Tự động xóa<br>log sau 180<br>ngày|
|Billing|ErrorLog|Warning|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Phân quyền chi<br>tiết|
|IPCC|PerformanceLog|Critical|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Tự động xóa<br>log sau 180<br>ngày|
|RPA|ErrorLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống RPA Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Gửi log sang<br>ELK|
|RPA|TransactionLog|Critical|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>TransactionLog<br>với mức Critical,|Không<br>mất mát<br>dữ liệu|Có dashboard<br>Grafana|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Phân quyền chi<br>tiết<br>Gửi log sang<br>ELK<br>Gửi log sang<br>ELK<br>Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết|
|||||||dữ liệu lưu trữ tối<br>thiểu 90 ngày.||||
||RPA||AuditLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống RPA Nén<br>và lưu trữ log loại<br>AuditLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Phân quyền chi<br>tiết|
||QA||ErrorLog|Fatal|Phân<br>tích<br>log|Hệ thống QA Phân<br>tích log loại<br>ErrorLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Gửi log sang<br>ELK|
||RPA||TransactionLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||RPA||ErrorLog|Warning|Phân<br>tích<br>log|Hệ thống RPA<br>Phân tích log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||CRM||PerformanceLog|Info|Xóa<br>log|Hệ thống CRM<br>Xóa log loại<br>PerformanceLog<br>với mức Info, dữ<br>liệu lưu trữ tối|Có chỉ<br>số<br>thống<br>kê||Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Theo chuẩn<br>syslog<br>RFC5424<br>Theo chuẩn<br>syslog<br>RFC5424<br>Gửi log sang<br>ELK<br>Phân quyền chi<br>tiết<br>Tự động xóa<br>log sau 180<br>ngày|
|||||||thiểu 90 ngày.||||
||Infra||AccessLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Infra Nén<br>và lưu trữ log loại<br>AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Theo chuẩn<br>syslog<br>RFC5424|
||IVR||ErrorLog|Critical|Phân<br>tích<br>log|Hệ thống IVR<br>Phân tích log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Theo chuẩn<br>syslog<br>RFC5424|
||Infra||PerformanceLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Infra Nén<br>và lưu trữ log loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||IPCC||TransactionLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Phân quyền chi<br>tiết|
||IPCC||ErrorLog|Error|Nén<br>và<br>lưu<br>trữ|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại ErrorLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

||||log|ngày.|||
|---|---|---|---|---|---|---|
|RPA|PerformanceLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Tự động xóa<br>log sau 180<br>ngày|
|Infra|ErrorLog|Critical|Xóa<br>log|Hệ thống Infra Xóa<br>log loại ErrorLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Gửi log sang<br>ELK|
|IVR|PerformanceLog|Critical|Gửi<br>log<br>sang<br>SIEM|Hệ thống IVR Gửi<br>log sang SIEM loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Theo chuẩn<br>syslog<br>RFC5424|
|Infra|AuditLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống Infra Gửi<br>log sang SIEM loại<br>AuditLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Theo chuẩn<br>syslog<br>RFC5424|
|IVR|ErrorLog|Critical|Xóa<br>log|Hệ thống IVR Xóa<br>log loại ErrorLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Phân quyền chi<br>tiết|
|QA|PerformanceLog|Fatal|Nén|Hệ thống QA Nén|Có thể|Tự động xóa|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||log sau 180<br>ngày<br>Gửi log sang<br>ELK<br>Phân quyền chi<br>tiết<br>Phân quyền chi<br>tiết<br>Tự động xóa<br>log sau 180<br>ngày<br>Gửi log sang<br>ELK|
||||||và<br>lưu<br>trữ<br>log|và lưu trữ log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|truy<br>xuất khi<br>cần||log sau 180<br>ngày|
||RPA||TransactionLog|Critical|Phân<br>tích<br>log|Hệ thống RPA<br>Phân tích log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Gửi log sang<br>ELK|
||RPA||PerformanceLog|Fatal|Xóa<br>log|Hệ thống RPA Xóa<br>log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Phân quyền chi<br>tiết|
||Billing||ErrorLog|Fatal|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>ErrorLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Phân quyền chi<br>tiết|
||RPA||AccessLog|Fatal|Xóa<br>log|Hệ thống RPA Xóa<br>log loại AccessLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||CRM||AccessLog|Warning|Xuất<br>log|Hệ thống CRM<br>Xuất log loại<br>AccessLogvới|Có thể<br>truy<br>xuất khi||Gửi log sang<br>ELK|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Tự động xóa<br>log sau 180<br>ngày<br>Gửi log sang<br>ELK<br>Phân quyền chi<br>tiết|
|||||||mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|cần|||
||IVR||PerformanceLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống IVR Gửi<br>log sang SIEM loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Tự động xóa<br>log sau 180<br>ngày|
||IPCC||PerformanceLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IPCC<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Có dashboard<br>Grafana|
||QA||TransactionLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||QA||AccessLog|Error|Phân<br>tích<br>log|Hệ thống QA Phân<br>tích log loại<br>AccessLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||RPA||AuditLog|Info|Phân<br>tích|Hệ thống RPA<br>Phân tích log loại<br>AuditLogvới mức|Có thể<br>truy<br>xuất khi||Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Có dashboard<br>Grafana<br>Gửi log sang<br>ELK<br>Gửi log sang<br>ELK<br>Gửi log sang<br>ELK<br>Có dashboard<br>Grafana|
||||||log|Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|cần|||
||Billing||ErrorLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại ErrorLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Có dashboard<br>Grafana|
||CRM||TransactionLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||Billing||TransactionLog|Fatal|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||CRM||TransactionLog|Error|Xuất<br>log|Hệ thống CRM<br>Xuất log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Gửi log sang<br>ELK|
||Infra||AccessLog|Warning|Gửi<br>log<br>sang|Hệ thống Infra Gửi<br>log sang SIEM loại<br>AccessLogvới|Có chỉ<br>số<br>thống||Có dashboard<br>Grafana|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Gửi log sang<br>ELK<br>Gửi log sang<br>ELK<br>Tự động xóa<br>log sau 180<br>ngày<br>Gửi log sang<br>ELK<br>Theo chuẩn<br>syslog<br>RFC5424|
||||||SIEM|mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|kê|||
||IPCC||AuditLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại AuditLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Gửi log sang<br>ELK|
||CRM||TransactionLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||IVR||AccessLog|Error|Xuất<br>log|Hệ thống IVR Xuất<br>log loại AccessLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Tự động xóa<br>log sau 180<br>ngày|
||CRM||TransactionLog|Critical|Xóa<br>log|Hệ thống CRM<br>Xóa log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Gửi log sang<br>ELK|
||Infra||TransactionLog|Fatal|Nén<br>và<br>lưu<br>trữ|Hệ thống Infra Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Fatal,dữ|Không<br>mất mát<br>dữ liệu||Theo chuẩn<br>syslog<br>RFC5424|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Gửi log sang<br>ELK<br>Gửi log sang<br>ELK<br>Tự động xóa<br>log sau 180<br>ngày<br>Gửi log sang<br>ELK<br>Gửi log sang<br>ELK|
||||||log|liệu lưu trữ tối<br>thiểu 90 ngày.||||
||IPCC||PerformanceLog|Critical|Xuất<br>log|Hệ thống IPCC<br>Xuất log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||Billing||TransactionLog|Fatal|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Gửi log sang<br>ELK|
||Infra||AccessLog|Fatal|Xóa<br>log|Hệ thống Infra Xóa<br>log loại AccessLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Tự động xóa<br>log sau 180<br>ngày|
||IPCC||TransactionLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||IPCC||AccessLog|Error|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>AccessLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Gửi log sang<br>ELK<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424|
|||||||ngày.||||
||Infra||PerformanceLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống Infra Gửi<br>log sang SIEM loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||IPCC||PerformanceLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại<br>PerformanceLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||Billing||AccessLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại AccessLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||Billing||PerformanceLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống Billing<br>Gửi log sang SIEM<br>loại<br>PerformanceLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Có dashboard<br>Grafana|
||CRM||ErrorLog|Fatal|Xuất<br>log|Hệ thống CRM<br>Xuất log loại<br>ErrorLog với mức<br>Fatal,dữ liệu lưu|Có chỉ<br>số<br>thống||Theo chuẩn<br>syslog<br>RFC5424|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|||||trữ tối thiểu 90<br>ngày.|kê||
|---|---|---|---|---|---|---|
|Billing|ErrorLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại ErrorLog với<br>mức Critical, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Tự động xóa<br>log sau 180<br>ngày|
|CRM|ErrorLog|Critical|Phân<br>tích<br>log|Hệ thống CRM<br>Phân tích log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Có dashboard<br>Grafana|
|QA|AuditLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>AuditLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Có dashboard<br>Grafana|
|QA|PerformanceLog|Fatal|Phân<br>tích<br>log|Hệ thống QA Phân<br>tích log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Tự động xóa<br>log sau 180<br>ngày|
|Infra|TransactionLog|Critical|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối|Có chỉ<br>số<br>thống<br>kê|Tự động xóa<br>log sau 180<br>ngày|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Phân quyền chi<br>tiết<br>Phân quyền chi<br>tiết<br>Có dashboard<br>Grafana<br>Gửi log sang<br>ELK<br>Có dashboard<br>Grafana|
|||||||thiểu 90 ngày.||||
||CRM||AuditLog|Critical|Phân<br>tích<br>log|Hệ thống CRM<br>Phân tích log loại<br>AuditLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Phân quyền chi<br>tiết|
||Billing||AuditLog|Warning|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>AuditLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Phân quyền chi<br>tiết|
||IPCC||AccessLog|Warning|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Có dashboard<br>Grafana|
||Billing||PerformanceLog|Critical|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||RPA||AuditLog|Critical|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>AuditLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Có dashboard<br>Grafana|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Phân quyền chi<br>tiết<br>Có dashboard<br>Grafana<br>Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết<br>Theo chuẩn<br>syslog<br>RFC5424|
|||||||ngày.||||
||CRM||AuditLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại AuditLog với<br>mức Critical, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Phân quyền chi<br>tiết|
||RPA||AuditLog|Info|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>AuditLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần||Có dashboard<br>Grafana|
||RPA||ErrorLog|Critical|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||RPA||ErrorLog|Error|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>ErrorLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Phân quyền chi<br>tiết|
||QA||AuditLog|Critical|Xóa<br>log|Hệ thống QA Xóa<br>log loại AuditLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Theo chuẩn<br>syslog<br>RFC5424|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|IVR|AccessLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống IVR Gửi<br>log sang SIEM loại<br>AccessLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Phân quyền chi<br>tiết|
|---|---|---|---|---|---|---|
|QA|TransactionLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Tự động xóa<br>log sau 180<br>ngày|
|Infra|AccessLog|Critical|Phân<br>tích<br>log|Hệ thống Infra<br>Phân tích log loại<br>AccessLog với<br>mức Critical, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Theo chuẩn<br>syslog<br>RFC5424|
|RPA|ErrorLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>ErrorLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê|Gửi log sang<br>ELK|
|CRM|AccessLog|Warning|Gửi<br>log<br>sang<br>SIEM|Hệ thống CRM<br>Gửi log sang SIEM<br>loại AccessLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Có dashboard<br>Grafana|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Phân quyền chi<br>tiết<br>Theo chuẩn<br>syslog<br>RFC5424<br>Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Gửi log sang<br>ELK<br>Gửi log sang|
||RPA||TransactionLog|Error|Xóa<br>log|Hệ thống RPA Xóa<br>log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Phân quyền chi<br>tiết|
||RPA||ErrorLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>ErrorLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần||Theo chuẩn<br>syslog<br>RFC5424|
||RPA||AuditLog|Critical|Xóa<br>log|Hệ thống RPA Xóa<br>log loại AuditLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||CRM||ErrorLog|Warning|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại ErrorLog với<br>mức Warning, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Có dashboard<br>Grafana|
||Infra||TransactionLog|Info|Xóa<br>log|Hệ thống Infra Xóa<br>log loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||Billing||PerformanceLog|Info|Nén<br>và|Hệ thống Billing<br>Nén và lưu trữ log|Không<br>mất mát||Gửi log sang|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

||||lưu<br>trữ<br>log|loại<br>PerformanceLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|dữ liệu|ELK|
|---|---|---|---|---|---|---|
|Infra|PerformanceLog|Fatal|Phân<br>tích<br>log|Hệ thống Infra<br>Phân tích log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Phân quyền chi<br>tiết|
|IPCC|TransactionLog|Critical|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Gửi log sang<br>ELK|
|IPCC|PerformanceLog|Error|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Gửi log sang<br>ELK|
|Billing|ErrorLog|Warning|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Tự động xóa<br>log sau 180<br>ngày|
|IVR|ErrorLog|Fatal|Gửi<br>log|Hệ thống IVR Gửi<br>logsangSIEM loại|Log<br>được|Có dashboard|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Grafana<br>Theo chuẩn<br>syslog<br>RFC5424<br>Phân quyền chi<br>tiết<br>Có dashboard<br>Grafana<br>Gửi log sang<br>ELK<br>Theo chuẩn<br>syslog|
||||||sang<br>SIEM|ErrorLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|mã hóa<br>AES-<br>256||Grafana|
||CRM||PerformanceLog|Error|Xuất<br>log|Hệ thống CRM<br>Xuất log loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Theo chuẩn<br>syslog<br>RFC5424|
||Billing||TransactionLog|Critical|Xóa<br>log|Hệ thống Billing<br>Xóa log loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Phân quyền chi<br>tiết|
||QA||ErrorLog|Fatal|Phân<br>tích<br>log|Hệ thống QA Phân<br>tích log loại<br>ErrorLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Có dashboard<br>Grafana|
||Infra||AuditLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống Infra Gửi<br>log sang SIEM loại<br>AuditLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Gửi log sang<br>ELK|
||QA||AuditLog|Critical|Xuất<br>log|Hệ thống QA Xuất<br>log loại AuditLog<br>với mức Critical,|Có chỉ<br>số<br>thống||Theo chuẩn<br>syslog|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||RFC5424<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Gửi log sang<br>ELK<br>Theo chuẩn<br>syslog<br>RFC5424|
|||||||dữ liệu lưu trữ tối<br>thiểu 90 ngày.|kê||RFC5424|
||QA||PerformanceLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||Infra||TransactionLog|Info|Xóa<br>log|Hệ thống Infra Xóa<br>log loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||IVR||PerformanceLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống IVR Nén<br>và lưu trữ log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Có dashboard<br>Grafana|
||CRM||TransactionLog|Info|Xóa<br>log|Hệ thống CRM<br>Xóa log loại<br>TransactionLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần||Gửi log sang<br>ELK|
||CRM||AccessLog|Critical|Phân<br>tích<br>log|Hệ thống CRM<br>Phân tích log loại<br>AccessLog với<br>mức Critical, dữ<br>liệu lưu trữ tối|Log<br>được<br>mã hóa<br>AES-||Theo chuẩn<br>syslog<br>RFC5424|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|||||thiểu 90 ngày.|256||
|---|---|---|---|---|---|---|
|RPA|AccessLog|Error|Xóa<br>log|Hệ thống RPA Xóa<br>log loại AccessLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Có dashboard<br>Grafana|
|RPA|AuditLog|Info|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>AuditLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê|Gửi log sang<br>ELK|
|Infra|ErrorLog|Warning|Phân<br>tích<br>log|Hệ thống Infra<br>Phân tích log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Tự động xóa<br>log sau 180<br>ngày|
|CRM|PerformanceLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Có dashboard<br>Grafana|
|Billing|AuditLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại AuditLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90|Log<br>được<br>mã hóa<br>AES-<br>256|Phân quyền chi<br>tiết|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|||||ngày.|||
|---|---|---|---|---|---|---|
|IVR|TransactionLog|Error|Phân<br>tích<br>log|Hệ thống IVR<br>Phân tích log loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Tự động xóa<br>log sau 180<br>ngày|
|QA|TransactionLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Tự động xóa<br>log sau 180<br>ngày|
|Infra|AuditLog|Warning|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>AuditLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Phân quyền chi<br>tiết|
|IPCC|PerformanceLog|Info|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>PerformanceLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Tự động xóa<br>log sau 180<br>ngày|
|IVR|PerformanceLog|Critical|Phân<br>tích<br>log|Hệ thống IVR<br>Phân tích log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối|Có chỉ<br>số<br>thống<br>kê|Theo chuẩn<br>syslog<br>RFC5424|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Phân quyền chi<br>tiết<br>Theo chuẩn<br>syslog<br>RFC5424<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424<br>Phân quyền chi<br>tiết|
|||||||thiểu 90 ngày.||||
||Infra||ErrorLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Infra Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Phân quyền chi<br>tiết|
||QA||ErrorLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống QA Gửi<br>log sang SIEM loại<br>ErrorLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Theo chuẩn<br>syslog<br>RFC5424|
||IVR||ErrorLog|Fatal|Xóa<br>log|Hệ thống IVR Xóa<br>log loại ErrorLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Có dashboard<br>Grafana|
||Billing||ErrorLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống Billing<br>Gửi log sang SIEM<br>loại ErrorLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần||Theo chuẩn<br>syslog<br>RFC5424|
||Infra||TransactionLog|Fatal|Xóa<br>log|Hệ thống Infra Xóa<br>log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Phân quyền chi<br>tiết|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|Billing|TransactionLog|Fatal|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu|Gửi log sang<br>ELK|
|---|---|---|---|---|---|---|
|IPCC|ErrorLog|Warning|Xóa<br>log|Hệ thống IPCC<br>Xóa log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Phân quyền chi<br>tiết|
|IVR|AccessLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống IVR Gửi<br>log sang SIEM loại<br>AccessLog với<br>mức Error, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Gửi log sang<br>ELK|
|Infra|PerformanceLog|Fatal|Phân<br>tích<br>log|Hệ thống Infra<br>Phân tích log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Theo chuẩn<br>syslog<br>RFC5424|
|Infra|AuditLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống Infra Gửi<br>log sang SIEM loại<br>AuditLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Gửi log sang<br>ELK<br>Gửi log sang<br>ELK<br>Theo chuẩn<br>syslog<br>RFC5424<br>Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog|
||Infra||AccessLog|Warning|Xóa<br>log|Hệ thống Infra Xóa<br>log loại AccessLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||IVR||ErrorLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống IVR Gửi<br>log sang SIEM loại<br>ErrorLog với mức<br>Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Gửi log sang<br>ELK|
||Infra||ErrorLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Infra Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu||Theo chuẩn<br>syslog<br>RFC5424|
||QA||TransactionLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống QA Nén<br>và lưu trữ log loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Tự động xóa<br>log sau 180<br>ngày|
||RPA||AccessLog|Info|Xóa<br>log|Hệ thống RPA Xóa<br>log loại AccessLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Có dashboard<br>Grafana|
||RPA||ErrorLog|Error|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>ErrorLogvới mức|Có chỉ<br>số<br>thống||Theo chuẩn<br>syslog|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||RFC5424<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424<br>Phân quyền chi<br>tiết<br>Tự động xóa<br>log sau 180<br>ngày<br>Phân quyền chi<br>tiết|
|||||||Error, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|kê||RFC5424|
||Infra||ErrorLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Infra Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Có dashboard<br>Grafana|
||IPCC||TransactionLog|Critical|Gửi<br>log<br>sang<br>SIEM|Hệ thống IPCC<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Theo chuẩn<br>syslog<br>RFC5424|
||Infra||PerformanceLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống Infra Gửi<br>log sang SIEM loại<br>PerformanceLog<br>với mức Info, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Phân quyền chi<br>tiết|
||RPA||PerformanceLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống RPA Nén<br>và lưu trữ log loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|
||Billing||AuditLog|Critical|Xuất<br>log|Hệ thống Billing<br>Xuất log loại<br>AuditLogvới mức|Có chỉ<br>số<br>thống||Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Gửi log sang<br>ELK<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424<br>Theo chuẩn<br>syslog<br>RFC5424<br>Gửi log sang<br>ELK|
|||||||Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|kê|||
||IVR||AuditLog|Info|Gửi<br>log<br>sang<br>SIEM|Hệ thống IVR Gửi<br>log sang SIEM loại<br>AuditLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Gửi log sang<br>ELK|
||RPA||AuditLog|Warning|Xuất<br>log|Hệ thống RPA<br>Xuất log loại<br>AuditLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Có dashboard<br>Grafana|
||IPCC||AuditLog|Info|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>AuditLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Theo chuẩn<br>syslog<br>RFC5424|
||IVR||AccessLog|Fatal|Xuất<br>log|Hệ thống IVR Xuất<br>log loại AccessLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Theo chuẩn<br>syslog<br>RFC5424|
||RPA||ErrorLog|Warning|Nén<br>và<br>lưu<br>trữ|Hệ thống RPA Nén<br>và lưu trữ log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90|Tích<br>hợp<br>cảnh<br>báo||Gửi log sang<br>ELK|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

||||log|ngày.|realtime||
|---|---|---|---|---|---|---|
|QA|AuditLog|Warning|Xóa<br>log|Hệ thống QA Xóa<br>log loại AuditLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có thể<br>truy<br>xuất khi<br>cần|Tự động xóa<br>log sau 180<br>ngày|
|IPCC|ErrorLog|Info|Phân<br>tích<br>log|Hệ thống IPCC<br>Phân tích log loại<br>ErrorLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime|Gửi log sang<br>ELK|
|IVR|ErrorLog|Warning|Phân<br>tích<br>log|Hệ thống IVR<br>Phân tích log loại<br>ErrorLog với mức<br>Warning, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Phân quyền chi<br>tiết|
|Infra|TransactionLog|Warning|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>TransactionLog<br>với mức Warning,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Theo chuẩn<br>syslog<br>RFC5424|
|RPA|AccessLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống RPA Gửi<br>log sang SIEM loại<br>AccessLog với<br>mức Fatal, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Gửi log sang<br>ELK|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD449|
|---|---|---|
||**BÁO CÁO HỆ THỐNG & LOG**|Lần ban hành: 1|

|CRM|ErrorLog|Fatal|Xóa<br>log|Hệ thống CRM<br>Xóa log loại<br>ErrorLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Tự động xóa<br>log sau 180<br>ngày|
|---|---|---|---|---|---|---|
|IPCC|ErrorLog|Critical|Xuất<br>log|Hệ thống IPCC<br>Xuất log loại<br>ErrorLog với mức<br>Critical, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Không<br>mất mát<br>dữ liệu|Theo chuẩn<br>syslog<br>RFC5424|
|RPA|AuditLog|Info|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống RPA Nén<br>và lưu trữ log loại<br>AuditLog với mức<br>Info, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có thể<br>truy<br>xuất khi<br>cần|Theo chuẩn<br>syslog<br>RFC5424|
|Billing|PerformanceLog|Critical|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256|Gửi log sang<br>ELK|
|Infra|AccessLog|Critical|Xuất<br>log|Hệ thống Infra<br>Xuất log loại<br>AccessLog với<br>mức Critical, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê|Phân quyền chi<br>tiết|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Gửi log sang<br>ELK<br>Tự động xóa<br>log sau 180<br>ngày<br>Tự động xóa<br>log sau 180<br>ngày<br>Theo chuẩn<br>syslog<br>RFC5424<br>Tự động xóa<br>log sau 180<br>ngày|
||IVR||AccessLog|Critical|Xuất<br>log|Hệ thống IVR Xuất<br>log loại AccessLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Gửi log sang<br>ELK|
||Billing||TransactionLog|Error|Gửi<br>log<br>sang<br>SIEM|Hệ thống Billing<br>Gửi log sang SIEM<br>loại<br>TransactionLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Log<br>được<br>mã hóa<br>AES-<br>256||Tự động xóa<br>log sau 180<br>ngày|
||CRM||AccessLog|Info|Xuất<br>log|Hệ thống CRM<br>Xuất log loại<br>AccessLog với<br>mức Info, dữ liệu<br>lưu trữ tối thiểu 90<br>ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Tự động xóa<br>log sau 180<br>ngày|
||CRM||PerformanceLog|Critical|Xóa<br>log|Hệ thống CRM<br>Xóa log loại<br>PerformanceLog<br>với mức Critical,<br>dữ liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Theo chuẩn<br>syslog<br>RFC5424|
||CRM||PerformanceLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Có chỉ<br>số<br>thống<br>kê||Tự động xóa<br>log sau 180<br>ngày|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|||TD449|
|---|---|---|---|---|---|---|---|---|---|
||||**BÁO CÁO HỆ THỐNG & LOG**||||||Lần ban hành: 1|
||||||||||Tự động xóa<br>log sau 180<br>ngày<br>Có dashboard<br>Grafana<br>Theo chuẩn<br>syslog<br>RFC5424|
||Billing||TransactionLog|Fatal|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống Billing<br>Nén và lưu trữ log<br>loại<br>TransactionLog<br>với mức Fatal, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Không<br>mất mát<br>dữ liệu||Tự động xóa<br>log sau 180<br>ngày|
||Infra||AuditLog|Fatal|Gửi<br>log<br>sang<br>SIEM|Hệ thống Infra Gửi<br>log sang SIEM loại<br>AuditLog với mức<br>Fatal, dữ liệu lưu<br>trữ tối thiểu 90<br>ngày.|Có chỉ<br>số<br>thống<br>kê||Có dashboard<br>Grafana|
||CRM||PerformanceLog|Error|Nén<br>và<br>lưu<br>trữ<br>log|Hệ thống CRM<br>Nén và lưu trữ log<br>loại<br>PerformanceLog<br>với mức Error, dữ<br>liệu lưu trữ tối<br>thiểu 90 ngày.|Tích<br>hợp<br>cảnh<br>báo<br>realtime||Theo chuẩn<br>syslog<br>RFC5424|