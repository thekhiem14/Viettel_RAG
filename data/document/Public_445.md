**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD445|
|---|---|---|
||**CHỈ TIÊU CRM - RPA**|Lần ban hành: 1|

|Nghiệp vụ|Loại chỉ<br>tiêu|Hành<br>động|API/Action|Mô tả chi tiết|Phương<br>pháp<br>đo|Kết quả<br>mong<br>muốn|Ghi chú|
|---|---|---|---|---|---|---|---|
|Opportunity|Chỉ tiêu<br>chức<br>năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.|
|Campaign|Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.|

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||trước khi<br>tải.|||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/lead/export|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>baogồm|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Contact||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.|||||
|Opportunity||Chỉ tiêu<br>bảo mật|Import|/crm/campaign/import|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>hiệu năng|Export|/crm/contact/update|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||bộ sang<br>hệ thống<br>Billing.|||
|Opportunity||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/contact/update|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Opportunity||Chỉ tiêu<br>bảo mật|Import|/crm/opportunity/delete|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||hai lớp<br>trước khi<br>tải.|||
|Campaign||Chỉ tiêu<br>hiệu năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>bảo mật|Xóa|/crm/lead/export|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>bảo mật|Import|/crm/lead/add|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||SLA đáp<br>ứng<br>99.99%.|||
|Opportunity||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>bảo mật|Import|/crm/campaign/import|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/lead/export|Cập nhật dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||ứng<br>99.99%.|||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/lead/export|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>bảo mật|Xóa|/crm/lead/add|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng5s,|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||tự động<br>retry khi<br>lỗi.|||
|Contact||Chỉ tiêu<br>bảo mật|Import|/crm/opportunity/delete|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/lead/add|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Export|/crm/contact/update|Export dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Contact||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Import|/crm/opportunity/delete|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>bảo mật|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/lead/export|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Campaign||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/lead/add|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Import|/crm/opportunity/delete|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu<br>Opportunity<br>trong CRM,<br>baogồm|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV,có|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||xác thực<br>hai lớp<br>trước khi<br>tải.|||
|Campaign||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Import|/crm/opportunity/delete|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.|||||
|Contact||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Contact||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/campaign/import|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/campaign/import|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>hiệu năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệthống|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Lead||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/opportunity/delete|Gắn thẻ dữ liệu<br>Campaign<br>trongCRM,|Kiểm<br>thử|Cảnh báo<br>nếu thiếu<br>trường|Dữ liệu được<br>backup hàng ngày,||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|hiệu<br>năng|bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộsang|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||hệ thống<br>Billing.|||
|Campaign||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/lead/export|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Lead||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/opportunity/delete|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng5s,|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||tự động<br>retry khi<br>lỗi.|||
|Opportunity||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Contact||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>bảo mật|Export|/crm/lead/export|Export dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Export|/crm/lead/add|Export dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s,dữ|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|||
|Lead||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/campaign/import|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/lead/export|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/lead/export|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Import|/crm/lead/export|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/opportunity/delete|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||SLA đáp<br>ứng<br>99.99%.|||
|Lead||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/opportunity/delete|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Lead||Chỉ tiêu<br>bảo mật|Export|/crm/lead/export|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>hiệu năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Lead||Chỉ tiêu<br>hiệu năng|Export|/crm/campaign/import|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>hiệu năng|Import|/crm/contact/update|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Contact||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu|Kiểm<br>thử|Thành<br>công với<br>thời gian<br>xử lý<|Dữ liệu được<br>backup hàng ngày,||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|hiệu<br>năng|1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>bảo mật|Import|/crm/lead/export|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Opportunity||Chỉ tiêu<br>bảo mật|Import|/crm/contact/update|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.|||||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/contact/update|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/lead/export|Cập nhật dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Export|/crm/contact/update|Export dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu|Kiểm<br>thử|Thành<br>công với<br>thời gian<br>xử lý<|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|chức<br>năng|1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|||
|Lead||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/opportunity/delete|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/lead/export|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>bảo mật|Export|/crm/lead/add|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Contact||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/lead/export|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/opportunity/delete|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||SLA đáp<br>ứng<br>99.99%.|||
|Campaign||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/contact/update|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Campaign||Chỉ tiêu<br>bảo mật|Import|/crm/opportunity/delete|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/opportunity/delete|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>bảo mật|Export|/crm/lead/export|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/campaign/import|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>hiệu năng|Import|/crm/lead/export|Import dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>chức<br>năng|Export|/crm/opportunity/delete|Export dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||SLA đáp<br>ứng<br>99.99%.|||
|Contact||Chỉ tiêu<br>bảo mật|Xóa|/crm/lead/add|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/lead/export|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Lead||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Contact||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/opportunity/delete|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||hai lớp<br>trước khi<br>tải.|||
|Campaign||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/lead/add|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Export|/crm/opportunity/delete|Export dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>bảo mật|Import|/crm/opportunity/delete|Import dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||bộ sang<br>hệ thống<br>Billing.|||
|Campaign||Chỉ tiêu<br>bảo mật|Import|/crm/campaign/import|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/lead/export|Cập nhật dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||bộ sang<br>hệ thống<br>Billing.|||
|Contact||Chỉ tiêu<br>bảo mật|Import|/crm/lead/export|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>hiệu năng|Export|/crm/opportunity/delete|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Export|/crm/opportunity/delete|Export dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệthống|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Contact||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>chức<br>năng|Import|/crm/campaign/import|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>hiệu năng|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/opportunity/delete|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||SLA đáp<br>ứng<br>99.99%.|||
|Opportunity||Chỉ tiêu<br>hiệu năng|Import|/crm/lead/add|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>bảo mật|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||hai lớp<br>trước khi<br>tải.|||
|Campaign||Chỉ tiêu<br>bảo mật|Export|/crm/lead/add|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Contact||Chỉ tiêu<br>bảo mật|Export|/crm/opportunity/delete|Export dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Contact||Chỉ tiêu<br>hiệu năng|Import|/crm/opportunity/delete|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/lead/export|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệthống|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Opportunity||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>chức<br>năng|Import|/crm/opportunity/delete|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/lead/add|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Contact||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/lead/export|Chuyển đổi dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||hai lớp<br>trước khi<br>tải.|||
|Campaign||Chỉ tiêu<br>bảo mật|Import|/crm/opportunity/delete|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>hiệu năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||ứng<br>99.99%.|||
|Opportunity||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>bảo mật|Xóa|/crm/lead/export|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>baogồm|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Lead||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/lead/export|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||||retry khi<br>lỗi.|||
|Contact||Chỉ tiêu<br>chức<br>năng|Import|/crm/campaign/import|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>hiệu năng|Export|/crm/lead/add|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm|Kiểm<br>thử|Xuất báo<br>cáo chi<br>tiết dưới|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|chức<br>năng|dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|||
|Opportunity||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộsang|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||hệ thống<br>Billing.|||
|Contact||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Opportunity||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Contact|Kiểm<br>thử|Cảnh báo<br>nếu thiếu|Dữ liệu được<br>backup hàng ngày,||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|hiệu<br>năng|trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Opportunity||Chỉ tiêu<br>bảo mật|Export|/crm/contact/update|Export dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộsang|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||hệ thống<br>Billing.|||
|Contact||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/opportunity/delete|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Export|/crm/lead/export|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>bảo mật|Import|/crm/contact/update|Import dữ liệu<br>Lead trong|Kiểm<br>thử|Cảnh báo<br>nếu thiếu|Dữ liệu được<br>backup hàng ngày,||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|hiệu<br>năng|trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>hiệu năng|Import|/crm/lead/export|Import dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/lead/export|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||ứng<br>99.99%.|||
|Lead||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/opportunity/delete|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>bảo mật|Export|/crm/lead/export|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||hệ thống<br>rollback<br>giao dịch.|||
|Campaign||Chỉ tiêu<br>bảo mật|Xóa|/crm/contact/update|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Export|/crm/lead/export|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Import|/crm/campaign/import|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/campaign/import|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/lead/export|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Opportunity||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Campaign||Chỉ tiêu<br>bảo mật|Xóa|/crm/lead/export|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>baogồm|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Contact||Chỉ tiêu<br>bảo mật|Xóa|/crm/lead/export|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộsang|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||hệ thống<br>Billing.|||
|Campaign||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/opportunity/delete|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s,dữ|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|||
|Campaign||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>bảo mật|Import|/crm/lead/add|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Campaign||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/lead/export|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>hiệu năng|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>hiệu năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>hiệu năng|Export|/crm/lead/add|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/lead/add|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s,dữ|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|||
|Campaign||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.|||||
|Opportunity||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/opportunity/delete|Cập nhật dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/campaign/import|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>chức<br>năng|Import|/crm/campaign/import|Import dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>bảo mật|Import|/crm/lead/export|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||hai lớp<br>trước khi<br>tải.|||
|Lead||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/lead/add|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/lead/export|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Export|/crm/lead/add|Export dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng5s,|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||tự động<br>retry khi<br>lỗi.|||
|Campaign||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/lead/add|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>bảo mật|Export|/crm/contact/update|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/contact/update|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/lead/export|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV,có|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||xác thực<br>hai lớp<br>trước khi<br>tải.|||
|Contact||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/opportunity/delete|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>chức<br>năng|Import|/crm/campaign/import|Import dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/campaign/import|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/opportunity/delete|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>hiệu năng|Export|/crm/opportunity/delete|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||hai lớp<br>trước khi<br>tải.|||
|Contact||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/opportunity/delete|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/campaign/import|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>chức<br>năng|Import|/crm/lead/export|Import dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Lead||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>hiệu năng|Export|/crm/lead/add|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/campaign/import|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|||
|Lead||Chỉ tiêu<br>bảo mật|Export|/crm/opportunity/delete|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộsang|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||hệ thống<br>Billing.|||
|Campaign||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/opportunity/delete|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Opportunity||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/lead/export|Cập nhật dữ<br>liệu Campaign<br>trongCRM,|Kiểm<br>thử|Đồng bộ<br>dữ liệu<br>sang|Yêu cầu tích hợp<br>với hệ thống RPA||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|hiệu<br>năng|DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>hiệu năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||ứng<br>99.99%.|||
|Lead||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Contact||Chỉ tiêu<br>hiệu năng|Import|/crm/opportunity/delete|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||hệ thống<br>rollback<br>giao dịch.|||
|Contact||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/lead/export|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/contact/update|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Import|/crm/contact/update|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||hai lớp<br>trước khi<br>tải.|||
|Campaign||Chỉ tiêu<br>chức<br>năng|Import|/crm/contact/update|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Contact||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Lead||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệthống|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Opportunity||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/campaign/import|Cập nhật dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/opportunity/delete|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Import|/crm/lead/export|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Contact||Chỉ tiêu<br>chức<br>năng|Import|/crm/contact/update|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệthống|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Contact||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/opportunity/delete|Thêm mới dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Lead||Chỉ tiêu<br>hiệu năng|Export|/crm/lead/add|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/opportunity/delete|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||rollback<br>giao dịch.|||
|Campaign||Chỉ tiêu<br>hiệu năng|Import|/crm/opportunity/delete|Import dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Opportunity||Chỉ tiêu<br>bảo mật|Xóa|/crm/lead/add|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/lead/add|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Lead||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệpvụ|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng5s,|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||tự động<br>retry khi<br>lỗi.|||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/lead/export|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Opportunity||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/lead/add|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Export|/crm/lead/export|Export dữ liệu<br>Opportunity<br>trong CRM,<br>baogồm|Kiểm<br>thử|Không<br>lỗi, log<br>đầy đủ<br>trong|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|hiệu<br>năng|AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|||
|Contact||Chỉ tiêu<br>bảo mật|Cập<br>nhật|/crm/contact/update|Cập nhật dữ<br>liệu Contact<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||||retry khi<br>lỗi.|||
|Opportunity||Chỉ tiêu<br>bảo mật|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Lead||Chỉ tiêu<br>hiệu năng|Xóa|/crm/contact/update|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>hiệu năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Campaign<br>trong CRM,<br>baogồm|Kiểm<br>thử|Đồng bộ<br>dữ liệu<br>sang<br>DataLake|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|hiệu<br>năng|trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Opportunity||Chỉ tiêu<br>hiệu năng|Import|/crm/lead/add|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.|||||
|Lead||Chỉ tiêu<br>chức<br>năng|Cập<br>nhật|/crm/lead/add|Cập nhật dữ<br>liệu Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Import|/crm/lead/export|Import dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Contact||Chỉ tiêu<br>bảo mật|Xóa|/crm/contact/update|Xóa dữ liệu<br>Contact trong|Kiểm<br>thử|Cảnh báo<br>nếu thiếu|Kết quả được gửi<br>mail và SMS cho||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|hiệu<br>năng|trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>bảo mật|Import|/crm/opportunity/delete|Import dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/lead/add|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộsang|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||và ghi log đầy<br>đủ.||hệ thống<br>Billing.|||
|Lead||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/lead/export|Gắn thẻ dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/campaign/import|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Opportunity||Chỉ tiêu<br>bảo mật|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Opportunity||Chỉ tiêu<br>bảo mật|Export|/crm/opportunity/delete|Export dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Opportunity||Chỉ tiêu<br>bảo mật|Xóa|/crm/campaign/import|Xóa dữ liệu<br>Opportunity<br>trong CRM,<br>baogồm|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake|Kết quả được gửi<br>mail và SMS cho||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>hiệu năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>bảo mật|Export|/crm/contact/update|Export dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV, có<br>xác thực<br>hai lớp<br>trước khi<br>tải.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Campaign||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/contact/update|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Chuyển<br>đổi|/crm/lead/export|Chuyển đổi dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Thêm<br>mới|/crm/lead/add|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>baogồm|Kiểm<br>thử|Đồng bộ<br>dữ liệu<br>sang<br>DataLake|Kết quả được gửi<br>mail và SMS cho||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|chức<br>năng|trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|quản trị viên phụ<br>trách.||
|Lead||Chỉ tiêu<br>chức<br>năng|Export|/crm/contact/update|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Phải kiểm thử với ≥<br>10.000 bản ghi để<br>đảm bảo hiệu năng.||
|Campaign||Chỉ tiêu<br>hiệu năng|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>chức<br>năng|Xóa|/crm/lead/add|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Contact||Chỉ tiêu<br>hiệu năng|Import|/crm/campaign/import|Import dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong<br>vòng 5s,<br>tự động<br>retry khi<br>lỗi.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Contact||Chỉ tiêu<br>hiệu năng|Export|/crm/lead/export|Export dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào,xử lý|Kiểm<br>thử<br>hiệu<br>năng|Xuất báo<br>cáo chi<br>tiết dưới<br>dạng<br>CSV,có|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||logic nghiệp vụ<br>và ghi log đầy<br>đủ.||xác thực<br>hai lớp<br>trước khi<br>tải.|||
|Opportunity||Chỉ tiêu<br>bảo mật|Gắn<br>thẻ|/crm/contact/update|Gắn thẻ dữ liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||
|Lead||Chỉ tiêu<br>chức<br>năng|Import|/crm/lead/export|Import dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>hiệu năng|Xóa|/crm/opportunity/delete|Xóa dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Campaign||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/opportunity/delete|Thêm mới dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu|Kiểm<br>thử<br>hiệu<br>năng|Đồng bộ<br>dữ liệu<br>sang<br>DataLake<br>trong|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.||vòng 5s,<br>tự động<br>retry khi<br>lỗi.|||
|Opportunity||Chỉ tiêu<br>bảo mật|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang<br>hệ thống<br>Billing.|Dữ liệu được<br>backup hàng ngày,<br>lưu giữ tối thiểu 30<br>ngày.||
|Lead||Chỉ tiêu<br>hiệu năng|Export|/crm/opportunity/delete|Export dữ liệu<br>Lead trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Thành<br>công với<br>thời gian<br>xử lý <<br>1s, dữ<br>liệu đồng<br>bộ sang|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
||||||||hệ thống<br>Billing.|||
|Campaign||Chỉ tiêu<br>bảo mật|Xóa|/crm/lead/add|Xóa dữ liệu<br>Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Kết quả được gửi<br>mail và SMS cho<br>quản trị viên phụ<br>trách.||
|Campaign||Chỉ tiêu<br>chức<br>năng|Chuyển<br>đổi|/crm/opportunity/delete|Chuyển đổi dữ<br>liệu Campaign<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>chức<br>năng|Không<br>lỗi, log<br>đầy đủ<br>trong<br>AuditLog,<br>SLA đáp<br>ứng<br>99.99%.|Theo chuẩn ISO<br>27001 và quy định<br>bảo mật Viettel.||

|||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD445|
|---|---|---|---|---|---|---|---|---|---|
|||||**CHỈ TIÊU CRM - RPA**|||||Lần ban hành: 1|
|||||||||||
|Contact||Chỉ tiêu<br>hiệu năng|Export|/crm/lead/add|Export dữ liệu<br>Contact trong<br>CRM, bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử bảo<br>mật|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||
|Opportunity||Chỉ tiêu<br>hiệu năng|Thêm<br>mới|/crm/lead/export|Thêm mới dữ<br>liệu<br>Opportunity<br>trong CRM,<br>bao gồm<br>validate dữ liệu<br>đầu vào, xử lý<br>logic nghiệp vụ<br>và ghi log đầy<br>đủ.|Kiểm<br>thử<br>hiệu<br>năng|Cảnh báo<br>nếu thiếu<br>trường<br>bắt buộc,<br>hệ thống<br>rollback<br>giao dịch.|Yêu cầu tích hợp<br>với hệ thống RPA<br>để tự động hóa quy<br>trình.||