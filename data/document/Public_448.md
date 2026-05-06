**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD448|
|---|---|---|
||**QUẢN LÝ API & LOG**|Lần ban hành: 1|

|API|Phương<br>thức|Hành<br>động|Mô tả chi tiết|Kết quả|Ghi chú|
|---|---|---|---|---|---|
|/customer/update|PATCH|Thêm<br>bản<br>ghi|API /customer/update<br>sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi|Giới hạn<br>rate-limit<br>1000<br>req/min|
|/invoice/export|PATCH|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka|Tích hợp<br>với API<br>Gateway|
|/security/firewall/config|GET|Xóa<br>thông<br>tin|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka|Giới hạn<br>rate-limit<br>1000<br>req/min|
|/ivr/callflow|POST|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka|Có<br>versioning<br>v1/v2|
|/crm/lead/import|PUT|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s|Tích hợp<br>với API<br>Gateway|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||POST|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/customer/update||GET|Thêm<br>bản<br>ghi|API /customer/update<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|
||/network/qos/monitor||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/invoice/export||POST|Cập<br>nhật<br>cấu<br>hình|API /invoice/export sử<br>dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/network/qos/monitor||GET|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>GET để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Tích hợp<br>với API<br>Gateway|
||/rpa/task/execute||POST|Export<br>dữ<br>liệu|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/crm/lead/import||PATCH|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||POST|Cập<br>nhật<br>cấu<br>hình|API /invoice/export sử<br>dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||GET|Xóa<br>thông<br>tin|API /ivr/callflow sử<br>dụng phương thức GET<br>để Xóa thông tin, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||DELETE|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API|
||/ivr/callflow||POST|Xóa<br>thông<br>tin|API /ivr/callflow sử<br>dụng phương thức<br>POST để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||GET|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức GET<br>để Thêm bản ghi, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/invoice/export||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||PUT|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||PUT|Thêm<br>bản|API /ivr/callflow sử<br>dụng phươngthức PUT|Log đầy||Tích hợp<br>với API|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful|
|||||ghi|để Thêm bản ghi, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|đủ||Gateway|
||/rpa/task/execute||POST|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/crm/lead/import||DELETE|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/network/qos/monitor||DELETE|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>DELETE để Thêm bản|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2|
||||||ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.||||
||/crm/lead/import||DELETE|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/rpa/task/execute||PATCH|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/invoice/export||GET|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức GET<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Theo<br>chuẩn<br>RESTful|
||/rpa/task/execute||POST|Kiểm<br>tra<br>trạng|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạngthái,có xác thực|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Giới hạn<br>rate-limit<br>1000<br>req/min<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML|
|||||thái|OAuth2 và log giao<br>dịch chi tiết.||||
||/security/firewall/config||GET|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/rpa/task/execute||GET|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/crm/lead/import||POST|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/ivr/callflow||GET|Export<br>dữ<br>liệu|API /ivr/callflow sử<br>dụng phương thức GET<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/ivr/callflow||DELETE|Thêm<br>bản<br>ghi|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp|
||||||dịch chi tiết.||||
||/invoice/export||PUT|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức PUT<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||PATCH|Export<br>dữ<br>liệu|API /ivr/callflow sử<br>dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/invoice/export||PUT|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức PUT<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/customer/update||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/rpa/task/execute||DELETE|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||PUT|Export|API|Rollback||Tích hợp|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit|
|||||dữ<br>liệu|/security/firewall/config<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|khi lỗi||với API<br>Gateway|
||/rpa/task/execute||PUT|Export<br>dữ<br>liệu|API /rpa/task/execute<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||PUT|Thêm<br>bản<br>ghi|API<br>/security/firewall/config<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/network/qos/monitor||DELETE|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/rpa/task/execute||PATCH|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||GET|Xóa<br>thông|API /invoice/export sử<br>dụng phươngthức GET|Rollback||Giới hạn<br>rate-limit|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful|
|||||tin|để Xóa thông tin, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|khi lỗi||1000<br>req/min|
||/rpa/task/execute||PATCH|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/ivr/callflow||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||DELETE|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||GET|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>GET để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/ivr/callflow||DELETE|Cập<br>nhật<br>cấu|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Cập nhật<br>cấu hình,có xác thực|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min|
|||||hình|OAuth2 và log giao<br>dịch chi tiết.||||
||/crm/lead/import||PUT|Xóa<br>thông<br>tin|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/crm/lead/import||POST|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||PATCH|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/customer/update||PATCH|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||POST|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min|
||||||dịch chi tiết.||||
||/security/firewall/config||PUT|Thêm<br>bản<br>ghi|API<br>/security/firewall/config<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/invoice/export||GET|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức GET<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/security/firewall/config||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/customer/update||GET|Cập<br>nhật<br>cấu<br>hình|API /customer/update<br>sử dụng phương thức<br>GET để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|
||/customer/update||POST|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>POST để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000|
||/network/qos/monitor||PUT|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/ivr/callflow||DELETE|Export<br>dữ<br>liệu|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||GET|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức GET<br>để Xóa thông tin, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/security/firewall/config||GET|Export<br>dữ<br>liệu|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/ivr/callflow||POST|Xóa<br>thông<br>tin|API /ivr/callflow sử<br>dụng phương thức<br>POST để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/customer/update||DELETE|Xóa<br>thông|API /customer/update<br>sử dụng phương thức<br>DELETE để Xóa thông|Rollback<br>khi lỗi||Giới hạn<br>rate-limit<br>1000|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||req/min<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2|
|||||tin|tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|||req/min|
||/security/firewall/config||POST|Thêm<br>bản<br>ghi|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/invoice/export||GET|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức GET<br>để Thêm bản ghi, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/customer/update||PUT|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>PUT để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/customer/update||POST|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/ivr/callflow||POST|Export<br>dữ<br>liệu|API /ivr/callflow sử<br>dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Hỗ trợ<br>JSON và<br>XML<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min|
||||||dịch chi tiết.||||
||/invoice/export||DELETE|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/security/firewall/config||GET|Export<br>dữ<br>liệu|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||PATCH|Xóa<br>thông<br>tin|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/network/qos/monitor||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/crm/lead/import||DELETE|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful|
||||||dịch chi tiết.||||
||/crm/lead/import||PUT|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/crm/lead/import||POST|Kiểm<br>tra<br>trạng<br>thái|API /crm/lead/import<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/customer/update||GET|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||PUT|Cập<br>nhật<br>cấu<br>hình|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PUT để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/network/qos/monitor||PUT|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PUT để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API<br>Gateway<br>Tích hợp<br>với API|
||||||dịch chi tiết.||||
||/security/firewall/config||GET|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/security/firewall/config||GET|Cập<br>nhật<br>cấu<br>hình|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||POST|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/security/firewall/config||DELETE|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/network/qos/monitor||GET|Cập<br>nhật<br>cấu|API<br>/network/qos/monitor<br>sử dụng phươngthức|Retry tối<br>đa 3 lần||Tích hợp<br>với API|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Gateway<br>Có<br>versioning<br>v1/v2<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML|
|||||hình|GET để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|||Gateway|
||/rpa/task/execute||PATCH|Export<br>dữ<br>liệu|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/customer/update||PUT|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>PUT để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/customer/update||PUT|Thêm<br>bản<br>ghi|API /customer/update<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/ivr/callflow||GET|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức GET<br>để Kiểm tra trạng thái,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Rollback<br>khi lỗi||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||PUT|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức PUT<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API<br>Gateway|
||/security/firewall/config||DELETE|Xóa<br>thông<br>tin|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/network/qos/monitor||DELETE|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/crm/lead/import||PATCH|Xóa<br>thông<br>tin|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|
||/invoice/export||POST|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/rpa/task/execute||POST|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min|
||/crm/lead/import||GET|Kiểm<br>tra<br>trạng<br>thái|API /crm/lead/import<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Theo<br>chuẩn<br>RESTful|
||/network/qos/monitor||PUT|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PUT để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|
||/customer/update||POST|Cập<br>nhật<br>cấu<br>hình|API /customer/update<br>sử dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||PUT|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/ivr/callflow||POST|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API<br>Gateway|
||/customer/update||PATCH|Cập<br>nhật<br>cấu<br>hình|API /customer/update<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/invoice/export||POST|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||PATCH|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/customer/update||GET|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/crm/lead/import||PATCH|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||GET|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|
||/security/firewall/config||GET|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Có<br>versioning<br>v1/v2|
||/crm/lead/import||PATCH|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/network/qos/monitor||GET|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/security/firewall/config||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Theo<br>chuẩn<br>RESTful|
||||||dịch chi tiết.||||
||/customer/update||POST|Export<br>dữ<br>liệu|API /customer/update<br>sử dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/ivr/callflow||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/network/qos/monitor||GET|Cập<br>nhật<br>cấu<br>hình|API<br>/network/qos/monitor<br>sử dụng phương thức<br>GET để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||PUT|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Theo|
||||||dịch chi tiết.||||
||/crm/lead/import||PUT|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||POST|Xóa<br>thông<br>tin|API /crm/lead/import<br>sử dụng phương thức<br>POST để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/network/qos/monitor||PATCH|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/ivr/callflow||PUT|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức PUT<br>để Cập nhật cấu hình,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/ivr/callflow||GET|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức GET<br>để Cập nhật cấu hình,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||PATCH|Thêm|API /crm/lead/import|Thông||Theo|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn|
|||||bản<br>ghi|sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|báo sự<br>kiện qua<br>Kafka||chuẩn<br>RESTful|
||/rpa/task/execute||PATCH|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/ivr/callflow||PATCH|Export<br>dữ<br>liệu|API /ivr/callflow sử<br>dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||PUT|Cập<br>nhật<br>cấu<br>hình|API /invoice/export sử<br>dụng phương thức PUT<br>để Cập nhật cấu hình,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||DELETE|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/crm/lead/import||PUT|Cập<br>nhật|API /crm/lead/import<br>sử dụng phươngthức|Rollback||Theo<br>chuẩn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||RESTful<br>Theo<br>chuẩn<br>RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000|
|||||cấu<br>hình|PUT để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|khi lỗi||RESTful|
||/rpa/task/execute||POST|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/rpa/task/execute||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/network/qos/monitor||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/customer/update||GET|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>GET để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/rpa/task/execute||POST|Kiểm<br>tra<br>trạng|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Kiểm tra|Thành<br>công||Giới hạn<br>rate-limit<br>1000|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||req/min<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API|
|||||thái|trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|<1s||req/min|
||/security/firewall/config||DELETE|Thêm<br>bản<br>ghi|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/security/firewall/config||DELETE|Xóa<br>thông<br>tin|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/customer/update||PATCH|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/security/firewall/config||PATCH|Cập<br>nhật<br>cấu<br>hình|API<br>/security/firewall/config<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/network/qos/monitor||GET|Cập<br>nhật<br>cấu|API<br>/network/qos/monitor<br>sử dụng phươngthức|Rollback<br>khi lỗi||Tích hợp<br>với API|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Gateway<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và|
|||||hình|GET để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|||Gateway|
||/customer/update||PUT|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>PUT để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/ivr/callflow||POST|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/invoice/export||POST|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||POST|Xóa<br>thông|API<br>/security/firewall/config|Retry tối||Hỗ trợ<br>JSON và|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||XML<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway|
|||||tin|sử dụng phương thức<br>POST để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|đa 3|lần|XML|
||/crm/lead/import||POST|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/network/qos/monitor||DELETE|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/network/qos/monitor||PATCH|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Tích hợp<br>với API|
||/rpa/task/execute||PATCH|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/crm/lead/import||GET|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/invoice/export||DELETE|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/customer/update||GET|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/rpa/task/execute||POST|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/crm/lead/import||POST|Xóa<br>thông|API /crm/lead/import<br>sử dụng phương thức<br>POST để Xóa thôngtin,|Thành<br>công||Tích hợp<br>với API|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Hỗ trợ<br>JSON và<br>XML|
|||||tin|có xác thực OAuth2 và<br>log giao dịch chi tiết.|<1s||Gateway|
||/network/qos/monitor||PATCH|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/ivr/callflow||GET|Xóa<br>thông<br>tin|API /ivr/callflow sử<br>dụng phương thức GET<br>để Xóa thông tin, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/customer/update||PATCH|Export<br>dữ<br>liệu|API /customer/update<br>sử dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Theo<br>chuẩn<br>RESTful|
||/invoice/export||POST|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/invoice/export||PUT|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức PUT<br>để Xóa thông tin, có<br>xác thực OAuth2 và log|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Tích hợp<br>với API<br>Gateway<br>Có<br>versioning<br>v1/v2|
||||||giao dịch chi tiết.||||
||/network/qos/monitor||PATCH|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/rpa/task/execute||GET|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/customer/update||PATCH|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/rpa/task/execute||PUT|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Có<br>versioning<br>v1/v2|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Tích hợp<br>với API<br>Gateway|
||/invoice/export||PATCH|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|
||/ivr/callflow||DELETE|Thêm<br>bản<br>ghi|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||GET|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>GET để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||PATCH|Cập<br>nhật<br>cấu<br>hình|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn|
||/ivr/callflow||POST|Export<br>dữ<br>liệu|API /ivr/callflow sử<br>dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||DELETE|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||GET|Xóa<br>thông<br>tin|API /crm/lead/import<br>sử dụng phương thức<br>GET để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/rpa/task/execute||PUT|Xóa<br>thông<br>tin|API /rpa/task/execute<br>sử dụng phương thức<br>PUT để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/crm/lead/import||PATCH|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/invoice/export||PUT|Kiểm<br>tra<br>trạng|API /invoice/export sử<br>dụng phương thức PUT<br>để Kiểm tra trạngthái,|Retry tối<br>đa 3 lần||Theo<br>chuẩn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML|
|||||thái|có xác thực OAuth2 và<br>log giao dịch chi tiết.|||RESTful|
||/ivr/callflow||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|
||/invoice/export||GET|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức GET<br>để Kiểm tra trạng thái,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||PATCH|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||GET|Xóa<br>thông<br>tin|API<br>/network/qos/monitor<br>sử dụng phương thức<br>GET để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/network/qos/monitor||POST|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML|
||||||dịch chi tiết.||||
||/invoice/export||PUT|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức PUT<br>để Xóa thông tin, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/security/firewall/config||DELETE|Thêm<br>bản<br>ghi|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/invoice/export||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Có<br>versioning<br>v1/v2|
||/network/qos/monitor||DELETE|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||PATCH|Export<br>dữ<br>liệu|API /ivr/callflow sử<br>dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML|
||||||dịch chi tiết.||||
||/crm/lead/import||PATCH|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/ivr/callflow||POST|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/ivr/callflow||PATCH|Xóa<br>thông<br>tin|API /ivr/callflow sử<br>dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||DELETE|Xóa<br>thông<br>tin|API<br>/network/qos/monitor<br>sử dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||DELETE|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min|
||||||dịch chi tiết.||||
||/customer/update||DELETE|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Có<br>versioning<br>v1/v2|
||/network/qos/monitor||GET|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Theo<br>chuẩn<br>RESTful|
||/crm/lead/import||DELETE|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/invoice/export||POST|Cập<br>nhật<br>cấu<br>hình|API /invoice/export sử<br>dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/security/firewall/config||GET|Export<br>dữ<br>liệu|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Hỗ trợ<br>JSON và<br>XML<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Hỗ trợ<br>JSON và<br>XML<br>Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||PATCH|Xóa<br>thông<br>tin|API<br>/security/firewall/config<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/network/qos/monitor||POST|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/rpa/task/execute||DELETE|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Có<br>versioning<br>v1/v2|
||/crm/lead/import||PUT|Kiểm<br>tra<br>trạng<br>thái|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/invoice/export||PUT|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức PUT<br>để Thêm bản ghi, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Giới hạn<br>rate-limit<br>1000<br>req/min<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn|
||/ivr/callflow||PATCH|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||DELETE|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/customer/update||PUT|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>PUT để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/network/qos/monitor||PATCH|Xóa<br>thông<br>tin|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/rpa/task/execute||POST|Xóa<br>thông<br>tin|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/crm/lead/import||PATCH|Xóa<br>thông|API /crm/lead/import<br>sử dụng phươngthức|Thông<br>báo sự||Theo<br>chuẩn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Có<br>versioning<br>v1/v2|
|||||tin|PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|kiện qua<br>Kafka||RESTful|
||/crm/lead/import||PATCH|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/customer/update||PUT|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>PUT để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/crm/lead/import||POST|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||PATCH|Cập<br>nhật<br>cấu<br>hình|API<br>/security/firewall/config<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/rpa/task/execute||GET|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ|
||||||log giao dịch chi tiết.||||
||/network/qos/monitor||POST|Xóa<br>thông<br>tin|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/customer/update||POST|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/rpa/task/execute||PATCH|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||PUT|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/invoice/export||GET|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức GET<br>để Xóa thông tin, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||PUT|Export|API /ivr/callflow sử|Thông||Hỗ trợ|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||JSON và<br>XML<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn|
|||||dữ<br>liệu|dụng phương thức PUT<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|báo sự<br>kiện qua<br>Kafka||JSON và<br>XML|
||/rpa/task/execute||POST|Xóa<br>thông<br>tin|API /rpa/task/execute<br>sử dụng phương thức<br>POST để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/crm/lead/import||DELETE|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/invoice/export||PATCH|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||PUT|Cập<br>nhật<br>cấu<br>hình|API<br>/security/firewall/config<br>sử dụng phương thức<br>PUT để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/invoice/export||POST|Cập<br>nhật<br>cấu|API /invoice/export sử<br>dụng phương thức<br>POST để Cậpnhật cấu|Thông<br>báo sự<br>kiệnqua||Theo<br>chuẩn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||RESTful<br>Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Có<br>versioning<br>v1/v2|
|||||hình|hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Kafka||RESTful|
||/rpa/task/execute||PUT|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>PUT để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/network/qos/monitor||PUT|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/security/firewall/config||PUT|Thêm<br>bản<br>ghi|API<br>/security/firewall/config<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/crm/lead/import||PUT|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||GET|Export<br>dữ<br>liệu|API<br>/security/firewall/config<br>sử dụng phương thức<br>GET để Export dữ liệu,|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful|
||||||có xác thực OAuth2 và<br>log giao dịch chi tiết.||||
||/rpa/task/execute||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/ivr/callflow||POST|Thêm<br>bản<br>ghi|API /ivr/callflow sử<br>dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||DELETE|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/rpa/task/execute||DELETE|Export<br>dữ<br>liệu|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||PUT|Export<br>dữ<br>liệu|API<br>/security/firewall/config<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Hỗ trợ<br>JSON và<br>XML<br>Theo<br>chuẩn<br>RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Hỗ trợ<br>JSON và<br>XML|
||||||log giao dịch chi tiết.||||
||/crm/lead/import||POST|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||PATCH|Xóa<br>thông<br>tin|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/invoice/export||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||GET|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>GET để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/customer/update||GET|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>GET để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn|
||/rpa/task/execute||GET|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/invoice/export||GET|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức GET<br>để Kiểm tra trạng thái,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/invoice/export||PATCH|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/invoice/export||DELETE|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||DELETE|Cập<br>nhật<br>cấu<br>hình|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||PUT|Xóa<br>thông|API /invoice/export sử<br>dụng phươngthức PUT|Retry tối||Theo<br>chuẩn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min|
|||||tin|để Xóa thông tin, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|đa 3|lần|RESTful|
||/crm/lead/import||POST|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/network/qos/monitor||GET|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/ivr/callflow||PUT|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức PUT<br>để Cập nhật cấu hình,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/rpa/task/execute||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||PUT|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Tích hợp<br>với API<br>Gateway<br>Tích hợp<br>với API<br>Gateway<br>Theo|
||||||log giao dịch chi tiết.||||
||/crm/lead/import||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/customer/update||PATCH|Xóa<br>thông<br>tin|API /customer/update<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Theo<br>chuẩn<br>RESTful|
||/ivr/callflow||POST|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||GET|Xóa<br>thông<br>tin|API<br>/network/qos/monitor<br>sử dụng phương thức<br>GET để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/crm/lead/import||DELETE|Xóa<br>thông<br>tin|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/ivr/callflow||PUT|Export|API /ivr/callflow sử|Retry tối||Theo|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||chuẩn<br>RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Có<br>versioning<br>v1/v2|
|||||dữ<br>liệu|dụng phương thức PUT<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|đa 3|lần|chuẩn<br>RESTful|
||/rpa/task/execute||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||PATCH|Export<br>dữ<br>liệu|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/crm/lead/import||PUT|Xóa<br>thông<br>tin|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Xóa thông tin,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/rpa/task/execute||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/crm/lead/import||GET|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>GET để Export dữ liệu,<br>có xác thực OAuth2 và|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful|
||||||log giao dịch chi tiết.||||
||/rpa/task/execute||DELETE|Export<br>dữ<br>liệu|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/network/qos/monitor||PATCH|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||GET|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức GET<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/rpa/task/execute||DELETE|Export<br>dữ<br>liệu|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||PATCH|Xóa<br>thông<br>tin|API<br>/security/firewall/config<br>sử dụng phương thức<br>PATCH để Xóa thông<br>tin,có xác thực OAuth2|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Giới hạn<br>rate-limit<br>1000<br>req/min<br>Tích hợp<br>với API<br>Gateway<br>Tích hợp<br>với API<br>Gateway<br>Tích hợp<br>với API<br>Gateway<br>Tích hợp<br>với API<br>Gateway<br>Tích hợp|
||||||và log giao dịch chi tiết.||||
||/customer/update||PUT|Cập<br>nhật<br>cấu<br>hình|API /customer/update<br>sử dụng phương thức<br>PUT để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||DELETE|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|
||/customer/update||PUT|Export<br>dữ<br>liệu|API /customer/update<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|
||/network/qos/monitor||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|
||/invoice/export||PUT|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức PUT<br>để Xóa thông tin, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/network/qos/monitor||GET|Export|API|Retry tối||Tích hợp|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful|
|||||dữ<br>liệu|/network/qos/monitor<br>sử dụng phương thức<br>GET để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|đa 3|lần|với API<br>Gateway|
||/ivr/callflow||GET|Thêm<br>bản<br>ghi|API /ivr/callflow sử<br>dụng phương thức GET<br>để Thêm bản ghi, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|
||/security/firewall/config||POST|Export<br>dữ<br>liệu|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||POST|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Có<br>versioning|
||/crm/lead/import||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|
||/rpa/task/execute||PUT|Cập<br>nhật<br>cấu<br>hình|API /rpa/task/execute<br>sử dụng phương thức<br>PUT để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/invoice/export||PUT|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức PUT<br>để Thêm bản ghi, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||DELETE|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/ivr/callflow||PUT|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức PUT<br>để Cập nhật cấu hình,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/invoice/export||PATCH|Thêm<br>bản|API /invoice/export sử<br>dụng phương thức<br>PATCH để Thêm bản|Thành<br>công||Có<br>versioning|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||v1/v2<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful|
|||||ghi|ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|<1s||v1/v2|
||/rpa/task/execute||PUT|Export<br>dữ<br>liệu|API /rpa/task/execute<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/invoice/export||DELETE|Thêm<br>bản<br>ghi|API /invoice/export sử<br>dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Tích hợp<br>với API<br>Gateway|
||/invoice/export||POST|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/customer/update||PUT|Thêm<br>bản<br>ghi|API /customer/update<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/rpa/task/execute||PATCH|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>PATCH để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway|
||||||dịch chi tiết.||||
||/network/qos/monitor||PUT|Kiểm<br>tra<br>trạng<br>thái|API<br>/network/qos/monitor<br>sử dụng phương thức<br>PUT để Kiểm tra trạng<br>thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/invoice/export||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /invoice/export sử<br>dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Hỗ trợ<br>JSON và<br>XML|
||/customer/update||PUT|Thêm<br>bản<br>ghi|API /customer/update<br>sử dụng phương thức<br>PUT để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Rollback<br>khi lỗi||Có<br>versioning<br>v1/v2|
||/rpa/task/execute||DELETE|Xóa<br>thông<br>tin|API /rpa/task/execute<br>sử dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Log đầy<br>đủ||Tích hợp<br>với API<br>Gateway|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Giới hạn<br>rate-limit<br>1000<br>req/min<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Hỗ trợ<br>JSON và<br>XML<br>Theo<br>chuẩn<br>RESTful|
||/crm/lead/import||DELETE|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/crm/lead/import||PUT|Export<br>dữ<br>liệu|API /crm/lead/import<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thành<br>công<br><1s||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/network/qos/monitor||POST|Export<br>dữ<br>liệu|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||POST|Kiểm<br>tra<br>trạng<br>thái|API<br>/security/firewall/config<br>sử dụng phương thức<br>POST để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Hỗ trợ<br>JSON và<br>XML|
||/ivr/callflow||PUT|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức PUT<br>để Cập nhật cấu hình,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Theo<br>chuẩn<br>RESTful|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Tích hợp<br>với API<br>Gateway<br>Tích hợp<br>với API<br>Gateway<br>Theo<br>chuẩn<br>RESTful<br>Có<br>versioning<br>v1/v2<br>Hỗ trợ<br>JSON và<br>XML<br>Hỗ trợ<br>JSON và|
||/crm/lead/import||DELETE|Cập<br>nhật<br>cấu<br>hình|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/ivr/callflow||DELETE|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Rollback<br>khi lỗi||Tích hợp<br>với API<br>Gateway|
||/crm/lead/import||GET|Thêm<br>bản<br>ghi|API /crm/lead/import<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Rollback<br>khi lỗi||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||PATCH|Export<br>dữ<br>liệu|API<br>/security/firewall/config<br>sử dụng phương thức<br>PATCH để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/ivr/callflow||PUT|Kiểm<br>tra<br>trạng<br>thái|API /ivr/callflow sử<br>dụng phương thức PUT<br>để Kiểm tra trạng thái,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Rollback<br>khi lỗi||Hỗ trợ<br>JSON và<br>XML|
||/network/qos/monitor||DELETE|Kiểm<br>tra|API<br>/network/qos/monitor|Rollback||Hỗ trợ<br>JSON và|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||XML<br>Có<br>versioning<br>v1/v2<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Theo<br>chuẩn<br>RESTful<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API|
|||||trạng<br>thái|sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|khi lỗi||XML|
||/invoice/export||DELETE|Xóa<br>thông<br>tin|API /invoice/export sử<br>dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/network/qos/monitor||POST|Thêm<br>bản<br>ghi|API<br>/network/qos/monitor<br>sử dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/security/firewall/config||DELETE|Xóa<br>thông<br>tin|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Theo<br>chuẩn<br>RESTful|
||/invoice/export||DELETE|Cập<br>nhật<br>cấu<br>hình|API /invoice/export sử<br>dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Theo<br>chuẩn<br>RESTful|
||/customer/update||PATCH|Xóa<br>thông|API /customer/update<br>sử dụng phươngthức|Rollback||Tích hợp<br>với API|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Gateway<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Có<br>versioning<br>v1/v2<br>Theo<br>chuẩn<br>RESTful<br>Tích hợp<br>với API|
|||||tin|PATCH để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|khi lỗi||Gateway|
||/ivr/callflow||POST|Cập<br>nhật<br>cấu<br>hình|API /ivr/callflow sử<br>dụng phương thức<br>POST để Cập nhật cấu<br>hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/security/firewall/config||DELETE|Cập<br>nhật<br>cấu<br>hình|API<br>/security/firewall/config<br>sử dụng phương thức<br>DELETE để Cập nhật<br>cấu hình, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/customer/update||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/customer/update||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Theo<br>chuẩn<br>RESTful|
||/security/firewall/config||POST|Export<br>dữ|API<br>/security/firewall/config<br>sử dụng phươngthức|Log đầy<br>đủ||Tích hợp<br>với API|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Gateway<br>Hỗ trợ<br>JSON và<br>XML<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Giới hạn<br>rate-limit<br>1000<br>req/min<br>Hỗ trợ<br>JSON và<br>XML|
|||||liệu|POST để Export dữ<br>liệu, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|||Gateway|
||/crm/lead/import||DELETE|Kiểm<br>tra<br>trạng<br>thái|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|
||/crm/lead/import||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /crm/lead/import<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Log đầy<br>đủ||Có<br>versioning<br>v1/v2|
||/customer/update||PUT|Export<br>dữ<br>liệu|API /customer/update<br>sử dụng phương thức<br>PUT để Export dữ liệu,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Tích hợp<br>với API<br>Gateway|
||/invoice/export||GET|Export<br>dữ<br>liệu|API /invoice/export sử<br>dụng phương thức GET<br>để Export dữ liệu, có<br>xác thực OAuth2 và log<br>giao dịch chi tiết.|Thông<br>báo sự<br>kiện qua<br>Kafka||Giới hạn<br>rate-limit<br>1000<br>req/min|
||/customer/update||POST|Thêm<br>bản<br>ghi|API /customer/update<br>sử dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao|Retry tối<br>đa 3 lần||Hỗ trợ<br>JSON và<br>XML|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD448|TD448|
|---|---|---|---|---|---|---|---|---|
||||**QUẢN LÝ API & LOG**||||Lần ban hành: 1||
|||||||||Có<br>versioning<br>v1/v2<br>Có<br>versioning<br>v1/v2<br>Tích hợp<br>với API<br>Gateway<br>Hỗ trợ<br>JSON và<br>XML|
||||||dịch chi tiết.||||
||/crm/lead/import||DELETE|Xóa<br>thông<br>tin|API /crm/lead/import<br>sử dụng phương thức<br>DELETE để Xóa thông<br>tin, có xác thực OAuth2<br>và log giao dịch chi tiết.|Thành<br>công<br><1s||Có<br>versioning<br>v1/v2|
||/rpa/task/execute||GET|Thêm<br>bản<br>ghi|API /rpa/task/execute<br>sử dụng phương thức<br>GET để Thêm bản ghi,<br>có xác thực OAuth2 và<br>log giao dịch chi tiết.|Retry tối<br>đa 3 lần||Có<br>versioning<br>v1/v2|
||/ivr/callflow||POST|Thêm<br>bản<br>ghi|API /ivr/callflow sử<br>dụng phương thức<br>POST để Thêm bản<br>ghi, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Retry tối<br>đa 3 lần||Tích hợp<br>với API<br>Gateway|
||/customer/update||PATCH|Kiểm<br>tra<br>trạng<br>thái|API /customer/update<br>sử dụng phương thức<br>PATCH để Kiểm tra<br>trạng thái, có xác thực<br>OAuth2 và log giao<br>dịch chi tiết.|Thành<br>công<br><1s||Hỗ trợ<br>JSON và<br>XML|