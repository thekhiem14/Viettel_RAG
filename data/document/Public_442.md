||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||1.1|Xử lý theo danh sách khách hàng<br>:<br>- Có chức năng xử lý theo danh<br>sách các nhóm KH<br>- Có chức năng xử lý theo gói<br>cước (vd gói dân tộc) được phép<br>gọi vào|||1. Đầu số 1789: nhóm danh sách:<br>- Khi khách hàng gọi lên đầu số 1789, hệ thống kiểm tra xem đầu số KH đang gọi thuộc<br>nhóm nào thì định tuyến về nhóm đó.<br>- Kênh điểm bán, KH nội bộ<br>- 2 nguồn nhóm: Lấy từ các hệ thống khác (WS trả về mã nhóm), Hoặc tạo thủ công, có thể<br>add thủ công các khách hàng<br>- Màn hình quản lý nhóm khách hàng : Thêm mới các nhóm khách hàng + Cấu hình mã nhóm<br>+ Luật ưu tiên nhóm khách hàng (1 khách hàng thuộc nhiều nhóm, nhưng sẽ xử lý theo kịch<br>bản ưu tiên)<br>- Tích hợp API check nhóm + check gói cước (line dân tộc)||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||1.2|Xử lý theo vị trí khách hàng gọi<br>lên : Phát nhac theo tỉnh trên<br>IVR, VIP theo tỉnh|||Các bất cập hiện có:<br>- Khi khai báo IVR lên thì phải có người thực hiện lại test âm báo cho từng 63CN, khi có bão<br>lũ không sử dụng được,… các nhiều trường hợp không sử dụng được. (anh Tungtt2 gửi lại<br>các tài liệu mô tả bất cập hiện có của hệ thống cũ về các tính năng này) -> Cải thiện những<br>vấn đề bất cập<br>- Mong muốn 1: Công cụ để test âm báo cho từng tỉnh thành khi cấu hình file audio tương<br>ứng với các tỉnh<br>- Giải pháp: sử dụng 3cx để thực hiện test cuộc gọi, khai báo suxfix lên 3cx và thực hiện cuộc<br>gọi test lên hệ thống để test âm báo<br>- Mong muốn 2: Phát âm báo theo tỉnh, theo hạng (từ nhiều nguồn, cả tự động và thủ công) ,<br>theo nhóm khách hàng (nguời dùng chủ động định nghĩa nhóm trên hệ thống)<br>*Chú ý*:<br>Nhóm định nghĩa: Mỗi nhóm được tạo và gắn mã code, khi có cuộc gọi thì check mã nhóm<br>của KH và tự động add KH vào nhóm + add thủ công vào nhóm<br>Nhóm thủ công: Tạo nhóm và add khách hàng thủ công vào nhóm||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||1.3|Xử lý theo loại KH : Nội mạng,<br>ngoại mạng, KH cá nhân, KH<br>Doanh nghiệp (hiện tại đang add<br>ds KHDN thủ công)||Lưu ý : kiểm tra xem<br>KH là KH nội bộ hay<br>KH đã chuyển mạng,<br>trong các báo cáo<br>cũng ghi rõ loại KH<br>này<br>1. KH gọi lên, hệ<br>thống kiểm tra KH<br>nội bộ Viettel, KH<br>nội mạng, ngoại<br>mạng, cá nhân,<br>doanh nghiệp, khách<br>hàng chuyển mạng<br>giữ số (Check WS) -<br>(Kịch bản nghiệp vụ<br>anh Tungtt2 gửi lại<br>nếu có)|1. KH gọi lên, hệ thống kiểm tra KH nội bộ Viettel, KH nội mạng, ngoại mạng, cá nhân,<br>doanh nghiệp, khách hàng chuyển mạng giữ số (Check WS) - (Kịch bản nghiệp vụ anh<br>Tungtt2 gửi lại nếu có)<br>Lưu ý : kiểm tra xem KH là KH nội bộ hay KH đã chuyển mạng, trong các báo cáo cũng ghi<br>rõ loại KH nà||
||1.4|Phát nhạc theo danh sách/theo<br>nhóm KH trên IVR|||Tương tự 1.3||
||1.5|Smart IVR 7 - check gói cước<br>(line dân tộc, TB TT TS - hàm<br>subinfor)|||1.Xây dựng luồng IVR theo đầu số gọi lên.<br>+ Thêm mới bizid check thông tin TBTT và TBTS.<br>+ Thêm mới bizid check thông tin dân tộc và gói cước dân tộc.<br>+ Hệ thống trả về thông tin gói cước ưu đãi dân tộc<br>2. Thêm mới báo cáo ghi nhận thông tin khách đăng ký gói cước dân tộc.<br>+ Tìm kiếm/ xem chi tiết<br>+ Xuất báo cáo<br>Phân quyền người dùng có thể xem và xuất báo cáo: Admin/Giám sát viên||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||1.6|Tự động check ngưỡng nghẽn :<br>- Xử lý theo ngưỡng, hỗ trợ<br>nhiều ngưỡng<br>- và SMS điều hướng KH sử<br>dụng kênh tương tác khác|||KH gọi lên hệ thống, khi queue có 100 TVV,<br>VD: queue 100% TVV đang gặp KH - Ngưỡng 1<br>queue 90% TVV đang gặp KH - Ngưỡng 2 ,...<br>=> Hệ thống đánh giá có tạo thêm cuộc gọi hay không, với mỗi ngưỡng có thể cấu hình hành<br>động là gì (chuyển node, ivr, gửi tin nhắn cảnh báo,...)<br>1. Khi gọi vào IVR, cho phép so sánh ngưỡng nghẽn của 1 Queue ACD.<br>- Có thể cấu hình ngưỡng nghẽn<br>- Có thể cấu hình IVR, Tại 1 node IVR, có thể:<br>+ Kiểm tra ngưỡng nghẽn 1 queue -> Đưa ra kết quả -> Cấu hình các bước xử lý tiếp theo<br>+ So sánh ngưỡng nghẽn của các queue -> Đưa ra kết quả -> Cấu hình các bước xử lý tiếp<br>theo<br>2. Gửi SMS điều hướng KH sử dụng kênh tương tác khác (khi đạt ngưỡng nghẽn, ...). Cho<br>phép KH nhập nội dung tin nhắn<br>(tài liệu IBM - anh Tungtt2 gửi lại)||
||1.7|Cho phép định tuyến cuộc gọi<br>vào IVR theo thời gian||Bổ xung mới :<br>- Định tuyến vào cây<br>IVR tương ứng theo<br>các khoảng thời gian<br>KH gọi vào theo<br>từng đầu số<br>- Mỗi đầu số có thể<br>đặt tối thiểu 10<br>khoảng thờigian|1. Hiện tại: KH gọi vào ACD thì cấu hình thời gian này cho gặp TVV, tgian này cho vào IVR<br>2. Mong muốn: Với cây IVR, KH gọi vào giờ A thì thực hiện hành động gì, giờ B thì thực<br>hiện hành động gì||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|1.8|Nhận diện giọng nói qua IVR<br>(voice - eKYC)|Bổ xung mới :<br>- HD khách hàng đọc<br>đoạn âm theo hướng<br>dẫn để thực hiện<br>nhận dạng<br>- Cấu hình được việc<br>chuyển file ghi âm<br>của KH đến hệ thống<br>so sánh nhận diện<br>khác nhau tùy theo<br>dịch vụ<br>**Cụ thể:**<br>**1. Luồng selfcare**<br>**trên IVR (đã mô tả**<br>**bên cạnh)**<br>**2. Luồng kiểm tra**<br>**trong lúc đàm**<br>**thoại:**<br>- ĐTV click button<br>xác minh KH trên<br>giao diện nghiệp vụ<br>BCCS -> BCCS<br>check ht eKYC xem<br>SĐT này đăng kí<br>eKYC chưa-> Nếu<br>có thì BCCS thực<br>hiện gửi yc sang<br>IPCC để IPCC lấy 1<br>phần ghi âm cuộc gọi<br>hiện tại gửi sang ht<br>eKYC -> eKYC so<br>sánh dữ liệu trả về<br>kết quả xác minh trên<br>giao diện BCCS cho|1. Khi KH gọi lên mong muốn tra cứu thông tin, thực hiện thao tác nghiệp vụ<br>- Hệ thống thực hiện Check đã đăng ký eKYC hay chưa (KH bấm phím chọn)<br>- Hệ thống kiểm tra KH đã có đăng ký trên eKYC hay chưa (kiểm tra trên hệ thống eKYC),<br>trả kết quả về hệ thống, nếu đúng khách hàng thì thực hiện nghiệp vụ<br>2. Nghiệp vụ Đăng ký eKYC<br>3. Hỗ trợ cho phép kết nối tới nhiều hệ thống eKYC khác nhau|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||ĐTV -> ĐTV dựa<br>vào KQ để thực hiện<br>nghiệp vụ cho KH<br>mà KH không bị hỏi<br>han nhiều.<br>Mô tả thêm:<br>1. LUỒNG CHUNG<br>trên IVR<br>- KH gọi -> Ipcc -><br>IVR -> :<br>+ VAS<br>connector check các<br>điều kiện bài toán AI<br>,<br>+ VAS<br>connector Check<br>sang hệ thống<br>Voicebiometric xem<br>KH đã đăng kí chưa<br>+ Phát âm HD<br>bấm phím (tr hợp đã<br>đăng kí và TH chưa<br>đăng kí có âm HD<br>riêng)<br>+ Check xem<br>KH có bấm nhánh<br>đến nhánh nào<br>(nhánh đăng kí<br>API/nhánh tra cứu<br>API/ nhánh đăng kí<br>& tra cứu qua voice<br>eKYC/nhánhchuyển||

**==> picture [38 x 47] intentionally omitted <==**

**VIETTEL AI RACE** TD442 **TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC** Lần ban hành: 1 

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||CALL BOT...)<br>Case 1:  KH chưa<br>đăng kí lần nào<br>+ Phát âm<br>hướng dẫn riêng với<br>KH chưa đăng kí (<br>HD bấm phím  như<br>hiện tại + Viettel có<br>sử dụng công nghệ<br>nhận dạng âm thanh<br>mời quý khách đăng<br>kí bằng cách thực<br>hiện như sau)<br>+ Khách hàng<br>làm theo HD để đăng<br>kí -> chuyển cuộc<br>gọi qua hệ thống<br>voice biometric (lưu<br>ý về mặt công nghệ<br>yêu cầu đăng kí dc<br>voice eKYC qua<br>IPCC - đáp ứng đc<br>không)<br>+ Đăng kí xong<br>giữ luồng cuộc gọi<br>hay bắt khách hàng<br>gọi lại?<br>Case 2:  KH bấm<br>phím chọn nghiệp vụ<br>tự selfcare dùng<br>voice eKYC<br>+ KH bấm phím<br>chọn nghiệp vụ tự<br>selfcare dùng voice||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||eKYC (Để đăng kí<br>các dịch vụ A,B,C<br>dùng voice eKYC<br>quý khách vui lòng<br>bấm phím X)<br>+ IPCC check<br>sang ht Voice eKYC<br>xem KH đã đăng kí<br>chưa :<br>Đã đăng<br>kí  -> check xem có<br>đúng chính chủ<br>không - > đúng chính<br>chủ -> Báo lại IPCC<br>-> IPCC tác động<br>sang các HT khác để<br>đăng kí. ()<br>Đã đăng<br>kí  -> check xem có<br>đúng chính chủ<br>không - > Không<br>chính chủ -> Báo lại<br>IPCC -> Hd khách<br>hàng dùng chức năng<br>gặp ĐTV hoặc đăng<br>kí lại. ()<br>Đã đăng<br>kí  -> check xem có<br>đúng chính chủ<br>không - > Không<br>chính chủ nhiều lần<br>trong ngày -> Báo lại<br>IPCC -> Hd khách<br>hàng dùng chứcnăng||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||gặp ĐTV hoặc đăng<br>kí lại.<br>Chưa<br>đăng kí -> Chuyển<br>sang hd đăng kí như<br>ở case 1<br>Case 3:  KH đăng kí<br>lại voice eKYC như<br>thế nào<br>+ Cần có nghiệp<br>vụ vhi tiết để bảo<br>đảm không bị giả<br>mạo???<br>2. Luồng trên BCCS:|||
||**2**|**Xử lý phím bấm**|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|2.1|Bấm phím để chọn nhánh Trả lời<br>tự động||Bấm phím để chọn nhánh Trả lời tự động|
|2.2|Phím #,*||Phím #,*|
|2.3|Phát âm khi bấmphím sai||Phát âm khi bấmphím sai|
|2.4|Cấu hình phát lặp||1. Cấu hình động số lần phát lặp lại file media<br>2. Cấu hình độngthờigian chờ khách hàngbấmphím|
|2.5|Bấm phím lớn hơn hoặc bằng 2<br>chữ số||Bấm phím lớn hơn hoặc bằng 2 chữ số|
|2.6|Xử lý khi không bấm phím<br>(chuyển vào nhánh IVR, chuyển<br>queue...)|- Cho phép cấu hình<br>trên bất kì Node IVR<br>nào nếu KH không<br>thao tác sẽ chuyển<br>đến ĐTV (hiện tại đã<br>đáp ứng, muốn<br>chuyển đến node nào<br>thì dựng link đến<br>node cần chuyển,<br>trên link đó khai điều<br>kiện thực hiện link,<br>có thể là Noaudio<br>(không bấm phím),<br>Mã phím (bấm<br>phím), defaule<br>(defaule chuyển đến<br>node nào đó)|1. Cấu hình file NoAudio, khi phát hết file media, khách hàng không bấm gì thì lập tức thực<br>hiện chuyển tiếp tới các hành động khác đã cấu hình|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||2.7|Hỗ trợ DTMF inband và outband|||1. DTMF: Dual tall frequency: hỗ trợ gửi các phím bấm lên tổng đài. Khi KH bấm phím,<br>DTMF hỗ trợ mã hóa các phím bấm và gửi lên tổng đài, tổng đài thực hiện giải mã các tín<br>hiệu phím bấm được gửi lên<br>2. Hệ thống MyCC có hỗ trợ cấu hình chọn inband hoặc outband được không?||
||2.8|Bấmphímgặpđiện thoại viên|||Bấmphímgặpđiện thoại viên||
||2.9|Node phát nhiều file nhạc.<br>Node play music hỗ trợ phát<br>nhạc thay đổi theo khung giờ.|||1. Mong muốn: Cấu hình được nhiều file phát trong 1 lần<br>2. Cấu hình theo luật phát (VD: xoay vòng, ngẫu nhiên,…)||
||2.10|Âm báo riêng với từng mã lỗi<br>dịch vụ của thuê bao|||- Tổng đài báo lỗi dịch vụ cố định 18008119: phát thông báo tình trạng lỗi liên quan đến dịch<br>vụ cố định băng rộng(CĐBR) theo số gọi lên để khách hàng có thể tự seflcare hoặc có thể biết<br>tình trạng lỗi thuê bao của mình ở tình trạng như thế nào. Thông tin lỗi do tư vấn viên(TVV)<br>cung cấp(tất cả các cuộc gọi phản ánh dịch vụ: chất lượng kém, chập chờn, mất dịch vụ...).<br>- Tổng đài báo lỗi dịch vụ di động||
||2.11|Smart IVR 1 – tra cứu/ đăng kí<br>gói data/VAS|||- Xây dựng Smart IVR đăng ký gói cước theo từng kịch bản nghiệp vụ||
||2.12|Smart IVR 1 – tra cứu/ đăng kí<br>gói data/VAS - Báo cáo thông kê<br>cho phép chủ động khai báo để<br>thông kê gói mới mà ko cần nâng<br>câp báo cáo|||- Xây dựng báo cáo thống kê phím bấm, tổng hợp đăng ký, chi tiết với từng gói cước||
||2.13|Smart IVR 2 - thông báo lỗi nợ<br>cước|||Smart IVR 2 - thông báo lỗi nợ cước||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||2.14|Smart IVR 3 - thông báo sự cố<br>(cố định/di động)/tạo phản ánh tự<br>động về BCCS||Lưu ý luồng tạo phản<br>ánh tự động|Smart IVR 3 - thông báo sự cố (cố định/di động)/tạo phản ánh tự động về BCCS||
||2.15|Smart IVR 4 - tạm mở nợ cước|||Khi KH gọi lên tổng đài di động và có yêu cầu, TVV có thể tạm mở chặn một chiều cho<br>khách hàng nếu khách hàng yêu cầu, thời gian tạm mở đến hết chu kỳ cước.||
||2.16|Smart IVR 5 - tích điểm, đổi<br>điểm|||Smart IVR 5 - tích điểm, đổi điểm||
||2.17|Smart IVR 6 - tra cứu thông tin,<br>gói cước đangsử dụng|||Tra cứu gói data trên 191 - 1228||
||2.18|Smart IVR 8 – đăng kí đổi SIM|||- Cho phép khai báo động các  kịch bản Smart IVR (dự kiến bổ sung Smart IVR đăng ký đổi<br>SIM 5G)<br>- Hệ thống IVR 197 xây dựng thêm 01 phím bấm cho KH thao tác đăng ký đổi sim 4G.<br>Khi KH bấm phím đổi sim, hệ thống IVR gửi yêu cầu sang hệ thống quản lý đơn hàng, tự<br>động tạo thành thành 01 yêu cầu đổi sim trên hệ thống Order, nhân viên địa bàn tiếp nhận và<br>liên hệ đổi sim tại nhà cho KH. Khi KH đổi sim 4G thà<br>nh công, hệ thống tự động cộng các ưu đãi cho KH theo chính sách hiện hành tương tự như<br>khi KH đổi sim 4G qua SMS.<br>- Báo cáo: Báo cáo tổng hợp thuê bao đăng ký đổi sim qua IVR, Báo cáo chi tiết thuê bao<br>đăng ký đổi sim qua IVR (đây chính là các tác động đăng ký đổi sim, hệ thống gửi||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||2.19|Chuyển cuộc gọi IVR sang cây<br>IVR khác trên cùng site ipcc,<br>sang cây IVR khác trên Ipcc site<br>khác|||Chuyển cuộc gọi IVR sang cây IVR khác trên cùng site ipcc<br>sang cây IVR khác trên Ipcc site khác<br>Tương tự các nội dung mô tả phân quyền đã mô tả tại mục 1.1||
||2.20|Chuyển cuộc gọi từ cây IVR<br>sang hệ thống IVR khác ngoài<br>ipcc**(trong và ngoài Viettel)**|||1. Chuyển cuộc gọi từ cây IVR này sang cây IVR khác, trong công ty, ngoài công ty. Trong<br>hệ thống , ngoài hệ thống||
||2.21|Tự động chuyển sang queue<br>ACD nếu khôngbấmphím|||Tương tự mục 2.6||
||2.22|Smart IVR 8 – đăng kí đổi<br>voucher||Bổ xung mới|- Thêm kênh IVR để KH đổi ưu đãi đối tác liên kết trên hệ sinh thái Viettel++<br>Bước 1: Khách hàng gọi IVR 197 để nghe thông báo các ưu đãi đối tác liên kết.<br>Bước 2: Hệ thống IVR gọi sang QLĐT thông báo ưu đãi KH đổi tương ứng với phím bấm.<br>Bước 3: Hệ thống QLĐT sẽ xử lý các thông tin theo điều kiện của voucher như: Hạng khách<br>hàng, danh sách Blacklist, danh sách Whitelist, chiến dịch, số lượng mã hạn chế lấy của mỗi<br>thuê bao theo chiến dịch, hạn chế số lượng mã theo chương trình,…<br>Bước 4: Sau khi QLĐT đổi mã thành công sẽ thông báo đến IVR để phát âm thông tin tới<br>KH.||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||2.23|Smart IVR 9 – tích hợp với các<br>hệ thống CSDL của các dịch vụ<br>khác để khai báo các chức năng<br>Smart IVR tương ứng với nghiệp<br>vụ của các dịch vụ khác viettel<br>cung cấp cho KH||**Bổ xung mới :**<br>Tích hợp với các hệ<br>thống CSDL của các<br>dịch vụ khác để khai<br>báo các chức năng<br>Smart IVR|1. Sau này khi phát sinh nghiệp vụ cần check từ các hệ thống khác (VTPost,..) thì cần tích<br>hợp với các hệ thống đó để kiểm tra thông tin<br>2. Tích hợp với các hệ thống CSDL của các dịch vụ khác để khai báo các chức năng Smart<br>IVR<br>3.<br>- Nhận diện thông tin khách hàng (KH) qua SĐT liên hệ<br>- Xem lại lịch sử chi tiết cuộc gọi của khách hàng<br>- Nhận biết các đơn hàng của KH đã gửi/ nhận<br>- Xử lý phản ánh của khách hàng VIP: Khách hàng VIP theo quy định của VTPost hiện được<br>chia thành 9 nhóm, mỗi nhóm có 1 đặc điểm khác nhau (PL- Khách hàng đặc thù).<br>- Hiển thị thông tin khi KH gọi vào hệ thống||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|2.24|Cho phép nhập thông tin từ IVR<br>để xử lý kịch bản (đối thủ có)|Bổ xung mới:<br>- Cho phép nhập vd<br>SDT/CMND/CCCD<br>- Cho phép nhập mã<br>số thuế, nhập số ID<br>dịch vụ, mã nhập đơn<br>hàng (cả số và chữ)...<br>vd : KH -> Phát âm<br>hỏi tra cho số nào -><br>chọn số đang gọi, số<br>khác -> Nhập số<br>khác -> yc nhập<br>thông tin xác minh -><br>OK -> check đơn<br>hàng liên quan -><br>đọc lại mã đơn hàng<br>cho KH xác nhận -><br>OK thì báo lại lịch<br>trình cho KH<br>- Cho phép khai báo<br>cấu hình node IVR<br>với mã  Node ID nào<br>đó:<br>+ Node này cho phép<br>cấu hình khai báo<br>chuyển các thông tin<br>INPUT sang 1 hoặc<br>nhiều Webservice<br>nào đó<br>+ Với các giá trị trả<br>về thì xử lý các kịch<br>bản tương ứng (phát<br>file, chuyển node|1. Đáp ứng nhập số<br>2. Xây dựng API Gateway<br>3. Xây dựng WS kiểm tra thông tin cho KH<br>Bổ xung mới:<br>- Cho phép nhập vd SDT/CMND/CCCD<br>- Cho phép nhập mã số thuế, nhập số ID dịch vụ, mã nhập đơn hàng (cả số và chữ)...<br>vd : KH -> Phát âm hỏi tra cho số nào -> chọn số đang gọi, số khác -> Nhập số khác -> yc<br>nhập thông tin xác minh -> OK -> check đơn hàng liên quan -> đọc lại mã đơn hàng cho KH<br>xác nhận -> OK thì báo lại lịch trình cho KH<br>- Cho phép khai báo cấu hình node IVR với mã  Node ID nào đó:<br>+ Node này cho phép cấu hình khai báo chuyển các thông tin INPUT sang 1 hoặc nhiều<br>Webservice nào đó<br>+ Với các giá trị trả về thì xử lý các kịch bản tương ứng (phát file, chuyển node khác...)<br>+ Khai báo kết nối được đến các WS của các Doanh nghiệp có Puplic internet dễ dàng qua<br>giao diện<br>(tham khảo Mitek : giao dịch nhập đơn hàng/tra đơn hàng..|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||khác...)<br>+ Khai báo kết nối<br>được đến các WS của<br>các Doanh nghiệp có<br>Puplic internet dễ<br>dàng qua giao diện<br>(tham khảo Mitek :<br>giao dịch nhập đơn<br>hàng/tra đơn hàng...)|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||2.25|Việc cấu hình khai báo kết nối<br>đến các ht khác lấy thông tin có<br>thể thực hiện qua giao diện thay<br>vì phải làm thủ tục UPCODE||- Cấu hình qua giao<br>diện, tham khảo thêm<br>yêu cầu ở 10.3<br>- Có giao diện báo<br>cáo tình hình trao đổi<br>thông tin giữa IPCC<br>và các WS hệ thống<br>IPCC kết nối đến để<br>đánh giá tình trạng<br>WS :<br>+ Số lượng bản tin bị<br>timeout của từng WS<br>+ Số lượng cuộc gọi<br>báo lỗi kết nối WS :<br>vd sai định dạng đầu<br>vào, sai đầu ra...|Tương tự bài toán API gateway<br>Liệt kê danh sách các chuẩn của API đang được hỗ trợ (REST và SOAP) - Liệt kê và gửi lại<br>thông tin cho VTT||
||2.26|Cảnh báo upâm báo IVR|||Cảnh báo upâm báo IVR||
||**3**|**Phânphối đến ĐTV**|||||
||3.1|Thiết lập hàng đợi và phân phối<br>các cuộcgọi thoại|||1. Các tham số trên cấu hình queue (anh Tungtt2 gửi lại)<br>2. VTNET xuất trên DB các tham số cấu hìnhqueue||
||3.2|Phân phối theo số dịch vụ Khách<br>hàngbấmgọi|||Phân phối theo số dịch vụ Khách hàng bấm gọi||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|3.2.1|Ngoài chức năng phân phối như<br>hiện tại bổ xung thêm:<br>- KH gọi lại n lần sẽ vào queue<br>riêng, Tham số trong cấu hình<br>queue|Ngoài chức năng<br>phân phối như hiện<br>tại bổ xung thêm:<br>- KH gọi lại n lần sẽ<br>vào queue riêng,<br>Tham số trong cấu<br>hình queue|1.<br>- Cấu hình số lần khách hàng gọi lại (n lần bao gồm cả cuộc gọi gặp TVV và cuộc gọi nhỡ - n<br>cấu hình được)<br>- Thời điểm bắt đầu đếm số lần gọi, đếm trong khoảng thời gian đã cấu hình, sang giờ đó của<br>ngày hôm sau thì thực hiện reset lại số lần gọi<br>2. Cấu hình queue route tới khi khách hàng gọi n lần (gồm cả gặp và không gặp)<br>3. Nếu khách hàng gọi lại n lần (thỏa mãn điều kiện cấu hình), thì thực hiện phân bổ tới queue<br>đã được cấu hình|
|3.2.2|Quản lý theo cả extent và<br>AgentID|Quản lý theo cả<br>extent và AgentID<br>- Khi tạo ID cho<br>phép tạo ID theo các<br>nhóm ( đặt tên theo<br>đơn vị hay theo vị<br>trí...)<br>- Khi tạo user thì bắt<br>buộc user phải được<br>gắn với ID hoặc<br>nhóm ID thì mới<br>hoạt động được'|1. Mong muốn: trên hệ thống, Agent A sử dụng đầu số A để thực hiện gọi ra, Agent B sử<br>dụng đầu số B để gọi ra<br>2. Thêm hàng loạt theo file, thủ công (Thêm Device User gọi ra)<br>3. Gán device hàng loạt theo file, thủ công (Gán Device cho User gọi ra)<br>4. Đồng bộ dữ liệu device và user giữa các hệ thống IPCC giữa các miền (2 hệ thống khác<br>nhau). Khi thao tác dữ liệu trên 1 hệ thống, hệ thống còn lại sẽ thực hiện đồng bộ về<br>5. Phân quyền gọi ra:<br>- Phân trên device, cho phép chỉ được gọi ra đầu số nào<br>- Phân quyền hàng loạt (phân theo list trên form và theo file)<br>6. Anh Tungtt2 tạo mã IBM và gửi lại theo phiếu Nâng cấp AgentID Callout (Phiếu Minhtd2<br>trình ký)<br>Danh sách tính năng|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.3|Phân phối theo số ĐT của KH<br>(giống case khách hàng roaming)|||1. Hiện tại: Phân phối theo đầu số khách hàng gọi lên<br>2. Mong muốn: Phân phối theo số thuê bao của khách hàng<br>- Cấu hình các định dạng thuê bao, và các hành động xử lý khi đầu số thuê bao tương ứng gọi<br>lên||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.4|Routeing dự phòng khi DB lỗi|||Yêu cầu KH:<br>- DB lỗi<br>- Check DB mà chết thì định tuyến sang khu vực khác , thực hiện nhắn tin cảnh báo theo danh<br>sách số thuê bao (cấu hình danh sách số thuê bao)<br>- Xử lý trường hợp mất mạng, TVV không đăng nhập được vào hệ thống thì sẽ thực hiện<br>chuyển sang khu vực khác (Site DB khác)<br>- Xử lý trường hợp TVV đăng nhập vào hệ thống, nhưng mất mạng thực hiện chuyển sang<br>khu vực khác<br>- VD:<br>+ Đầu số 1800, do TVV ở Hà Nội và Hải Phòng, mất mạng ở HN -> Không định tuyến -<br>Trường hợp chung queue<br>+ Đầu số 198 gán Hà Nội, 199 gán Hải Phòng, 198 mất mạng -> Queue 198 chuyển site khác<br>(VTS đánh giá lại) - Khi 1 queue không có điện thoại viên trực trong giờ làm việc<br>Tính năng:<br>- Service check trường hợp DB lỗi, mất mạng (trước và sau khi đăng nhập)<br>- Luồng xử lý thực hiện chuyển sang khu vực khác (Site khác)<br>- Cấu hình template tin nhắn (cấu hình chủ động)<br>- Cấu hình danh sách nhận tin nhắn (cấu hình chủ động)<br>- Tích hợp SMSgateway thực hiện gửi tin nhắn khi định tuyến chuyển sang khu vực khác<br>Chú ý: tất cả các tính năng giám sát đều có tính năng nhắn tin và gửi mail (khi thỏa mãn điều<br>kiện, có thể cấu hình điều kiện)||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.5|Phân phối theo thâm niên và<br>trình độ Agent (Skill), Gán độ ưu<br>tiên trực nhiều queue|||Yêu cầu KH:<br>- Cấu hình độ ưu tiên (phạm vi từ mức độ 1 - mức độ 10), khách hàng chủ động cấu hình trên<br>queue (khi gán Agent)<br>- Phân quyền: Tương tự cách phân quyền trên VSA<br>Danh sách tính năng:<br>- Gán Agent vào queue (gán đơn lẻ và gán theo file)<br>- Gán độ ưu tiên cho Agent trên queue (gán đơn lẻ và gán theo file)<br>- Xử lý tìm kiếm và phân phối Agent có độ ưu tiên cao nhất khi có cuộc gọi đến||
||3.6|Phân phối theo đối tác Outsource<br>(chi tiết xem PYC)||Trước đã làm giải<br>pháp nhưng có bất<br>cập trưởng ca phải<br>nhập danh sách liên<br>tục mất thời gian|KH cần đánh giá lại||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.7|Phân phối theo vùng miền - theo<br>định dạng user (xem PYC)||Với chức năng theo<br>vùng miền , tìm hiểu<br>thêm tổng đài Mobile<br>phone:<br>Bên Mobile Phone<br>dùng giải pháp tràn<br>tự động nên TLPV<br>luôn ổn định ở mức<br>98% ngày thường.<br>Mobile Phone cho<br>tràn theo khu vực, và<br>có Call Center ở 6<br>miền.<br>Khu vực phía Bắc thì<br>HN và HP backup<br>cho nhau.<br>Do vậy, khi lưu<br>lượng cao thì :<br>+ Vẫn tăng<br>cường nhân sự đi đáp<br>ứng được, vì có thể<br>huy động ở cả HN và<br>HP để điều phối cho<br>nhau.<br>+ Với giải<br>pháp tràn tự động, thì<br>cứ tràn đi tràn lại và<br>do IVR (trả lời tự<br>động trên menu) trả<br>lời KH, không cho<br>đến ĐTV nên về mặt<br>chỉ số vẫn OK|KH cần đánh giá lại||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.8|Xử lý ưu tiên khách hàng VIP<br>cho phép cấu hình tham số<br>“Ngưỡng Agent rảnh tràn queue”|||Yêu cầu KH:<br>- Cho phép Cấu hình tràn queue (Cấu hình được queue Đích), đánh giá<br>- Điều kiện tràn queue: check Ngưỡng nghẽn<br>- Mong muốn xây dựng tính năng tràn từ queue VIP (Kim cường, Vàng, Bạc) sang queue<br>Thường<br>- Mong muốn xây dựng tính năng tràn từ queue Thường -> Queue VIP<br>Danh sách tính năng:<br>- Cấu hình hạng khách hàng<br>- Xử lý route cuộc gọi vào queue tương ứng hạng khách hàng<br>- Cấu hình đội ưu tiên tràn queue (VD: Kim cương thì tràn queue trước, đến Vàng)<br>- Xử lý tràn sang queue có độ ưu tiên cao nhất||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|3.9|Xử lý blacklist, cập nhật có tác<br>dụng ngay||Yêu cầu KH:<br>- Cấu hình danh sách Blacklist<br>- Xử lý chặn danh sách người gọi lên trong danh sách Blacklist<br>- Cập nhật luồng xử lý khi danh sách Blacklist được cập nhật<br>- Khi thuê bao của Khách hàng gọi tổng đài quá số lần quy định theo luật cấu hình chặn**Quấy**<br>**rối**có sẵn, hệ thống IPCC thực hiện chặn hướng gọi tổng đài cho thuê bao sẽ hiển thị Log<br>chặn trên chức năng “Lịch sử tác động” của BCCS.<br>- Hệ thống IPCC cung cấp cho BCCS các dữ liệu để hiển thị: Số TB bị chặn, Thời gian (giờ<br>phút giây ngày tháng năm),  Loại tác động (Chặn hướng gọi tổng đài), Lý do tác động (Chặn<br>hướng gọi tổng đài kênh xxx), Lý do tác động (KH gọi tổng đài QR), Đơn vị tác động<br>(Viettel).<br>- Cấu hình Blacklist theo queue<br>- Các chế độ chặn: Chặn vĩnh viễn, chặn có kỳ hạn, chặn tại cửa hàng (provissioning) -<br>- Khi add danh sách Blacklist thủ công thì ghi log lịch sử tác động (người tác động, ngày<br>tháng, căn cứ, file đính kèm, PYC)<br>- Cấu hình luật chặn tự động<br>+ Tham số: Cuộc gọi lên trong 1 ngày, Thời gian đàm thoại mỗi cuộc, Số giờ chặn<br>+ Cấu hình tần suất quét danh sách chặn<br>- Chặn thủ công: Có kỳ hạn, không chặn (gọi lên mà thỏa mãn luật chặn thì cũng ko chặn<br>- Cấu hình danh sách blacklist trên queue<br>- Cấu hình chặn trên toàn tổng đài<br>Danh sách  tính năng:<br>- Cấu hình danh sách blacklist trên queue<br>- Cấu hình chặn trên toàn tổng đài<br>- Cấu hình không chặn<br>- Cấu hình luật chặn tự động<br>- Cấu hình luật chặn thủ công (người tác động, ngày tháng, căn cứ, file đính kèm, PYC)<br>- Cấu hình chặn provissioning (chặn ở cửa hàng, phải ra cửa hàng mới mở được - VTT gửi<br>lại)<br>+ Cung cấp WS kiểm tra thuê bao đã bị chặn phía cửa hàng<br>- Gửi thông tin sang CC log thông tin chặn của khách hàng|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.10|Ưu tiên gặp ĐTV khi lỡ CG||Trên IPCC 2.0 có y/c<br>cho nội dung này<br>nhưng không có IBM<br>riêng cập nhật y/c<br>này vào IBM<br>4078954 để theo dõi<br>thực hiện trên IPCC<br>2.0|Yêu cầu KH:<br>- Cấu hình ưu tiên cuộc gọi lỡ (số cuộc gọi lỡ, thời gian chờ, số lượng cuộc gọi thỏa mãn điều<br>kiện gọi lỡ liên tục)<br>- Khi thỏa mãn điều kiện, hệ thống cho phép 2 option:<br>+ Chuyển queue (cấu hình được queue đích)<br>+ Ưu tiên trong queue<br>- Trên popup cho phép TVV xem lý do vì sao chuyển queue (thông tin gọi nhỡ)<br>- Khi KH đạt điều kiện, cuộc gọi sẽ được ưu tiên nhất trong queue<br>+ KH là VIP -> Vào queue VIP và dc ưu tiên<br>+**KH là thường**<br>- Phát nhạc ưu tiên cho khách hàng thỏa mãn điều kiện<br>- Transfer cuộc gọi thì vẫn ưu tiên tại queue mới. Vẫn phát file nhạc ưu tiên của queue nguồn||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.11|Nhận diện khách hang theo tỉnh|||Yêu cầu KH:<br>- Kiểm tra KH ở tỉnh nào thì vào queue ACD nào<br>- Cho phép phát nhạc chờ riêng theo các tỉnh<br>- Phát nhạc chờ theo danh sách khách hàng được add lên hệ thống<br>Danh sách tính năng:<br>1.Cho phép nhận diện thông tin khách hàng theo tỉnh.<br>+ Dựa vào suxfix GMSC cấu hình để nhận diện thống tin khách hàng theo tỉnh.<br>+ Cho phép phát nhạc chờ riêng đối với mỗi khách hàng thuộc tỉnh tương ứng.<br>2. Xây dựng báo cáo ghi nhận thông tin cuộc gọi/ khách hàng theo tỉnh hệ thống ghi nhận<br>được.<br>+ Xem/ tìm kiếm .<br>+ Xuất báo cáo.||
||3.12|Cấu hình định tuyến thông minh|||Chức năng này cho phép cấu hình ngưỡng định tuyến thông minh theo từng queue<br>+ Cho phép cấu hình ngưỡng định tuyến<br>+ Ngưỡng tin nhắn cảnh báo.<br>+ Cấu hình định tuyến sang khu vực khác cùng đầu số.<br>+ Cấu hình định tuyến từ ACD sang IVR||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|3.13|Nhận diện cuộc gọi đc định<br>tuyến thông minh trên giao diện<br>Web||Chức năng này cho phép hiển thị thông tin khách hàng được định tuyến theo khu vực trên<br>popup up màn hình điện thoại viên.<br>+ Hiển thị thông tin chi tiết khách hàng.<br>+ Hiển thị thông tin khách hàng được định tuyến từ vùng miền nào|
|3.14|Định tuyến cuộc gọi theo từng<br>đầu số, từngkhu vực.||Định tuyến cuộc gọi theo từng đầu số, từng khu vực.<br>Tham khảo nội dungPYC mã 4078954|
|3.15|Người dùng chủ động cấu hình<br>ngưỡngđịnh tuyến.||Người dùng chủ động cấu hình ngưỡng định tuyến.<br>Tham khảo nội dungPYC mã 4078954|
|3.16|Người dùng chủ động cấu hình<br>các điều kiện định tuyến bao<br>gồm khu vực, kênh, số lượng<br>cuộc gọi định tuyến đi, số lượng<br>cuộc gọi định tuyến tiếp nhận.||Người dùng chủ động cấu hình các điều kiện định tuyến bao gồm khu vực, kênh, số lượng<br>cuộc gọi định tuyến đi, số lượng cuộc gọi định tuyến tiếp nhận.<br>Tham khảo nội dung PYC mã 4078954|
|3.17|Người dùng chủ động trong công<br>tác cảnh báo: Tự cập nhật danh<br>sách nhắn tin theo các ngưỡng<br>nghẽn khác nhau.||Người dùng chủ động trong công tác cảnh báo: Tự cập nhật danh sách nhắn tin theo các<br>ngưỡng nghẽn khác nhau.<br>Tham khảo nội dung PYC mã 4078954|
|3.18|Xử lý ưu tiên khách hàng VIP -<br>Có chức năng xử lý VIP, SVIP,<br>Tràn queue trên ACD||Yêu cầu KH:<br>- Queue SVIP: Chọn hạng phục vụ - Hạng Kim cương và Vàng<br>- Queue VIP: Chọn hạng Bạc, Thân thiết<br>- Xử lý tràn queue**(Tương tự tính năng 3.8)**|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.19|**Xử lý last/recently Agent (xem**<br>**PYC chi tiết)**|||Sửa đổi nâng cấp tính năng LastAgent và bổ xung luồng nghiệp vụ “recently agent” như sau:<br>-Khách hàng khi gọi vào queue có cấu hình LastAgent và gặp ĐTV A,B,C vào các giờ tương<br>ứng a,b,c, trong thời gian cấu hình (vd hiện tại là 48h) khi gọi lại lần tiếp theo có thể xảy ra<br>các tình huống sau :<br>oKhách hàng muốn gặp 1 ĐTV bất kì hoặc;<br>oKhách hàng muốn gặp chính xác bạn một trong các bạn ĐTV A, B, C<br>-Để đáp ứng các mong muốn của trên của khách hàng, TTCSKH đề xuất và bổ xung luồng<br>nghiệp vụ “recently agent” như sau:<br>-Bổ xung thêm 1 option cấu hình queue liên quan đến chức năng “recently agent”, khi cấu<br>hình queue cho phép chọn 1 trong 2 option :<br>oLast Agent: giữ nguyên option như chức năng Last agent hiện tại, bổ xung chức năng chủ<br>động cấu hình thay đổi thời gian last agent (đang là 48h)<br>oRecently agent: Cấu hình yêu cầu bổ xung, cụ thể: Khi khách hàng gọi vào 1 queue ACD,<br>nếu queue này được cấu hình Recently agent thì HT sẽ kiểm tra trong thời gian cấu hình tạm<br>gọi là “Recently_time” (vd 48h) để xem khách hàng trước đó gặp những Agent nào, queue<br>nào, trong vòng 10 phút hiện tại các ĐTV đó có đang đăng nhập hệ thống hay không. (vd<br>ACD server sẽ hỏi Agent Server các thông tin trên), kết quả kiểm tra sẽ được lưu vào 1 biến<br>cho cuộc gọi đó và trả cho Callserver để phát câu thông báo cho khách hàng, kịch bản cụ thể<br>gồm :<br>1.1 Kịch bản xử lý phát âm báo:<br>§Nếu khách hàng trước đó (trong khoảng recently_time) có gặp các bạn ĐTV và số lần gặp<br>lớn hơn hoặc bằng 2 lần :<br>Hệ thống sẽ CHỈ lấy thông tin của 2 lần gần nhất gồm user và thời điểm trả lời (vd KH gặp<br>ĐTV A vào thời điểm a và gặp ĐTV B vào thời điểm b, thời điểm b là thời điểm gần nhất) và<br>kiểm tra:<br>·Nếu tại thời điểm hiện tại (t0) cả ĐTV A&B đều đang làm việc (available) : Hệ thống sẽ báo<br>cho callserrver phát âm báo Recently_agent_1.wave cho KH như sau “Viettel xin kính chào<br>…để gặp lại ĐTV lần gần nhất bấm phím 1, để gặp lại ĐTV trước đó bấm phím 2, để gặp<br>ĐTV khác bấm *”<br>·Nếu tại thời điểm hiện tại (t0) chỉ có 1 trong 2 ĐTV A&B làm việc. Nếu chỉ có B available<br>thì phát âm báo Recently_agent_2.wave  “Viettel xin kính chào …để gặp lại ĐTV lần gần<br>nhất bấm phím 1, để gặp ĐTV khác bấm *”.<br>·Nếu chỉ có ĐTV A available thì phát âm nhạc chờ mặc định như hiện tại (tức là không xử lý<br>last agent)||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
||||·Nếu tại thời điểm hiện tại (t0) cả 2 ĐTV A&B đều không làm việc, phát âm nhạc chờ mặc<br>định như hiện tại (tức là không xử lý last agent)<br>§ Nếu khách hàng trước đó (trong khoảng recently_time) có gặp các bạn ĐTV và số lần gặp 1<br>lần:<br>Hệ thống sẽ lấy thông tin của lần duy nhất này, cũng gồm user và thời điểm trả lời như trên<br>và kiểm tra :<br>·Nếu ĐTV A available thì phát âm báo Recently_agent_2.wave  “Viettel xin kính chào …để<br>gặp lại ĐTV lần gần nhất bấm phím 1, để gặp ĐTV khác bấm *”.<br>·Nếu tại thời điểm hiện tại (t0) ĐTV này không làm việc, phát âm nhạc chờ mặc định như<br>hiện tại (tức là không xử lý last agent)<br>Lưu ý :<br>- Các âm thông báo này TTCSKH chủ động thay đổi nội được<br>- Hệ thống kiểm tra TVV gần nhất nếu có cuộc gọi KH yêu cầu gặp người gần nhất hệ thống<br>sẽ phát nhạc và chờ trong 1 khoảng thời gian (có thể cấu hình thời gian timeout). Hết thời<br>gian timeout, Nếu người gần nhất vẫn đang bận, hệ thống sẽ thông báo Agent gần nhất đang<br>bận, hệ thống sẽ chuyển bạn gặp TVV khác, đồng thời hệ thống chuyển KH vào queue như<br>bình thường|
|3.20|Xư lýLast Agent như hiện tại||Tươngtựmô tả 3.19|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.21|Xử lý Last agent nâng cao<br>"Recently Agent": KH chọn gặp<br>ĐTV gần nhất hoặc trước đó|||Tương tự mô tả 3.19||
||3.22|Xử lý Last agent nâng cao<br>"Recently Agent": Phát ấm HD<br>khách hàng chọn gặp ĐTV trước<br>đó hay không|||Tương tự mô tả 3.19||
||3.23|Cấu hình thời gian áp dụng<br>Last/recentlyagent|||Tương tự mô tả 3.19||
||3.24|Cấu hình chọn chuyển BOT hay<br>không|||1. Tìm kiếm cấu hình chuyển bot<br>2. Quản lý cấu hình chuyển bot: Thêm danh sách, sửa danh sách, xóa danh sách, xóa hàng<br>loạt<br>3. Cấu hình chọn điều hướng BOT/ ACD<br>4. Xuất file excel báo cáo danh sách cấu hình chuyển bot||
||3.25|Cho phép chọn BOT chuyển từ<br>IPCC đến BOT|||Yêu cầu của KH:<br>- Với mỗi queue cho phép chọn Bot để gặp KH<br>- Cho phép cấu hình queue ACD chọn BOT chuyển đến<br>- Bổ sung thông tin BOT trong báo cáo trạng thái kết thúc cuộc gọi<br>Danh sách tính năng:<br>- Cấu hình chọn bot trên queue<br>- Xử lý KH gặp Bot đã được cấu hình trên queue<br>- Tích hợp các Bot vào hệ thống||
||3.26|Chuyển BOT theo tậpdanh sách|||Chuyển BOT theo tậpdanh sách||
||3.27|Nhận cuộc gọi từ BOT chuyển<br>đến IPCC||Hỗ trợ cả luồng call<br>in ( KH -> IPCC -><br>BOT -> ĐTV)<br>và luồng call BOT<br>out từ HT khác<br>chuyểnđến ĐTV|Nhận cuộc gọi từ BOT chuyển đến IPCC||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.28|Xử lý blacklist - Có chức năng<br>xử lý blacklist chuyển IVR|||1.Thêm mới màn hình blaclist danh sách khách hàng theo từng kênh<br>+ Cho phép cấu hình thêm mới danh sách blacklist theo kênh, ngày giờ chặn, mở chặn blaclist<br>+ Loại chặn: có kỳ hạn, không kỳ hạn, vĩnh viên theo từng danh sách được cấu hình.<br>+ Sửa/ xóa thông tin khách hàng.<br>+ Xuất báo cáo.<br>2. Cấu hình Blacklist chuyển IVR<br>3. Thêm mới báo cáo lịch sử chặn thuê bao:<br>+ Xem/ tìm kiếm.<br>+ Xuất báo cáo.<br>4. Thêm mới báo cáo thống kê khách hàng bị chặn vẫn gọi lên hệ thống.<br>+ Xem/ tìm kiếm.<br>+ Xuất báo cáo||
||3.29|Xử lý blacklist - Có chức năng<br>xử lý blacklist, chặn gọi vào có<br>kì hạn, không kì hạn, chặn vĩnh<br>viễn, áp riêng cho từng kênh|||Tương tự tính năng Blacklist đã mô tả||
||3.30|Xử lý blacklist - Nâng cấp tính<br>năng kiểm tra danh sách thuê bao<br>có nằm trong danh sách từ chối<br>nhận tin nhắn 197, 199 trước khi<br>thực hiện survey khách hàng qua<br>các hình thức hiện có trên tổng<br>đài trên HT IPCC|||Xử lý blacklist - Nâng cấp tính năng kiểm tra danh sách thuê bao có nằm trong danh sách từ<br>chối nhận tin nhắn 197, 199 trước khi thực hiện survey khách hàng qua các hình thức hiện có<br>trên tổng đài trên HT IPCC<br>Tham khảo PYC mã IBM 4079613||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||3.31|ACD theo danh sách nhóm<br>khách hàng - Cho phép nhóm<br>nào đc gọi vào ht|||- Cấu hình danh sách số điện được được phép gọi theo queue<br>- Add thủ công hoặc import danh sách số thuê bao<br>- Cho phép on/off chức năng||
||**4**|**Tiền xử lý khigặp ĐTV**|||||
||4.1|Nhạc chờ mặc định khi tạo queue|||Nhạc chờ cho từng queue: Chức năng này cho phép khách hàng gọi lên nghe nhạc chờ riêng<br>được cậu hình trong queue:<br>1. Tại màn hình cấu hình queue:<br>+ Thêm mới param_id: Nhạc chờ trong queue: Cho phép/ thêm sửa xóa<br>+ Khách hàng gọi lên hệ thống với đầu số queue được cấu hình sẽ nghe nhạc chờ tương ứng<br>được cấu hình trong queue||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||4.2|Thời<br>chờ|gian bắt buộc nghe Nhạc||Thời gian nghe nhạc chờ: Đây là khoảng cấu hình phát nhạc chờ trong queue khi khách hàng<br>gọi lên hệ thống mà TVV chưa nhấc máy:<br>+ Khi cuộc gọi lên hệ thống check file thông tin file nhạc cấu hình, thời gian phát nhạc để xử<br>lý.<br>+ Nếu khách hàng gọi lên hệ thống, hết thời gian phát nhạc chờ trong queue mà TVV không<br>nhấc máy thì sẽ kết thúc cuộc gọi.<br>+ Báo cáo<br>Điều kiện đảm bảo:<br>+ Thêm mới một tham số: Cấu hình thời gian chờ trong queue.<br>- Luồng xử lý:<br>+ Tách thành 2 luồng nghe: nghe nhạc truyền thông + nghe nhạc chờ<br>+ Nghe hết 1 file nhạc truyền thông, sau đó vào queue<br>+ Cấu hình thời gian chờ trong queue<br>+ Cấu hình thời gian nghe file truyền thông<br>+ Cấu hình file truyền thông||
||4.3|Nhạc|chờ cuộc gọi ưu tiên riêng||Yêu cầu KH:<br>- Với các khách hàng ưu tiên, sẽ phát nhạc chờ riêng cho khách hàng nghe.<br>-  Nếu không để file nhạc ưu tiên thì sẽ xử lý ưu tiên như bình thường<br>- Cho phép chọn file media từ list trong màn hình cấu hình queue<br>Danh sách tính năng:<br>- Cấu hình nhạc chờ ưu tiên||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||4.4|Phát nhiều file nhạc chờ khác<br>nhau|||Yêu cầu KH:<br>- Các chế độ play tuần tự, random<br>- Cấu hình được nhiều file nhạc chờ trong queue||
||4.5|Cấu hình luật phát : lặp lại,<br>random, xoay vòng...|||Yêu cầu KH:<br>- Cấu hình thuật toán phát file media<br>- Cấu hình chọn file media (trường hợp phát lặp lại 1 file)<br>- Cấu hình chọn nhiều file media (trường hợp phát xoay vòng, random)||
||4.6|Nhạc chờ riêngcho từng queue|||Chophépcấu hình nhạc chờ riêngcho từngkênh||
||4.7|Nhạc chờ theo mã tỉnh|||Nhạc chờ theo mã tỉnh<br>Đã mô tả ở tính năng3.11||
||4.8|Nghe truyền thông cuộc gọi|||Yêu cầu KH<br>- Bắt buộc nghe âm báo(tươngtự 4.2)||
||4.9|Popup theo danh sách khách<br>hang|||Popup theo danh sách khách hang<br>Tương tự 4.16 -> 4.22 đã được mô tả chi tiết||
||4.10|Đáp ứng như ht hiện tại với đầu<br>sô 1789, line dân tộc|||Đáp ứng như hệ thống hiện tại với đầu sô 1789 (nhận biết nhóm khách hàng dựa trên các mã<br>kênh được code trên hệ thống), line dân tộc (nhận diện theo gói cước)||
||4.11|Nghe nhạc chờ theo danh sách|||Cấu hình danh sách số thuê bao<br>Cấu hình được file nhạc chờ cho danh sách<br>Cấu hình được nhiều danh sách trên queue<br>Mỗi danh sách là 1 file nhạc chờ||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||4.12|Chức năng IVR ảo|||Cấu hình phát âm báo<br>Tách nhánh gặp điện thoại viên<br>Không bấm phím -> Có thể chuyển được đến queue ACD cấu hình<br>Cấu hình được thời gian bắt buộc nghe âm báo<br>Chỉ tính phí khi gặp điện thoại viên||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||4.13|Xử lý nghẽn thông minh - Nhắn<br>tin điều hướng chuyển kênh<br>tương tác khác|||**Yêu cầu:**<br>- Hệ thống căn cứ vào tần suất kh gọi lên tổng đài/ ngày - Cấu hình (số lần)<br>- Căn cứ vào thời gian chờ (tối thiểu bao nhiêu s)<br>- Cấu hình Khung giờ nhắn tin<br>- Cấu hình khung giờ tính toán tham số<br>- Hệ thống thực hiện nhắn tin cho người dùng khi đạt điều kiện cấu hình<br>- Cấu hình nội dung tin nhắn<br>- KH có xu hướng gọi lại nhiều lần vào hệ thống khi ko gọi được TVV -> mục tiêu để giảm<br>tải cho hệ thống<br>- Xử lý trên luồng cuộc gọi (khi đang gọi thì thực hiện kiểm tra thuê bao xem có thỏa mãn<br>điều kiện không)<br>==> Định hướng cuộc gọi khi nghẽn<br>- Check theo tỉ lệ nghẽn: Tổng số cuộc gọi đang chờ / tổng số điện thoại viên rảnh (cấu hình<br>số tỉ lệ nghẽn trong khoảng thời gian được cấu hình, cho phép cấu hình nhiều khung giờ)<br>ngưỡng nghẽn được tính toán và cập nhật liên tục -> Gửi hết các khách hàng đang chờ và<br>thỏa mãn điều kiện<br>- Check KH gọi lên hệ thống nhiều lần và gửi đơn lẻ<br>+ Check số lần KH gọi lên bị lỡ và nguy cơ lỡ (đang chờ >= n s - n cấu hình được) trong<br>khoảng thời gian lùi so với thời điểm quét (VD: trước thời điểm quét bao nhiêu lâu)<br>+ Check khung giờ gửi tin nhắn - nhiều khung giờ (cấu hình được)<br>+ Không check KH đã gặp TVV hay chưa trước khi nhắn tin<br>- Với trường hợp định tuyến thông minh thì không nhắn tin<br>- Cấu hình thời gian tối thiểu từ thời điểm khách hàng gọi vào để nhắn tin<br>- Tính ngưỡng nghẽn theo từng queue||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|4.14|Pop up sang BCCS (và các UD<br>khác)|**Popup dữ liệu từ**<br>**CCAI sang:**<br>**- Nếu queue có cấu**<br>**hình chọn hiển thị**<br>**lịch sử phân tích**<br>**KH từ nguồn dữ**<br>**liệu là ht CCAI thì :**<br>+ Chức năng hiển thị<br>danh sách trang web<br>khách hàng tham<br>quan <br>+ Nguồn khách hàng<br>chính là lịch sử truy<br>cập website của<br>khách hàng trước khi<br>tìm đến sự hỗ trợ của<br>ĐTV. ĐTV sẽ biết<br>được khách hàng đến<br>từ trang nào, họ dừng<br>lại ở chủ đề nào lâu<br>nhất,… Từ đó cơ bản<br>nắm bắt được những<br>_x005finsight mà<br>khách hàng quan tâm<br>ở doanh nghiệp.<br>Agent lúc này có thể<br>tư vấn đúng trọng<br>tâm nhu cầu của<br>khách hàng, khiến<br>cuộc trò chuyện trực<br>tuyến trở nên thoải<br>mái và gần gũi hơn.|1. Yêu cầu khách hàng<br>- Ví dụ:<br>Popup dữ liệu từ CCAI sang:<br>- Nếu queue có cấu hình chọn hiển thị lịch sử phân tích KH từ nguồn dữ liệu là ht CCAI thì :<br>+ Chức năng hiển thị danh sách trang web khách hàng tham quan<br>+ Nguồn khách hàng chính là lịch sử truy cập website của khách hàng trước khi tìm đến sự hỗ<br>trợ của ĐTV. ĐTV sẽ biết được khách hàng đến từ trang nào, họ dừng lại ở chủ đề nào lâu<br>nhất,… Từ đó cơ bản nắm bắt được những insight mà khách hàng quan tâm ở doanh nghiệp.<br>Agent lúc này có thể tư vấn đúng trọng tâm nhu cầu của khách hàng, khiến cuộc trò chuyện<br>trực tuyến trở nên thoải mái và gần gũi hơn.<br>- Chuyển thông tin sang ứng dụng khác: SĐT, Mã hoá đơn, mã lịch sử chuyển tiền,vv. Chọn<br>theo từng queue, từng kênh và thông tin theo queue|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|4.14.1|Popup để MAP cuộc gọi với ID<br>nhập trên BCCS (hoặc UD khác<br>của doanh nghiệp)|- Cho phép tạo ngay<br>ID tương tác và loại<br>kênh và hiển thị trên<br>Popup cho ĐTV, cho<br>phép copy ID<br>- Tự động chuyển ID<br>tương tác này vào bộ<br>nhớ giao diện để các<br>UD khác có thể lấy<br>thông tin ID này<br>- Khi ĐTV vào CRM<br>riêng của doanh<br>nghiệp (vd BCCS) để<br>tạo TICKET mới thì<br>trước khi bấn nút<br>SAVE thì ht CRM sẽ<br>tự động lấy giá trị ID<br>tương tác của ĐTV<br>trên trình duyệt, view<br>lên cho ĐTV kiểm<br>tra, nếu ĐTV so sánh<br>ID/Kênh ht CRM lấy<br>về đúng với ID?kênh<br>do IPCC tạo ra thì<br>ĐTV sẽ click để<br>LƯU ID và kênh vào<br>TICKET trên CRM<br>(nếu sai cho phép<br>ĐTV copy từ IPCC<br>để paste sang BCCS<br>trước khi lưu)<br>=> Mục đích để lưu<br>được thông tin IPCC<br>trênCRMtừ đó|1. Yêu cầu nghiệp vụ<br>'- Cho phép tạo ngay ID tương tác và loại kênh và hiển thị trên Popup cho ĐTV, cho phép<br>copy ID<br>- Tự động chuyển ID tương tác này vào bộ nhớ giao diện để các UD khác có thể lấy thông tin<br>ID này<br>- Khi ĐTV vào CRM riêng của doanh nghiệp (vd BCCS) để tạo TICKET mới thì trước khi<br>bấn nút SAVE thì ht CRM sẽ tự động lấy giá trị ID tương tác của ĐTV trên trình duyệt, view<br>lên cho ĐTV kiểm tra, nếu ĐTV so sánh ID/Kênh ht CRM lấy về đúng với ID?kênh do IPCC<br>tạo ra thì ĐTV sẽ click để LƯU ID và kênh vào TICKET trên CRM  (nếu sai cho phép ĐTV<br>copy từ IPCC để paste sang BCCS trước khi lưu)<br>=> Mục đích để lưu được thông tin IPCC trên CRM từ đó MAP ping việc tiếp nhận và xử lý<br>của ĐTV. Tương tự với các cuộc gọi ra cho KH, cũng như các kênh tương tác khác như mail,<br>chat...<br>Lưu ý: - Vẫn tạo TICKET riêng trên IPCC , trường hợp doanh nghiệp không có CRM vẫn có<br>thê sd TICKET của IPCC|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||MAP ping việc tiếp<br>nhận và xử lý của<br>ĐTV.**Tương tự với**<br>**các cuộc gọi ra cho**<br>**KH, cũng như các**<br>**kênh tương tác**<br>**khác như mail,**<br>**chat...**<br>_Lưu ý: - Vẫn tạo_<br>_TICKET riêng trên_<br>_IPCC , trường hợp_<br>_doanh nghiệp không_<br>_có CRM vẫn có thê_<br>_sd TICKET của_<br>_IPCC_||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|4.14.2|Cấu hình động để IPCC chuyển<br>hay không chuyển các giá trị này<br>lịn hoạt|- Cấu hình chuyển<br>hay không chuyển<br>các thông tin này ra<br>catche theo từng<br>kênh<br>- Cho phép cấu hình<br>ngoài việc lưu ra<br>biến trên cache thì có<br>thể khai đường link<br>để gửi thông tin sang<br>các ht CRM khác<br>như kiểu gửi SĐT<br>sang BCCS hiện tại<br>để hỗ trợ các UD<br>khác link hoạt, cho<br>phép khai theo từng<br>kênh, mỗi kênh có<br>thể cấu hình >2 link<br>(ngoài số ĐT có thể<br>chuyển cả các dữ liệu<br>khác đã có trên CRM<br>của IPCC (xem mục<br>4.17.1)|1. Yêu cầu nghiệp vụ<br>'- Cấu hình chuyển hay không chuyển các thông tin này ra catche theo từng kênh<br>- Cho phép cấu hình ngoài việc lưu ra biến trên cache thì có thể khai đường link để gửi thông<br>tin sang các ht CRM khác như kiểu gửi SĐT sang BCCS hiện tại để hỗ trợ các UD khác link<br>hoạt, cho phép khai theo từng kênh, mỗi kênh có thể cấu hình >2 link<br>(ngoài số ĐT có thể chuyển cả các dữ liệu khác đã có trên CRM của IPCC (xem mục 4.17.1)|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|4.15|Pop up thông tin KH, nhóm KH<br>(nâng cao)|Chức năng popup<br>nhóm khách hàng:<br>1. Cho phép chọn<br>một hoặc nhiều<br>nguồn dữ liệu để<br>POPUP<br>2. Với mỗi nguồn<br>cho phép :<br>- Cho phép hiện thị<br>tối thiểu 20 trường (<br>20 hay hơn nên tham<br>khảo ht Customer<br>360 hoặc ht khác)<br>- Cho phép cấu hình<br>hiển thị theo Queue<br>- Cho phép cấu hình<br>ĐTV được/không<br>được COPY dữ liệu<br>từng trường trên cửa<br>sổ POP up<br>- Cho phép cấu hình<br>FONT chữ, MÀU<br>sắc từng trường<br>- Cho phép cấu hình<br>chuyển thông tin<br>trong trường nào đến<br>1 link/ hoặc nhiều<br>link  nào đó theo<br>từng Queue để<br>POPUP thông tin KH<br>trên UD link đến<br>- Cho phép lựa chọn<br>thứ tự ưu tiên hiển<br>thị các trường, số|**1. Yêu cầu nghiệp vụ**<br>"Chức năng popup nhóm khách hàng:<br>1. Cho phép chọn một hoặc nhiều nguồn dữ liệu để POPUP<br>2. Với mỗi nguồn cho phép :<br>- Cho phép hiện thị tối thiểu 20 trường ( 20 hay hơn nên tham khảo ht Customer 360 hoặc ht<br>khác)<br>- Cho phép cấu hình hiển thị theo Queue<br>- Cho phép cấu hình ĐTV được/không được COPY dữ liệu từng trường trên cửa sổ POP up<br>- Cho phép cấu hình FONT chữ, MÀU sắc từng trường<br>- Cho phép cấu hình chuyển thông tin trong trường nào đến 1 link/ hoặc nhiều link  nào đó<br>theo từng Queue để POPUP thông tin KH trên UD link đến<br>- Cho phép lựa chọn thứ tự ưu tiên hiển thị các trường, số trường cần hiển thị tùy thời điểm và<br>tùy queue<br>- Năng lực add khoảng 100 tr thuê bao<br>- Cho phép ĐTV thực hiện gửi yêu cầu cập nhật thông tin cho KH nếu phát hiện thông tin<br>Popup bị sai, các yc này sẽ được gửi đến cho giám sát viên, gs viên sẽ là người cập nhật, ht<br>ghi log lại các yc, ng yc, tình trạng đã đc cập nhật, chưa cập nhật, thời điểm cập nhật (phân<br>quyền gs queue nào chỉ nhìn đc yc & sửa queue đó). - Có thể cấu hình ON/OFF các trường<br>nào ĐTV có thể tự cập nhật trong khi KH gọi lên<br>- Mỗi trường đều có chức năng cấu hình : hiện rõ hay hiện 1 phần thông tin để bảo đảm<br>BMATTT<br>- Phần quyền cho user nào có thể cập nhật nhóm KH nào...Tham khảo giao diện quản lý của<br>Strxxx<br>(với các trường cấu hình hiển thị cho queue, nếu KH nào mà thiếu thông tin trường nào thì sẽ<br>hiển thị chữ mờ để ĐTV biết)"|

**==> picture [38 x 47] intentionally omitted <==**

**VIETTEL AI RACE** TD442 **TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC** Lần ban hành: 1 

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||trường cần hiển thị<br>tùy thời điểm và tùy<br>queue<br>- Năng lực add<br>khoảng 100 tr thuê<br>bao<br>- Cho phép ĐTV<br>thực hiện gửi yêu cầu<br>cập nhật thông tin<br>cho KH nếu phát<br>hiện thông tin Popup<br>bị sai, các yc này sẽ<br>được gửi đến cho<br>giám sát viên, gs<br>viên sẽ là người cập<br>nhật, ht ghi log lại<br>các yc, ng yc, tình<br>trạng đã đc cập nhật,<br>chưa cập nhật, thời<br>điểm cập nhật (phân<br>quyền gs queue nào<br>chỉ nhìn đc yc & sửa<br>queue đó). - Có thể<br>cấu hình ON/OFF<br>các trường nào ĐTV<br>có thể tự cập nhật<br>trong khi KH gọi lên<br>- Mỗi trường đều có<br>chức năng cấu hình :<br>hiện rõ hay hiện 1<br>phần thông tin để bảo<br>đảm BMATTT<br>- Phần quyền cho<br>user nào có thể cập||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||nhật nhóm KH<br>nào...Tham khảo<br>giao diện quản lý của<br>Strxxx<br>_(với các trường cấu_<br>_hình hiển thị cho_<br>_queue, nếu KH nào_<br>_mà thiếu thông tin_<br>_trường nào thì sẽ_<br>_hiển thị chữ mờ để_<br>_ĐTV biết)_||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|4.16|Popup lịch sử thống kê (thống kê<br>tự động trên BCCS)||Tương tự hệ thống cũ.<br>1. Yêu cầu nghiệp vụ: Truyền thông tin sang ứng dụng khác|
|4.17|View được Lịch sử tương tác qua<br>các kênh|Có 2 chức năng :<br>- Hiển thị lịch sử<br>tương tác:<br>+ Hiển thị lịch sử<br>tương tác trong 1<br>khoảng thời gian gần<br>nhất (cấu hình được<br>khoảng thời gian này<br>theo từng kênh)<br>+ Lịch sử tương tác<br>gồm các kênh và các<br>hướng<br>inbound/outbound<br>- Hiện thị thói quen<br>tương tác của KH<br>theo kênh nào :<br>+ Sắp sếp kênh<br>tương tác KH thực<br>hiện nhiều nhất lên<br>đầu + số lần tương<br>tác<br>+ Làm nổi bật kênh<br>KH hay tương tác<br>nhất với tổng đài<br>+ Số lượng tương tác<br>theo các kênh của<br>KH được cấu hình<br>khoảng thời gian<br>đếm theo từng queue<br>+ Hiển thị tên<br>Agent/queue/kênh|1. Yêu cầu nghiệp vụ<br>Có 2 chức năng :<br>- Hiển thị lịch sử tương tác:<br>+ Hiển thị lịch sử tương tác trong 1 khoảng thời gian gần nhất (cấu hình được khoảng thời<br>gian này theo từng kênh)<br>+ Lịch sử tương tác gồm các kênh và các hướng inbound/outbound<br>- Hiện thị thói quen tương tác của KH theo kênh nào :<br>+ Sắp sếp kênh tương tác KH thực hiện nhiều nhất lên đầu + số lần tương tác<br>+ Làm nổi bật kênh KH hay tương tác nhất với tổng đài<br>+ Số lượng tương tác theo các kênh của KH được cấu hình khoảng thời gian đếm theo từng<br>queue<br>+ Hiển thị tên Agent/queue/kênh tương tác trước đó KH gọi lên (khi KH liên hệ lên tổng đài<br>ở tất cả các kênh)|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||tương tác trước đó<br>KH gọi lên (khi KH<br>liên hệ lên tổng đài ở<br>tất cả các kênh)|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||4.18|Popup thời gian KH phải chờ đợi<br>và cảnh báo cho ĐTV (chức<br>năng đối thủ có)||Popup số giây cụ thể<br>KH đã phải chờ từ<br>khi vào queue và<br>cảnh báo cho ĐTV<br>Cấu hình số giây<br>trong khoảng nào sẽ<br>hiển thị thêm cảnh<br>bảo kh chờ "LÂU",<br>"RẤT LÂU" và hiển<br>thị màu chữ khác, nổi<br>bật|1. Yêu cầu nghiệp vụ<br>- Popup số giây cụ thể KH đã phải chờ từ khi vào queue và cảnh báo cho ĐTV.<br>- Cấu hình số giây trong khoảng nào sẽ hiển thị thêm cảnh bảo kh chờ "LÂU", "RẤT LÂU"<br>và hiển thị màu chữ khác, nổi bật<br>- Cấu hình màu sắc theo khoảng thời gian chờ đợi, theo queue||
||4.19|Pop up nhận diện tích cách, cảm<br>xúc khách hàng||Chức năng popup<br>tính cách của KH<br>(nếu là KH đã liên hệ<br>tổng đài):<br>- Lấy thông tin tính<br>cách KH từ hệ thống<br>nhận diện cảm xúc<br>KH với KH vừa gọi<br>lại trong vòng x giờ<br>(cấu hình được, vd<br>48h)<br>- Nếu cảm xúc KH là<br>cáu giận, Không hài<br>lòng cần có cảnh báo<br>(cảnh báo ntn?) cho<br>ĐTV biết<br>- Cấu hình được để<br>có thể kết nối đến<br>các hệ thống nhận<br>diện tích cách KH<br>khác nhau của các<br>nhà cung cấp dv khác<br>nhau (đi bán cho các|1. Yêu cầu nghiệp vụ<br>Chức năng popup tính cách của KH theo queue (nếu là KH đã liên hệ tổng đài):<br>- Lấy thông tin tính cách KH từ hệ thống nhận diện cảm xúc KH với KH vừa gọi lại trong<br>vòng x giờ (cấu hình được, vd 48h)<br>- Nếu cảm xúc KH là cáu giận, Không hài lòng cần có cảnh báo (cảnh báo ntn?) cho ĐTV<br>biết<br>- Cấu hình được để có thể kết nối đến các hệ thống nhận diện tích cách KH khác nhau của các<br>nhà cung cấp dv khác nhau (đi bán cho các KH khác nhau có ht  nhận diện khác nhau||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||KH khác nhau có ht<br>nhận diện khác nhau)|||
||4.20|Thay đổi màu sắc nền giao diện<br>cửa sổ POP UP||Hỗ trợ tự động hiển<br>thị 3 màu sắc :<br>- Nền popup màu<br>XANH với các cuộc<br>gọi thông thường<br>- Nền popup màu<br>VÀNG với các cuộc<br>KH thỏa mãn 1 trong<br>các đk sau :<br>+ KH phải chờ lâu<br>+ Khách hàng gọi lại<br>, tương tác lại trên<br>các kênh<br>+ Khách hàng có<br>cảm xúc cáu gắt<br>trong các kênh tương<br>tác khác<br>-Nền popup màu ĐỎ|Hỗ trợ tự động hiển thị 3 màu sắc :<br>- Nền popup màu XANH với các cuộc gọi thông thường<br>- Nền popup màu VÀNG với các cuộc KH thỏa mãn 1 trong các đk sau :<br>+ KH phải chờ lâu<br>+ Khách hàng gọi lại , tương tác lại trên các kênh<br>+ Khách hàng có cảm xúc cáu gắt trong các kênh tương tác khác<br>- Nền popup màu ĐỎ với các KH thỏa mãn 2 trong 3 điều kiện nêu trên<br>- Nếu khách hàng là VIP của 1 trong 2 công ty thì coi là VIP chung của queue đó||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||với các KH thỏa mãn<br>2 trong 3 điều kiện<br>nêu trên|||
||4.21|POP UP danh sách KH vị thế||Lấy thông tin từ hệ<br>thống QLKH Viettel<br>Popup với danh sách<br>KH vị thế<br>Cảnh báo cho ĐTV<br>biết|||
||**5**|**Xử lý trong khi tương tác**|||||
||5.1|Quản lý trạng thái của Agent|||Hiển thị chi tiết thông tin trạng thái của agent trong queue: availble, not_available, no_acd,<br>no_anwser, meeting, at_lunch, go_out, typing.<br>**Go_out**là trạng thái do hệ thống tự set cho Điện thoại viên, khi cuộc gọi đang hold mà khách<br>hàng ngắt máy||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.2|Chuyển trạng thái nếu ĐTV<br>không nhận 3 cuộc liên tiếp|||Chuyển trạng thái làm việc của TVV: Khi tư vẫn viên đang đặt trạng thái sẵn sàng Không<br>nhấc máy cuộc gọi khách hàng 3 lần liên tiếp chuyển trạng thái TVV về NO_ANSWER<br>+ Xây dựng tiến trình check khi tư vẫn viên đang đặt chế độ Available mà không nghe máy<br>cuộc gọi 3 lần của khách hàng tự động chuyển trạng thái agent về NO_ANSWER||
||5.3|Transfer ACD - chuyên gia : cho<br>phép cấu hình chọn : hiển thị số<br>khách hàng, không hiển thị số<br>KH, hiển thị số ảo|||- Tự động tranfeer sang số chuyên gia đã có<br>- Có prefix + số đt khách hàng gửi sang cho chuyên gia cả 2 hình thức (chủ động, tự động)<br>- Tự động: hệ thống tự động transfer cho chuyên gia<br>- Chủ động: TVV lựa chọn chuyên gia để transfer<br>- Cấu hình trên queue (prefix, replace đều ở trong cấu hình queue)<br>Chú ý: transfer chuyên gia sử dụng SIP TRUNK khai 0 đồng (có thể phải xin thêm luồng SIP<br>trunk riêng)||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|5.4|Transfer ACD –ACD : chức<br>năng kiểm tra ĐTV rảnh trên<br>queue đích||1. Yêu cầu nghiệp vụ<br>- Transfer bằng tay<br>- Hiển thị số lượng ĐTV đang rảnh rỗi trong<br>queue ACD đích (là số lượng ĐTV đang chọn chế độ Available nhưng thời<br>điểm transfer không tiếp nhận cuộc gọi) khi sử dụng chức năng transfer<br>ACD – ACD<br>- Chức năng trong cấu hình transfer ACD – ACD: chỉ được<br>phép transfer khi có agent rỗi. Chức năng này chỉ sử dụng được khi cấu hình<br>transfer có Agent trực. Nếu transfer không có Agent trực thì bỏ qua chức<br>năng này.<br>chức năng hiển thị<br>số lượng Agent có thể tiếp nhận cuộc gọi ĐTTM của khu vực khác đối với<br>các queue có cấu hình chức năng ĐTTM|
|5.5|Transfer ACD - IVR : chức năng<br>chuyển IVR khi kết thúc cuộc<br>gọi (ko cần bấm phím - xử lý kết<br>thúc cuộc gọi)||Tương tự hệ thống cũ<br>1. Yêu cầu nghiệp vụ<br>- Kết thúc cuộc gọi: Hết thời gian chờ trong queue<br>- Nếu KH không bấm phím => Cuộc gọi chuyển sang cây IVR khác<br>- Cho chép cấu hình trỏ sang cây IVR nào|
|5.6|Transfer ACD - IVR : chức năng<br>chuyển IVR trong cuộc gọi -<br>ĐTV chuyển cuộc gọi vào IVR||Hệ thống cho phép agent tiếp nhận cuộc gọi trong queue A, thực hiện transfer cuộc gọi đến<br>một callflow khác  là luống IVR.|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.7|Transfer AG –AG : cho phép<br>ĐTV trc khi tranfer thì nói<br>chuyện với người nhận tranfer để<br>trao đổi trc về vấn đề của khách<br>hang sau đó người nhận tranfer<br>mới nói chuyện với khách hàng||Đồng thời tiếp nhận<br>cuộc gọi đến đang<br>hold và gọi ra được<br>luôn, gồm:<br>- gọi ra cho người<br>đang đăng nhập trên<br>HT<br>- gọi ra cho thuê bao<br>di động cố định<br>Sau đó có thể<br>transfer hoặc nối lại<br>cuộc gọivới KH|1. Yêu cầu nghiệp vụ (tham khảo genesys)<br>Đồng thời tiếp nhận cuộc gọi đến đang hold và gọi ra được luôn, gồm:<br>- gọi ra cho người đang đăng nhập trên HT<br>- gọi ra cho thuê bao di động cố định<br>Sau đó có thể transfer hoặc nối lại cuộc gọi với KH<br>- Đối với giám sát nghe lén: nghe được nội dung cuộc đàm thoại của KH vs ĐTV, ĐTV vs<br>ĐTV nhận transfer||
||5.8|Tranfer từ kênh chat sang kênh<br>voice/video OTT (Myviettel):<br>KH đang chat với ĐTV muốn<br>chuyển sang kênh voice/video,<br>ĐTV bấm button Call trên giao<br>diện chat, ht make cuộc gọi OTT<br>ring trên UD MyViettel (thực<br>hiện với các KH cài đặt<br>MyViettel)|||- Kênh voice, appMyViettel, WebPortal mapping qua số điện thoai của KH<br>- Khi tạo Ticket hoặc thống kê thì xác nhận một KH đã tồn tại thì ticet, thống gắn với khách<br>hàng<br>- Trường hợp không xác định KH thì tạo ra 1 KH mới<br>- Tạo một khách hàng mới trên IPCC nếu không đính được khách hàng||
||5.9|Tranfer từ kênh voice sang kênh<br>video trên MyViettel:<br>Khi khách hàng đang trên kênh<br>voice, KH muốn chuyển qua<br>kênh video call (vd để ĐTV kiểm<br>tra modem) thì ĐTV có thể click<br>vào chức năng video call cho<br>khách hàng trên Agent desktop,<br>hệ thống tạo cuộc gọi video call<br>đến KH qua MyViettel|||Tranfer từ kênh voice sang kênh video trên MyViettel:<br>Khi khách hàng đang trên kênh voice, KH muốn chuyển qua kênh video call (vd để ĐTV<br>kiểm tra modem) thì ĐTV có thể click vào chức năng video call cho khách hàng trên Agent<br>desktop, hệ thống tạo cuộc gọi video call đến KH qua MyViettel||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.10|Tranfer từ kênh voice sang kênh<br>video Facebook<br>messenger/Zalo/mocha:<br>Khi khách hàng đang trên kênh<br>voice, KH muốn chuyển qua<br>kênh video call (vd để ĐTV kiểm<br>tra modem) thì ĐTV có thể click<br>vào chức năng video call cho<br>khách hàng trên Agent desktop,<br>hệ thống tạo cuộc gọi video call<br>đến KH (có thể qua Facebook<br>messenger, zalo, mocha)|||1. Yêu cầu nghiệp vụ<br>- Bổ sung chuyến sang kênh Video tiktok (Đánh giá lại)<br>- Tạo menu chuyển từ kênh voice sang các kênh video khác (Fb/Zalo/Mocha)<br>2. Ghi chú<br>- Không chuyển được sang Facebook/Messenger/Tiktok||
||5.11|Tranfer theo lịch, ngày, giờ, thứ|||1. Yêu cầu nghiệp vụ<br>- Cho phép đặt nhiều khung giờ<br>- Tương tự hệ thống cũ||
||5.12|Nhạc tranfer linh hoạt : khi cấu<br>hình tranfer tự động thì thuê bao<br>ưu tiên kênh nguồn cũng được<br>phát ưu tiên ở kênh tranfer|||1. Yêu cầu nghiệp vụ<br>- Tương tự phát nhạc nhờ thuê bao ưu tiên||
||5.13|Nhạc tranfer tự động ACD -<br>ACD :  cho phép cấu hình phát<br>âm nhạc chờ của queue nguồn,<br>quueue đích hoặc phát âm riêng|||1. Yêu cầu nghiệp vụ<br>- Khi cấu hình transfer tự động. Cho phép cấu hình phát nhạc chờ theo queue nguồn, queue<br>đích, file riêng (1 file)||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.14|Nghe nhạc tranfer chuyên gia :<br>Cấu hình file riêng cho từng<br>nhóm chuyên gia|||1. Yêu cầu nghiệp vụ<br>- Cấu hình file nhạc chờ (1 file riêng) cho từng nhóm (bằng tay và tự động). Khi một chuyên<br>gia ở trong nhiều nhóm => nhạc phát cho chuyên gia khi nhận transfer sẽ theo nhóm đã chọn<br>(yêu cầu chọn nhóm trước)<br>- Hiện tại transfer sang chuyên gia chỉ nghe đc 1 file (không sửa được)||
||5.15|Nhạc HOLD|||Cho phép Admin cấu hình 1 file nhạc sẽ phát cho khách hàng nghe khi điện thoại viên thực<br>hiện hold cuộcgọi.||
||5.16|Nghe nhạc HOLD linh hoạt -<br>Chọn chế độ xoayvòng, lặplại..|||1. Yêu cầu nghiệp vụ:<br>- Phát được nhiều file nhạc chờ: Xoayvòng+ lặplại||
||5.17|Nghe nhạc HOLD bắt buộc|||Tương tự hệ thống cũ<br>1. Yêu cầu nghiệp vụ:<br>- Cấu hình thời gian bắt buộc nghe nhạc chờ => Không cho phép unhold (Phím unhold mờ đi<br>+ hiện thời gian đếm ngược)||
||5.18|Cấu hình nhiều file nhạc HOLD|||Tương tự hệ thống cũ<br>1. Yêu cầu nghiệp vụ:<br>Cấu hình nhiều file nhạc HOLD||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|5.19|Kết nối đến hệ thống nhận diện<br>VOICE BIOMETRIC|**Luồng kiểm tra**<br>**nhận diện trong lúc**<br>**đàm thoại:**<br>- ĐTV click button<br>xác minh KH trên<br>giao diện nghiệp vụ<br>BCCS -> BCCS<br>check ht eKYC xem<br>SĐT này đăng kí<br>eKYC chưa-> Nếu<br>có thì BCCS thực<br>hiện gửi yc sang<br>IPCC để IPCC lấy 1<br>phần ghi âm cuộc gọi<br>hiện tại gửi sang ht<br>eKYC -> eKYC so<br>sánh dữ liệu trả về<br>kết quả xác minh trên<br>giao diện BCCS cho<br>ĐTV -> ĐTV dựa<br>vào KQ để thực hiện<br>nghiệp vụ cho KH<br>mà KH không bị hỏi<br>han nhiều.<br>**_(luồng trên IVR thì_**<br>**_đã mô tả trên mục_**<br>**_1.9)_**|1. Yêu cầu nghiệp vụ<br>Luồng kiểm tra nhận diện trong lúc đàm thoại:<br>- ĐTV click button xác minh KH trên giao diện nghiệp vụ BCCS -> BCCS check ht eKYC<br>xem SĐT này đăng kí eKYC chưa-> Nếu có thì BCCS thực hiện gửi yc sang IPCC để IPCC<br>lấy 1 phần ghi âm cuộc gọi hiện tại gửi sang ht eKYC -> eKYC so sánh dữ liệu trả về kết quả<br>xác minh trên giao diện BCCS cho ĐTV -> ĐTV dựa vào KQ để thực hiện nghiệp vụ cho KH<br>mà KH không bị hỏi han nhiều.<br>(luồng trên IVR thì đã mô tả trên mục 1.9)|
|5.20|Trả lời cuộc gọi||Tương tự hệ thống cũ<br>Bổ xung thêm :<br>- Đáp ứng mô hinh 1 ĐTV trả lời queue cho 2 cty<br>- 1 Công ty chủ dịch vụ thuê 2 đơn vị Out tiếp nhận phản ánh của khách hàng<br>=> VTS đánh giá (tương tự như các kênh khác)|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|5.21|Hold/Unhold cuộc gọi,||Cho phép điện thoại viên thực hiện HOLD/ UNHOLD cuộc gọi mà agent đang trả lời khách<br>hàng.|
|5.22|Bắt buộc phát hết nhạc HOLD<br>mới đc Unhold||Trùng 5.17|
|5.23|Chuyển cuộc gọi||Sau khi tiếp nhận cuộc gọi vào của khách hàng, cho phép điện thoại viên chủ động chuyển<br>cuộc gọi đến các đích khác nhau: ACD (queue khác), IVR nào đó hoặc chuyên gia.|
|5.24|Kết thúc cuộcgọi||Chophépđiện thoại viên chủ độngkết thúc cuộcgọi.|
|5.25|Mute/Umute cuộc gọi||Cho phép điện thoại viên thực hiện MUTE/UNMUTE cuộc gọi mà agent đang trả lời khách<br>hàng.|
|5.26|Chuyển trạng thái Agent||Cho phép điện thoại viên chủ động thay đổi trạng thái tiếp nhận cuộc gọi : chọn 1 trong các<br>chế độ sau:<br>- Available<br>- Not Available<br>- Lunch<br>- Meeting<br>- Training<br>- Break.<br>Hệ thống tự động chuyển trạng thái của điện thoại viên thành:<br>- Connecting: khi có cuộc gọi ring đến điện thoại viên<br>- Connected: khi điện thoại viên trả lời cuộc gọi<br>- Wrapup: khi điện thoại viên ở trạng thái after call work|
|5.27|Hiển thị thông tin cá nhân||1. Yêu cầu nghiệp vụ<br>- Hiển thị thông tin Agent<br>- Tương tự hệ thống cũ|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.28|Hiển thị cảnh báo về thời gian<br>đàm thoại|||Tương tự hệ thống cũ<br>1.Yêu cầu nghiệp vụ<br>- Cho phép cấu hình được thời gian cảnh báo<br>- Trong quá trình điện thoại viên trả lời khách hàng, khi thời gian trả lời vượt quá mức cấu<br>hình thời gian trả lời cho phép, hệ thống hiển thị cảnh báo trên màn hình của điện thoại viên||
||5.29|Nghe cuộc gọi online|||Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin<br>của hệ thống có thể thực hiện nghe online cuộc gọi giữa điện thoại viên và khách hàng.||
||5.30|Tham gia vào cuộc gọi|||Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin<br>của hệ thống có thể thực hiện tham gia vào cuộc gọi giữa điện thoại viên và khách hàng --<br>>cuộc gọi trở thành cuộc gọi 3 bên.||
||5.31|Cướp cuộc gọi|||Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin<br>của hệ thống có thể thực hiện cướp cuộc gọi của điện thoại viên với khách hàng, luồng cuộc<br>gọi của agent bị ngắt||
||5.32|Nghe lén|||Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin<br>của hệ thống có thể thực hiện nghe lén cuộc gọi giữa điện thoại viên và khách hàng.<br>Điện thoại viên, Khách hàng không biết đến hàng động này.||
||5.33|Chuyển trạng thái của Agent từ<br>xa|||Giám sát viên hoặc Admin của hệ thống có thể thay đổi trạng thái tiếp nhận cuộc gọi của các<br>điện thoại viên.||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.34|Hiển|thị lịch sử cuộc gọi||Hiển thị thông tin lịch sử cuộc gọi:<br>Số gọi từ, Số gọi đến, Tên queue ACD, Thời gian vào ACD, tên agent tiếp nhận, Thời gian<br>bắt đầu cuộc gọi, Thời điểm kết thúc cuộc gọi.||
||5.35|Hiển|thị thông tin cuộc gọi||Khi điện thoại viên tiếp nhận cuộc gọi inbound ring tới mình, trên màn hình hiển thị các<br>thông tin:<br>số điện thoại khách hàng, tên queue ACD, đếm thời gian trả lời.||
||5.36|Trưởng nhóm ngắt cuộc gọi của<br>điện thoại viên|||Khi điện thoại viên đang trả lời cuộc gọi inbound của khách hàng, Giám sát viên hoặc Admin<br>của hệ thống có thể chủ động kết thúc cuộc gọi giữa điện thoại viên và khách hàng.||
||5.37|Quản lý Queue|||Tương tự hệ thống cũ<br>1. Yêu cầu nghiệp vụ<br>- Cho phép gán ĐTV vào queue<br>- Quản lý agent theo zone và lọc theo zone<br>- Cty=>khu vực => nhóm (theo vị trí, theo quản lý)||
||5.38|Giám sát queue|||Tương tự hệ thống cũ<br>1. Yêu cầu nghiệp vụ<br>- Cho phép giám sát nhiều đơn vị<br>- Phân quyền theo queue, đơn vị<br>- Mô hình giám sát: 1 user giám sát đc bản thân, 1 user giám sát các dịch vụ trong cty, 1 user<br>giám sát được cả bên trong cty và bên ngoài cty, 1 user giám sát được nhiều khu vực||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.39|**Chat**|**nội bộ**|Hiện tại, hệ thống<br>IPCC đã có tính năng<br>Chat cho Điện thoại<br>viên (ĐTV) và nhân<br>viên BO có thể thực<br>hiện Chat trong ca<br>trao đổi thông tin.<br>Tuy nhiên hệ thống<br>chưa có tính năng<br>chặn chiều Chat theo<br>đối tượng người sử<br>dụng, do đó cần thực<br>hiện nâng cấp chức<br>năng để hệ thống<br>đảm bảo quản lý và<br>kiểm soát được các<br>chiều Chat thông tin<br>theo từng đối tượng|1. Yêu cầu nghiệp vụ<br>- Hiện tại, hệ thống IPCC đã có tính năng Chat cho Điện thoại viên (ĐTV) và nhân viên BO<br>có thể thực hiện Chat trong ca trao đổi thông tin. Tuy nhiên hệ thống chưa có tính năng chặn<br>chiều Chat theo đối tượng người sử dụng, do đó cần thực hiện nâng cấp chức năng để hệ<br>thống đảm bảo quản lý và kiểm soát được các chiều Chat thông tin theo từng đối tượng<br>'- Mới chỉ gửi text (chat thông thường)<br>- Cho phép gửi Media, file, hình ảnh, biểu tượng, emoji||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.40|Hiển|thị danh sách chat||1. Yêu cầu nghiệp vụ<br>- 3 nhóm: Trưởng ca, giám sát…<br>- Chưa phân quyền<br>2. Đề xuất chức năng<br>- Hiển thị danh sách nhóm chat:<br>- Chia nhiều cấp cấp trên nhìn cấp dưới<br>- ĐTV chỉ chat trong nhóm<br>- GS Viettel quản lý GS Hoa sao, kim cương, GS kim cương HCM<br>- KHông cho ĐTV chat trong nhóm<br>- Cho phép ĐTV chat lại với cấp trên giám sát<br>- Cho add nhóm vật lý, nhóm nghiệp vụ<br>- Nhóm nghiệp vụ thì liên quan đến queue<br>- Nhóm vật lý thì từ mức đối tác trở xuống<br>- Viettel GS tất cả các đối tác<br>- Công ty quản lý các đối tác<br>- Đối tác có superviser GS của đối tác<br>- CHo phép add nhóm động||
||5.41|Thay|đổi trạng thái của user chat||Thay đổi trạng thái tiếp nhận chat: sẵn sàng nhận chat (available), đang bận hoặc không tiếp<br>nhận chat (not available)||
||5.42|Tìm kiếm user chat|||1. Chức năng tìm kiếm user chat theo thông tin được nhập<br>Điều kiện đảm bảo<br>2. Phân quyền:<br>Phân quyền cho từng loại và vai trò trên vsa||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.43|Chat|1-1||Giao diện chat<br>Tiếp nhận và hiển thị tin nhắn<br>Lưu trữ xử lý tin nhắn||
||5.44|Chat|nhắc nhở||1. Yêu cầu nghiệp vụ<br>- Chủ dv chat toàn bộ<br>- Làm thuê chat cho trong nhân sự  của đơn vị làm thuê<br>2. Đề xuất chức năng<br>- Đối tượng phân quyền được gửi gì (ĐTV, TVV, lãnh đạo)<br>- Cho thêm quản lý nhóm chat (Trường nhóm add nhóm) (Trùng với yêu cầu): giám sát viên<br>Nhắn cho nhiều nhóm tuy vào từng quyền<br>- Cấu hình không cho phép ĐTV nhắn với nhau||
||5.46|Chat|theo nhóm||- Chophép giám sát tạo nhóm chat trao đổi nghiệpvụ||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.47|Yêu cầu trợ giúp|||1. Yêu cầu nghiệp vụ<br>- Có trợ giúp của giám sát chưa có trợ giúp của trưởng ca, trưởng nhóm, agent<br>- Agent xin trợ giúp cấp trên (không xin trợ giúp ngang cấp)<br>- Có màn hình chát hỗ trợ màn hình có vùng dữ liệu (trưởng ca trưởng nhóm, giám sát), nội<br>dung hỗ trợ, hình thức hỗ trợ (chat, điện thoại)<br>- Có hình thức cảnh báo cho ông nhận hỗ trợ biết thông tin trợ<br>- thiết lập 1 luông chat giữa 2 cán bộ hỗ trợ và cán bộ nhân hỗ trợ<br>- Với hỗ trợ theo luồng voice thì cuộc gọi của khách hàng sẽ được hold trong khi chờ trợ giúp<br>2. Đề xuất chức năng||
||5.48|Trưởng nhóm tìm kiếm trạng thái<br>agent|||1. Yêu cầu nghiệp vụ<br>'- Phân quyền chức năng tìm kiếm trạng thái agent<br>- Dữ liệu chỉ hiện thị các ĐTV trong đơn vị tổ chức mà Trưởng ca đó đang thuộc vào (thuộc<br>nhóm vật lý)<br>2. Đề xuất chức năng<br>- Đề xuất đưa vào giám sát agent và hiển thị theo dữ liệu theo phạm vi quản lý<br>- Các tiêu chí như hệ thống cũ (bỏ IP phone)||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|5.49|Trưởng ca tìm kiếm trạng thái<br>agent|Bổ xung thêm ngoài<br>giao diện như tìm<br>kiếm trên AD hiện<br>tại:<br>Hệ thống cảnh báo<br>cuộc gọi của NV dài<br>quá thời gian quy<br>định (ví dụ 6 phút)<br>để giám sát có thể<br>nghe song song hỗ<br>trợ. Hệ thống có thể<br>cảnh báo nếu NV để<br>sai chế độ ví dụ away<br>from desk hơn 30<br>phút. Hệ thống có thể<br>cảnh báo khi số<br>lượng cuộc gọi<br>chờ/số lượng email<br>chưa được xử lý/số<br>tương tác mạng xã<br>hội chưa được xử lý<br>vượt quá số lượng<br>quy định. Số lượng<br>hoặc thời gian có thể<br>chủ động tùy chỉnh.|Bổ xung thêm ngoài giao diện như tìm kiếm trên AD hiện tại:<br>Hệ thống cảnh báo cuộc gọi của NV dài quá thời gian quy định (ví dụ 6 phút) để giám sát có<br>thể nghe song song hỗ trợ. Hệ thống có thể cảnh báo nếu NV để sai chế độ ví dụ away from<br>desk hơn 30 phút. Hệ thống có thể cảnh báo khi số lượng cuộc gọi chờ/số lượng email chưa<br>được xử lý/số tương tác mạng xã hội chưa được xử lý vượt quá số lượng quy định. Số lượng<br>hoặc thời gian có thể chủ động tùy chỉnh.<br>**Đề xuất:**<br>**- Đã đáp ứng ở chức năng GS thông tin cuộc gọi**|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.50|Cảnh báo tự động, cảnh báo<br>cưỡng bức, cảnh báo thời gian<br>đàm thoại||Bổ xung thêm cảnh<br>báo cho ĐTV:<br>Hệ thống cảnh báo<br>(Tạo notification)<br>toàn bộ nhân viên<br>đang login khi cuộc<br>gọi trong hàng chờ<br>vượt quá số lượng<br>cài đặt (số này có thể<br>chủ động cài đặt theo<br>thời gian, theo queue,<br>tần xuất cảnh báo).|Bổ xung thêm cảnh báo cho ĐTV:<br>Hệ thống cảnh báo (Tạo notification) toàn bộ nhân viên đang login khi cuộc gọi trong hàng<br>chờ vượt quá số lượng cài đặt (số này có thể chủ động cài đặt theo thời gian, theo queue, tần<br>xuất cảnh báo).<br>**Đề xuất:**<br>- Bổ sung 1 chức năng cảnh bảo khi hệ thống đến ngưỡng thì sẽ cảnh báo, cảnh báo cho TVV,<br>GS<br>- Cho phép cấu hình theo màu cảnh báo<br>- Cảnh báo màn hình: màn hình ĐTV và màn hình của GS<br>- TungTV đề xuất đưa vào bài toán ngẽn||
||5.51|Cảnh báo các chế độ quá thời<br>gian cho ĐTV trên AD|||- Giữ nguyên như hệ thống 1<br>- Cảnh báo các chế độ quá thời gian cho ĐTV trên AD (Hiển thị cho từng ĐTV)<br>- Cấu hình theo từng queue||
||5.52|Cảnh báo cho giám sát|||1. Yêu cầu nghiệp vụ<br>- Cảnh báo của DTV cũng hiện trên màn hình của ông giám sát<br>2. Đề xuất chức năng||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.53|Tinh năng hạn chế người dùng<br>chuyển chế độ trên<br>AgentDesktop|||1. Yêu cầu nghiệp vụ<br>' - Căn cứ tỷ lệ ngẽn hệ thống (cấu hình được)<br>- Thỏa mãn tất cả các queue<br>2. Đề xuất chức năng<br>- Bổ sung tham số % ĐTV avaiable/Tổng số user đăng nhập/Queue<br>- Quá số thì không cho chuyển và cảnh bảo<br>- Cho phép GS mở được trạng thái cho người xin||
||5.54|Transfer AG - AG|||1. Yêu cầu nghiệp vụ<br>- Giống hệ thống cũ<br>2. Đề xuất chức năng<br>- Giữ nguyên từ hệ thống cũ<br>- Bổ sung kiểm tra trạng thái avaiable và chỉ chuyển trạng trong queue<br>- Bổ sung trưởng nhóm, trưởng ca có thể chuyển cuộc từ AG này sang AG khác trong cùng<br>queue||
||5.55|Transfer AG - Supervisor|||1. Yêu cầu nghiệp vụ<br>- Lấy được Supervisor quản lý ông AG đó<br>2. Đề xuất chức năng<br>Chỉ chuyển được tới Supervíor quản lý nhóm của AG đó||
||5.56|Transfer AG – Chuyên gia (phân<br>biệt với cuộcgọi thôngthường)|||Transfer AG – Chuyên gia (phân biệt với cuộc gọi thông thường). ĐTV chủ động chuyển<br>sangchuyêngia||
||5.57|transfer từ ACD – sang các kênh<br>khác và tranfer giữa các kênh|||Tham khảo 5.7; 5.8; 5.9; 5.10<br>-Tranfer từ ACD - sang các kênh khác (Hệ thống đang có )||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.58|Đa kênh (voice, video, Email,<br>Chat, Social – Facebook, Mocha,<br>Zalo…)|||1. Yêu cầu nghiệp vụ<br>- Cho phép xem lịch sử tương tác KH đa kênh (Các kênh trong IPCC, các kênh ngoài IPCC)<br>- Cho phép xem lịch sử xử lý với từng Khách hàng, với nhiều khách hàng, lịch sử tương tác,<br>lịch sử phản ánh<br>- Xem thông tin KH đa kênh<br>- Tương tác với KH trên kênh bất kỳ<br>2. Đề xuất chức năng||
||5.59|Đa kênh trên cùng giao diện - all<br>in one|||1. Yêu cầu nghiệp vụ<br>- Hiển thị thông tin theo đặc thù từng kênh<br>2. Đề xuất chức năng||
||5.60|Nhận diện khách trên các kênh<br>khác nhau - Customer jouney|||1. Yêu cầu nghiệp vụ<br>- Cho phép cấu hình thông tin hiển thị: Công ty (chủ dịch vụ), kênh tương tác, nguồn dữ liệu:<br>IPCC, mBCCS, app của các nhà cung cấp dịch vụ, tương tác tại cửa hàng.vv<br>- Hiển thị lịch sử tương tác, popup theo kênh tương tác, chủ sở hữu dịch vụ<br>- Cấu hình động theo từng nguồn thông tin<br>-<br>2. Đề xuất chức năng||
||5.61|Popup lịch sử tương tác với BOT|||1. Yêu cầu nghiệp vụ<br>- Hiển thị lịch sử tương tác với bot (theo các kênh), tên bot (nguồn nào)<br>2. Đề xuất chức năng||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||5.62|Popup & TAG khi Transfer<br>(tham khảo Mitek)||Bổ xung chức năng<br>tag nội dung khi<br>tranfer (tham khảo<br>Mitek):<br>+ Chọn loại chủ để<br>KH hỏi theo danh<br>mục sẵn có để TAG<br>khi chuyển tranfer<br>+ Cho ô để ĐTV<br>nhập nội dung KH<br>phản ánh chi tiết khi<br>chuyển, nd này có<br>thể copy từ ô ĐTV<br>nhập trên BCCS để<br>tranfer|Bổ xung chức năng tag nội dung khi tranfer (tham khảo Mitek):<br>- Popup thông tin khi transfer giữa các kênh<br>- Cho phép nhập ghi chú khi transfer||
||**6**|**Xử lý kết thúc tương tác**|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|6.1|Kết thúc thông thường,**tạo**<br>**TICKET**<br>(tham khảo thêm phần 12.2.8 -<br>các chức năng phần mạng xã hôi)|**- Tự động tạo**<br>**TICKET đối với**<br>**kênh thoại cũng**<br>**như các kênh khác**<br>**cho cả 2 chiều**<br>**INbound/Outbound**<br>**- TICKET có thể**<br>**mapping với 1 bản**<br>**ghi trên hệ thống**<br>**CRM của 1 đơn vi**<br>**khác (BCCS_CC),**<br>**CRM của**<br>**VTPost...)**<br>**- Bổ xung chi tiết**<br>**danh sách THUỘC**<br>**TÍNH của 1**<br>**TICKET**<br>**Ngoài ra lưu ý các**<br>**bất cập ht cũ:**<br>Hiện tại khi Giám sát<br>thực hiện giao lại<br>ticket thủ công cho<br>NVCSKH gặp tình<br>trạng: hệ thống<br>Econtact hiển thị<br>toàn bộ NVCSKH<br>bao gồm cả<br>NVCSKH đang<br>online (NVCSKH đi<br>làm) và offline<br>(NVCSKH không đi<br>làm) dẫn đến tình<br>trạngnhầm lẫntrong|1. Yêu cầu nghiệp vụ<br>- Tự động tạo TICKET đối với kênh thoại cũng như các kênh khác cho cả 2 chiều<br>INbound/Outbound<br>- TICKET có thể mapping với 1 bản ghi trên hệ thống CRM của 1 đơn vi khác (BCCS_CC),<br>CRM của VTPost...)<br>- Bổ xung chi tiết danh sách THUỘC TÍNH của 1 TICKET<br>Trao đổi :<br>Định hướng : 100% các phản ánh phải được tiếp nhận và xử lý, cần có giải pháp cho các<br>trường hợp không dc xử lý trên kênh phi thoại<br>Hiện tại : đối với Voice đã có chức năng gọi lại tự động, đang đề xuất thêm chức năng hẹn<br>gọi lại. Với các kênh khác đề xuất bổ xung<br>Trao đổi :<br>- Với kênh FB đã có định danh, VTS đã hiểu mong muỗn<br>- Với kênh Chat web : cần xử lý với KH không định danh<br>+ Xây dựng chức năng cho khách hàng để lại thông tin liên hệ<br>+ Xây dựng chức năng phân phối lại phản ánh đến ĐTV với các KH để lại thông tin liên hệ,<br>có ưu tiên xử lý<br>+ Khi phân phối lại có hiện thị lịch sử trước đó<br>+ Có thể ON/OFF chức năng này chủ động trong quá trình khai thác|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||quá trình giao (hình<br>ảnh bên dưới).<br>-Mong muốn nâng<br>cấp:<br>+ Ưu tiên hiển thị<br>danh sách các<br>NVCSKH đang<br>online lên đầu.<br>+ Có ký hiệu nhận<br>biết để phân biệt<br>giữa NVCSKH đang<br>online và offline.<br>(tham khảo thêm<br>phần 12.2.8 - các<br>chức năng phần<br>mạng xã hôi)||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||6.2|Chuyển cuộc gọi sang ht survey<br>tập trung|||1. Yêu cầu nghiệp vụ<br>- Bổ sung cho tất cả các kênh<br>- Gửi survey sms theo đầu số và sđt khách hàng<br>- Kênh thoại survey qua sms; kênh chat survey trực tiếp||
||6.3|Survey ngay trên IPCC||Yêu cầu phân quyền<br>- Queue (các  kênh)<br>nghiệp vụ nào thực<br>hiện survey thì chỉ có<br>đơn vị đó được tác<br>động cấu hình, thực<br>hiện survey và xuất<br>báo cáo<br>- Trường hợp 1 đầu<br>số thoại có 2 nhánh<br>ACD, mỗi nhánh<br>thuộc 1 cty thì nhánh<br>của cty nào dc tác<br>động đến các chiến<br>dịch survey của kênh<br>đó<br>(bất cập ht IPCC 1.0<br>là không thể cấp<br>quyên cấu hình<br>servey cho các đơn<br>vị khác như VTP...)|1. Yêu cầu nghiệp vụ<br>- Survey qua email<br>- Survey qua USSD<br>- Survey qua sms<br>- Survey trực tiếp (chat)<br>- Survey qua IVR||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||6.4|Gửi tin nhắn giới thiệu cho KH<br>linh hoạt, cấu hình được theo<br>line, theo giờ, theo hạng…|||1. Yêu cầu nghiệp vụ<br>- Cấu hình sms campaign: Cấu hình gửi tin nhắn theo thời gian, queue, add danh sách KH<br>(insert thủ công hoặc kết thúc của 1 queue), nội dung tin nhắn, template sms (CRUD).<br>- Trước khi gửi tin nhắn check KH có thuộc danh sách không nhận tin nhắn hay không<br>(Bổ xung: Sms các kênh khác  Bổ sung tính năng gửi tin nhắn truyền thông chủ động tới các<br>KH sử dụng Zalo, Mocha, MyViettel, Facebook để quảng bá/khảo sát KH,… khi sử dụng<br>dịch vụ.)||
||6.5|Survey all kênh/ đa kênh||- Survey voice<br>- Survey IVR<br>- Survey Chat,<br>- Survey Videocall|1. Yêu cầu nghiệp vụ<br>- Survey voice<br>- Survey IVR<br>- Survey Chat,<br>- Survey Videocall||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|6.5.1|6.5.1 Survey Voice|Có các lựa chon sau :<br>- Cấu hình được cuộc<br>gọi chỉ voice sang<br>survey<br>- Cấu hình được chỉ<br>gửi survey các cuộc<br>gặp ĐTV<br>- Cấu hình được chỉ<br>gửi survey các cuộc<br>gặp BOT (nếu cuộc<br>gọi KH vào queue<br>nghe hết nhạc chờ<br>sang BOT luôn thì<br>IPCC không gửi<br>survey ACD nữa)<br>Bất cập Hiện tại :<br>- Khi cấu hình<br>queeue chuyển BOT<br>thì mỗi cuộc chuyển<br>BOT hê thống IPCC<br>hiểu đó là ĐTV kết<br>thúc cuộc gọi và thực<br>hiện gửi lệnh sang ht<br>survey tập trung, sau<br>đó BOT lại gửi lần<br>nữa, nếu KH đó lại<br>được chuyển lại<br>IPCC để gặp ĐTV<br>thì lại được survey<br>thêm lần thứ 3|Có các lựa chon sau :<br>- Cấu hình được cuộc gọi chỉ voice sang survey<br>- Cấu hình được chỉ gửi survey các cuộc gặp ĐTV<br>- Cấu hình được chỉ gửi survey các cuộc gặp BOT (nếu cuộc gọi KH vào queue nghe hết nhạc<br>chờ sang BOT luôn thì IPCC không gửi survey ACD nữa)<br>1. Yêu cầu nghiệp vụ<br>Lựa chọn được các cấu hình cho survey|
|6.6|Voice mail||1. Cho phép để lại voice mail trong TH queue có cấu hình để lại voice mail (hướng dẫn KH<br>để lại Voice mail)|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||6.7|Nhạc kết thúc cuộc gọi (nhạc<br>peep)khi KH kết thúc trước|||1. KH kết thúc trước => có nhạc riêng để ĐTV biết được thông tin. Cấu hình theo từng queue||
||6.8|Thăm dò ý kiến Khách hàng qua<br>IVR (đề xuất này GĐ yêu cầu<br>PGS bổ xung nghiệp vụ|||- Thăm dò ý kiến Khách hàng qua IVR . Tương tự hệ thống cũ<br>- Bổ sung báo cáo||
||6.9|Phát âm để hỏi KH có đồng ý<br>Khảo sát không? Có thìgửi|||Phát âm để hỏi KH có đồng ý Khảo sát không? Có thì gửi||
||6.10|Khách hàng chọn không đồng ý<br>khảo sát thì không gửi|||Khách hàng chọn không đồng ý khảo sát thì không gửi||
||6.11|Khách hàng không lựa chọn thì<br>vẫngửi khảo sát|||Khách hàng không lựa chọn thì vẫn gửi khảo sát||
||6.12|Thống kê tỉ lệ khao sát theo loại<br>KH đồng ý và hệ thống tự<br>chuyển|||Thống kê tỉ lệ khao sát theo loại KH đồng ý và hệ thống tự chuyển||
||6.13|Thăm dò ý kiến Khách hàng qua<br>SMS||Có thể chọn được<br>đầu số SMS để thực<br>hiện survey với mỗi<br>queue.<br>Có thể nhiều queue<br>dùng chung 1 đầu số<br>để survey<br>(Sau này nếu bán<br>dịch vụ cho các đơn<br>vị ngoài, mỗi đơn vị<br>sẽ yêu cầu 1 đầu số<br>SMS riêng để gắn<br>với ALIAS của đơn<br>vị đó khi thực hiện<br>survey trên các kênh<br>dịch vụ của đơn vị<br>đó)|- Tích hợp với Survey tập trung và xây dựng mới<br>- Có thể chọn được đầu số SMS để thực hiện survey với mỗi queue.<br>- Có thể nhiều queue dùng chung 1 đầu số để survey<br>(Sau này nếu bán dịch vụ cho các đơn vị ngoài, mỗi đơn vị sẽ yêu cầu 1 đầu số SMS riêng để<br>gắn với ALIAS của đơn vị đó khi thực hiện survey trên các kênh dịch vụ của đơn vị đó)||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|6.14|Chuyển cuộc gọi từ ACD sang<br>IVR||- Khi kết thúc cuộc gọi chủ động và tự động (nhỡ) chuyển cuộc gọi từ ACD sang IVR|
|6.15|Chuyển cuộc gọi từ ACD sang<br>ACD||- Bao gồm chuyển chủ động và chuyển tự động|
|**7**|**Gọi ra**|||
|7.1|Cấu hình dạng số được phép gọi<br>ra||Mục đích để chặn gọi quốc tế, ngoại mạng,vv|
|7.2|Cấu hình giờ được gọi ra, theo<br>ngày, theo thứ, hỗ trợ nhiều<br>khoảng giờ<br>Gọi ra theo lịch hẹn (tự động) (<br>tự điền thêm khách hàng vào<br>danh sách gọi lại )|- Cấu hình gọi ra<br>theo giờ áp dụng<br>theo từng Queue<br>- Với queue gọi ra<br>cho phép cấu hình<br>mapping với 1<br>trường thông tin nào<br>đó trên 1 chiến dịch<br>thuộc modun chiến<br>dịch để tự động kích<br>hoạt cuộc gọi ra<br>- Vd : Khi KH hẹn<br>gọi lại, ĐTV nhập<br>thông tin yc gọi lại<br>trên IPCC, hệ thống<br>tự validate thông tin<br>ĐTV nhập, đến thời<br>điểm cần gọi ht tự<br>động make cuộc gọi<br>ra,  popup lý do gọi<br>ra cho ĐTV nếu<br>ĐTV O thì make<br>cuộc gọi đến KH ,<br>trường hợp KH ko<br>nghe máy thì ht sẽ<br>gọi lại theoQĐ và|- Cấu hình giờ được gọi ra, theo ngày (ngày cụ thể trong năm dd/mm/yyyy), theo thứ, hỗ trợ<br>nhiều khoảng giờ, cấu hình theo queue<br>- Cấu hình gọi ra theo lịch hẹn tự động: ĐTV có thể nhập thông tin gọi lại cho KH (khoảng<br>thời gian hẹn gọi lại, khoảng cách giữa 2 lần gọi, số lần gọi tối đa, cấu hình queue gọi ra, nội<br>dung cuộc gọi trước). Đến thời gian hẹn gọi lại hệ thống tự động gọi ra cho KH<br>- Đối với khách hàng có Định danh thì phản ánh theo các kênh<br>- Đối với khách hàng không định danh hỗ trợ khách hàng bổ sung thêm thông tin nếu  khách<br>hàng cần phản hồi sau khi bị lỡ (chat bạn bị lỡ, bạn cần gặp TVV thì đề nghị để lại thông tin<br>(email, SĐT) để TVV liên lạc, có thể đưa vào chiến dịch HPC.<br>- Đối với các chat lỡ thì có cớ chế cho phân phối lại và cho phép cấu hình để đưa các chat lỡ<br>đưa tới TVV với mức độ ưu tiên.<br>- Bổ sung các chiến dịch cho các kênh khách khi cần truyền thông|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||thông báo cả số lần<br>đã gọi ra trc đó<br>nhưng KH ko nghe<br>máy để ĐTV nắm<br>được<br>**_(Tương tự trên các_**<br>**_kênh khác có thể_**<br>**_thiết lập chiến dịch_**<br>**_outbound : Zalo_**<br>**_broadcast, SMS_**<br>**_Broadcast, Email_**<br>**_Broadcast ...vd nhắc_**<br>**_cm sinh nhat)_**||
|7.3|Cấu hình thay đổi số hiển thị gọi<br>ra||- Cấu hình thay đổi số hiển thị gọi ra<br>- Có prefix + số đt khách hàng hoặc thay thế gửi sang cho chuyên gia cả 2 hình thức (chủ<br>động, tự động)|
|7.4|Check DNC khi gọi ra||- Check hạn nghạch cuộc gọi quảng cáo|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||7.4.1|Đồng bộ KH DNC và tích hợp hệ<br>thống quảng lý tương tác TT||- Đồng bộ danh sách<br>KH đăng kí DNC<br>qua 5656 (ht của Cục<br>TTTT)<br>- Đồng bộ danh sách<br>KH đăng kí DNC<br>qua 197 (ht của<br>VTT)<br>- Check quotar đến<br>hệ thống quản lý<br>tương tác tập trung|- Đồng bộ danh sách KH đăng kí DNC qua 5656 (ht của Cục TTTT)<br>- Đồng bộ danh sách KH đăng kí DNC qua 197 (ht của VTT)<br>- Check quotar đến hệ thống quản lý tương tác tập trung||
||7.5|Check TB gọi ra có phải TB<br>đăng kí voice mail hay nhạc chờ<br>khi gọi ra|||- Tất cả các trường hợp<br>Các chiến dịch tự động gọi cho khách hàng trước||
||7.6|Định tuyến router callout tách<br>biệt với call in|||- Định tuyến tách biệt callout và callin<br>- Để đảm bảo cuộc gọi ra không bị quay ngược lại đầu số callin của HT||
||7.7|SMS MCA đúng số cần hiển thị<br>khigọi ra nhỡ cho KH|||- Không liên quan đến HT IPCC đề xuất bỏ ( thuộc hệ thống của bên VAS đã sửa)||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|7.8|Khi KH gọi lại các số đã gọi ra<br>thì POPUP các thông tin đã gọi<br>ra trước đó|Cần làm kĩ<br>- Mục tiêu là quản lý<br>được thời gian phản<br>hồi lại cho khách<br>hàng nhanh hay<br>chậm|1. Yêu cầu nghiệp vụ<br>Cần làm kĩ<br>- Mục tiêu là quản lý được thời gian phản hồi lại cho khách hàng nhanh hay chậm.<br>- Mỗi cuộc gọi và phiên tương tác IPCC sinh ra ID => Hiển thị cho ĐTV + chuyển ID, thời<br>gian giao dịch, kênh giao dịch sang Ứng dụng khác.<br>- Nhận thông tin mã giao dịch từ Ứng dụng khác<br>- Cấu hình thông tin ID cuộc gọi của queue gửi sang hệ thống nào<br>- Sử dụng với các ứng dụng khác có CRM và không có CRM<br>2. Đề xuất<br>- Hiển thị các cuộc gọi ra theo cùng công ty ( User thuộc công ty)<br>- Bổ sung phân quyền cho phép khai thác cuộc gọi theo mô hình<br>-|
|7.8.1|Popup gọi ra từ BCCS (cũng như<br>các UD khác) xem phần call in|Cần làm kĩ<br>- Mục tiêu là quản lý<br>được thời gian phản<br>hồi lại cho khách<br>hàng nhanh hay<br>chậm|Tương tự như trên<br>- Thông tin trên PopUp: số đã gọi ra, kênh gọi ra, người gọi ra, thời gian gọi ra<br>- TT CSKH cần phản hồi lại|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||7.9|Khi chuyển cuộc gọi tới di động<br>yêu cầu hiển thị đúng số di động<br>của khách hàng à Trường hợp<br>hiển thị đúng số di động của<br>khách hàng thì tổng đài sẽ tính<br>cước cho số khách hàng, đồng<br>thời hệ thống IPCC cũng sẽ tính<br>cước gọi lên tổng đài, khách<br>hàng sẽ bị tính cước hai lần. Cần<br>confirm lại cách làm.<br>Vì vậy đối với luồng này ipcc<br>cho qua sip trunk khác và ko<br>khai cước cho síp trunk này tránh<br>kh bị tính cước 2 lần|||- Bổ sung luồng sip trunk nếu tranfer chuyên gia thì tùy queue có thể chọn đượcluồng sip<br>trunk<br>- Để khai phí 0 đồng cho sip trunk này (tùy theo quy định)||
||7.10|Luồng tự động gọi lại cấu hình<br>số gốc (tính cước) nhưng vẫn<br>hiển thị số chung 2660198|||Như hiện tại<br>Luồng tự động gọi lại cấu hình số gốc (tính cước) nhưng vẫn hiển thị số chung 2660198||
||7.11|Popup khi gọi ra||- Hiển thị các màn<br>hình popup khi gọi ra<br>- Hiển thị các cảnh<br>báo khi gọi ra từ giao<br>diện:<br>+ Popup DNC<br>+ Popup Quotar|- Hiển thị các màn hình popup khi gọi ra<br>- Hiển thị các cảnh báo khi gọi ra từ giao diện:<br>+ Popup DNC<br>+ Popup Quotar<br>- Quota thì đội dự án đề xuất||
||7.12|Gọi ra từ các hệ thống khác:<br>- Gọi ra từ BCCS<br>- Gọi ra từ Happy call<br>- Gọi ra từ hệ thống khác (nâng<br>cấp nếu phát sinh)|||IPCC cung cấp các API để các hệ thống khác tích hợp để gọi ra||
||**8**|**Xử lý call back**|||||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||8.1|**Voice call back (auto call back)**||**Callbacks:**<br>**https://help.mypure**<br>**cloud.com/articles/a**<br>**bout-callbacks/**|**Hiện tại có chức năng tự động gọi lại KH nhỡ**<br>**(có nên xây dựng chức năng để KH đăng kí gọi lại trên queue chờ ACD)**<br>- Callback cho Agent:<br>Voice interactions for agents overview<br>Place, transfer, and dismiss a callback<br>Schedule callbacks during a voice interaction<br>Schedule a callback in a script<br>- Callbacks for administrators and contact center managers:<br>Scheduled Callbacks view<br>Add a rule<br>Callbacks in campaigns<br>Schedule callbacks from a website||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||8.2|Gọi lại KH thường|||Gọi lại khách hàng thường: cho phép tự động gọi lại khách hàng thường khi bị nhỡ:<br>1. Cấu hình tham số gọi lại khách hàng thường thỏa mã các tham số mô tả bên dưới-> hệ<br>thống tự động thực hiện cuộc gọi lại cho khách hàng thường khi bị nhỡ<br>2. Thêm mới màn hình báo cáo/thống kê cuộc gọi lại tự động: Thống kê thông tin cuộc gọi tự<br>động trong ngày<br>+ Cho phép tìm kiếm thông tin khách hàng/ queue gọi lại.<br>+ Xuất báo cáo chi tiết<br>Điều kiện đảm bảo:<br>1. Màn hình Cấu hình queue callout<br>+ Thêm mới loại callout: Gọi ra tự động khách hàng thường cho phép gọi ra cho khách hàng<br>thường theo giờ cấu hình trong màn cấu hình queue callout<br>+ Thêm mới param_id: Cấu hình tham số giá trị agent gọi lại: tất cả agent trong queue/ theo<br>danh sách import.<br>+ Thêm mới Tham số cấu hình trạng thái gọi lại tự động: Cho phép on/off khi cần thiết<br>2. Cấu hình queue:<br>+ Đối với queue thường với tham số cho phép gọi lại khách hàng thường.<br>3. Thêm mới màn hình Quản lý chiến dịch gọi lại: Cho phép quản lý tất cả thông tin queue<br>callout được cấu hình.<br>+ Tìm kiếm.<br>+ ON/OFF các trạng thái gọi lại các queue.<br>4. Thêm mới màn hình cấu hình ưu tiên cuộc gọi nhỡ:||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|8.3|Gọi lại KH VIP||Gọi lại khách hàng VIP: Cho phép gọi lại khách VIP bị nhỡ khi gọi lên hệ thống theo khoảng<br>khung giờ cấu hình.<br>1. Màn hình Cấu hình queue callout<br>+ Thêm mới loại callout: Gọi ra tự động khách hàng VIP cho phép gọi ra cho khách hàng VIP<br>2. Cấu hình queue<br>+ Đối với queue thường với tham số cho phép gọi lại khách hàng VIP theo các hạng VIP<br>tương ứng.<br>3. Thêm mới màn hình Quản lý chiến dịch gọi lại: Cho phép quản lý tất cả thông tin queue<br>callout được cấu hình.<br>+ Tìm kiếm.<br>+ ON/OFF các trạng thái gọi lại các queue.<br>4. Thêm mới màn hình cấu hình ưu tiên cuộc gọi nhỡ:<br>4. Thêm mới màn hình Thống kê cuộc gọi lại tự động trong ngày<br>+ Cho phép tìm kiếm thông tin khách hàng/ queue gọi lại.<br>+ Xuất báo cáo chi tiết|
|8.4|Cấu hình thời gian gọi lại theo<br>giờ, theo thứ, theo ngày||Cấu hình thời gian gọi lại: Hiện tại trên hệ thống cũ chỉ cấu hình khoảng khung giờ gọi lại:<br>1.Thêm mới màn hình cấu hình thời gian gọi lại khách hàng:<br>+ Thêm mới tính năng cấu hình theo thứ, theo giờ.<br>+ Xây dựng tiến trình gọi lại cho khách theo khoảng khung giờ, thời gian được cấu hình.|
|8.5|**Gọi ra**|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||8.6|Gọi ra chủ động từ IPCC - từ<br>Agentdesktop|||Gọi ra chủ đổng IPCC: Tính năng này cho phép gọi ra chủ động từ agent Destop cho khách<br>hàng<br>1. Thêm mới màn hình Cấu hình queue callout:<br>+ Tạo mới tất cả param_id dùng gọi lại cho khách hàng: Tỉ lệ rảnh, queue gọi lại, agent gọi<br>lại, trạng thái gọi lại….(tham khảo IPCC1.0).<br>2. Tạo Agent Destop: Cho phép agent có thể nghe máy, chủ động gọi ra cho khách hàng.<br>+ TVV có thể chủ động đăng nhập Agent Destop chuyển trạng thái đăng nhập.<br>+ Thực hiện cuộc gọi ra / vao tưowng ứng.<br>3. Xây dựng báo cáo thông kê thông tin cuộc gọi ra chủ động từ các queue:<br>+ Xem chi tiết/ tìm kiếm.<br>+ Xuất báo cáo<br>4. Phân quyền:  admin/giám sát/ trưởng ca điều hành có quyenf xem xuất báo cáo.||
||8.7|Gọi ra Từ ud happy call, gọi ra từ<br>BCCS:<br>- Chiến dịch MNP<br>- Chiến dịch CĐBR<br>- BADO…|||Hiện tại đã có<br>"Gọi ra Từ ud happy call, gọi ra từ BCCS:<br>- Chiến dịch MNP<br>- Chiến dịch CĐBR<br>- BADO…"||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||8.8|Hỗ trợ 2 chức năng gọi ra thông<br>thường và gọi ra KH nhấc máy<br>mới chuyển đến ĐTV (autocall)|||Chức năng này cho phép gọi ra:<br>Trùng nội dung.<br>Gọi ra khách hàng nhấc máy đến DTV:<br>+ Hệ thống tính toán lượng agent rảnh.<br>+ Tính toán danh sách khách hàng được cấu hình.<br>+ Tự động đổ cuộc gọi ra cho khách hàng.<br>+ Khách hàng nhấc máy sẽ điều phối cuộc gọi đến TVV.<br>+ Tư vấn viên tiếp nhận cuộc gọi và trả lời yêu cầu khách hàng<br>Trùng với tính năng chủ động gọi ra 8.6 và tính năng thực hiện cuộc gọi HappyCall||
||8.9|gọi ra từ BCCS|||||
||**9**|**Vận hành**|||||
||9.1|Xây dựng (thêm mới/sửa) kịch<br>bản cây IVR qua giao diện đồ<br>họa|||||
||9.2|Cập nhật kịch bản chủ động<br>không làm gián đoạn hệ thống,<br>không phải làm thủ tục sang đơn<br>vị vận hành hỗ trợ|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|9.3|Cấu hình các kết nối API qua<br>giao diện|- Cho phép cấu hình<br>các kết nối API qua<br>giao diện,<br>- Các API cần được<br>quy hoạch tên để dễ<br>quản lý<br>- Các tham số liên<br>quan API có thể điều<br>chỉnh được qua giao<br>diện như: tăng giảm<br>số lượng threar xử lý,<br>thiết đặt thời gian<br>timeout, số lượng ccu<br>xử lý đồng thời của<br>mỗi API...||
|9.4|Cây IVR có thể hỗ trợ đón nhiều<br>đầu số|- Cho phép phân<br>quyền chỉnh sửa từng<br>cây IVR riêng, chỉ<br>được tác động thay<br>đổi, chỉnh sửa cây<br>được phân quyền<br>- Ghi log tác động<br>chỉnh sửa cấu trúc<br>cây và log tác động<br>thay file âm thanh||
|9.5|Tool xây cây IVR không bị giới<br>hạn số lượng nốt hoặc đáp ứng<br>100K nốt, số lượng cây IVR<br>không giới hạn hoặc tối thiểu<br>1000 cây|- Cho phép phân<br>quyền chỉ được thay<br>đổi file nhạc của cây<br>được phân quyền<br>(tìm kiếm, backup,<br>update, rollback, ...).<br>- Ghi log tác động<br>chỉnhsửa cấu trúc||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||cây và log tác động<br>thay file âm thanh|||
||9.6|Phân|quyền trên cây IVR :|- Cho phép phân<br>quyền chỉnh sửa từng<br>cây IVR riêng, chỉ<br>được tác động thay<br>đổi, chỉnh sửa cây<br>được phân quyền<br>- Ghi log tác động<br>chỉnh sửa cấu trúc<br>cây và log tác động<br>thay file âm thanh|||
||9.7|Cho phép thay đổi âm của riêng<br>từng cây IVR||- Cho phép phân<br>quyền chỉ được thay<br>đổi file nhạc của cây<br>được phân quyền<br>(tìm kiếm, backup,<br>update, rollback, ...).<br>- Ghi log tác động<br>chỉnh sửa cấu trúc<br>cây và log tác động<br>thay file âm thanh|||
||9.8|Phân quyền báo cáo thống kê<br>phím bấm từngcây, từngđầu số|||||
||9.9|Chức năngcảnh báo upâm IVR|||||
||9.10|Năng lực xử lý của 1 cây IVR<br>đáp ứng >5000 ccu và khả năng<br>mở rộng theo chiều ngang|||||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||9.11|Ghi âm cuộc gọi, 3 file (file gộp<br>và file tách ĐTV và KH),|||||
||9.12|cho phép tắt bật chức năng ghi<br>âm với từng đầu số (gd chỉ đạo<br>chưa cần nếu ht mới chưa đáp<br>ứng)|||||
||9.13|Tạo queue mới và tích hợp với<br>các hệ thống khác :||- Dễ dàng nhúng các<br>kênh tương tác (chat,<br>e mail, FB, Zalo...)<br>trên Web của các<br>đơn vị<br>- Dễ dàng tích hợp<br>video call với các<br>app của các doanh<br>nghiệp<br>- Tạo sẵn nhiều SIP<br>trunk, nhiều danh<br>sách đầu số Callin<br>sẵn để giảm thời gian<br>khai báo khi triển<br>khai<br>- Cho phép tiếp nhận<br>cuộc gọi từ các tổng<br>đài SIP khác qua<br>khai báo đơn giản|||
||9.14|Tạo queue (thoại/video) mới<br>không cần chuyển VTN thực<br>hiện|||||
||9.15|Tạo các queue chat<br>fanpage/group mới không cần<br>chuyển VTN thực hiện|||||
||9.16|Tạo các queue (email, sms )<br>không cần VTN thực hiện|||||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||9.17|Chủ động cấu hình thêm, chon<br>kết nối đến các kênh CallBOT|||||
||9.18|Chủ động cấu hình thêm, chon<br>kết nối đến các kênh Chat BOT|||||
||9.19|Quy hoạch được các đầu số,<br>nhóm đầu số vào các modun<br>riêng để bảo đảm khi lỗi không<br>ảnh hưởng đến nhau|||||
||9.20|Đồng bộ danh sách KH tự động<br>từ các HT|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|9.21|Đồng bộ danh sách VIP tự động<br>từ Viettel ++|**1. Đồng bộ tự động:**<br>**Đồng bộ hạng**<br>**khách hàng từ TẤT**<br>**CẢ các hệ thống**<br>**dịch vụ của Viettel :**<br>- Đồng bộ danh sách<br>KH VIP tự động từ<br>Viettel ++ (đang<br>triển khai dở theo mã<br>IBM 1550194)<br>-  Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng KH của<br>ViettelPost<br>- Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng KH của XNK<br>-  Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng KH của Công<br>ty Công trình<br>-  Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng KH dịch vụ<br>SME<br>- Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng khách hàng<br>dịchvụ tàichính||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||ngân hàng<br>Đồng bộ với các ht<br>khác nếu có dịch vụ<br>mới<br>**2. Phân quyền :**<br>- Trong các màn hình<br>tìm kiếm, cho phép<br>lựa chọn "nguồn dữ<br>liệu VIP"  cho tìm<br>kiếm trong tất cả các<br>nguồn, hoặc từng<br>nguồn tùy theo phân<br>quyền<br>- Phân quyền đến<br>từng nút tìm kiếm,<br>xuất báo cáo<br>- Các chức năng xuất<br>báo cáo có 2 loại<br>buton : xuất danh<br>sách không mã hóa<br>số TB và xuất có mã<br>hóa 1 phần số<br>**3. Nghiệp vụ:**<br>- Cho phép import<br>danh sách để tìm<br>hạng tương ứng theo<br>file||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|9.22|Đồng bộ danh sách KH tự động<br>từ các HT khác của Viettel :<br>VTP, VDS, VTS...|-  Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng KH của<br>ViettelPost<br>- Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng KH của XNK<br>-  Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng KH của Công<br>ty Công trình<br>-  Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng KH dịch vụ<br>SME<br>- Đồng bộ danh sách<br>KH VIP tự động từ<br>hệ thống quản lý<br>hạng khách hàng<br>dịch vụ tài chính<br>ngân hàng<br>Đồng bộ với các ht<br>khác nếu có dịch vụ<br>mới||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||9.23|Đồng bộ danh sách KH tự động<br>từ các HT ngoài Viettel :<br>GoldenGate, Nước sạch...||- Có thiết kế quy<br>hoạch để nhanh<br>chóng dễ dàng trong<br>việc đồng bộ dữ liệu<br>từ các hệ thống dữ<br>liệu bên ngoài Viettel<br>- Khi đồng bộ sử<br>dụng giao diện thiết<br>kế sẵn không phải<br>gửi tác động sang<br>VTN|||
||9.24|Sẵn sàng tích hợp với hệ thống<br>CRM nếu TĐ thực hiện đầu tư hệ<br>thống CRM cho IPCC 2.0|||||
||9.25|Chủ động cấu hình thời gian :<br>- Thời gian timeout từng queue<br>- Thời gian giãn cách 2 cuộc gọi<br>từng queue<br>- Thời gian ringing cho từng<br>Queue|||||
||9.26|Ghi mã lỗi hệ thống, kết nối đến<br>HT log tập trung của TĐ và hệ<br>thống giám sát VTN về các tác<br>động thay đổi tham số queue,<br>tham số định tuyến, phân<br>quyền/ghi log thay đổi tham số<br>từng queue|||||
||9.27|Báo cáo thống kê số lượng CG<br>định tuyến từ khu vực khác|||||
||9.28|Báo các định tuyến thôngminh|||||
||9.29|Cấu hình tính cước linh hoạt (bỏ)<br>-> chuyển thành Sent 200 OK|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|9.30|Partime(xem tài liệu chi tiết)|||
|9.31|Voice to text|||
|9.32|Chức năngtest nhóm ĐTV|||
|9.33|Phân quyền tác động thay đổi<br>tham số theoqueue|||
|9.34|Ghi log tác động thay đổi tham<br>sốqueue|||
|9.35|Cấu hình cho phép đăng nhập<br>theo định dạnguser|||
|9.36|Giám sátgọi ra|||
|9.37|Thống kê trạng thái cuộc gọi và<br>ĐTV|||
|9.38|Ghi âm cuộcgọi ra|||
|9.39|Nhóm kênh cần giám sát cho<br>Trưởngca|||
|9.40|Đăng kí và trả lời cuộc gọi trên<br>ĐT di động|||
|9.41|Agent desktop hỗ trợ 3 giao diện<br>Mobile_app/Web/AgentDesktop|||
|9.42|Đồngbộtrạngthái hangloạt|||
|9.43|Đặt lịch khảo sát|||
|9.44|Import danh sách<br>VIP/Blacklist/Agent từ file|||
|9.45|Import khách hàng không được<br>phép gọi ra(DNC)từ file|||
|9.46|Importgán hủyID theo file|||
|9.47|Import nhóm khách hàng|||
|9.48|Tìm kiếm Agentgán choQueue|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||9.49|Gán agent choqueue từ file|||||
||9.50|Gán username trưởng ca vào<br>zone||Mục đích :<br>- Giám sát được<br>trạng thái nhân viên<br>trên từng Queue trên<br>giao diện theo 2 hình<br>thức:<br>+ Giám sát theo vị trí<br>địa lý (từng queue,<br>tất các queue)<br>+ Giám sát được theo<br>nhóm nhân sự quản<br>lý|||
||9.51|Gán callout cho agent|||||
||9.52|Nghe lại lịch sử cuộc gọi||Chính là chức năng<br>tìm kiếm nghe lại<br>cuộc gọi<br>Yêu cầu cho phép<br>tìm kiếm nghe lại từ<br>internet|||
||9.53|Nghe lại lịch sử cuộc gọi từ<br>ngoài internet|||||
||9.54|Gán agent vào zone/cập nhật<br>location cho user ĐTV|||||
||9.55|Quản lýnhạc|||||
||9.56|Quản lýthôngtin line-server|||||
||9.57|Cậpnhật nhạc chờ ACD|||||
||9.58|Thốngkê mã lỗigọi ra|||||
||9.59|Thống kê tổng hợp thông tin<br>cuộcgọi cuộcgọi(S-001)|||||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||9.60|Thống kê cuộc gọi theo số lần và<br>theo thuê bao|||||
||9.61|Thống kê danh sách thuê bao<br>thực hiện khảo sát|||||
||9.62|Báo cáo tác động|||||
||9.63|Báo cáo tác độngâm báo IVR|||||
||9.64|Thống kê tổng hợp cuộc gọi<br>được ĐTV chuyển vào khảo sát<br>IVR|||||
||9.65|Thống kê thời gian chờ và gặp<br>trungbình|||||
||9.66|Thống kê trạng thái disconnect<br>cuộcgọi|||||
||9.67|Thống kê tổng hợp cuộc gọi thực<br>hiện khảo sát SMS, USSD|||||
||9.68|Thống kê tổng hợp phím bấm<br>(kênh IVR)|||||
||9.69|Thống kê lịch sử tác động cây<br>IVR|||||
||9.70|Thống kê tổng hợp thông tin<br>cuộcgọi(kênh ACD) (CG-002)|||||
||9.71|Thống kê thời gian chờ TB (CG-<br>001.1)|||||
||9.72|Thống kê cuộc gọi vào IVR theo<br>thờigian nghe(CG-004)|||||
||9.73|Thống kê cuộc gọi theo phút (CG<br>- 005)|||||
||9.74|Thống kê chi tiết cuộc gọi (kênh<br>IVR) (CG - 006)|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|9.75|Thốngkê cuộcgọi chuyển ACD|||
|9.76|Thống kế tổng hợp thông tin<br>cuộcgọi VIP|||
|9.77|Thống kê số lần thay đổi trạng<br>thái của Agent(AG - 001)|||
|9.78|Thống kê trạng thái làm việc của<br>Agent(AG - 003)|||
|9.79|Thống kê tác động của Agent<br>(AG - 005)|||
|9.80|Thống kê thời gian trạng thái<br>(AG - 002)|||
|9.81|Thống kê số cuộc gọi của Agent<br>(AG - 004)|||
|9.82|Thống kê theo đầu số khách hàng<br>(KH - 004)|||
|9.83|Thống kê khách hàng gọi lên hệ<br>thốngN lần(KH - 002)|||
|9.84|Thống kê khách hàng rớt và gặp<br>Agent(KH - 003)|||
|9.85|Thống kê thông tin chi tiết khách<br>hàng (KH - 001)|||
|9.86|Thống kê khách hàng bị chặn<br>vẫngọi lên hệ thống (BL - 001)|||
|9.87|Quản lýBlack List|||
|9.88|Thốngkê lịch sử chặn thuê bao|||
|9.89|Thống kê tổng hợp thuê bao bị<br>chặn theo kênh|||
|9.90|Quản lýhạngkhách hàngVIP|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|9.91|Quản lýkhách hàngVIP|||
|9.92|Danh mục đầu số người dùng|||
|9.93|Quản lý tin nhắn (menu này cho<br>chức năngtạo sms survey)|||
|9.94|Danh mục khảo sát (SMS,<br>USSD)|||
|9.95|Danh mục câyIVR|||
|9.96|Danh mục kênh|||
|9.97|Thêm kênh cho người dùng|||
|9.98|Quản lýmở khóa tài khoản|||
|9.99|Quản lýnhóm tin nhắn|||
|9.100|Quản lý chiến dịch (survey KH<br>nhỡ, KH gặp, cho phép KH từ<br>chối)|||
|9.101|Cấu hình tranfer|||
|9.102|Cấu hình số ĐT tranfer cho ĐTV|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|9.103||Cấu hình queue||- Yêu cầu phân<br>quyền đến "Từng<br>THAM SỐ" của<br>"từng Queue" để chủ<br>động cấp quyền cho<br>các đơn vị chủ động<br>cấu hình các tham số<br>đơn giản (hiện tại<br>phân quyền chưa linh<br>hoạt nên khó khăn<br>trong việc để các đơn<br>vị chủ động thay đổi<br>một số các tham số<br>đơn giản phục vụ<br>công tác điều hành<br>trong ca trực)<br>Tương tự với tất cả<br>các tham số của các<br>loại Queue khác<br>nhau trên hệ thống<br>(Thoại, chat, mail,<br>video...), Queue<br>in/out|||
|9.104||Cấu hìnhqueue Callout|||||
|9.105||Cấu hình cuộcgọi nhỡ|||||
|9.106||Cấu hình định tuyến thông minh||Có thể cấp quyền cho<br>trưởng ca thực hiện<br>theo từng đơn vị,<br>từng công ty|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|9.107||Các báo cáo thống kê được phân<br>quyền từng báo cáo, từng đầu số<br>và phân quyền xuất các định<br>dang sau. được chia làm các 3<br>dạng xuất báo cáo:<br>-          Xuất file excel  không mã<br>hoá số thuê bao<br>-          Xuất file excel mã hoá số<br>TB<br>-          Xuất pdf|||||
|9.108||Các báo cáo thống kê được phân<br>quyền từng báo cáo, từng đầu số<br>có 2 loại báo cáo<br>-          Mã hoá số TB<br>-          Không mã hoá số TB|||||
|9.109||Báo cáo thống kê đăng kí dịch vụ<br>qua IVR|||||
|9.110||-map ds user gọi ra trên queue<br>gọi ra|||||
|9.111||Cho phép hiển thị avatar của KH<br>trên cácqueue MXH|||||
|9.112||Ưu tiên hiển thị ảnh avatar với<br>các kênh không phải MXH như<br>thoại, email|||||
|**10**||**Phân hệ Monitor**|||||
|**10.1**||**Kênh chat**|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.1.1|View được tỉ lệ kết nối, tỷ lệ<br>phản hồi|HPG<br>'- Cho phép View<br>được tỷ lệ kết nối, tỷ<br>lệ phản hồi trong hạn<br>của các kênh (Chat +<br>MXH) dưới dạng<br>biểu đồ, chỉ số%, lưu<br>lượng theo múi giờ<br>và toàn ngày:<br>+ Kênh chat: Tỷ lệ<br>kết nối; tỷ lệ phản<br>hồi phiên chat đầu<br>tiên trong hạn 60s.<br>(Tổng toàn kênh và<br>chi tiết từng Queue:<br>Zalo, MyViettel...)<br>=> Hiển thị biểu đồ<br>% theo từng múi giờ<br>+ Kênh MXH:  Tỷ lệ<br>phản hồi trong hạn<br>30 phút => Hiển thị<br>biểu đồ % theo từng<br>múi giờ<br>- Cho phép thống kê<br>trạng thái của ĐTV<br>=> Biểu đồ<br>- Cho phép giám sát<br>KPI phản hồi trong<br>phiên chat của ĐTV<br>=>Biểu đồ|HPG<br>'- Cho phép View được tỷ lệ kết nối, tỷ lệ phản hồi trong hạn của các kênh (Chat + MXH)<br>dưới dạng biểu đồ, chỉ số%, lưu lượng theo múi giờ và toàn ngày:<br>+ Kênh chat: Tỷ lệ kết nối; tỷ lệ phản hồi phiên chat đầu tiên trong hạn 60s. (Tổng toàn kênh<br>và chi tiết từng Queue: Zalo, MyViettel...) => Hiển thị biểu đồ % theo từng múi giờ<br>+ Kênh MXH:  Tỷ lệ phản hồi trong hạn 30 phút => Hiển thị biểu đồ % theo từng múi giờ<br>- Cho phép thống kê trạng thái của ĐTV => Biểu đồ<br>- Cho phép giám sát KPI phản hồi trong phiên chat của ĐTV => Biểu đồ|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|10.1.2||Báo cáo chat||-Báo cáo chỉ số kênh<br>Chat+MXH theo<br>ngày, múi giờ:<br>+ Lấy dữ liệu các<br>kênh trên hệ thống<br>Econtact.<br>+ Nội dung báo cáo<br>bao gồm:<br>Lưu lượng đầu vào;<br>Lưu lượng tiếp nhận;<br>Lưu lượng tiếp nhận<br>trong hạn; Tỷ lệ kết<br>nối; Tỷ lệ phản hồi<br>trong hạn; Thời gian<br>trả lời trung bình (áp<br>dụng với kênh chat).|-Báo cáo chỉ số kênh Chat+MXH theo ngày, múi giờ:<br>+ Lấy dữ liệu các kênh trên hệ thống Econtact.<br>+ Nội dung báo cáo bao gồm:<br>Lưu lượng đầu vào; Lưu lượng tiếp nhận; Lưu lượng tiếp nhận trong hạn; Tỷ lệ kết nối; Tỷ lệ<br>phản hồi trong hạn; Thời gian trả lời trung bình (áp dụng với kênh chat).||
|10.1.3||Báo cáo chỉ số kênh||-Báo cáo chỉ số kênh<br>Chat+MXH theo<br>ngày, múi giờ:<br>+ Lấy dữ liệu các<br>kênh trên hệ thống<br>Econtact.<br>+ Nội dung báo cáo<br>bao gồm:<br>Lưu lượng đầu vào;<br>Lưu lượng tiếp nhận;<br>Lưu lượng tiếp nhận<br>trong hạn; Tỷ lệ kết<br>nối; Tỷ lệ phản hồi<br>trong hạn; Thời gian<br>trả lời trung bình (áp<br>dụng với kênh chat).|-Báo cáo chỉ số kênh Chat+MXH theo ngày, múi giờ:<br>+ Lấy dữ liệu các kênh trên hệ thống Econtact.<br>+ Nội dung báo cáo bao gồm:<br>Lưu lượng đầu vào; Lưu lượng tiếp nhận; Lưu lượng tiếp nhận trong hạn; Tỷ lệ kết nối; Tỷ lệ<br>phản hồi trong hạn; Thời gian trả lời trung bình (áp dụng với kênh chat).||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.1.4|Báo cáo so sánh chỉ số theo<br>ngày, theo giờ giữa ngày 2 ngày<br>được chọn||-So sánh Lưu lượng đầu vào; Lưu lượng tiếp nhận; Lưu lượng tiếp nhận trong hạn; Tỷ lệ kết<br>nối; Tỷ lệ phản hồi trong hạn; Thời gian trả lời trung bình (áp dụng với kênh chat) giữa 2<br>ngày được chọn.|
|**10.2**|**Kênh thoại **|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.2.1|View được tỉ lệ kết nối của tất cả<br>các kênh ( thoại + econtact)|Hiện đang giám sát<br>dựa trên Agent<br>desktop + CCMS +<br>KPI online. Veiw đc<br>các thông tin sau:<br>- Biểu đồ TLKN,<br>hiển thị: (1) Lưu<br>lượng CG theo<br>khoảng giờ và lũy kế<br>ngày vào ACD, BOT<br>(Bot tách riêng chỉ<br>gặp BOT và gặp<br>BOT chuyển agent),<br>Tất cả. (2) Target<br>KPI, --> Hiển thị<br>theo queue<br>- Veiw đc các thông<br>số trên**Agent**<br>**desktop**, các tab:<br>+**Giám sát queue**<br>(Tổng CG vào, CG<br>chờ, CG trả lời, Ag<br>chính/phụ, Các thông<br>tin khác đã có trên<br>Giám sát queue<br>+**Tìm kiếm trạng**<br>**thái agent**<br>**+ Thống kê trạng**<br>**thái CG và ĐTV**<br>(hiển thị theo đối tác,<br>theo tổng đài: ready,<br>not ready, ringing...,<br>tổng)<br>+Các tiện ích khác:|Vấn đề:<br>- Trùng Trạng thái Agent<br>- Thông tin hệ thống (ít dùng) giống thông tin trong Giám sát Queue<br>1. Yêu cầu nghiệp vụ<br>- Giám sát queue nhìn thông tin theo queue (không chia nhỏ đến đối tác + khu vực)<br>- Cho phép phân cấp ĐTV theo nhóm, theo khu vực. Phân cấp máy tính (Địa chỉ MAC). Gán<br>người quản lý cho cácc nhóm<br>- View đc các thông số trên Agent desktop, các tab:<br>+ Giám sát queue (Tổng CG vào, CG chờ, CG trả lời, Ag chính/phụ, Các thông tin khác đã có<br>trên Giám sát queue<br>+ Tìm kiếm trạng thái agent<br>+ Thống kê trạng thái CG và ĐTV (hiển thị theo đối tác, theo tổng đài: ready, not ready,<br>ringing..., tổng)<br>- Hiển thị biểu đồ giám sát theo khu : KPI, chỉ số (%), lưu lượng (số tuyệt đối), bảng chi tiết<br>số liệu<br>- Cấu hình KPI : Cấu hình thông tin hiển thị biểu đồ và số liệu theo kênh cố định, di động,<br>theo khu vực, khoảng thời gian và thể loại...|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||Quản lý queue (gán<br>queue thủ công),<br>Trạng thái CG (dùng<br>để nghe line), Chat,<br>Gọi ra ngoài (hiện<br>gọi ra trên bccs)  =><br>Check đưa sang mục<br>nào<br>+ Tiện ích của Giám<br>sát: Nghe online,<br>Gán CG, Nghe<br>online CG ra<br>+ Tab không dùng:<br>Trạng thái ag (giống<br>tìm kiếm trạng thái<br>ag), Thông tin HT<br>(giống giám sát<br>queue)||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.2.2|SMS báo cáo chỉ số tự động theo<br>múi giờ|Tham khảo tài liệu<br>KPI Monitor:<br>- Cho phép cấu hình<br>template tin nhắn,<br>xem/thêm/sửa/xóa<br>template tin nhắn<br>- Tự động nhắn tin<br>theo giờ/ngày --><br>Cho phép ng dùng<br>setup đc các khung<br>giờ nhắn tin (vd:<br>Ngày N lúc 8h nhắn<br>báo cáo ngày N-1 từ<br>00h-23h59)<br>- Cho phép cấu hình<br>ngưỡng chỉ số cảnh<br>báo<br>- Gửi tin nhắn:<br>Tạo/xem/sửa/xóa<br>nhóm SMS; Tính<br>toán chỉ số tự động,<br>Tích hợp thêm tính<br>năng khác, Gửi tin...|- Cho phép cấu hình template tin nhắn, xem/thêm/sửa/xóa template tin nhắn: bổ sung cấu thời<br>gian so sánh (option so sánh số liêu VD: cùng kỳ tuần trước, tháng trước, quý trước, năm<br>trước)<br>- Tự động nhắn tin theo giờ/ngày --> Cho phép ng dùng setup đc các khung giờ nhắn tin (vd:<br>Ngày N lúc 8h nhắn báo cáo ngày N-1 từ 00h-23h59)<br>- Cho phép cấu hình ngưỡng chỉ số cảnh báo<br>- Gửi tin nhắn: Tạo/xem/sửa/xóa nhóm SMS; Tính toán chỉ số tự động, Tích hợp thêm tính<br>năng khác, Gửi tin theo nhóm nhận SMS<br>- Tạo nhóm nhận tin nhắn: Import người dùng vào nhóm tin nhắn<br>- Cho phép cấu hình các tham số: Thời gian nhắn,|
|10.2.3|SMS báo cáo chỉ số chủ động<br>theo múi giờ|Tham khảo tài liệu<br>KPI Monitor =><br>SMS báo cáo<br>(Tương tự SMS mục<br>11.2 => Ng dùng cấu<br>hình tay|- Người dùng cấu hình thủ công sms cảnh báo chỉ số<br>- Gộp vào 2 chức năng SMS báo cáo tự động và chủ động và một màn hình cấu hình<br>- Với kênh trực tuyến: Bỏ sms tự động|
|10.2.4|SMS cảnh báo chỉ số theo<br>ngưỡng nghẽn|Tham khảo tài liệu<br>KPI Monitor<br>Tương tự mục 11.2|- Người dùng cấu hình thủ công sms cảnh báo theo ngưỡng nghẽn<br>- Mong muốn bổ sung phẩn thay đổi cấu hình các cấp|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|10.2.5||Báo cáo chỉ số cuộc gọi theo<br>ngày theo giờ||- Tham khảo tài liệu<br>KPI Monitor: Báo<br>cáo theo giờ, theo<br>ngày, Chi tiết theo<br>múi giờ<br>- Gửi kèm nội dung<br>word chi tiết|- Bổ sung lấy dữ liệu các kênh (bổ sung các kênh)<br>Hiện tại đang lấy dữ liệu kênh hệ thống báo cáo, CCMS, IPCC CG008<br>- Lấy dữ liệu cuộc gọi CG002<br>- Đang bắt buộc lấy từng kênh (bổ sung chọn danh sách kênh và ra dữ liệu ra từng kênh<br>không ra số tổng)||
|10.2.6||Báo cáo so sánh chỉ số theo<br>ngày, theo giờ giữa ngày 2 ngày<br>được chọn||1. Lưu lại thông tin<br>cuộc gọi<br>- Lưu lại thông tin<br>cuộc gọi<br>- Tính toán các chỉ số<br>cuộc gọi theo ngày,<br>giờ<br>2. So sánh chỉ số<br>cuộc gọi giữa 2 ngày<br>được chọn<br>3.  Phân quyền:<br>- Cho phép admin so<br>sánh chỉ số cuộc gọi<br>giữa 2 ngày được<br>chọn|1. Lưu lại thông tin cuộc gọi<br>- Lưu lại thông tin cuộc gọi: Thông tin cuộc gọi vào, gặp ĐTV, rớt (do KH, do hệ thống), KH<br>tự ngắt => tỷ lệ kết nối thành công đến ĐTV, tỷ lệ rớt, tỷ lệ ngắt...<br>- Tính toán các chỉ số cuộc gọi theo ngày, giờ: chọn từ giờ đến giờ, ngày<br>2. So sánh chỉ số cuộc gọi giữa 2 ngày được chọn||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.2.7|Phân quyền người dùng|Chức năng quản lý<br>người dùng cho phép<br>cấu hình người dùng<br>gồm các quyền:<br>- Super admin: cho<br>phép thêm đầu số<br>cho Doanh nghiệp,<br>Quản lý người dùng<br>cho các doanh<br>nghiệp. - Admin:<br>chức năng cấu hình,<br>tiếp nhận voice, chat;<br>Xem lịch sử cuộc<br>gọi; xem thông tin<br>dashboard; Xem<br>thông tin báo cáo;<br>Giám sát agent,<br>Giám sát queue,<br>Giám sát giao dịch<br>cuộc gọi/chat<br>- User: chức năng<br>tiếp nhận voice, chat;<br>Xem lịch sử cuộc<br>gọi, xem thông tin<br>dashboard của chính<br>user đấy<br>- Supervisor: chức<br>năng tiếp nhận voice,<br>chat; Xem lịch sử<br>cuộc gọi; xem thông<br>tin dashboard; Xem<br>thông tin báo cáo;<br>Giám sát agent,<br>queue, giao dịch|Chức năng quản lý người dùng cho phép cấu hình người dùng gồm các quyền:<br>- Super admin: cho phép thêm đầu số cho Doanh nghiệp, Quản lý người dùng cho các doanh<br>nghiệp. - Admin: chức năng cấu hình, tiếp nhận voice, chat; Xem lịch sử cuộc gọi; xem thông<br>tin dashboard; Xem thông tin báo cáo; Giám sát agent, Giám sát queue, Giám sát giao dịch<br>cuộc gọi/chat<br>- User: chức năng tiếp nhận voice, chat; Xem lịch sử cuộc gọi, xem thông tin dashboard của<br>chính user đấy<br>- Supervisor: chức năng tiếp nhận voice, chat; Xem lịch sử cuộc gọi; xem thông tin<br>dashboard; Xem thông tin báo cáo; Giám sát agent, queue, giao dịch cuộc gọi, chat<br>- Phân theo Viettel, Đối tác<br>- Bổ sung quản lý nhóm phân quyền<br>- Add được người dùng VSA vào nhóm<br>- Gán các kênh cho các nhóm|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||cuộc gọi, chat<br>- Phân theo Viettel,<br>Đối tác||
|10.2.8|Thêm/sửa/ xóa kênh cho đối tác|- Xử lý giao diện<br>Thêm/sửa/ xóa kênh<br>cho đối tác<br>- Xử lý logic<br>Thêm/sửa/ xóa kênh<br>cho đốitác|- Add thêm kênh để hiển thị biểu dồ<br>- Là chức năng thiết lập đối tác kênh: bổ sung nút chọn all (bỏ all)<br>- Nhóm kênh monitor OS cho phếp hiển thị biếu đồ theo nhóm kênh quản lý|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|10.2.9||Cấu hình kênh/ nhóm kênh hiển<br>thị||- Cấu hình kênh hiển<br>thị (Thêm/ Sửa/ Xóa/<br>Cập nhật)<br>- Cấu hình nhóm<br>kênh hiển thị (Thêm/<br>Sửa/ Xóa/ Cập nhật)|Chức năng đăng có (CN: phân quyền, phân quyền Monitor)||
|10.2.10||cấu hình Danh sách kênh/nhóm<br>kênh để tạo nội dung gửi sms||1.Cấu hình danh sách<br>kênh để tạo nội dung<br>SMS (Thêm mới,<br>sửa, xóa)<br>2. Cấu hình danh<br>sách nhóm kênh<br>SMS (Thêm mới,<br>sửa, xóa)<br>3.Xử lý luồng tạo nội<br>dung gửi SMS từ<br>danh sách kênh/<br>nhóm kênh|Là chức năng SMS- Nhóm kênh trên hệ thống Monitor||
|10.2.11||cấu hình danh sách sdt nhận sms||1. Cấu hình danh<br>sách SDT nhận SMS<br>- Thêm mới<br>- sửa<br>- Xóa<br>2.'Import danh sách<br>số điện thoại nhận<br>sms<br>Tải file import lỗi|Cho phép cấu hình danh sách sđt nhận sms||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|10.2.12||cấu hình cấp độ gửi sms theo<br>từng danh sách||1. Cấu hình cấp độ<br>gửi sms theo từng<br>danh sách<br>- Thêm mới<br>- sửa<br>- Xóa<br>2. Xử lý gửi tin nhắn<br>theo danh sách số<br>điện thoại đã cấu<br>hình|Cho phép cấu hình cấp độ gửi sms theo từng danh sách||
|10.2.13||Cấu hình định nghĩa các loại<br>cuộcgọi|||Cho phép cấu hình định nghĩa loại cuộc gọi: Cuộc gọi nhiều lần, cuộc gọi đầu số lạ…||
|10.2.14||Quản lýaccount|||Chophép quản lýaccount||
|**10.3**||**Kênh video call**|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.3.1|View được tỉ lệ kết nối của tất cả<br>các kênh ( thoại + econtact)|Hiện đang giám sát<br>dựa trên Agent<br>desktop + CCMS +<br>KPI online. Veiw đc<br>các thông tin sau:<br>- Biểu đồ TLKN,<br>hiển thị: (1) Lưu<br>lượng CG theo<br>khoảng giờ và lũy kế<br>ngày vào ACD, BOT<br>(Bot tách riêng chỉ<br>gặp BOT và gặp<br>BOT chuyển agent),<br>Tất cả. (2) Target<br>KPI, --> Hiển thị<br>theo queue<br>- Veiw đc các thông<br>số trên**Agent**<br>**desktop**, các tab:<br>+**Giám sát queue**<br>(Tổng CG vào, CG<br>chờ, CG trả lời, Ag<br>chính/phụ, Các thông<br>tin khác đã có trên<br>Giám sát queue<br>+**Tìm kiếm trạng**<br>**thái agent**<br>**+ Thống kê trạng**<br>**thái CG và ĐTV**<br>(hiển thị theo đối tác,<br>theo tổng đài: ready,<br>not ready, ringing...,<br>tổng)<br>+Các tiện ích khác:|Vấn đề:<br>- Trùng Trạng thái Agent<br>- Thông tin hệ thống (ít dùng) giống thông tin trong Giám sát Queue<br>1. Yêu cầu nghiệp vụ<br>- Giám sát queue nhìn thông tin theo queue (không chia nhỏ đến đối tác + khu vực)<br>- Cho phép phân cấp ĐTV theo nhóm, theo khu vực. Phân cấp máy tính (Địa chỉ MAC). Gán<br>người quản lý cho cácc nhóm<br>- View đc các thông số trên Agent desktop, các tab:<br>+ Giám sát queue (Tổng CG vào, CG chờ, CG trả lời, Ag chính/phụ, Các thông tin khác đã có<br>trên Giám sát queue<br>+ Tìm kiếm trạng thái agent<br>+ Thống kê trạng thái CG và ĐTV (hiển thị theo đối tác, theo tổng đài: ready, not ready,<br>ringing..., tổng)<br>- Hiển thị biểu đồ giám sát theo khu : KPI, chỉ số (%), lưu lượng (số tuyệt đối), bảng chi tiết<br>số liệu<br>- Cấu hình KPI : Cấu hình thông tin hiển thị biểu đồ và số liệu theo kênh cố định, di động,<br>theo khu vực, khoảng thời gian và thể loại...|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||Quản lý queue (gán<br>queue thủ công),<br>Trạng thái CG (dùng<br>để nghe line), Chat,<br>Gọi ra ngoài (hiện<br>gọi ra trên bccs)  =><br>Check đưa sang mục<br>nào<br>+ Tiện ích của Giám<br>sát: Nghe online,<br>Gán CG, Nghe<br>online CG ra<br>+ Tab không dùng:<br>Trạng thái ag (giống<br>tìm kiếm trạng thái<br>ag), Thông tin HT<br>(giống giám sát<br>queue)||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.3.2|SMS báo cáo chỉ số tự động theo<br>múi giờ|Tham khảo tài liệu<br>KPI Monitor:<br>- Cho phép cấu hình<br>template tin nhắn,<br>xem/thêm/sửa/xóa<br>template tin nhắn<br>- Tự động nhắn tin<br>theo giờ/ngày --><br>Cho phép ng dùng<br>setup đc các khung<br>giờ nhắn tin (vd:<br>Ngày N lúc 8h nhắn<br>báo cáo ngày N-1 từ<br>00h-23h59)<br>- Cho phép cấu hình<br>ngưỡng chỉ số cảnh<br>báo<br>- Gửi tin nhắn:<br>Tạo/xem/sửa/xóa<br>nhóm SMS; Tính<br>toán chỉ số tự động,<br>Tích hợp thêm tính<br>năng khác, Gửi tin...|- Cho phép cấu hình template tin nhắn, xem/thêm/sửa/xóa template tin nhắn: bổ sung cấu thời<br>gian so sánh (option so sánh số liêu VD: cùng kỳ tuần trước, tháng trước, quý trước, năm<br>trước)<br>- Tự động nhắn tin theo giờ/ngày --> Cho phép ng dùng setup đc các khung giờ nhắn tin (vd:<br>Ngày N lúc 8h nhắn báo cáo ngày N-1 từ 00h-23h59)<br>- Cho phép cấu hình ngưỡng chỉ số cảnh báo<br>- Gửi tin nhắn: Tạo/xem/sửa/xóa nhóm SMS; Tính toán chỉ số tự động, Tích hợp thêm tính<br>năng khác, Gửi tin theo nhóm nhận SMS<br>- Tạo nhóm nhận tin nhắn: Import người dùng vào nhóm tin nhắn<br>- Cho phép cấu hình các tham số: Thời gian nhắn,|
|10.3.3|SMS báo cáo chỉ số chủ động<br>theo múi giờ|Tham khảo tài liệu<br>KPI Monitor =><br>SMS báo cáo<br>(Tương tự SMS mục<br>11.2 => Ng dùng cấu<br>hình tay|- Người dùng cấu hình thủ công sms cảnh báo chỉ số<br>- Gộp vào 2 chức năng SMS báo cáo tự động và chủ động và một màn hình cấu hình<br>- Với kênh trực tuyến: Bỏ sms tự động|
|10.3.4|SMS cảnh báo chỉ số theo<br>ngưỡng nghẽn|Tham khảo tài liệu<br>KPI Monitor<br>Tương tự mục 11.2|Hiện tại đang đảm bảo<br>- Mong muốn bổ sung phẩn thay đổi cấu hình các cấp|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|10.3.5||Báo cáo chỉ số cuộc gọi theo<br>ngày theo giờ||- Tham khảo tài liệu<br>KPI Monitor: Báo<br>cáo theo giờ, theo<br>ngày, Chi tiết theo<br>múi giờ<br>- Gửi kèm nội dung<br>word chi tiết|Đã có báo cáo<br>- Bổ sung lấy dữ liệu các kênh (bổ sung các kênh)<br>Hiện tại đang lấy dữ liệu kênh hệ thống báo cáo, CCMS, IPCC CG008<br>- Lấy dữ liệu cuộc gọi CG002<br>- Đang bắt buộc lấy từng kênh (bổ sung chọn danh sách kênh và ra dữ liệu ra từng kênh<br>không ra số tổng)||
|10.3.6||Báo cáo so sánh chỉ số theo<br>ngày, theo giờ giữa ngày 2 ngày<br>được chọn||1. Lưu lại thông tin<br>cuộc gọi<br>- Lưu lại thông tin<br>cuộc gọi<br>- Tính toán các chỉ số<br>cuộc gọi theo ngày,<br>giờ<br>2. So sánh chỉ số<br>cuộc gọi giữa 2 ngày<br>được chọn<br>3.  Phân quyền:<br>- Cho phép admin so<br>sánh chỉ số cuộc gọi<br>giữa 2 ngày được<br>chọn|1. Lưu lại thông tin cuộc gọi<br>- Lưu lại thông tin cuộc gọi: Thông tin cuộc gọi vào, gặp ĐTV, rớt (do KH, do hệ thống), KH<br>tự ngắt => tỷ lệ kết nối thành công đến ĐTV, tỷ lệ rớt, tỷ lệ ngắt...<br>- Tính toán các chỉ số cuộc gọi theo ngày, giờ: chọn từ giờ đến giờ, ngày<br>2. So sánh chỉ số cuộc gọi giữa 2 ngày được chọn||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.3.7|Phân quyền người dùng|Chức năng quản lý<br>người dùng cho phép<br>cấu hình người dùng<br>gồm các quyền:<br>- Super admin: cho<br>phép thêm đầu số<br>cho Doanh nghiệp,<br>Quản lý người dùng<br>cho các doanh<br>nghiệp. - Admin:<br>chức năng cấu hình,<br>tiếp nhận voice, chat;<br>Xem lịch sử cuộc<br>gọi; xem thông tin<br>dashboard; Xem<br>thông tin báo cáo;<br>Giám sát agent,<br>Giám sát queue,<br>Giám sát giao dịch<br>cuộc gọi/chat<br>- User: chức năng<br>tiếp nhận voice, chat;<br>Xem lịch sử cuộc<br>gọi, xem thông tin<br>dashboard của chính<br>user đấy<br>- Supervisor: chức<br>năng tiếp nhận voice,<br>chat; Xem lịch sử<br>cuộc gọi; xem thông<br>tin dashboard; Xem<br>thông tin báo cáo;<br>Giám sát agent,<br>queue, giao dịch|Chức năng quản lý người dùng cho phép cấu hình người dùng gồm các quyền:<br>- Super admin: cho phép thêm đầu số cho Doanh nghiệp, Quản lý người dùng cho các doanh<br>nghiệp. - Admin: chức năng cấu hình, tiếp nhận voice, chat; Xem lịch sử cuộc gọi; xem thông<br>tin dashboard; Xem thông tin báo cáo; Giám sát agent, Giám sát queue, Giám sát giao dịch<br>cuộc gọi/chat<br>- User: chức năng tiếp nhận voice, chat; Xem lịch sử cuộc gọi, xem thông tin dashboard của<br>chính user đấy<br>- Supervisor: chức năng tiếp nhận voice, chat; Xem lịch sử cuộc gọi; xem thông tin<br>dashboard; Xem thông tin báo cáo; Giám sát agent, queue, giao dịch cuộc gọi, chat<br>- Phân theo Viettel, Đối tác<br>- Bổ sung quản lý nhóm phân quyền<br>- Add được người dùng VSA vào nhóm<br>- Gán các kênh cho các nhóm|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||cuộc gọi, chat<br>- Phân theo Viettel,<br>Đối tác||
|10.3.8|Thêm/sửa/ xóa kênh cho đối tác|- Xử lý giao diện<br>Thêm/sửa/ xóa kênh<br>cho đối tác<br>- Xử lý logic<br>Thêm/sửa/ xóa kênh<br>cho đốitác|- Add thêm kênh để hiển thị biểu dồ<br>- Là chức năng thiết lập đối tác kênh: bổ sung nút chọn all (bỏ all)<br>- Nhóm kênh monitor OS cho phếp hiển thị biếu đồ theo nhóm kênh quản lý|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|10.3.9||Cấu hình kênh/ nhóm kênh hiển<br>thị||- Cấu hình kênh hiển<br>thị (Thêm/ Sửa/ Xóa/<br>Cập nhật)<br>- Cấu hình nhóm<br>kênh hiển thị (Thêm/<br>Sửa/ Xóa/ Cập nhật)|Chức năng đăng có (CN: phân quyền, phân quyền Monitor)||
|10.3.10||cấu hình Danh sách kênh/nhóm<br>kênh để tạo nội dung gửi sms||1.Cấu hình danh sách<br>kênh để tạo nội dung<br>SMS (Thêm mới,<br>sửa, xóa)<br>2. Cấu hình danh<br>sách nhóm kênh<br>SMS (Thêm mới,<br>sửa, xóa)<br>3.Xử lý luồng tạo nội<br>dung gửi SMS từ<br>danh sách kênh/<br>nhóm kênh|Là chức năng SMS- Nhóm kênh trên hệ thống Monitor||
|10.3.11||cấu hình danh sách sdt nhận sms||1. Cấu hình danh<br>sách SDT nhận SMS<br>- Thêm mới<br>- sửa<br>- Xóa<br>2.'Import danh sách<br>số điện thoại nhận<br>sms<br>Tải file import lỗi|Cho phép cấu hình danh sách sđt nhận sms||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|10.3.12||cấu hình cấp độ gửi sms theo<br>từng danh sách||1. Cấu hình cấp độ<br>gửi sms theo từng<br>danh sách<br>- Thêm mới<br>- sửa<br>- Xóa<br>2. Xử lý gửi tin nhắn<br>theo danh sách số<br>điện thoại đã cấu<br>hình|Cho phép cấu hình cấp độ gửi sms theo từng danh sách||
|10.3.13||Cấu hình định nghĩa các loại<br>cuộcgọi|||Cho phép cấu hình định nghĩa loại cuộc gọi||
|10.3.14||Quản lýaccount|||Chophép quản lýaccount||
|**10.4**||**Email**|||||
|10.4.1||Biểu đồ giám sát mail theo<br>khung giờ||Giám sát số lượng<br>mail trong khung giờ|Biểu đồ cột bao gồm các chỉ số<br>- Cột 1: Số lượng mail nhận trong khung giờ. Bao gồm mail cần xử lý và mail bỏ qua<br>- Cột 2: Mail hoàn thành: Số lượng mail hoàn thành trong khung giờ của các mail nhận trong<br>khung giờ. Bao gồm trong hạn và quá hạn<br>- Cột 3: Mail tạm đóng: Số lượng mail tạm đóng trong khung giờ của các mail nhận trong<br>khung giờ. Bao gồm trong hạn và quá hạn<br>- Cột 4: Mail chưa xử lý: Số lượng mail chưa xử lý trong khung giờ của các mail nhận trong<br>khung giờ. Bao gồm trong hạn và quá hạn<br>Cột 1 = Mail bỏ qua + Cột 2 + Cột 3 + Cột 4||
|10.4.2||Số liệu mail chưa xử lý và tạm<br>đóng luỹ kế đến thời điểm hiện<br>tại|||Số liệu mail chưa xử lý (trong hạn và quá hạn) và tạm đóng (trong hạn và quá hạn) luỹ kế đến<br>thời điểm hiện tại||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|10.4.3|8 Báo cáo theo các loại ĐTV,<br>Loại mail, Loại KH, Hệ thống||8 Báo cáo theo các loại ĐTV, Loại mail, Loại KH, Hệ thống|
|**11**|**Các chức năng liên quan đến**<br>**kênhphi thoại **|||
|**11.1**|**Phân hệ email**|||
|11.1.1|Xem nội dung email khách hàng<br>gửi||- Chức năng cho phép Agent xem nội dung email khách hàng gửi khi được khi được giao xử<br>lý Ticket Email.<br>- Từ màn hình Danh sách Ticket, Agent click vào xem chi tiết 1 Ticket Email. Hệ thống hiển<br>thị màn hình Ticket Detail Email, trong đó có hiển thị nội dung email khách hàng gửi đến.|
|11.1.1.1|Phản hồi email cho khách hàng||- Chức năng cho phép Agent trả lời email khách hàng<br>- Trên màn hình Ticket Detail Email, Agent click vào “Phản hồi” tương ứng với email mà<br>khách hàng gửi đến hệ thống ==> Hiển thị màn hình soạn thảo email|
|11.1.1.2|Chuyển tiếpemail||Chuyển tiếpemail cho một người khác|
|11.1.1.3|Chức năng tiếp nhận email||- Chức năng cho phép Agent forward email của khách hàng gửi đến tới 1 hay nhiều địa chỉ<br>email bất kỳ<br>- Trên màn hình Ticket Detail Email, Agent click vào “Chuyển tiếp” tương ứng với email mà<br>khách hàng gửi đến hệ thống ==> Hiển thị màn hình Forward email|
|11.1.1.4|Tiếp nhận email qua nhiều địa<br>chỉ email của khách hàng B2B<br>(không giới hạn địa chỉ email)|Một khách hàng B2B<br>có thể có nhiều địa<br>chỉ email tiếp nhận<br>dịch vụ. Phục vụ<br>được nhiều khách<br>hàng B2B.|1. Yêu cầu nghiệp vụ<br>- Một khách hàng B2B có thể có nhiều địa chỉ email tiếp nhận dịch vụ. Phục vụ được nhiều<br>khách hàng B2B.<br>- Mỗi email được cấu hình vào 1 queue|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|11.1.1.5||Phân vùng làm việc cho từng địa<br>chỉ email tiếp nhận dịch vụ||Mỗi địa chỉ email<br>tiếp nhận dịch vụ có<br>1 inbox riêng.|1. Yêu cầu nghiệp vụ<br>- Mỗi địa chỉ email tiếp nhận dịch vụ có 1 queue riêng.||
|11.1.1.6||Phân vùng xử lý email cho nhân<br>viên CSKH||Một nhân viên<br>CSKH có thể được<br>phân vùng xử lý 1<br>inbox hoặc nhiều<br>inbox|1. Yêu cầu nghiệp vụ<br>- Một nhân viên CSKH có thể được phân vùng xử lý 1 queue hoặc nhiều queue||
|11.1.1.7||Chức năng báo email mới||Khi có Email mới, hệ<br>thống eContact sẽ<br>popup cửa sổ thông<br>báo h ở góc cuối bên<br>phải của màn hình<br>(tương tự như thông<br>báo từ Outlook) hoặc<br>thông báo bằng âm<br>thanh để NVCSKH<br>nhận biết|Popup thông báo đến người được phân phối Email||
|11.1.2||Chức năngxử lýemail|||||
|11.1.2.1||Chương trình có đầy đủ các tính<br>năng xử lý email của ứng dụng<br>Outlook như đọc, trả lời, chuyển<br>tiếp, soạn thảo email, chỉnh sửa,<br>đính kèm file. Các thao tác xử lý<br>được thực hiện trực tiếp trên<br>chương trình, không qua công cụ<br>trung gian.||Người dùng đọc thư<br>gửi đến, soạn thư và<br>chỉnh sửa thư trả lời,<br>chuyển tiếp trực tiếp<br>được thư cho các cá<br>nhân, đơn vị khác,<br>đính kèm và tải được<br>các file đính kèm.|1. Yêu cầu nghiệp vụ<br>- Người dùng đọc thư gửi đến, soạn thư, chuyển tiếp trực tiếp được thư cho các cá nhân, đơn<br>vị khác, đính kèm và tải được các file đính kèm.<br>- Cho phép cấu hình dung lượng file đính kèm (gửi ra) theo mail<br>- Khi soạn mail<br>+ Nếu tích chọn mail nội bộ => Hiển thị chữ ký cá nhân<br>+ Nếu khác nội bộ => Không hiển thị chữ ký cá nhân||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.2.2|Thay đổi các trạng thái xử lý của<br>email|Hệ thống tự động<br>chuyển trạng thái thư<br>khi người dùng thao<br>tác và xử lý thư: Thư<br>chưa đọc, thư đã đọc,<br>thư đã trả lời, thư đã<br>xử lý.<br>Người dùng có thể<br>lựa chọn chuyển<br>trạng thái của thư<br>trong các trường hợp<br>không cần trả lời lại<br>thư khách hàng, tạo<br>ghi chú để đánh dấu<br>phân loại.|1. Yêu cầu nghiệp vụ<br>- Hệ thống tự động chuyển trạng thái thư khi người dùng thao tác và xử lý thư: Thư chưa đọc<br>(màu), thư đã đọc (màu), thư đã trả lời (trạng thái), thư đã xử lý (trạng thái ticket).<br>Người dùng có thể lựa chọn chuyển trạng thái của thư trong các trường hợp không cần trả lời<br>lại thư khách hàng, phân loại phản ánh|
|11.1.2.3|Có chức năng bàn giao email và<br>lịch sử bàn giao email.|Người dùng thực<br>hiện được bàn giao<br>email của mình cho<br>người khác, SUP<br>thực hiện bàn giao<br>giữa các nhân viên<br>và lưu được lý do<br>chuyển tiếp email.<br>Nhân viên đọc được<br>lịch sử bàn giao và lý<br>do của việc bàn giao<br>thư.|1. Yêu cầu nghiệp vụ<br>- Người dùng thực hiện được bàn giao email của mình cho người khác, lưu được lý do chuyển<br>tiếp email. Nhân viên đọc được lịch sử bàn giao và lý do của việc bàn giao thư.|
|11.1.2.4|Có tính năng tạo lưu ý trong<br>email, bàn giao thư từ user này<br>sang user khác.|Người dùng soạn<br>được lưu ý và lưu<br>vào mail khách gửi<br>đến khi email đang<br>cần theo dõi, đang<br>chờxửlý.|1. Yêu cầu nghiệp vụ<br>- Cho phép tạo lưu ý khi bàn giao mail từ user này sang user khác<br>- Cho phép ghi chú riêng tư (chỉ người tạo nhìn thấy) và ghi chú công khai. Cho phép xem<br>danh sách ghi chú|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.2.5|Có tính năng tạo thư mới để gửi<br>cho khách hàng|Người dùng soạn và<br>tạo được thư mới để<br>gửi cho tập khách<br>hàng nhất định từ các<br>đầu email đã được<br>cài đặt vào chương<br>trình.|1. Yêu cầu nghiệp vụ<br>- Người dùng soạn và tạo được thư mới để gửi cho tập khách hàng nhất định từ các đầu email<br>đã được cài đặt vào chương trình: Hàng loạt (import theo file) và đơn lẻ<br>- Hàng loạt: Tạo nhiều mail cho 1 danh sách địa chỉ email<br>- Đơn lẻ: Tạo 1 mail (1 hay nhiều địa chỉ trong to)|
|11.1.2.6|Dung lượng mail đính kèm|Nâng dung lượng file<br>đính kèm khi phản<br>hồi mail tới KH:<br>Hiện tại hệ thống chỉ<br>cho phép gửi file<br>đính kèm có dung<br>lượng<br><5MB, tuy nhiên với<br>những file mà BO<br>ngửi đến KH có dung<br>lượng lớn hơn 5MB<br>nên sẽ không gửi<br>được, NV CSKH<br>phải tách thành nhiều<br>file để gửi nhiều lần<br>tới mail của KH<br>=> / Cần nâng dung<br>lượng file đính kèm<br>lên cao hơn (trên<br>20MB) để NVCSKH<br>gửi mail phản hồi tới<br>KH|Nâng dung lượng file đính kèm khi phản hồi mail tới KH: Hiện tại hệ thống chỉ cho phép gửi<br>file đính kèm có dung lượng<br><5MB, tuy nhiên với những file mà BO ngửi đến KH có dung lượng lớn hơn 5MB nên sẽ<br>không gửi được, NV CSKH phải tách thành nhiều file để gửi nhiều lần tới mail của KH<br>=> / Cần nâng dung lượng file đính kèm lên cao hơn (trên 20MB) để NVCSKH gửi mail phản<br>hồi tới KH|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.2.7|Tính năng theo dõi các phản ánh<br>chuyển BO trên ht|Tính năng theo dõi<br>các phản ánh chuyển<br>BO trên ht. Xây dựng<br>giao diện cho người<br>dùng nhập loại khiếu<br>nại của KH và thời<br>gian xử lý tương ứng<br>của các phản ánh<br>nhập chuyển BO, hệ<br>thống sẽ hiển thị<br>thông báo khi phản<br>ánh hết hạn hoặc quá<br>hạn để người dùng<br>chủ động vào cập<br>nhật thông tin đóng<br>phản ánh đúng hạn;<br>Người quản trị được<br>phép cấu hình thay<br>đổi/thêm/bớt đầu<br>mục nhập và thời<br>gian tương ứng.|- Chức năng tạo phản ánh trên eContact (cần Người quản trị được phép cấu hình thay<br>đổi/thêm/bớt đầu mục nhập và thời gian tương ứng) hoặc BCCS<br>- Cập nhật hạn phản ánh BO trên eContact (BCCS truyền sang)<br>- Theo dõi hạn, trạng thái xử lý<br>- Quá trình xử lý (VD:có thể mở link sang BCCS => Xem lịch sử xử lý phản ánh)|
|11.1.2.8|Tính năng gửi mail cho KH theo<br>file:|Tính năng gửi mail<br>cho KH theo file: Hệ<br>thống cho phép<br>người dùng thao  tác<br>gửi Email cho KH<br>theo file danh sách<br>mail đính kèm, nhằm<br>mục đích truyền<br>thông, quảng cáo tùy<br>thuộc từng giai đoạn<br>của chiến dịch<br>CSKH:|Tính năng gửi mail cho KH theo file: Hệ thống cho phép người dùng thao  tác gửi Email cho<br>KH theo file danh sách mail đính kèm, nhằm mục đích truyền thông, quảng cáo tùy thuộc<br>từng giai đoạn của chiến dịch CSKH:|
|11.1.3|Chức nănghiển thị|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|11.1.3.1||Hiển thị đầy đủ các trường thông<br>tin khi có email gửi đến chương<br>trình||Người dùng kiểm tra<br>được các trường<br>thông tin tương tác<br>của khách hàng qua<br>email trên màn hình<br>hiển thị: email khách<br>hàng, thời gian gửi<br>đến, thời gian phải<br>trả lời, subject, số thẻ<br>hội viên, hạng thẻ<br>hội viên|1. Yêu cầu nghiệp vụ:<br>- Người dùng kiểm tra được các trường thông tin tương tác của khách hàng qua email trên<br>màn hình hiển thị: email khách hàng, thời gian gửi đến, thời gian phải trả lời (SLA), subject,<br>các trường thông tin động<br>- Các trường thông tin động: Đồng bộ/gọi API/Import||
|11.1.3.2||Hiển thị trạng thái của email trên<br>chương trình||Người dùng kiểm tra<br>được tình trạng của<br>email: Đã đọc, đã trả<br>lời, đã xử lý nhưng<br>không cần gửi thư,<br>đã chuyển tiếp cho<br>nhóm xử lý nghiệp<br>vụ.|- Tương tự trạng thái email||
|11.1.3.3||Hiển thị lịch sử trao đổi mail với<br>KH||Người dùng kiểm tra<br>và đọc được loop<br>trao đổi thư theo thứ<br>tự thời gian xử lý<br>trong một email.|- Người dùng kiểm tra và đọc được loop trao đổi thư theo thứ tự thời gian xử lý trong một<br>email.<br>- Hiển thị luồng trao đổi mail||
|11.1.3.4||Hiển thị email gửi đến và gửi đi<br>theo đầu email nhận||Người dùng kiểm tra<br>được số lượng, nội<br>dung thư đã nhận, đã<br>gửi theo đầu email<br>nhận thư.|- Xây dựng báo cáo thống kê mail vào, báo cáo mail ra (luồng chủ động)||
|11.1.4||Chức năng phân loại|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.4.1|Nâng cấp tính năng nhập thông|Cấu hình bộ nhập<br>thống kê cho kênh<br>email trên hệ thống :<br>(1) Cần nâng cấp bổ<br>sung thêm cấp 5<br>trường nhập thống<br>kê;<br>(2) Cập nhật bộ nhập<br>thống kê mới lên hệ<br>thống ;<br>(3) Cấu hình trường<br>nhập thống kê cho<br>kênh Email<br>- Cho phép phân<br>quyền thêm bớt bộ<br>nhập<br>- Xây dựng cơ chế<br>động bộ tự động sang<br>BCCS|Hiện tại nhập thống kê theo 4 cấp  => Chuyển nhập thống kê theo 5 cấp<br>Hệ thống eContact đã có chức năng nhập thống kê nhu cầu của KH theo 4 cấp tương tự như<br>trên BCCS (đã cấu hình trên kênh Fanpage-MXH). Tuy nhiên bộ nhập đã cũ và không phù<br>hợp với hiện tại (hiện có 5 cấp). Do đó: (1) Cần nâng cấp bổ sung thêm cấp 5 trường nhập<br>thống kê; (2) Cập nhật bộ nhập thống kê mới lên hệ thống eContact; (3) Cấu hình trường<br>nhập thống kê cho kênh Email.|
|11.1.4.2|Đồng bộ dữ liệu nhập thống kê<br>trên hệ thống eContact sang hệ<br>thống BCCS|Sau khi NVCSKH<br>cập nhật thông tin<br>thống kê nhu cầu trên<br>eContact, hệ thống<br>có tính năng cho<br>phép người dùng có<br>thể đồng bộ dữ liệu<br>nhập lên hệ thống<br>BCCS (mục nhập<br>thống kê). Import dữ<br>liệu theo file.|Hệ thống có tính năng cho phép người dùng có thể đồng bộ dữ liệu nhập lên hệ thống BCCS<br>(mục nhập thống kê)<br>Đồng bộ phân cấp (5 cấp nhập thống kê)<br>Import dữ liệu theo file: Danh mục bộ nhập thống kê có thể tự định nghĩa được theo file<br>Danh mục loại phản ánh đang được khai báo độc lập cả BCCS và IPCC. Để đồng bộ dữ liệu<br>loại phản ánh ticket sang thì danh mục 2 bên phải đồng bộ|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|11.1.4.3||Theo|chủ đề.|Người dùng tiếp<br>nhận email gửi đến<br>và kiểm tra nội dung<br>email có thể chọn<br>chủ đề email theo list<br>chủ đề được cấu hình<br>sẵntronghệ thống.|- Phân loại phản ánh email||
|11.1.5||Chức năngtìm kiếm|||||
|11.1.5.1||Có tính năng tìm kiếm email theo<br>các trường thông tin: địa chỉ<br>email khách gửi đến, theo chủ<br>đề, theo từ khóa trong nội dung,<br>theo thời gian nhận, theo số thẻ<br>hội viên||Người dùng tìm kiếm<br>được luồng email<br>khách gửi đến, luồng<br>email trao đổi với<br>khách thông qua địa<br>chỉ email khách gửi<br>đến, chủ đề khách<br>viết, theo một vài từ<br>khóa trong nội dung,<br>theo thời gian khách<br>gửi đến, theo số thẻ<br>hội viên.|- Tìm kiếm theo nhiều tiêu chí: Người dùng tìm kiếm được luồng email khách gửi đến, luồng<br>email trao đổi với khách thông qua địa chỉ email khách gửi đến, chủ đề khách viết, theo một<br>vài từ khóa trong nội dung, theo thời gian khách gửi đến, theo số thẻ hội viên.||
|11.1.5.2||Lọc email nhanh theo user, thời<br>gian, chủ đề, wrap up code, trạng<br>thái để theo dõi và xử lý theo thứ<br>tự.||Agent vào trang<br>Supervisor và tìm<br>kiếm theo các nội<br>dung: user, thời gian,<br>chủ đề, wrap up<br>code, trạng thái|- Chức năng filter theo các tiêu chí: user (ĐTV đang được giao), thời gian, chủ đề,**wrap up**<br>**code**, trạng thái||
|11.1.5.3||Nhận biết email trùng||Trong quá trình xử lý<br>agent sẽ chủ động<br>phát hiện được email<br>gửi trùng (tiêu chí<br>trùng sẽ do IT cấu<br>hình trên hệ thống)<br>để chọn trả lời hoặc<br>không|- Cho phép lọc trùng email theo các thuộc tính<br>- Cho phép cấu hình thời gian quét, luật check trùng||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.5.4|Bổ sung tính năng tìm kiếm<br>Email theo nội dung:|Bổ sung tính năng<br>tìm kiếm Email theo<br>nội dung:<br>Hệ thống mới chỉ<br>cho phép người dùng<br>tìm kiếm các Email<br>gửi đến mail<br>cskh@viettel.com.vn<br>, chưa cho phép tìm<br>kiếm theo mail người<br>nhận và nội dung<br>mail da gửi đến/đi<br>=> Cần xây dựng<br>tính năng tìm kiếm<br>các mail theo mail<br>người nhận và nội<br>dung đã gửi đến/đi<br>cho KH để<br>NVCSKH có thể tìm<br>kiếm các Email<br>nhanh hơn.<br>Mô tả: Tạo thêm ô<br>tìm kiếm “nội dung”<br>ở mục “Lọc phản<br>ánh” bên trái của<br>giao diện mail. NV<br>CSKH gõ nội dung<br>cần tìm vào ô tìm<br>kiếm này<br>=> hệ thống sẽ lọc và<br>trả về tất cả các<br>email có nội dung mà<br>NV đang cần tìm<br>kiếm.|Hệ thống mới chỉ cho phép người dùng tìm kiếm các Email gửi đến mail<br>cskh@viettel.com.vn, chưa cho phép tìm kiếm theo mail người nhận và nội dung mail gửi<br>đến/đi => Cần xây dựng tính năng tìm kiếm các mail theo mail người nhận và nội dung đã<br>gửi đến/đi cho KH để NVCSKH có thể tìm kiếm các Email nhanh hơn.<br>Mô tả: Tạo thêm ô tìm kiếm “nội dung” ở mục “Lọc phản ánh” bên trái của giao diện mail.<br>NV CSKH gõ nội dung cần tìm vào ô tìm kiếm này => hệ thống sẽ lọc và trả về tất cả các<br>email có nội dungmàNVđangcần tìmkiếm.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.5.5|Tính năng hiển thị các địa chỉ<br>email khi người dùng gõ các chữ<br>cái đầu email vào trong các mục<br>To/CC/ BCC để NV CSKH có<br>thể chọn nhanh các mail đã gửi|Bổ sung tính năng<br>hiển thị các địa chỉ<br>email khi người dùng<br>gõ các chữ cái đầu<br>email vào trong các<br>mục To/CC/ BCC để<br>NV CSKH có thể<br>chọn nhanh các mail<br>đã gửi, không cần<br>mất thời gian gõ lại,<br>ví dụ: NV CSKH chỉ<br>cần gõ: “tien”hệ<br>thống sẽ d hiển thị<br>các địa chỉ mail gần<br>giống mà NV CSKH<br>đã từng gửi:<br>tienthanh@viettel.co<br>m.vn,<br>tienthanh02@viettel.<br>com.vn,<br>tienpd1@viettel.com.<br>vn.|để NV CSKH có thể chọn nhanh các mail đã gửi, không cần mất thời gian gõ lại, ví dụ: NV<br>CSKH chỉ cần gõ: “tien”, hệ thống sẽ hiển thị các địa chỉ mail gần giống mà NV CSKH đã<br>từng gửi: tienthanh@viettel.com.vn, tienthanh02@viettel.com.vn, tienpd1@viettel.com.vn.<br>Hiển thị với các email đã gửi đi và đã được nhận|
|11.1.6|Chức năngcảnh báo|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.6.1|Hệ thống cảnh báo được thời<br>gian Email sắp hết hạn xử lý, đã<br>hết hạn xử lý dựa trên thời gian<br>khách gửi thư đến trong số thư<br>được nhận và trong quese|Agent có thể tự xem<br>thư nào sắp hết hạn<br>xử lý, thư nào đã hết<br>hạn xử lý trong số<br>thư nhận được hoặc<br>thư trong Q để biết<br>thời hạn phải xử lý<br>cho đúng hạn hoặc<br>có cảnh báo từ hệ<br>thống.<br>Khi phản ánh còn 10<br>phút ht sẽ popup<br>thông báo lên màn<br>hình phản ánh sắp<br>hết hạn, và đến khi u<br>hết hạn, hệ thống sẽ<br>tiếp tục popup một<br>lần nữa báo đỏ lên<br>cảnh báo cho người<br>dùng i phản ánh đã<br>quá hạn<br>Thời gian cảnh báo<br>được cấu hình theo<br>từng queue email<br>riêng|- Cảnh báo sắp hết hạn: Agent có thể tự xem thư nào sắp hết hạn xử lý, thư nào đã hết hạn xử<br>lý trong số thư nhận được hoặc thư trong queue để biết thời hạn phải xử lý cho đúng hạn hoặc<br>có cảnh báo từ hệ thống.<br>- Cho phép filter mail sắp hết hạn theo thời gian từ đến: Ví dụ email sắp hết hạn trong 20 phút<br>đến 30 phút<br>- Cấu hình màu email sắp hết hạn theo từng email dịch vụ<br>- Cảnh báo sắp hết hạn hoặc quá hạn cho TVV (người được giao xử lý email) và Giám sát<br>viên (hiển thi tất cả cảnh báo) (popup hoặc noti hoặc bảng thông báo)<br>- Cho phép cấu hình người giám sát email (thêm, xoá)|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.6.2|Nhận diện từ khóa có dấu hiệu<br>tiêu cưc, từ khóa chuyên ngành|Chương trình có thể<br>tự động tìm kiếm và<br>nhận diện từ khóa<br>tiêu cực, từ khóa<br>chuyên ngành… theo<br>bộ từ khóa được cài<br>đặt trong hệ thống để<br>gắn vào email của<br>khách, giúp nhân<br>viên nhận diện và xử<br>lý theo thứ tự ưu tiên|- Tích hợp với API KGM|
|11.1.6.3|Tính năng thông báo khi có :<br>Email đặc biệt gửi đến|Hệ thống gửi SMS<br>tới các số TB được<br>cấu hình sẵn trên hệ<br>thống khi KH gửi<br>Email tới Email và<br>có CC/BCC tới các<br>Email đặc biệt (Ví<br>dụ: Email của Ban<br>Tổng Giám đốc, :<br>Hiệp hội người tiêu<br>dùng, Email tới các<br>đơn vị báo chí...).<br>Danh sách Email đặc<br>biệt sẽ do TT CSKH<br>đề xuất. Hệ thống<br>cho phép người quản<br>trị có thể thay<br>đổi/thêm/bớt số điện<br>thoại người nhận<br>SMS, danh sách<br>Email đặc biệt.|- Nếu có mail đặc biệt nằm trong: To; BCC, CC thì gửi sms đến danh sách thuê bao được cấu<br>hình<br>- Cấu hình sms cảnh báo cho từng mail dịch vụ|
|11.1.7|Chức nănglưu trữ|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|11.1.7.1||Soạn thảo và lưu trữ mẫu<br>(template) email để nhân viên xử<br>lý chọn template thư phù hợp trả<br>lời khách. User quản lý có thể<br>thay đổi, chỉnh sửa, tạo mới các<br>template email.||Tạo được các mẫu<br>thư trả lời sẵn trên hệ<br>thống để hỗ trợ nhân<br>viên lựa chọn tên<br>template khi soạn thư<br>trả lời khách. Không<br>hạn chế việc chỉnh<br>sửa, thêm mới các<br>mẫu thư này trên hệ<br>thống.|Cho phép NVCSKH lựa chọn mẫu Email được cấu hình sẵn để gửi cho KH<br>Người quản trị được phép cấu hình thay đổi/thêm/bớt các mẫu Email chung cho toàn bộ hệ<br>thống||
|11.1.7.2||Lưu trữ địa chỉ email (Contacts)<br>của các bộ phận/đơn vị có liên<br>quan để nhân viên sử dụng khi<br>cần gửi thư mới, CC, BCC email.||Lưu được các địa chỉ<br>email/số điện thoại,<br>tên các bộ phận nội<br>bộ trên hệ thống để<br>khi cần gửi thư cho<br>các bộ phận nhân<br>viên có thể search và<br>lấy contact gửi trực<br>tiếp, không cần phải<br>copy địa chỉ email<br>thủ công.|- Xây dựng tính năng lưu trữ danh sách email: email đã được gửi nhận, import<br>- Tạo group mail||
|11.1.7.3||Soạn và lưu trữ được chữ ký của<br>các user||Tạo và chỉnh sửa<br>được chữ ký cho<br>từng user trên hệ<br>thống|- Cho phép tạo và chỉnh sửa được chữ ký (cá nhân) của user sử dụng email<br>- Nếu tích chọn mail nội bộ => Hiển thị chữ ký cá nhân<br>- Nếu khác nội bộ => Không hiển thị chữ ký cá nhân<br>VD: CSKH@viettel.com.vn có 20 người dùng. Hiển thị chữ ký riêng với từng người||
|11.1.8||Chức năngchia email|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.1.8.1|Chia email ưu tiên cho user xử lý<br>thư trước đó của khách|Hệ thống chia mail<br>đều theo vòng lặp<br>theo thứ tự ưu tiên:<br>cho người dùng đã<br>xử lý gần nhất email<br>của khách nếu người<br>dùng đang ở trạng<br>thái sẵn sàng sau đó<br>chia đều mail còn lại<br>cho số lượng nhân<br>viên được khai báo<br>trong calàmviệc|Hệ thống chia mail đều theo vòng lặp theo thứ tự ưu tiên: cho người dùng đã xử lý gần nhất<br>(người xử lý cuối cùng) email của khách nếu người dùng đang ở trạng thái sẵn sàng sau đó<br>chia đều mail còn lại cho số lượng nhân viên được khai báo trong ca làm việc|
|11.1.8.2|Chia email gửi đến theo nhóm<br>user/user được cài đặt/chỉ định.|Hệ thống nhận diện<br>và cài đặt được một<br>số phân loại email<br>gửi đến nhóm/cá<br>nhân nhân viên được<br>chỉ định xử lý mà<br>không tuân theo<br>nguyên tắc chia mail<br>đều.|Hệ thống nhận diện và cài đặt được một số phân loại email gửi đến nhóm/cá nhân nhân viên<br>được chỉ định xử lý mà không tuân theo nguyên tắc chia mail đều.|
|11.1.8.3|Chia email theo trạng thái của<br>nhân viên được khai báo|Hệ thống chia mail<br>đều theo vòng lặp<br>cho số lượng nhân<br>viên được khai báo<br>có tình trạng sẵn<br>sàng trong ca làm<br>việc.|Hệ thống chia mail đều theo vòng lặp cho số lượng nhân viên được khai báo có tình trạng sẵn<br>sàng trong ca làm việc. Giống như hiện tại đang xoay vòng|
|11.1.9|**Chức năng vận hành**|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|11.1.9.1||Tnh năng cho phép người dùng<br>(BO) thay đổi mật khẩu của<br>email||Hệ thống cho phép<br>người dùng có thể<br>chủ động thay đổi<br>mật khẩu của email<br>cskh@viettel.com.vn<br>thay vì phải gửi yêu<br>cầu đơn : lẻ sang<br>VTS khi có nhu cầu|Hệ thốngcho phép người dùng có thể chủ động thay đổi mật khẩu của email<br>cskh@viettel.com.vn thay vì phải gửi yêu cầu đơn lẻ sang VTS khi có nhu cầu.||
|11.1.9.2||tính năng cho phép người dùng<br>chủ động cấu hình thêm/ xóa tài<br>khoản Email (chỉ phân quyền<br>cho Admin)|||Bổ sung tính năng cho phép người dùng chủ động cấu hình thêm/ xóa tài khoản Email (chỉ<br>phân quyền cho Admin)||
|11.1.9.3||Tính năng thay đổi chữ ký Email<br>trên hệ thống||Tính năng thay đổi<br>chữ ký Email trên hệ<br>thống eContact (theo<br>PYC số 912/PYC-<br>CSKH ngày<br>28/07/2021): Thay<br>đổi chữ ký mail<br>CSKH theo nhận<br>diện Logo mới trên<br>hệ thống eContact<br>nhằm đồng nhất bộ<br>nhận diện thương<br>hiệu của T Viettel<br>trên toàn bộ sản<br>phẩm dịch vụ và các<br>kênh đang cung cấp<br>tới Khách hàng|Thay đổi chữ ký mail dịch vụ (vào hoặc ra). CSKH theo nhận diện Logo mới trên hệ thống<br>eContact nhằm đồng nhất bộ nhận diện thương hiệu của Viettel trên toàn bộ sản phẩm dịch vụ<br>và các kênh đang cung cấp tới Khách hàng<br>Cho phép người dùng thêm mới và thay đổi chữ ký<br>Chi tiết mã IBM 912||
|11.1.9.4||Thêm/ xóa người dùng vào hệ<br>thống eContact; Thêm/xóa ID<br>đăng nhập hệ thống eContact;||Thêm/ xóa người<br>dùng vào hệ thống<br>eContact; Thêm/xóa|Thêm/ xóa người dùng vào hệ thống eContact; Thêm/xóa ID đăng nhập hệ thống eContact;<br>Thay đổi phông nền Email;…||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||ID đăng nhập hệ<br>thống eContact;||
|11.1.9.5|Thay đổi phông nền Email;|CHủ động Thay đổi<br>phôngnền Email;|CHủ động Thay đổi phông nền Email;|
|11.1.10|**Chức năng báo cáo**|Xây dựng tính năng<br>cho NVCSKH 1 tích<br>chọn phân loại dữ<br>liệu đầu vào Email<br>cskh@viettel.com.vn<br>(Email 0 từ KH và<br>Email phối hợp<br>phòng ban), xuất báo<br>cáo đánh giá số<br>lượng mail tương tác<br>0 tới KH. Bổ sung<br>thời gian phản hồi<br>KH lần đầu và thời<br>gian đóng phản ánh<br>trên BC chi tiết phản<br>ánh Email.|"- Xây dựng tính năng cho NVCSKH tích chọn phân loại dữ liệu đầu vào Email<br>cskh@viettel.com.vn (Email từ KH và Email phối hợp phòng ban), xuất báo cáo đánh giá số<br>lượng mail tương tác tới KH. Tích chọn loại email khi cập nhật phản ánh<br>- Bổ sung thời gian phản hồi KH lần đầu và thời gian đóng phản ánh trên BC chi tiết phản<br>ánh Email."<br>Chị Trà gửi lại Template tất cả báo cáo email 15/06/2022|
|**11.2**|**Phân hệ mạng xã hội**|||
|11.2.1|Popuptrên kênh Mạngxã hội||- Popupthôngtin khách hàngtrên kênh MXH|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.2.2|Bổ xung tính năng tiếp nhận các<br>phản ánh từ kênh MyViettel|- Trên App My<br>Viettel, mục Gói<br>cước/DV GTGT 2<br>cho phép người dùng<br>vào comment<br>(bình luận), đánh giá<br>và gửi các yêu cầu hỗ<br>trợ về dịch vụ. Tuy<br>nhiên không có nhân<br>viên trả lời/hỗ trợ<br>Khách hàng khiến<br>KH không hài lòng<br>và nguy cơ phát sinh<br>khiếu nại.<br>- Nguyên nhân do<br>các comment này<br>chưa 0 / được đẩy/ 2<br>về hệ thống giải đáp<br>đa kênh trực tuyến<br>(eContact)|- Tích hợp toàn bộ dữ liệu KH comments trên App My Viettel lên hệ thống<br>Quyền BO:<br>+ Tiếp nhận ticket, chuyển ticket.<br>+ Đóng ticket hàng loạt.<br>+ Giám sát lưu lượng trên tất cả các kênh.<br>+ Xuất báo cáo chi tiết ticket.<br>Quyền NV CSKH<br>+ Tiếp nhận ticket, chuyển ticket.<br>- Cho phép tiếp nhận và giải đáp phản ánh<br>- Xuất báo cáo chi tiết ticket<br>- Theo dõi được lượng dữ liệu đầu vào online trên kênh, số lượng queue<br>- Xây dựng báo cáo KPIs thời gian phản hồi cho KH|
|11.2.3|Tiếp nhận tương tác qua nhiều<br>nền tảng MXH (không giới hạn<br>số lượng nền tảng MXH)||- Tiếp nhận tương tác qua FB<br>- Chat: Zalo, Mocha|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.2.4|Chức năng phân luồng xử lý|Khi có thông tin cần<br>xử lý, hệ thống sẽ có<br>thông báo có tin nhắn<br>mới (có cảnh báo),<br>nhân viên tích vào<br>mục cần xử lý tương<br>ứng và lần lượt xử lý<br>các tương tác theo<br>thứ tự thời gian.<br>Trong ca làm việc có<br>từ 2 người trở lên<br>cùng tham gia xử lý,<br>để tránh trả lời trùng,<br>một khi nhân viên<br>nhấn vào bài<br>viết/inbox/comment<br>cần xử lý thì item<br>này sẽ bị khóa lại ở ở<br>các user còn lại.<br>Trong trường hợp<br>sau 5 phút người xử<br>lý chưa xử lý xong<br>items, hệ thống mở<br>khóa chuyển sang<br>nhân viên khác xử lý<br>hoặc nhân viên khác<br>có thể chủ động mở<br>khóa để xử lý.|- Khi có thông tin cần xử lý, hệ thống sẽ có thông báo có tin nhắn mới (có cảnh báo), nhân<br>viên tích vào mục cần xử lý tương ứng và lần lượt xử lý các tương tác theo thứ tự thời gian.<br>Trong ca làm việc có từ 2 người trở lên cùng tham gia xử lý, để tránh trả lời trùng, một khi<br>nhân viên nhấn vào bài viết/inbox/comment cần xử lý thì item này sẽ bị khóa lại ở ở các user<br>còn lại.<br>- Luồng chat: Nếu không có ĐTV tiếp nhận => Rớt. Nếu có ĐTV tiếp nhận mà không phản<br>hồi => Cảnh báo<br>-Sau 5 phút không phản hồi chat + không hold hoặc offline => Transfer (Bỏ nội dung này vì<br>Giám sát có thể transfer thủ công 12.2.1.3)<br>- KH chat bị rớt => Tái phân bổ. Khi phân bổ lại từ thời điểm rớt đến thời điểm quét. Nếu KH<br>đã chat lại và được tiếp nhận thì không tái phân bổ nữa<br>- Áp dụng cho định danh: Với TH chat rớt, kh chat tiếp lên => note hội thoại trc (nhỡ) + xem<br>lịch sử + không tái phân bổ chat nhỡ<br>- Cấu hình được tỷ lệ % ĐTV rảnh tiếp nhận phiên chat phân bổ lại để đảm bảo tỷ lệ ĐTV<br>tiếp nhận KH online<br>- Duration phân bổ = 24h kể từ lúc KH phản ánh (Cấu hình cho inbox từng page) => Áp dụng<br>cho chat, cmt, email|
|11.2.5|- Giám sát: cho phép Transfer<br>chat sangĐTV khác||- Giám sát: cho phép Transfer chat sang ĐTV khác|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|11.2.6||Các tác vụ xử lý||1.Thêm tính năng<br>ngắt dòng (xuống<br>dòng trong 1 lần<br>tương tác) khi<br>NVCSKH phản hồi<br>thông tin tới KH<br>(kênh Chat)<br>-Hiện tại khi<br>NVCSKH tương<br>tác/phản hồi thông<br>tin tới KH qua đoạn<br>hội thoạt chat chưa<br>có tính năng ngắt<br>dòng  NVCSKH<br>không thực hiện<br>được việc tách ý<br>trong cùng 1 nội<br>dung tương tác<br>Bổ sung thêm tính<br>năng ngắt dòng trong<br>1 lần tương tác.|1.Thêm tính năng ngắt dòng (xuống dòng trong 1 lần tương tác) khi NVCSKH phản hồi<br>thông tin tới KH (kênh Chat)<br>-Hiện tại khi NVCSKH tương tác/phản hồi thông tin tới KH qua đoạn hội thoạt chat chưa có<br>tính năng ngắt dòng  NVCSKH không thực hiện được việc tách ý trong cùng 1 nội dung<br>tương tác<br>Bổ sung thêm tính năng ngắt dòng trong 1 lần tương tác.||
|11.2.7||Comment/bài viết: Trả lời, Nhắn<br>tin, Thích, Theo dõi, Xóa, Ẩn,<br>Trung lập, gắn nhãn phân loại,<br>bỏ qua, phân user xử lý.||Nhân viên tuân thủ<br>quy trình làm việc,<br>nội dung tương tác<br>để lựa chọn các tác<br>vụ xử lý đã nêu.|- Comment/bài viết: Trả lời, Nhắn tin, Thích, Theo dõi, Xóa, Ẩn, Trung lập, gắn nhãn phân<br>loại, bỏ qua, phân user xử lý.||
|11.2.8||Inbox: Bỏ qua, trả lời, gắn nhãn<br>phân loại, thả icon.||Nhân viên tuân thủ<br>quy trình làm việc,<br>nội dung tương tác<br>để lựa chọn các tác<br>vụ xử lý đã nêu.|- Chat: Bỏ qua, trả lời, gắn nhãn phân loại, thả icon.||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|11.2.9||Chức năng nhập thống kê||Cấu hình bộ nhập<br>thống kê cho các<br>kênh trên hệ thống :<br>(1) Cần nâng cấp bổ<br>sung thêm cấp 5<br>trường nhập thống<br>kê;<br>(2) Cập nhật bộ nhập<br>thống kê mới lên hệ<br>thống ;<br>(3) Cấu hình trường<br>nhập thống kê cho<br>các kênh<br>- Cho phép phân<br>quyền thêm bớt bộ<br>nhập<br>- Xây dựng cơ chế<br>động bộ tự động sang<br>BCCS|Cấu hình bộ nhập thống kê cho các kênh trên hệ thống :<br>(1) Cần nâng cấp bổ sung thêm cấp 5 trường nhập thống kê;<br>(2) Cập nhật bộ nhập thống kê mới lên hệ thống ;<br>(3) Cấu hình trường nhập thống kê cho các kênh<br>- Cho phép phân quyền thêm bớt bộ nhập<br>- Xây dựng cơ chế động bộ tự động sang BCCS||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.2.10|Chức năng ticket (tham khảo<br>phần 6.1)|Giao lại ticket thủ<br>công cho NVCSKH<br>Thêm tính năng đánh<br>giá ticket trong<br>hạn/ngoài hạn trong<br>báo cáo<br>Nâng cấp tính năng<br>đóng ticket hàng loạt<br>Popup thông báo khi<br>có ticket mới được<br>giao<br>Quyền ẩn/xóa/sửa<br>ticket của BO|1. Hiện tại khi Giám sát thực hiện giao lại ticket thủ công cho NVCSKH gặp tình trạng: hệ<br>thống Econtact hiển thị toàn bộ NVCSKH bao gồm cả NVCSKH đang online (NVCSKH đi<br>làm) và offline (NVCSKH không đi làm) dẫn đến tình trạng nhầm lẫn trong quá trình giao<br>(hình ảnh bên dưới).<br>-Mong muốn nâng cấp:<br>+ Ưu tiên hiển thị danh sách các NVCSKH đang online lên đầu.<br>+ Có ký hiệu nhận biết để phân biệt  giữa NVCSKH đang online và offline.<br>2. '-Hiện tại trong báo cáo ticket đã có thông tin về tổng thời gian NVCSKH phản hồi, tuy<br>nhiên trong cột Tiến độ vi phạm chưa có mục đánh giá trong hạn, quá hạn để phục vụ công<br>tác kiểm soát của BO.<br>-Mong muốn nâng cấp: cột Tiến độ vi phạm trả dữ liệu bao gồm: (1) Trong hạn, (2) Quá hạn,<br>(3) Không đánh giá. Cụ thể:<br>vDữ liệu trong hạn được đánh giá như sau:<br>üTrong khung giờ từ 6h30-22h hàng ngày (ngày n): các trường hợp NVCSKH giải đáp và<br>phản hồi lại KH, thời gian NV CSKH phản hồi nhỏ hơn hoặc bằng 30 phút (Cột Tổng thời<br>gian TVV phản hồi)  Đánh giá: Trong hạn.<br>üTrong khung giờ từ 22h ngày hôm trước (ngày n)-6h30 ngày hôm sau (ngày n+1): các<br>trường hợp NV CSKH giải đáp và phản hồi lại KH trước 08h AM của ngày n+1  Đánh giá:<br>Trong hạn.<br>vDữ liệu quá hạn được đánh giá như sau:<br>üTrong khung giờ từ 6h30-22h hàng ngày (ngày n): các trường hợp NV CSKH giải đáp và<br>phản hồi lại KH, thời gian NV CSKH phản hồi lớn hơn 30 phút (Cột Tổng thời gian TVV<br>phản hồi)  Đánh giá: Quá hạn.<br>üTrong khung giờ từ 22h ngày hôm trước (ngày n)-6h30 ngày hôm sau (ngày n+1): các<br>trường hợp NV CSKH giải đáp và phản hồi lại KH sau 08h AM của ngày n+1  Đánh giá: Quá<br>hạn.<br>vDữ liệu KĐG được đánh giá như sau: các trường hợp NVCSKH tích bỏ qua ticket, không<br>giải đáp  Đánh giá: Không đánh giá.<br>Hình ảnh chi tiết các cột trong báo cáo<br>3. Nâng cấp tính năng đóng ticket hàng loạt<br>-Đốivớitính năng đóng tickethàngloạt:hiệntại hệ thốngEcontact chỉ hỗ trợngườidùng|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||||||đóng toàn bộ ticket hoặc đóng 1 phần ticket (theo khoảng thời gian từ ngày tới ngày)  Chưa<br>hỗ trợ đóng ticket hàng loạt theo bài post hoặc từ khóa… (như hình ảnh bên dưới).<br>ðĐối với các bài post dạng livestream hoặc minigame, số lượng ticket đẩy về hệ thống rất<br>lớn, phần lớn là các ticket không cần giải đáp  Người dùng phải thực hiện đóng thủ công trên<br>hệ thống, ảnh hưởng tới tiến độ xử lý đối với các ticket khác.<br>-Mong muốn nâng cấp: Bổ sung thêm tính năng đóng ticket hàng loạt theo bài post (theo mã<br>bài post, link bài post) hoặc từ khóa.<br>Người sử dụng có thể chọn từng bài post, hoặc nhập từ khóa tra cứu  Hệ thống sẽ hiển thị<br>toàn bộ các ticket có liên quan để người dùng có thể thực hiện đóng ticket.<br>4 & 5. Xem trong PYC mã IBM đính kèm||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.2.11|Bổ sung tính năng tương tác lại<br>với các KH kết nối lên kênh<br>nhưng bị rớt|Với mục đích đảm<br>bảo 100% KH kết<br>nối lên kênh đều<br>được hỗ trợ (bao<br>gồm cả các KH kết<br>nối bị rớt) => Xây<br>dựng lại cơ chế giao<br>tương tác của KH<br>trên hệ thống về cho<br>TVV và có công cụ<br>để TVV chủ động<br>tương tác lại với các<br>KH bị rớt, trong đó<br>-         Về cơ chế<br>phân bổ tương tác tới<br>TVV:<br>+ Hiện tại: trong<br>trường hợp toàn bộ<br>TVV trên hệ thống<br>đều bận (full queue)<br>=> KH sẽ chờ trên hệ<br>thống trong 5 phút<br>(300s), trong thời<br>gian này nếu vẫn<br>không có TVV rảnh<br>=> Phiên chat rớt =><br>Kết thúc mà không<br>có thông báo tới KH.<br>+ Mong muốn: hệ<br>thống tăng thêm số<br>lần chờ của KH: từ 1<br>lần 300s tăng thành 2<br>lần 300s (tổng thời<br>gianchờ củaKHtrên|Với mục đích đảm bảo 100% KH kết nối lên kênh đều được hỗ trợ (bao gồm cả các KH kết<br>nối bị rớt) => Xây dựng lại cơ chế giao tương tác của KH trên hệ thống về cho TVV và có<br>công cụ để TVV chủ động tương tác lại với các KH bị rớt, trong đó<br>-         Về cơ chế phân bổ tương tác tới TVV:<br>+ Hiện tại: trong trường hợp toàn bộ TVV trên hệ thống đều bận (full queue) => KH sẽ chờ<br>trên hệ thống trong 5 phút (300s), trong thời gian này nếu vẫn không có TVV rảnh => Phiên<br>chat rớt => Kết thúc mà không có thông báo tới KH.<br>+ Mong muốn: hệ thống tăng thêm số lần chờ của KH: từ 1 lần 300s tăng thành 2 lần 300s<br>(tổng thời gian chờ của KH trên hàng chờ là 600s). Trong trường hợp vẫn không có TVV<br>rảnh để tiếp nhận phiên chat từ KH => Hệ thống sẽ hiển thị thông báo:<br>(1)  Với các KH có dữ liệu có thể tương tác lại (định danh) bao gồm: (1) App: MyViettel,<br>Mocha, Zalo; (2) Facebook => hiển thị thông báo: “Hiện tại toàn bộ các tư vấn viên đang bận,<br>Viettel sẽ sớm liên hệ lại để hỗ trợ KH”<br>(2)  Với các KH không có dữ liệu để tương tác lại bao gồm: KH tương tác trên các web<br>(4g.viettel.vn, viettel.vn, vtracking.viettel.vn, smartmotor.vn) => hiển thị thông báo: “Hiện tại<br>toàn bộ các tư vấn viên đang bận, Quý khách vui lòng để lại thông tin liên hệ để Viettel có thể<br>liên hệ lại hỗ trợ (email, SĐT)”. => nội dung này anh xin ý kiến của Sếp và chốt giúp em<br>-         Về cơ chế tương tác lại với các KH bị rớt<br>+ Với các KH có dữ liệu có thể tương tác lại (định danh) => Hệ thống cho phép TVV tương<br>tác lại qua hệ thống chat ngay cả khi KH đã bị rớt.<br>+ Với các KH không có dữ liệu để tương tác lại (không định danh) bao gồm: KH tương tác<br>trên các web (4g.viettel.vn, viettel.vn, vtracking.viettel.vn, smartmotor.vn) => TVV sẽ liên hệ<br>lại theo thông tin mà KH để lại (email, SĐT). Với nội dung này sẽ phát sinh trường hợp: KH<br>để lại số liên hệ của người khác, không phải số thực tế của KH => Phát sinh các trường hợp<br>khiếu nại do không xác nhận được SĐT mà KH cung cấp có chính xác hay không?|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||hàng chờ là 600s).<br>Trong trường hợp<br>vẫn không có TVV<br>rảnh để tiếp nhận<br>phiên chat từ KH =><br>Hệ thống sẽ hiển thị<br>thông báo:<br>(1)  Với các KH có<br>dữ liệu có thể tương<br>tác lại (định danh)<br>bao gồm: (1) App:<br>MyViettel, Mocha,<br>Zalo; (2) Facebook<br>=> hiển thị thông<br>báo: “Hiện tại toàn<br>bộ các tư vấn viên<br>đang bận, Viettel sẽ<br>sớm liên hệ lại để hỗ<br>trợ KH”<br>(2)  Với các KH<br>không có dữ liệu để<br>tương tác lại bao<br>gồm: KH tương tác<br>trên các web<br>(4g.viettel.vn,<br>viettel.vn,<br>vtracking.viettel.vn,<br>smartmotor.vn) =><br>hiển thị thông báo:<br>“Hiện tại toàn bộ các<br>tư vấn viên đang bận,<br>Quý khách vui lòng<br>để lại thông tin liên<br>hệ để Viettelcó thể||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||liên hệ lại hỗ trợ<br>(email, SĐT)”. =><br>nội dung này anh xin<br>ý kiến của Sếp và<br>chốt giúp em<br>-         Về cơ chế<br>tương tác lại với các<br>KH bị rớt<br>+ Với các KH có dữ<br>liệu có thể tương tác<br>lại (định danh) => Hệ<br>thống cho phép TVV<br>tương tác lại qua hệ<br>thống chat ngay cả<br>khi KH đã bị rớt.<br>+ Với các KH không<br>có dữ liệu để tương<br>tác lại (không định<br>danh) bao gồm: KH<br>tương tác trên các<br>web (4g.viettel.vn,<br>viettel.vn,<br>vtracking.viettel.vn,<br>smartmotor.vn) =><br>TVV sẽ liên hệ lại<br>theo thông tin mà<br>KH để lại (email,<br>SĐT). Với nội dung<br>này sẽ phát sinh<br>trường hợp: KH để<br>lại số liên hệ của<br>người khác, không<br>phải số thực tế của<br>KH => Phát sinhcác||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||trường hợp khiếu nại<br>do không xác nhận<br>được SĐT mà KH<br>cung cấp có chính<br>xác hay không?||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.2.12|Tính năng báo cáo|Các yc bổ xung xem<br>trong PYC|- Xây dựng tính năng xuất báo cáo thống kê, báo cáo chi tiết thời gian phản hồi trong phiên<br>chat của NVCSKH<br>- Xây dựng tính năng suất báo cáo thống kê thời gian trạng thái của NVCSKH trong ca trực|
|11.2.13|- Cửa số chat có câu chào mừng,<br>thông tin quảng cáo web app.<br>Khi khách hàng chat popup (nội<br>dung chat) lên cửa sổ, trước khi<br>ĐTV chat. Có thể cấu hình thông<br>tin (câu chào, thông tin quảng<br>cáo), tần suất hiển thị (ví dụ: sau<br>30 phút mới hiện lại câu chào)<br>trên cửa sổ theo queue chat<br>- Chưa dùng bot: Zalo,<br>web4g.viettel.vn<br>- Phạm vi: Làm cho cửa sổ chat<br>không có bot, từ bot sang ĐTV||- Cửa số chat có câu chào mừng, thông tin quảng cáo web app. Khi khách hàng chat popup<br>(nội dung chat) lên cửa sổ, trước khi ĐTV chat. Có thể cấu hình thông tin (câu chào, thông tin<br>quảng cáo), tần suất hiển thị (ví dụ: sau 30 phút mới hiện lại câu chào) trên cửa sổ theo queue<br>chat<br>- Chưa dùng bot: Zalo, web4g.viettel.vn<br>- Phạm vi: Làm cho cửa sổ chat không có bot, từ bot sang ĐTV|
|11.2.14|- Thống kê báo cáo chi tiết giữa<br>các phiên chat: thời gian trả lời<br>khách hàng trong đoạn hội thoại||- Thống kê báo cáo chi tiết giữa các phiên chat: thời gian trả lời khách hàng trong đoạn hội<br>thoại|
|11.2.15|- Nâng cấp: Bóc tách thời gian<br>KH chat lên hệ thống (lấy tin<br>nhắn cuối cùng của KH trong<br>phiên), thời gian hệ thống đẩy dữ<br>liệu về ĐTV, thời gian ĐTV tiếp<br>nhận phiên chat => ghi nhận lên<br>báo cáo<br>- KPI đánh giá thời gian tiếp<br>nhận phiên chat||- Nâng cấp: Bóc tách thời gian KH chat lên hệ thống (lấy tin nhắn cuối cùng của KH trong<br>phiên), thời gian hệ thống đẩy dữ liệu về ĐTV, thời gian ĐTV tiếp nhận phiên chat => ghi<br>nhận lên báo cáo<br>- KPI đánh giá thời gian tiếp nhận phiên chat|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.2.16|- Trưởng ca xem thời gian ĐTV<br>chuyển trạng thái theo ngày, theo<br>khung giờ<br>- Kiểm soát real time hành động<br>chuyển trạng thái||- Trưởng ca xem thời gian ĐTV chuyển trạng thái theo ngày, theo khung giờ<br>- Kiểm soát real time hành động chuyển trạng thái|
|11.2.17|- Tính năng năng ngắt dòng (ví<br>dụ: ctrl + enter, shift + enter)||- Tính năng năng ngắt dòng (ví dụ: ctrl + enter, shift + enter)|
|11.2.18|- Popup thông tin khách hàng từ<br>IPCC sang BCCS với các kênh<br>định danh (MyViettel, Mocha)||- Popup thông tin khách hàng từ IPCC sang BCCS với các kênh định danh (MyViettel,<br>Mocha)|
|11.2.19|- Đẩy group viettel giải đáp<br>online lên hệ thốngeContact||- Đẩy group viettel giải đáp online lên hệ thống eContact => Không được do fb không cấp<br>API|
|11.2.20|- Tictok đẩy qua hệ thống<br>econtact||- Tictok đẩy qua hệ thống econtact|
|11.2.21|- Đóng hàng loạt (select all) các<br>ticket theo bài đăng (comment<br>không có nội dung, hoặc không<br>phải trả lời). Có filter theo<br>keyword||- Đóng hàng loạt (select all) các ticket theo bài đăng (comment không có nội dung, hoặc<br>không phải trả lời). Có filter theo keyword|
|11.2.22|- Lấy thời gian ĐTV phản hồi<br>khách hàng (trong 30 phút). Tính<br>KPI theo việc xử lý ticket =><br>xuất trên báo cáo.||- Lấy thời gian ĐTV phản hồi khách hàng (trong 30 phút). Tính KPI theo việc xử lý ticket =><br>xuất trên báo cáo.|
|11.2.23|- Admin có quyền CRUD các<br>ticket(cmt FB)||- Admin có quyền CRUD các ticket (cmt FB) => VTS check lại quyền|
|11.2.24|- Tính năng giao ticket cả online<br>và offline: Bổ sung đk tìm kiếm<br>ĐTV online||- Tính năng giao ticket cả online và offline: Bổ sung đk tìm kiếm ĐTV online|
|11.2.25|- Kiểm soát real time hành động<br>chuyển trạngthái||- Kiểm soát real time hành động chuyển trạng thái|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|11.2.26||**Các tính năng tích hợp với**<br>**FaceBook**|||||
|11.2.27||Quản trị facebook page|||- Chức năng cho phép người dùng là quản trị hệ thống thực hiện tích hợp page của doanh<br>nghiệp vào hệ thống với các thông tin sau:<br>+ Tên trang Facebook<br>+ Mô tả<br>+ Đường link<br>- Cho phép thêm, sửa xóa thông tin tích hợp||
|11.2.28||Chức năng Ticket facebook.|||- Chức năng cho phép sau khi đã tích hợp 1 page vào hệ thống thành công, với tất cả các<br>comments/bài post khách hàng để lại trên page của DN<br>- Hệ thống tiếp nhận và tạo thành ticket trên hệ thống IPCC.<br>- Trên chức năng quản lý Tickets, chọn kênh Facebook : người dùng có thể thấy danh sách<br>các tickets||
|11.2.29||Chức năng chat facebook.|||Khách hàng vào page của doanh nghiệp, gửi chat Inbox page của doạnh nghiệp. Hệ thống get<br>chat và tạo thành hội thoại trên IPCC, phân bổ chat đến tư vấn viên đủ điều kiện||
|11.2.30||Báo cáo facebook|||- Bổ sung 1 báo cáo facebook với thông tin tìm kiếm: thời gian tiếp nhận, thời gian xử lý,<br>trạng thái, người gửi<br>- Cho phép xuất dữ liệu ra file excel||
|11.2.31||**Báo cáo chat**|||||
|11.2.32||Báo cáo chat tổng hợp|||- Bổ sung 1 báo cáo tổng hợp với thông tin tìm kiếm: thời gian tiếp nhận, thời gian xử lý,<br>TVV<br>- Cho phép xuất dữ liệu ra file excel||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.2.33|Báo cáo chat theo phiên<br>Báo cáo chat theo hội thoại||- Bổ sung 1 báo cáo tổng hợp với thông tin tìm kiếm: thời gian tiếp nhận, thời gian xử lý,<br>TVV<br>- Cho phép xuất dữ liệu ra file excel|
|11.2.34|||- Bổ sung 1 báo cáo tổng hợp với thông tin tìm kiếm: thời gian tiếp nhận, thời gian xử lý,<br>TVV<br>- Cho phép xuất dữ liệu ra file excel|
|11.2.35|**IPCC CLOUD BAMBOO -**<br>**CHAT ON WEB PORTAL**|||
|11.2.36|Cấu hình Domain Chat||- Chức năng cho phép khai báo thông tin Chung của Trang web, bao gồm: Tên, Mô tả|
|11.2.37|Tab Thôngtin web||- Chophépcậpnhật thôngtin Tên,mô tả trangweb|
|11.2.38|Tab Quản lý dịch vụ||- Cho phép thêm/sửa/xóa dịch vụ cho trang web. Mặc định khi thêm mới 1 domain, hệ thống<br>sẽ tự sinh 1 dịch vụ. Admin cũng có thể khai báo thêm dịch vụ|
|11.2.39|Tab Cấu hình hiển thị||- Cho phép cấu hình các thông tin hiển thị trên cửa sổ chat như: Tiêu đề, Màu sắc, Nhân viên<br>hỗ trợ, Ngôn ngữ|
|11.2.40|Tab Nhập thông tin||- Cho phép cấu hình 1 số thông tin như: Lời chào khách hàng khi khách hàng bắt đầu chat, tin<br>nhắn thông báo giao dịch chat kết thúc, thời gian cảnh báo khi khách hàng để quá lâu không<br>phản hồi Agent, tin nhắn cảnh báo khi khách hàng để quá lâu không phản hồi Agent|
|11.2.41|Tab Script Nhúng||- Cho phép xem Script của Domain do hệ thống tự sinh ra. Khi triển khai kênh chat trên Web,<br>cần nhúng Script này vào trang web để hiển thị được Domain|
|11.2.42|**Luồng chat**|||
|11.2.43|Gán danh sách agents vào queue<br>chat||- Với mỗi dịch vụ của domain, chương trình tự động sinh một queue chat tương ứng. Admin<br>hoặc giám sát viên của doanh nghiệp cần gán agents vào queue để tiếp nhận và xử lý chat|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|11.2.44|Khách hàng gửi yêu cầu chat||- Khách hàng có thể gửi yêu cầu chat đến hệ thống từ kênh web chat|
|11.2.45|Hiển thị thông báo có chat đến||- Chức năng cho phép hiển thị thông báo tới Agent khi có giao dịch chat phân bổ đến<br>- Khi có giao dịch chat (KH chat từ web), hệ thống sẽ thực hiện tìm kiếm Agent rảnh rỗi kênh<br>chat để phân bổ đến Agent. Agent được phân bổ giao dịch chat, màn hình sẽ hiển thị thông<br>báo|
|11.2.46|Agent tiếp nhận chat / Từ chối<br>chat||- Chức năng cho phép hiển Agent tiếp nhận / Từ chối chat khi có chat phân bổ đến|
|11.2.47|Agent thực hiện chat với khách<br>hàng||- Chức năng cho phép Agent thực hiện chat với khách hàng sau khi đã tiếp nhận giao dịch<br>web chat|
|11.2.48|Agent hold chat||- Khi Agent cần tra cứu hoặc trao đổi với Agent khác, Agent có thể hold chat bằng cách nhấn<br>vào icon hold|
|11.2.49|Kết thúc chat||- Giao dịch chat với khách hàng kết thúc bằng 1 trong các cách sau:<br>- Agent kết thúc chat<br>- Agent click vào icon x để thực hiện kết thúc chat è Hệ thống hiển thị confirm|
|11.2.50|Cảnh báo KPI phiên chat đầu<br>tiên||Cảnh báo KPI phiên chat đầu tiên|
|11.2.51|Cảnh báo KPI phiên chat tiếp<br>theo||Cảnh báo KPI phiên chat tiếp theo|
|11.2.52|Cảnh báo KPI số lần hold chat||Cảnh báo KPI số lần hold chat|
|11.2.53|Cảnh báo KPI thờigian hold chat||Cảnh báo KPI thờigian hold chat|
|**12**|**HappyCall**|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||**12.1**|**Cấu hình tham số HT**||**Thêm sửa xóa các**<br>**tham số chung của**<br>**hệ thống**|Thêm sửa xóa các tham số chung của hệ thống||
||**12.2**|**Quản lý khách hàng**|||||
|12.2.1||Quản lý danh sách khách hàng||- Xem thông tin chi<br>tiết khách hàng:<br>- Thêm sửa xóa danh<br>sách khách hàng<br>- Tìm kiếm theo tên<br>danh sách, mã danh<br>sách.<br>- Xem thông tin chi<br>tiết gồm:<br>+ Họ tên<br>+ Số điện thoại<br>+ Địa chỉ<br>+ Loại khiếu nại<br>- Sửa:<br>+ Cập nhật theo file,<br>+ Xóa bản ghi trong<br>danh sách|- Xem thông tin chi tiết khách hàng:<br>- Thêm sửa xóa danh sách khách hàng<br>- Tìm kiếm theo tên danh sách, mã danh sách.<br>- Xem thông tin chi tiết gồm:<br>+ Họ tên<br>+ Số điện thoại<br>+ Địa chỉ<br>+ Loại khiếu nại<br>- Sửa:<br>+ Cập nhật theo file,<br>+ Xóa bản ghi trong danh sách||
|12.2.2||Bổ sung tính năng tìm kiếm||Tìm kiếm theo:<br>- Ngày tạo<br>- Người tạo<br>- Ngày cập nhật<br>- Người cập nhật<br>- Đã được gán vào<br>chiến dịch|- Nâng cấp tính năng<br>- Bổ sung tiêu chí||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.2.3||Quản khách hàng(menu con)||- Thêm sửa xóa<br>nhóm khách hàng<br>- Tìm kiếm theo:<br>+ Tên<br>+ Giới tính<br>+ Số ĐT<br>+ Trạng thái chiến<br>dịch<br>+ CMND<br>- Xem thông tin danh<br>sách khách hàng<br>- Mở khóa/ khóa<br>khách hàng|- Thêm sửa xóa nhóm khách hàng<br>- Tìm kiếm theo:<br>+ Tên<br>+ Giới tính<br>+ Số ĐT<br>+ Trạng thái chiến dịch<br>+ CMND<br>- Xem thông tin danh sách khách hàng<br>- Mở khóa/ khóa khách hàng||
|12.2.4||Xuất danh sách||Xuất danh sách KH<br>trong Menu Quản lý<br>khách hàng\ Quản lý<br>danh sách khách<br>hàng\ trong cột hành<br>động, khi chọn “Xem<br>thông tin chi tiết<br>khách hàng”|Tham khảo mã IBM<br>- Bổ sung chính sách an toàn của TĐ (các trường dữ liệu quy định thì có xuất mã hóa)<br>- Bổ sung phân quyền xuất nhìn full dữ liệu hoặc xuất thấy dữ liệu ẩn<br>Bổ sung xuất pdf, excel||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.2.5|Cấu hình file excel import|- Thêm sửa xóa cấu<br>hình file excel<br>- Cho phép người sử<br>dụng thực hiện cấu<br>hình file excel import<br>như mong muốn:<br>+ Thuộc tính nào của<br>khách hàng sẽ xuất<br>hiện trên file<br>+ Vị trí thuộc tính<br>+ Thuộc tính nào bắt<br>buộc<br>- Tìm kiếm theo:<br>+ Mã cấu hình<br>+ Loại chiến dịch<br>+ Ngày tạo<br>+ Tên cấu hình.<br>- Xem, tải, cập nhật<br>file biểu mẫu trong<br>kết quả tìm kiếm|<br>- Thêm sửa xóa cấu hình file excel<br>- Cho phép người sử dụng thực hiện cấu hình file excel import  như mong muốn:<br>+ Thuộc tính nào của khách hàng sẽ xuất hiện trên file<br>+ Vị trí thuộc tính<br>+ Thuộc tính nào bắt buộc<br>- Tìm kiếm theo:<br>+ Mã cấu hình<br>+ Loại chiến dịch<br>+ Ngày tạo<br>+ Tên cấu hình.<br>- Xem, tải, cập nhật file biểu mẫu trong kết quả tìm kiếm|
|12.2.6|Cấu hình thuộc tính  khách hàng|- Cho phép người sử<br>dụng thực hiện cấu<br>hình động các thuộc<br>tính của khách hàng.<br>- Thêm mới, cập<br>nhật, tìm kiếm, xóa<br>thuộc tính, active<br>thuộc tính khách<br>hàng<br>- Cập nhật thuộc tính<br>trong kết quả tìm<br>kiếm|- Cho phép người sử dụng thực hiện cấu hình động các thuộc tính của khách hàng.<br>- Thêm mới, cập nhật, tìm kiếm, xóa thuộc tính, active thuộc tính khách hàng<br>- Cập nhật thuộc tính trong kết quả tìm kiếm|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.2.7||Danh sách khách hàng không<br>liên lạc||- Cho phép người sử<br>dụng thực hiện nhập<br>các danh sách khách<br>hàng không liên lạc<br>lên hệ thống. Những<br>khách hàng thuộc<br>danh sách không liên<br>lạc sẽ được bỏ qua<br>khi thực hiện chiến<br>dịch<br>- Thêm mới, cập<br>nhật, tìm kiếm, xóa<br>danh sách, xóa khách<br>hàng khỏi danh sách<br>- Tìm kiếm theo:<br>+ Mã danh sách<br>+ Loại chiến dịch<br>+ Loại danh sách<br>+ Tên danh sách.<br>- Tải file biểu mẫu,<br>cập nhật trong kết<br>quả tìm kiếm|- Bổ xung danh sách KH Vị thế, sẽ không thực hiện gọi ra HappyCall<br>Khi trong chiến dịch gọi ra có thuê bao nằm trong danh sách này thực hiện POPup cảnh báo<br>cho ĐTV biết đang gọi cho KH vị thế<br>- Đồng bộ tự động danh sách KH Vị thế về IPCC<br>Các chiến dịch Campain khác trên IPCC cũng check ds KH Vị thế trước khi thực hiện (không<br>thực hiện các "chiến dịch" gửi mail, sms với KH Vị thế)||
|12.2.8||ĐTV bổ sung KH vào danh sách<br>blacklist||- Nếu trong Khi đàm<br>thoại, KH yêu cầu<br>TVV dừng mọi liên<br>hệ trong tương lai,<br>TVV có thể chọn ô<br>Blacklist trong kết<br>quả tương tác của<br>chiến dịch đó để đưa<br>KH vào danh sách<br>Blacklist.|- Bổ sung chức năng mới<br>- Đưa vào backlist đối tượng khách hàng đang tương tác||
|12.2.9||Xuất excel||- Xuất DS KH<br>blacklist|- Bổ sung chức năng mới<br>- Bổ sungxuất dữ liệu nhạycảm||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.2.10||Bổ sung tính năng tìm kiếm||- Tìm theo số ĐT<br>khách hàng|- Bổ sung tiêu chí tìm kiếm: để tìm kiếm được các KH đang nằm trong danh sách Backlist||
|**12.3**||**Quản lý chiến dịch**|||||
|12.3.1||Quản lý nhóm Agents||- Thêm sửa xóa<br>nhóm agent<br>- Cho phép tìm kiếm<br>theo:<br>+ Mã danh sách<br>+ Loại chiến dịch<br>+ Loại danh sách<br>+ Tên danh sách.<br>- Trong kết quả tìm<br>kiếm cho phép:<br>+ Cập nhật danh sách<br>+ Gán trưởng nhóm<br>cho danh sách<br>+ Tải danh sách TVV<br>+ Gán IP Phone cho<br>user|- Thêm sửa xóa nhóm agent<br>- Cho phép tìm kiếm theo:<br>+ Mã danh sách<br>+ Loại chiến dịch<br>+ Loại danh sách<br>+ Tên danh sách.<br>- Trong kết quả tìm kiếm cho phép:<br>+ Cập nhật danh sách<br>+ Gán trưởng nhóm cho danh sách<br>+ Tải danh sách TVV<br>+ Gán IP Phone cho user||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.3.2||Quản lý thông tin chiến dịch||- Tím kiếm theo:<br>+ Mã chiến dịch<br>+ Thời gian bắt đầu<br>+ Thời gian kết thúc<br>+ Tên chiến dịch<br>+ Loại chiến dịch<br>+ Kiểu gọi ra<br>+ Xuất báo cáo chiến<br>dịch tìm kiếm<br>- Thêm mới chiến<br>dịch:<br>+ Chọn HT gọi ra<br>+ Kịch bản chiến<br>dịch<br>+ Gán danh sách KH<br>+ Danh sách TVV<br>Trong kết quả tìm<br>kiếm cho phép<br>chuyển chiến dịch tự<br>động sang thủ công<br>và ngược lại, xem<br>thông tin chiến dịch,<br>xóa chiến dịch,<br>chuyển chiến dịch<br>sang trạng thái chuẩn<br>bị, giahạnchiếndịch|- Tím kiếm theo:<br>+ Mã chiến dịch<br>+ Thời gian bắt đầu<br>+ Thời gian kết thúc<br>+ Tên chiến dịch<br>+ Loại chiến dịch<br>+ Kiểu gọi ra<br>+ Xuất báo cáo chiến dịch tìm kiếm<br>- Thêm mới chiến dịch:<br>+ Chọn HT gọi ra<br>+ Kịch bản chiến dịch<br>+ Gán danh sách KH<br>+ Danh sách TVV<br>Trong kết quả tìm kiếm cho phép chuyển chiến dịch tự động sang thủ công và ngược lại, xem<br>thông tin chiến dịch, xóa chiến dịch, chuyển chiến dịch sang trạng thái chuẩn bị, gia hạn<br>chiến dịch||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.3|Thêm mới chiến dịch|- Bổ sung Thoại/<br>Thoại và Video Call/<br>Video Call<br>- Thời gian nhập kết<br>quả tương tác:<br>+ Kết nối: là thời<br>gian nhập kết quả<br>cho các cuộc gọi kết<br>nối thành công được<br>tới KH, hết thời gian<br>nhập kết quả tương<br>tác mà TVV không<br>nhập hệ thống sẽ<br>đóng màn hình nhập<br>kết quả tương tác<br>đồng thời lưu một<br>bản ghi nháp để TVV<br>có thể chỉnh sửa kết<br>quả tương tác<br>+ Không kết nối: là<br>thời gian nhập kết<br>quả cho các cuộc gọi<br>kết nối không thành<br>công được tới KH,<br>hết thời gian nhập<br>kết quả tương tác mà<br>TVV không nhập hệ<br>thống sẽ đóng màn<br>hình nhập kết quả<br>tương tác đồng thời<br>lưu một bản ghi nháp<br>để TVV có thể chỉnh<br>sửa kết quả tương tác<br>-Chế độ thựchiện:|- Áp dụng cho chiến dịch Telesale<br>- Hiển thị các thông  từ BCCS CC<br>Bổ sung tích hợp với các API cung cấp thông tin BCCS<br>- Cung cấp các API tạo các chiến dịch HPC<br>- Bổ sung Thoại/ Thoại và Video Call/ Video Call<br>- Thời gian nhập kết quả tương tác:<br>+ Kết nối: là thời gian nhập kết quả cho các cuộc gọi kết nối thành công được tới KH, hết thời<br>gian nhập kết quả tương tác mà TVV không nhập hệ thống sẽ đóng màn hình nhập kết quả<br>tương tác đồng thời lưu một bản ghi nháp để TVV có thể chỉnh sửa kết quả tương tác<br>+ Không kết nối: là thời gian nhập kết quả cho các cuộc gọi kết nối không thành công được<br>tới KH, hết thời gian nhập kết quả tương tác mà TVV không nhập hệ thống sẽ đóng màn hình<br>nhập kết quả tương tác đồng thời lưu một bản ghi nháp để TVV có thể chỉnh sửa kết quả<br>tương tác<br>- Chế độ thực hiện: Theo múi giờ trong ngày hay khoảng thời gian<br>- Chọn chế độ thực hiện cho chiến dịch:<br>+ Manual<br>+ Preview<br>+ Progressive<br>+ Predictive"|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||Theo múi giờ trong<br>ngày hay khoảng thời<br>gian<br>- Chọn chế độ thực<br>hiện cho chiến dịch:<br>+ Manual<br>+ Preview<br>+ Progressive<br>+ Predictive||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.4|Thêm mới chiến dịch|Bổ sung thêm trường<br>cấu hình “Số lượng<br>khảo sát thành công<br>tối đa”: được tính<br>theo số lượng dữ liệu<br>KH kết nối thành<br>công. Với những<br>chiến dịch có yêu cầu<br>đặc thù thì khi tạo<br>chiến dịch tích chọn<br>vào trường này và<br>nhập số lượng dữ<br>liệu KH yêu cầu.<br>Khi đếm đủ số lượng<br>tối đa theo chiến dịch<br>-> Chiến dịch tạm<br>dừng (không cho<br>nhận dữ liệu thêm) -<br>> Hệ thống thông<br>báo: “Dữ liệu khảo<br>sát đã đạt tốiđa”.|- Áp dụng cho chiến dịch HPC<br>- Bổ sung thêm trường cấu hình “Số lượng khảo sát thành công tối đa”: được tính theo số<br>lượng dữ liệu KH kết nối thành công. Với những chiến dịch có yêu cầu đặc thù thì khi tạo<br>chiến dịch tích chọn vào trường này và nhập số lượng dữ liệu KH yêu cầu.  Khi đếm đủ số<br>lượng tối đa theo chiến dịch -> Chiến dịch tạm dừng (không cho nhận dữ liệu thêm) -> Hệ<br>thống thông báo: “Dữ liệu khảo sát đã đạt tối đa”.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.5|Cấu hình hiển thị thông tin khi<br>thêm mới chiến dịch|Cho lựa chọn cấu<br>hình thông tin hiển<br>thị: thông tin trên<br>BCCS, thông tin từ<br>hệ thống khác có<br>giao tiếp với HPC để<br>phục vụ chiến dịch<br>đặc thù.<br>- Cho lựa chọn cấu<br>hình hiển thị lịch sử<br>tương tác của KH lên<br>các kênh CSKH như:<br>thoại, Video call.<br>chat.<br>- Người tạo chiến<br>dịch cần được phân<br>quyền mới được cấu<br>hình hiển thị các<br>thông tin này<br>Phân quyền cho phép<br>tạo chiến dịch happy<br>call, chỉ những người<br>của đơn vị nào mới<br>được cấu hình các<br>trường dữ liệu của<br>đơn vị đó liên quan<br>đến việc hiển thị<br>thông tin khigọi ra|Cho lựa chọn cấu hình thông tin hiển thị: thông tin trên BCCS, thông tin từ hệ thống khác có<br>giao tiếp với HPC để phục vụ chiến dịch đặc thù.<br>- Cho lựa chọn cấu hình hiển thị lịch sử tương tác của KH lên các kênh CSKH như: thoại,<br>Video call. chat.<br>- Người tạo chiến dịch cần được phân quyền mới được cấu hình hiển thị các thông tin này<br>Phân quyền cho phép tạo chiến dịch happy call, chỉ những người của đơn vị nào mới được<br>cấu hình các trường dữ liệu của đơn vị đó liên quan đến việc hiển thị thông tin khi gọi ra|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.6|Chiến dịch HPC Sự cố lặp(tự<br>động)|- Lấy dữ liệu PA từ<br>BCCS của ngày được<br>chọn<br>- Lấy dữ liệu PA từ<br>BCCS của 30 ngày<br>trước ngày được<br>chọn.<br>- Thực hiện đếm<br>trùng theo số thuê<br>bao của ngày được<br>chọn so với danh<br>sách số thuê bao gặp<br>sự cố trong 30 ngày<br>trước đó. Lấy toàn bộ<br>số thuê bao lặp lại từ<br>3 lần trở lên đẩy vào<br>chiến dịch HPC sự<br>cố lặp.<br>- Đẩy dữ liệu lặp từ 3<br>lần trở lên vào chiến<br>dịch HPC sự cố lặp<br>- Tự động đồng bộ<br>kết quả HPC trên<br>phần mềm HPC về<br>BCCS, khi ĐTV cập<br>nhật kết quả khảo sát<br>trên tool HPC thì kết<br>quả cũng được cập<br>nhật và đóng trên<br>BCCS.<br>- Xuất báo cáo DL đã<br>đẩy tự động trên 2<br>chiến dịch.<br>- Xuất được báo cáo|- Lấy dữ liệu PA từ BCCS của ngày được chọn<br>- Lấy dữ liệu PA từ BCCS của 30 ngày trước ngày được chọn.<br>- Thực hiện đếm trùng theo số thuê bao của ngày được chọn so với danh sách số thuê bao gặp<br>sự cố trong 30 ngày trước đó. Lấy toàn bộ số thuê bao lặp lại từ 3 lần trở lên đẩy vào chiến<br>dịch HPC sự cố lặp.<br>- Đẩy dữ liệu lặp từ 3 lần trở lên vào chiến dịch HPC sự cố lặp<br>- Tự động đồng bộ kết quả HPC trên phần mềm HPC về BCCS, khi ĐTV cập nhật kết quả<br>khảo sát trên tool HPC thì kết quả cũng được cập nhật và đóng trên BCCS.<br>- Xuất báo cáo DL đã đẩy tự động trên 2 chiến dịch.<br>- Xuất được báo cáo tiến độ HPC.<br>- Báo cáo Campaign: Đảm bảo hệ thống cho phép xuất được kết quả đầy đủ thông tin các<br>trường như dữ liệu đồng bộ sang|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||tiến độ HPC.<br>- Báo cáo Campaign:<br>Đảm bảo hệ thống<br>cho phép xuất được<br>kết quả đầy đủ thông<br>tin các trường như dữ<br>liệu đồng bộ sang|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.7|Chiến dịch HPC đóng PA DV Cố<br>định BOT không xử lý|- Lấy dữ liệu PA từ<br>BCCS<br>- Lọc trùng theo<br>trường số thuê bao<br>với những DL đã đẩy<br>vào chiến dịch HPC<br>sự cố lặp. - Loại bỏ<br>những DL bị trùng<br>với chiến dịch HPC<br>sự cố lặp<br>- Đẩy dữ liệu vào<br>chiến dịch HPC đóng<br>PA DV Cố định.<br>- Tự động đồng bộ<br>kết quả HPC trên<br>phần mềm HPC về<br>BCCS, khi ĐTV cập<br>nhật kết quả khảo sát<br>trên tool HPC thì kết<br>quả cũng được cập<br>nhật và đóng trên<br>BCCS.<br>- Xuất báo cáo DL đã<br>đẩy tự động trên 2<br>chiến dịch.<br>- Xuất được báo cáo<br>tiến độ HPC.<br>- Báo cáo Campaign:<br>Đảm bảo hệ thống<br>cho phép xuất được<br>kết quả đầy đủ thông<br>tin các trường như dữ<br>liệu đồng bộ sang|- Lấy dữ liệu PA từ BCCS<br>- Lọc trùng theo trường số thuê bao với những DL đã đẩy vào chiến dịch HPC sự cố lặp. -<br>Loại bỏ những DL bị trùng với chiến dịch HPC sự cố lặp<br>- Đẩy dữ liệu vào chiến dịch HPC đóng PA DV Cố định.<br>- Tự động đồng bộ kết quả HPC trên phần mềm HPC về BCCS, khi ĐTV cập nhật kết quả<br>khảo sát trên tool HPC thì kết quả cũng được cập nhật và đóng trên BCCS.<br>- Xuất báo cáo DL đã đẩy tự động trên 2 chiến dịch.<br>- Xuất được báo cáo tiến độ HPC.<br>- Báo cáo Campaign: Đảm bảo hệ thống cho phép xuất được kết quả đầy đủ thông tin các<br>trường như dữ liệu đồng bộ sang.<br>- Tham khảo PYC mã 4075452 trên hệ thống quản lý sản xuất|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.3.8||Chiến dịch Manual||- Agent nhận KH, hệ<br>thống phân phối về<br>KH A => (2) Agent<br>xem thông tin KH và<br>bấm gọi => (3)<br>Agent kết thúc cuộc<br>gọi với KH A =><br>Agent thao tác nhận<br>KH tiếp theo (B) và<br>lặp lại các bước 2-3.<br>- Agent xem được<br>thông tin KH trước<br>khi gọi.<br>- Agent có thể bỏ qua<br>một KH và xử lý tiếp<br>KH khác.<br>- Với dạng chiến<br>dịch này, người quản<br>lý muốn Agent chủ<br>động nhận KH từ list<br>KH sẵn có, xem<br>thông tin và chủ<br>động thao tác gọi<br>khách khisẵnsàng.|- AG có thể xem được thông tin KH<br>Chủ động nhận KH từ list khách hàng có sẵn<br>- Chuyển sang menu<br>- Nội dung chi tiết tham khảo PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.9|Chiến dịch Predictive|- Hệ thống tự động<br>gọi ra nhiều số điện<br>thoại KH, chỉ khi KH<br>nghe máy, cuộc gọi<br>mới được đổ tới<br>agent.<br>+ (1) Hệ thống gọi<br>cho KH A trước khi<br>kết nối với Agent =><br>(2) Khách hàng A<br>nghe máy, hệ thống<br>gọi đến agent. Trong<br>lúc chưa được kết nối<br>đến agent, khách<br>hàng nghe nhạc chờ<br>=> (3) Agent nghe<br>máy, lúc này KH và<br>Agent được kết nối<br>với nhau. Nếu Agent<br>không nghe máy,<br>cuộc gọi đổ sang<br>Agent khác sau 10s<br>(KH chờ lâu sẽ tắt<br>máy).<br>+ Lưu ý: hệ thống<br>tính toán số cuộc gọi<br>cần thực hiện tại một<br>thời điểm để tối ưu<br>trong phạm vi tỷ lệ<br>nhỡ cho phép, có thể<br>KH đã nghe máy rồi<br>nhưng chưa có agent<br>rảnh để đổ cuộc gọi.<br>+ Agentkhôngxem|- Hệ thống tự động gọi ra nhiều số điện thoại KH, chỉ khi KH nghe máy, cuộc gọi mới được<br>đổ tới agent.<br>+ (1) Hệ thống gọi cho KH A trước khi kết nối với Agent => (2) Khách hàng A nghe máy, hệ<br>thống gọi đến agent. Trong lúc chưa được kết nối đến agent, khách hàng nghe nhạc chờ =><br>(3) Agent nghe máy, lúc này KH và Agent được kết nối với nhau. Nếu Agent không nghe<br>máy, cuộc gọi đổ sang Agent khác sau 10s (KH chờ lâu sẽ tắt máy).<br>+ Lưu ý: hệ thống tính toán số cuộc gọi cần thực hiện tại một thời điểm để tối ưu trong phạm<br>vi tỷ lệ nhỡ cho phép, có thể KH đã nghe máy rồi nhưng chưa có agent rảnh để đổ cuộc gọi.<br>+ Agent không xem được thông tin KH trước khi gọi.<br>+ Agent không được phép bỏ qua một KH và xử lý tiếp KH khác (Agent chỉ có thể từ chối<br>cuộc gọi đến từ hệ thống).<br>+ Với dạng chiến dịch này, người quản lý muốn tối đa nhất công suất gọi điện của Agent,<br>chấp nhận trường hợp có thể KH nghe máy nhưng không gặp được Agent (chưa có Agent<br>rảnh tiếp nhận cuộc gọi, hoặc KH tắt máy trước khi gặp Agent)<br>- Nội dung chi tiết tham khảo PYC có mã IBM 4075458 trên hệ thống quản lý sản xuất|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||được thông tin KH<br>trước khi gọi.<br>+ Agent không được<br>phép bỏ qua một KH<br>và xử lý tiếp KH<br>khác (Agent chỉ có<br>thể từ chối cuộc gọi<br>đến từ hệ thống).<br>+ Với dạng chiến<br>dịch này, người quản<br>lý muốn tối đa nhất<br>công suất gọi điện<br>của Agent, chấp nhận<br>trường hợp có thể<br>KH nghe máy nhưng<br>không gặp được<br>Agent (chưa có<br>Agent rảnh tiếp nhận<br>cuộc gọi, hoặc KH<br>tắt máy trước khi gặp<br>Agent)||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.10|Chiến dịch Preview|- Chiến dịch đổ KH<br>về cho agent, cho<br>agent 1 khoảng thời<br>gian để xem trước<br>thông tin KH trước<br>khi quay số.<br>+ (1) Hệ thống hiển<br>thị thông tin KH A<br>=> (2) Agent có 1<br>khoảng thời gian<br>nhất định để xem<br>thông tin KH => (3)<br>Hết thời gian trên, hệ<br>thống gọi cho Agent<br>=> (4) Khi Agent<br>nghe máy, hệ thống<br>gọi đến KH để kết<br>nối 2 bên => (5) Sau<br>khi cuộc gọi kết thúc,<br>hệ thống hiển thị<br>thông tin KH tiếp<br>theo và lặp lại các<br>bước (2) đến (5).<br>+ Agent xem được<br>thông tin KH trước<br>khi gọi.<br>+ Agent có thể bỏ<br>qua một KH và xử lý<br>tiếp KH khác (Agent<br>hẹn gọi lại, sau đó hệ<br>thống hiển thị KH<br>tiếp theo).<br>+ Với dạng chiến<br>dịch này,ngườiquản|- Chiến dịch đổ KH về cho agent, cho agent 1 khoảng thời gian để xem trước thông tin KH<br>trước khi quay số.<br>+ (1) Hệ thống hiển thị thông tin KH A => (2) Agent có 1 khoảng thời gian nhất định để xem<br>thông tin KH => (3) Hết thời gian trên, hệ thống gọi cho Agent => (4) Khi Agent nghe máy,<br>hệ thống gọi đến KH để kết nối 2 bên => (5) Sau khi cuộc gọi kết thúc, hệ thống hiển thị<br>thông tin KH tiếp theo và lặp lại các bước (2) đến (5).<br>+ Agent xem được thông tin KH trước khi gọi.<br>+ Agent có thể bỏ qua một KH và xử lý tiếp KH khác (Agent hẹn gọi lại, sau đó hệ thống<br>hiển thị KH tiếp theo).<br>+ Với dạng chiến dịch này, người quản lý muốn agent có thời gian nhất định để xem thông tin<br>KH trước khi đàm thoại|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||lý muốn agent có<br>thời gian nhất định<br>để xem thông tin KH<br>trước khi đàm thoại|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.11|Chiến dịch Progressive|Khi agent sẵn sàng<br>nhận cuộc gọi, chiến<br>dịch liên tục đổ cuộc<br>gọi cho agent:<br>- (1) Hệ thống gọi<br>cho Agent trước khi<br>kết nối với KH A =><br>(2) Khi agent nghe<br>máy, hệ thống gọi<br>đến KH A để kết nối<br>hai bên => (3) Agent<br>kết thúc cuộc gọi với<br>KH A => (4) Hệ<br>thống gọi cho Agent<br>trước khi kết nối với<br>KH tiếp theo (B) và<br>lặp lại các bước (2)<br>đến (4).<br>- Agent không xem<br>được thông tin KH<br>trước khi gọi.<br>- Agent không được<br>phép bỏ qua một KH<br>và xử lý tiếp KH<br>khác (Agent chỉ có<br>thể từ chối cuộc gọi<br>đến từ hệ thống).<br>- Với dạng chiến<br>dịch này, người quản<br>lý muốn Agent thực<br>hiện liên tục các cuộc<br>gọi, không có thời<br>gian xem thông tin<br>KHtrước cuộc gọi|Khi agent sẵn sàng nhận cuộc gọi, chiến dịch liên tục đổ cuộc gọi cho agent:<br>- (1) Hệ thống gọi cho Agent trước khi kết nối với KH A => (2) Khi agent nghe máy, hệ<br>thống gọi đến KH A để kết nối hai bên => (3) Agent kết thúc cuộc gọi với KH A => (4) Hệ<br>thống gọi cho Agent trước khi kết nối với KH tiếp theo (B) và lặp lại các bước (2) đến (4).<br>- Agent không xem được thông tin KH trước khi gọi.<br>- Agent không được phép bỏ qua một KH và xử lý tiếp KH khác (Agent chỉ có thể từ chối<br>cuộc gọi đến từ hệ thống).<br>- Với dạng chiến dịch này, người quản lý muốn Agent thực hiện liên tục các cuộc gọi, không<br>có thời gian xem thông tin KH trước cuộc gọi.<br>- Nội dung chi tiết tham khảo PYC mã 4075458 trên hệ thống quản lý sản xuất|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.12|Tìm kiếm chiến dịch|- Khi TVV chọn<br>chiến dịch để triển<br>khai, hệ thống sẽ<br>phân bổ các khách<br>hàng cho tư vấn viên<br>trong tập các khách<br>hàng được gán với<br>chiến dịch theo quy<br>tắc sau:<br>+ Khách hàng hẹn<br>gọi lại của TVV đang<br>trong khoảng thời<br>gian hẹn gọi lại.<br>+ Khách hàng hẹn<br>gọi lại của TVV khác<br>đang trong khoảng<br>thời gian hẹn gọi lại<br>nhưng TVV đó<br>không đăng nhập<br>hoặc không thực hiện<br>chiến dịch.<br>+ Khách hàng chưa<br>được gọi.Khách hàng<br>từng được liên lạc<br>nhưng có kết quả kết<br>nối là “Không liên<br>lạc được” hoặc<br>“Không kết nối do hạ<br>tầng viễn thông”<br>hoặc 1 giá trị trạng<br>thái kết nối động<br>được cấu  hình cho<br>phép gọi lại cho KH,<br>chưa đạt sốlầngọi ra|- Khi TVV chọn chiến dịch để triển khai, hệ thống sẽ phân bổ các khách hàng cho tư vấn viên<br>trong tập các khách hàng được gán với chiến dịch theo quy tắc sau:<br>+ Khách hàng hẹn gọi lại của TVV đang trong khoảng thời gian hẹn gọi lại.<br>+ Khách hàng hẹn gọi lại của TVV khác đang trong khoảng thời gian hẹn gọi lại nhưng TVV<br>đó không đăng nhập hoặc không thực hiện chiến dịch.<br>+ Khách hàng chưa được gọi.Khách hàng từng được liên lạc nhưng có kết quả kết nối là<br>“Không liên lạc được” hoặc “Không kết nối do hạ tầng viễn thông” hoặc 1 giá trị trạng thái<br>kết nối động được cấu  hình cho phép gọi lại cho KH, chưa đạt số lần gọi ra tối đa và khoảng<br>cách từ thời điểm cuộc gọi gần nhất đến thời điểm phân bổ >= tham số khoảng cách giữa 2<br>lần liên lạc.<br>- Chi tiết tham khảo PYC mã IBM 4075468|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||tối đa và khoảng<br>cách từ thời điểm<br>cuộc gọi gần nhất<br>đến thời điểm phân<br>bổ >= tham số<br>khoảng cách giữa 2<br>lần liên lạc.||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.3.13|Quản lý đơn vị|- Tìm kiếm theo:<br>+ Mã đơn vị<br>+ Tên đơn vị<br>+ Đơn vị cha<br>+ Trạng thái đơn vị<br>+ Mã tư vấn viên<br>+ Thêm, sửa, xóa<br>đơn vị.<br>- Gán danh sách tư<br>vấn viên vào mã cây<br>đơn vị tương ứng|- Tìm kiếm theo:<br>+ Mã đơn vị<br>+ Tên đơn vị<br>+ Đơn vị cha<br>+ Trạng thái đơn vị<br>+ Mã tư vấn viên<br>+ Thêm, sửa, xóa đơn vị.<br>- Gán danh sách tư vấn viên vào mã cây đơn vị tương ứng|
|12.3.14|Quản lýkhách hàngbáo đỏ||Đề xuất bỏ|
|12.3.15|Chiến dịch tạo tự động Cảnh báo<br>Roaming, BADO||Đề xuất bỏ|
|12.3.16|Chiến dịch tự động HappyCall<br>MNP||- Áp dụng cho cả chiến dịch tự động thủ công<br>- IPCC 4.0 cung cấp API<br>- Các đơn vị tích hợp các API để truyền sang cho IPCC tạo thông tin dữ liệu cho chiến dịch.|
|12.3.17|Cảnh báo giám sát|Không hoạt động|- Đảm bảo chức năng tương tự như chức năng trên hệ thống cũ<br>- Kiểm tra tính năng tại sao chưa hoạt động|
|12.3.18|Đánh giá chiến dịch|Không hoạt động|- Đảm bảo chức năng tương tự như chức năng trên hệ thống cũ<br>- Kiểm tra tính năng tại sao chưa hoạt động|
|**12.4**|**Thực hiện chiến dịch**|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.4.1|Nhập kết quả tương tác|- Thực hiện gọi ra<br>cho khách hàng theo<br>chiến dịch.<br>- Tím kiếm theo: Mã<br>chiến dịch,  thời gian<br>bắt đầu, thời gian kết<br>thúc, tên chiến dịch,<br>loại chiến dịch<br>- Chuyển trạng thái<br>chiến dịch từ chuẩn<br>bị sang triển khai<br>- Tư vấn viên nhận<br>KH thực hiện chiến<br>dịch theo kịch bản<br>-Nhập kết quả.|Đảm bảo chức năng tương tự như chức năng trên hệ thống cũ|
|12.4.2|Sửa đổi, thêm mới kết quả|- Bổ sung tính năng<br>sửa đổi/ thêm mới<br>kết quả trong “Trạng<br>thái liên lạc với<br>Khách hàng” và áp<br>dụng cho tất cả các<br>loại chiến dịch HPC|đã upcode ==> đề xuất bỏ yêu cầu này|
|12.4.3|Cảnh báo KH hẹn gọi lại, nhắn<br>tin KH|- Đối với những<br>khách hàng là khách<br>hàng hẹn gọi lại thì<br>phần kết quả tương<br>tác với KH sẽ hiển<br>thị thêm thông báo<br>“Chú ý đây là khách<br>hàng hẹn gọi lại”.<br>- Trường hợp KH<br>không nghe máy/ KH<br>báo bận, TVV có thể<br>nhấn nút gửi tin nhắn|- Bổ sung cảnh báo KH hẹn gọi lại<br>- Bổ sung 1 tin nhắn mẫu để nhắn gọi lại cho KH<br>- Cho phép tùy chỉnh template nội dung tin nhắn<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản<br>xuất|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||đến KH theo tin nhắn<br>đã được cấu hình<br>trước để xin lịch hẹn<br>gọi lại cho KH|||
|12.4.4||Yêu cầu nhập thông tin||Trên bảng hỏi HPC<br>phần câu hỏi mặc<br>định “Quest 2” và<br>mục “ Ghi chú” dùng<br>để lấy<br>thông tin về GBOC<br>chỉ cho phép người<br>dùng thực hiện đóng<br>kết quả khi 02 nội<br>dung này<br>được cập nhật thông<br>tinđầy đủ.|Đã upcode ==> đề xuất bỏ yêu cầu này||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.4.5|Nhận diện KH gọi thành công<br>chuyển trạng thái sang DNC|- Hệ thống kiểm tra<br>số lần khách hàng<br>được gọi ra thành<br>công ứng với loại<br>chiến dịch mà khách<br>hàng vừa được gọi<br>ra, tính từ đầu tháng<br>tính đến thời điểm<br>hiện tại. Sau đó sẽ so<br>sánh với số lần kết<br>nối KH thành<br>công/tháng của loại<br>chiến dịch đó (được<br>cấu hình trong mục<br>Cấu hình số lần tham<br>gia chiến dịch của<br>khách hàng). Nếu số<br>kết quả tương tác có<br>trạng thái kết nối là<br>thành công của KH<br>đó theo loại chiến<br>dịch >= Số lần kết<br>nối KH thành công<br>/tháng thì KH đó<br>được cập nhật thành<br>KH DNC.<br>- Khi KH là DNC thì<br>sẽ không được phân<br>bổ gọi ra nếu tồn tại<br>trong các chiến dịch<br>khác.<br>- Đến ngày đầu tiên<br>của tháng mới, tất cả<br>cáckhách hànglà|- Hệ thống kiểm tra số lần khách hàng được gọi ra thành công ứng với loại chiến dịch mà<br>khách hàng vừa được gọi ra, tính từ đầu tháng tính đến thời điểm hiện tại. Sau đó sẽ so sánh<br>với số lần kết nối KH thành công/tháng của loại chiến dịch đó (được cấu hình trong mục Cấu<br>hình số lần tham gia chiến dịch của khách hàng). Nếu số kết quả tương tác có trạng thái kết<br>nối là thành công của KH đó theo loại chiến dịch >= Số lần kết nối KH thành công /tháng thì<br>KH đó được cập nhật thành KH DNC.<br>- Khi KH là DNC thì sẽ không được phân bổ gọi ra nếu tồn tại trong các chiến dịch khác.<br>- Đến ngày đầu tiên của tháng mới, tất cả các khách hàng là DNC của tháng cũ sẽ được cập<br>nhật thành khách hàng bình thường, không còn là khách hàng DNC.<br>- Chỉ liên quan đến cuộc gọi Telesale<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản<br>xuất|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||DNC của tháng cũ sẽ<br>được cập nhật thành<br>khách hàng bình<br>thường, không còn là<br>khách hàng DNC.|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.4.6|Hiển thị talktime|- Hiển thị thông tin<br>talktime (tổng thời<br>gian đàm thoại với<br>KH) lũy kế trong<br>ngày để ĐTV nhìn<br>thấy khi đang thực<br>hiện chiến dịch. Mục<br>đích để ĐTV đảm<br>bảo đủ thời lượng gọi<br>bắt buộc/ngày theo<br>quy định.|- Hiển thị thông tin talktime (tổng thời gian đàm thoại với KH) lũy kế trong ngày để ĐTV<br>nhìn thấy khi đang thực hiện chiến dịch. Mục đích để ĐTV đảm bảo đủ thời lượng gọi bắt<br>buộc/ngày theo quy định.<br>Thời gian đàm thoại của ĐTV chỉ liên quan đến cuộc gọi Telesale tham gia trong ngày<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản<br>xuất|
|12.4.7|Sửa kết quả tương tác|Chức năng cho 3<br>nhóm người dùng sử<br>dụng:<br>+ Trưởng nhóm: Cho<br>phép sửa kết quả<br>tương tác của tất cả<br>các Agent mình là<br>trưởng nhóm. Thời<br>gian sửa trong vòng<br>24h tính từ thời điểm<br>lưu bản ghi.<br>+ Giám sát viên: Cho<br>phép sửa kết quả<br>tương tác của tất cả<br>các agent. Thời gian<br>sửa không giới hạn.<br>+ Tư vấn viên: Cho<br>phép sửa kết quả<br>tương tác của mình.<br>Thời gian sửa trong<br>vòng 12h tính từ thời<br>điểm lưu bảnghi.|Xây dựng chức năng trên hệ thống mới tương tự chức năng trên hệ thống cũ<br>Chức năng cho 3 nhóm người dùng sử dụng:<br>+ Trưởng nhóm: Cho phép sửa kết quả tương tác của tất cả các Agent mình là trưởng nhóm.<br>Thời gian sửa trong vòng 24h tính từ thời điểm lưu bản ghi.<br>+ Giám sát viên: Cho phép sửa kết quả tương tác của tất cả các agent. Thời gian sửa không<br>giới hạn.<br>+ Tư vấn viên: Cho phép sửa kết quả tương tác của mình. Thời gian sửa trong vòng 12h tính<br>từ thời điểm lưu bản ghi.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.4.8|Ưu tiên thực hiện gọi|- Ưu tiên gọi trước<br>cho các khách hàng<br>cho từng tư vấn viên<br>- Tím kiếm theo:<br>+ Mã chiến dịch<br>+ Mã TVV<br>+ Tên chiến dịch<br>+ Lloại chiến dịch<br>+ CMND<br>+ Số ĐT<br>+ Thứ tự ưu tiên|Xây dựng chức năng trên hệ thống mới tương tự chức năng trên hệ thống cũ<br>- Ưu tiên gọi trước cho các khách hàng cho từng tư vấn viên<br>- Tím kiếm theo:<br>+ Mã chiến dịch<br>+ Mã TVV<br>+ Tên chiến dịch<br>+ Loại chiến dịch<br>+ CMND<br>+ Số ĐT<br>+ Thứ tự ưu tiên|
|12.4.9|Quản lý kịch bản|- Người dùng nhập<br>thông tin Tìm kiếm,<br>hệ thống hiển thị<br>thông tin kết quả Tìm<br>kiếm gồm:<br>+ STT.<br>+ Mã kịch bản<br>+ Tên kịch bản<br>+ Ngày tạo<br>+ Người tạo<br>+ Ngày cập nhật<br>+ Người cập nhật<br>+ Đã được gán vào<br>chiến dịch<br>+ Hành động<br>- Người dùng có thể<br>lựa chọn kịch bản<br>cần xem/chỉnh sửa để<br>thực hiện: xem chi<br>tiết,xóa kịch bản,|- Người dùng nhập thông tin Tìm kiếm, hệ thống hiển thị thông tin kết quả Tìm kiếm gồm:<br>+ STT.<br>+ Mã kịch bản<br>+ Tên kịch bản<br>+ Ngày tạo<br>+ Người tạo<br>+ Ngày cập nhật<br>+ Người cập nhật<br>+ Đã được gán vào chiến dịch<br>+ Hành động<br>- Người dùng có thể lựa chọn kịch bản cần xem/chỉnh sửa để thực hiện: xem chi tiết, xóa kịch<br>bản, chỉnh sửa nội dung kịch bản, sắp xếp thứ tự kịch bản<br>- Cho phép import kịch bản theo file<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản<br>xuất|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||chỉnh sửa nội dung<br>kịch bản.<br>- Cho phép import<br>kịch bản theo file|||
|12.4.10||Quản lý tin nhắn gửi đến KH||Cho phép người<br>dùng quản lý và gửi<br>tin nhắn đến khách<br>hàng:<br>- Hệ thống cho phép<br>thêm mới, tìm kiếm,<br>chỉnh sửa, xóa tin<br>nhắn.<br>- Cấu hình tin nhắn<br>vào từng chiến dịch<br>để TVV có thể bấm<br>gửi tin trong trường<br>hợp KH không nghe<br>máy/KHbáo bận.|Cho phép người dùng quản lý và gửi tin nhắn đến khách hàng:<br>- Hệ thống cho phép thêm mới, tìm kiếm, chỉnh sửa, xóa tin nhắn.<br>- Cấu hình tin nhắn vào từng chiến dịch để TVV có thể bấm gửi tin trong trường hợp KH<br>không nghe máy/KH báo bận.<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản<br>xuất||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.4.11|Quản lý cuộc gọi vào của KH|- ĐTV thực hiện<br>chiến dịch telesales<br>tới KH, KH bị lỡ<br>cuộc gọi & sau đó<br>KH thực hiện gọi lại<br>tổng đài hệ thống tự<br>động hiển thị cuộc<br>gọi đến cho chính<br>Agent đã thực hiện<br>gọi ra trước đó cho<br>KH:<br>+ Nếu Agent này<br>không online thì<br>cuộc gọi được<br>chuyển đến Agent<br>khác đang rảnh rỗi.<br>+ Nếu Agent này<br>đang bận hoặc không<br>có Agent nào nhận<br>cuộc gọi cho đến Khi<br>hết chuông chờ thì<br>KH Ađược xếp vào<br>hàng gọi nhỡ, được<br>hiển thị cho tất cả<br>các Agent, đến Khi<br>có Agent gọi lại cho<br>KH và nhập kết quả<br>đã xử lý thì KH A<br>được đẩy sang hàng<br>đã xử lý.|Đề xuất bỏ (từ chị PhuongCT) ==> đề xuất bỏ|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.4.12||Chuyển sang chiến dịch khác||Tính năng tự động<br>cho phép người quản<br>lý cấu hình nếu<br>Agent đạt năng suất<br>trên chiến dịch này<br>thì được phép tự<br>động chuyển sang<br>chiến dịch khác để<br>không phải thêm thủ<br>công|- Tính năng tự động cho phép cấu hình nếu Agent đạt năng suất trên chiến dịch này thì được<br>phép tự động chuyển sang chiến dịch khác để không phải thêm thủ công.<br>- KPI bán hàng thành công trên ngày của chiến dịch<br>- Đạt KPI mới được chuyển<br>- KPI cấu hình trên chiến dịch<br>- Tùy chiến dịch cho phép chuyển và không cho phép chuyển<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản<br>xuất||
|12.4.13||Phân quyền VSA||- Phân hệ VSA của<br>HappyCall các nhóm<br>chức năng hiện tại<br>gán cứng với role<br>nên khi lấy các chức<br>năng con xây nhóm<br>chức năng riêng cho<br>từng đơn vị thì<br>không hoạt động dẫn<br>đến tất cả các đơn vị<br>đều đang dùng chung<br>nhóm chức năng của<br>TTCSKH và quản trị<br>user đơn vị không<br>thể cấp quyền cho<br>người dùng đơn vị<br>mình.<br>- Nâng cấp để có thể<br>cấp quyền riêng cho<br>từng đơn vị.|- Phân hệ VSA của HappyCall các nhóm chức năng hiện tại gán cứng với role nên khi lấy các<br>chức năng con xây nhóm chức năng riêng cho từng đơn vị thì không hoạt động dẫn đến tất cả<br>các đơn vị đều đang dùng chung nhóm chức năng của TTCSKH và quản trị user đơn vị không<br>thể cấp quyền cho người dùng đơn vị mình.<br>- Nâng cấp để có thể cấp quyền riêng cho từng đơn vị.<br>- Quyền áp dụng đến mức nút chức năng<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 2743689 trên hệ thống quản lý sản<br>xuất||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||- Quyền áp dụng đến<br>mức nút chức năng|||
|12.4.14||Chuyển GBOC||Khách hàng MNP<br>không kịp níu kéo thì<br>tick chuyển hàng loạt<br>sang GBOC để kịp<br>thời gian gìn giữ|Đã upcode ==> đề xuất bỏ yêu cầu này||
|12.4.15||Chuyển GBOC||Tự động hóa luồng<br>giao kết quả HPC<br>sang GBOC để giao<br>kênh đi tiếp xúc giữ<br>gìn|Đã upcode ==> đề xuất bỏ yêu cầu này||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.4.16|Tích hợp tính năng video call<br>trên màn hình gọi ra của TVV|- Khi ĐTV nhận KH,<br>màn hình giao diện<br>hiển thị 2 tab<br>“MyViettel” và “Gọi<br>video call”:<br>+ Đối với tab<br>“MyViettel”:<br>Nếu TB của KH có<br>cài app MyViettel<br>Tab “MyViettel” sẽ<br>hiển thị màu đậm.<br>Nếu KH không cài<br>app MyViettel thì tab<br>“MyViettel” sẽ hiển<br>thị mờ.<br>+ Đối với tab “Gọi<br>video call”:<br>Nếu App MyViettel<br>của KH đang để<br>online Tab “Gọi<br>video call” hiển thị<br>màu đậm ĐTV click<br>vào tab “Gọi video<br>call” để thực hiện<br>cuộc gọi videocall tới<br>KH.<br>Nếu App MyViettel<br>của KH đang để<br>offline Tab “Gọi<br>video call” hiển thị<br>mờ.|- Bổ sung tính năng video call trên màn hình nhận KH của TVV<br>- Khi ĐTV nhận KH, màn hình giao diện hiển thị 2 tab “MyViettel” và “Gọi video call”:<br>+ Đối với tab “MyViettel”:<br>Nếu TB của KH có cài app MyViettel  Tab “MyViettel” sẽ hiển thị màu đậm.<br>Nếu KH không cài app MyViettel thì tab “MyViettel” sẽ hiển thị mờ.<br>+ Đối với tab “Gọi video call”:<br>Nếu App MyViettel của KH đang để online Tab “Gọi video call” hiển thị màu đậm ĐTV<br>click vào tab “Gọi video call” để thực hiện cuộc gọi videocall tới KH.<br>Nếu App MyViettel của KH đang để offline Tab “Gọi video call” hiển thị mờ.<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản<br>xuất|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.4.17|Tích hợp hệ thống BCCS, CC và<br>hệ thống Order vào hệ thống<br>Happycall .|- Khi ĐTV nhận KH,<br>màn hình giao diện<br>bổ sung thêm 1 tab<br>“Hệ thống CC”, khi<br>click vào tab này sẽ<br>mở ra trang<br>BCCS_Chăm sóc<br>khách hàng:<br>+ Khi click vào Tab<br>“Hệ thống CC” mở<br>ra thông tin TB của<br>KH trên trang BCCS<br>+ Khi ĐTV nhận<br>KH, màn hình giao<br>diện bổ sung thêm 1<br>tab “Hệ thống Hỗ trợ<br>tư vấn”.Khi click vào<br>tab này sẽ mở ra<br>trang BCCS_Hỗ trợ<br>tư vấn (ĐTV không<br>phải thao tác đăng<br>nhập số thuê bao của<br>KH và mã capcha mà<br>màn hình sẽ hiển thị<br>luôn thông tin của<br>thuê bao trên<br>BCCS_Hỗ trợ tư<br>vấn)<br>- Cho phép hiển thị<br>thông tin toàn bộ các<br>gói cước KH đang<br>dùng và tài khoản<br>của KH trên hệ thống<br>HPC.|Theo mã IBM<br>- Bổ sung link trên hệ thống HappyCall , CC, Orders khi ĐTV nhận KH<br>- ĐTV nhấn vào link vào BCCS, CC, Orders<br>- Khi ĐTV nhận KH, màn hình giao diện bổ sung thêm 1 tab “Hệ thống CC”, khi click vào<br>tab này sẽ mở ra trang BCCS_Chăm sóc khách hàng:<br>+ Khi click vào Tab “Hệ thống CC” mở ra thông tin TB của KH trên trang BCCS<br>+ Khi ĐTV nhận KH, màn hình giao diện bổ sung thêm 1 tab “Hệ thống Hỗ trợ tư vấn”.Khi<br>click vào tab này sẽ mở ra trang BCCS_Hỗ trợ tư vấn (ĐTV không phải thao tác đăng nhập<br>số thuê bao của KH và mã capcha mà màn hình sẽ hiển thị luôn thông tin của thuê bao trên<br>BCCS_Hỗ trợ tư vấn)<br>- Cho phép hiển thị thông tin toàn bộ các gói cước KH đang dùng và tài khoản của KH trên<br>hệ thống HPC.<br>- Link BCCS, CC, Orders để cấu hình cho phép thay đổi thuận<br>- Nội dung chi tiết tham khảo nội dung PYC có mã IBM 4075458 trên hệ thống quản lý sản<br>xuất|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.4.18||Cập nhật danh sách khách hàng<br>Pri hàng tháng|||- Bổ sung đồng bộ khách hàng VIP từ Viettel++<br>- Đồng bộ hàng ngày đảm bảo dữ liệu mới nhất đến thời điểm đồng bộ<br>- Khi gọi ra trên IPCC thì hiển thị khách hàng VIP theo phân loại và lấy dữ liệu trực tiếp trên<br>IPCC<br>- Ưu tiên lấy dữ liệu VIP theo thủ công||
|12.4.19||Tối ưu KH đẩy về chiến dịch<br>MNP||Lọc KH tiêu dùng<br>trung bình 3 tháng <<br>10k và sử dụng chưa<br>đủ 6 tháng thì HPC<br>sẽ lọc không đẩy vào<br>chiến dịch MNP các<br>KH có mã mã lý do<br>bị từ chối là DNO16.|PYC này đã upcode ==> Đề xuất bỏ||
|**12.5**||**Báo cáo Campaign **|||||
|12.5.1||Bổ sung các trường thông tin||Bổ sung các trường<br>thông tin khi xuất dữ<br>liệu báo cáo kết quả<br>HPC trên “Báo cáo<br>BI tập trung (CĐGS,<br>HPC, Workforce) đối<br>với chiến dịch HPC<br>MNP|PYC này đã upcode ==> Đề xuất bỏ||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.5.2|Báo cáo tổng hợp chiến dịch|Tìm kiếm theo:<br>- Mã chiến dịch<br>- Từ ngày đến ngày<br>- Đầu số gọi<br>- Xuất excel|- Bổ sung báo cáo tổng hợp chiến dịch:<br>- Nhập các tiêu chí tìm kiếm:<br>+ Mã chiến dịch: chọn mã chiến dịch từ danh sách chiến dịch đang có trên hệ thống<br>+ Từ ngày, đến ngày: tìm kiếm theo thời gian tạo bản ghi kết quả tương tác.<br>+ Đầu số gọi<br>- Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin:<br>Tên chiến dịch<br>Mã chiến dịch<br>Thời gian thực hiện<br>Thời gian kết thúc<br>Trạng thái chiến dịch<br>Số lượng KH của chiến dịch<br>Số lượng KH đã gọi<br>Số lượng KH chưa gọi<br>Số lượng TVV của chiến dịch<br>Số lượng TVV đã tham gia<br>Số lượng TVV không tham gia<br>Kết quả kết nối<br>+ KH đồng ý nghe máy<br>+ KH hẹn gọi lại<br>+ KH yêu cầu không gọi<br>+ KH không liên lạc được<br>+ KH báo bận<br>+ Sai số ĐT<br>Kết quả bán hàng<br>+ KH đồng ý mua<br>+ KH không đồng ý mua<br>+ KH xem xét<br>+ KH tự đăng ký<br>- Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ<br>thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.5.3|Báo cáo chi tiết theo chiến dịch|- Tìm kiếm theo: Mã<br>chiến dịch, Từ ngày,<br>đến ngày, đầu số gọi<br>- Dữ liệu tìm kiếm<br>hiển thị trên màn<br>hình và được xuất<br>excel với các thông<br>tin:<br>+ Tên chiến dịch<br>+ Mã chiến dịch<br>+ Thời gian thực<br>hiện<br>+ Thời gian kết thúc<br>+ Trạng thái chiến<br>dịch<br>+ Số lượng KH của<br>chiến dịch<br>+ Số lượng KH đã<br>gọi<br>+ Số lượng KH chưa<br>gọi<br>+ Số lượng TVV của<br>chiến dịch<br>+ Số lượng TVV đã<br>tham gia<br>+ Số lượng TVV<br>không tham gia<br>- Kết quả kết nối:<br>+ KH đồng ý nghe<br>máy<br>+ KH hẹn gọi lại<br>+ KH yêu cầu không<br>gọi<br>+ KH khôngliên lạc|- Bổ sung Báo cáo hiệu suất Agent<br>- Tìm kiếm theo:<br>+ Mã chiến dịch<br>+ Từ ngày đến ngày<br>+ Đầu số gọi<br>- Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin:<br>+ STT<br>+ Số điện thoại đã gọi<br>+ Số lần liên lạc<br>+ Thời gian gọi<br>+ Agent<br>+ Kết quả kết nối (Agent nhập kịch bản)<br>+ Kết quả bán hàng (Agen nhập kịch bản)<br>+ Ghi chú (Agent nhập nội dung)<br>- Bổ sung phân quyền báo cáo<br>- Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ<br>thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||được<br>+ KH báo bận<br>+ Sai số ĐT<br>Kết quả bán hàng<br>+ KH đồng ý mua<br>+ KH không đồng ý<br>mua<br>+ KH xem xét<br>+ KH tự đăng ký||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.5.4||Báo cáo hiệu quả theo chiến dịch||- Tìm kiếm theo:<br>+ Mã chiến dịch<br>+ Từ ngày đến ngày<br>+ Đầu số gọi<br>- Dữ liệu tìm kiếm<br>hiển thị trên màn<br>hình và được xuất<br>excel với các thông<br>tin:<br>+ STT<br>+ Số điện thoại đã<br>gọi<br>+ Số lần liên lạc<br>+ Thời gian gọi<br>+ Agent<br>+ Kết quả kết nối<br>(Agent nhập kịch<br>bản)<br>+ Kết quả bán hàng<br>(Agen nhập kịch<br>bản)<br>+ Ghi chú (Agent<br>nhập nội dung)|- Bổ sung Báo cáo hiệu suất Agent<br>- Tìm kiếm theo:<br>+ Mã chiến dịch<br>+ Từ ngày đến ngày<br>+ Đầu số gọi<br>- Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin:<br>+ STT<br>+ Số điện thoại đã gọi<br>+ Số lần liên lạc<br>+ Thời gian gọi<br>+ Agent<br>+ Kết quả kết nối (Agent nhập kịch bản)<br>+ Kết quả bán hàng (Agen nhập kịch bản)<br>+ Ghi chú (Agent nhập nội dung)<br>- Bổ sung phân quyền báo cáo<br>- Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ<br>thống quản lý sản xuất.||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.5.5||Báo cáo hiệu suất Agent||- Tìm kiếm theo:<br>+ Mã chiến dịch<br>+ Từ ngày đến ngày<br>+ Đầu số gọi<br>- Dữ liệu tìm kiếm<br>hiển thị trên màn<br>hình và được xuất<br>excel với các thông<br>tin:<br>+ STT<br>+ Agent<br>+ Tổng số cuộc gọi<br>nhỡ<br>+ Thời gian chờ TB<br>(giây)<br>+ Thời gian chờ tối<br>đa (giây)<br>+ Thời gian đàm<br>thoại TB của Agent<br>(giây)<br>+ Thời gian đàm<br>thoại tối đa của<br>Agent (giây)<br>+ Tổng thời gian<br>đàm thoại của<br>Agent(phút)<br>+ Số cuộc kết thúc<br>do Agent|- Bổ sung Báo cáo hiệu suất Agent<br>- Tìm kiếm theo:<br>+ Mã chiến dịch<br>+ Từ ngày đến ngày<br>+ Đầu số gọi<br>- Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin:<br>+ STT<br>+ Agent<br>+ Tổng số cuộc gọi nhỡ<br>+ Thời gian chờ TB (giây)<br>+ Thời gian chờ tối đa (giây)<br>+ Thời gian đàm thoại TB của Agent (giây)<br>+ Thời gian đàm thoại tối đa của Agent (giây)<br>+ Tổng thời gian đàm thoại của Agent(phút)<br>+ Số cuộc kết thúc do Agent<br>- Bổ sung phân quyền báo cáo<br>- Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ<br>thống quản lý sản xuất.||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|12.5.6|Báo cáo tổng hợp KQ HPC|- Nhóm trường dữ<br>liệu cố định:<br>+ Trạng thái kết nối<br>+ Nhân viên HPC<br>+ Thời gian HPC<br>+ Ghi chú<br>+ Kết quả Khảo sát<br>các câu hỏi<br>- Nhóm các trường<br>dữ liệu còn lại: Lấy<br>theo dữ liệu đầu vào<br>=> Theo cấu hình file<br>import dữ liệu KH<br>˗ Dữ liệu xuất ra cần<br>đủ các trường câu hỏi<br>trong cả trường hợp<br>dữ liệu KH không có<br>đáp án tương ứng.|- Bổ sung Báo cáo hiệu suất Agent<br>- Tìm kiếm theo: Mã chiến dịch, Từ ngày, đến ngày, đầu số gọi<br>- Dữ liệu tìm kiếm hiển thị trên màn hình và được xuất excel với các thông tin:<br>+ Tên chiến dịch<br>+ Mã chiến dịch<br>+ Thời gian thực hiện<br>+ Thời gian kết thúc<br>+ Trạng thái chiến dịch<br>+ Số lượng KH của chiến dịch<br>+ Số lượng KH đã gọi<br>+ Số lượng KH chưa gọi<br>+ Số lượng TVV của chiến dịch<br>+ Số lượng TVV đã tham gia<br>+ Số lượng TVV không tham gia<br>- Kết quả kết nối:<br>+ KH đồng ý nghe máy<br>+ KH hẹn gọi lại<br>+ KH yêu cầu không gọi<br>+ KH không liên lạc được<br>+ KH báo bận<br>+ Sai số ĐT<br>Kết quả bán hàng<br>+ KH đồng ý mua<br>+ KH không đồng ý mua<br>+ KH xem xét<br>+ KH tự đăng ký<br>- Bổ sung phân quyền báo cáo<br>- Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075458 trên hệ<br>thống quản lý sản xuất.|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|12.5.7||Báo cáo chi tiết KQ HPC||- Nhóm trường dữ<br>liệu cố định:<br>+ Trạng thái kết nối<br>+ Nhân viên HPC<br>+ Thời gian HPC<br>+ Ghi chú<br>+ Kết quả Khảo sát<br>các câu hỏi<br>- Nhóm các trường<br>dữ liệu còn lại: Lấy<br>theo dữ liệu đầu vào<br>=> Theo cấu hình file<br>import dữ liệu KH<br>˗ Dữ liệu xuất ra cần<br>đủ các trường câu hỏi<br>trong cả trường hợp<br>dữ liệu KH không có<br>đáp án tương ứng.|- Bổ sung báo cáo chi tiết kết quả HPC với các thông tin như sau:<br>˗ Kết quả báo cáo xuất 2 có 2 nhóm trường:<br>+ Nhóm trường dữ liệu cố định: (1) Trạng thái kết nối (2) Nhân viên HPC (3) thời gian HPC<br>(4) Ghi chú (5) Kết quả Khảo sát các Q hỏi<br>+ Nhóm các trường dữ liệu còn lại: Lấy theo dữ liệu đầu vào => Theo cấu hình file import dữ<br>liệu KH<br>˗ Dữ liệu xuất ra cần đủ các trường câu hỏi trong cả trường hợp dữ liệu KH không có đáp án<br>tương ứng.<br>- Cho phép xuất excel báo cáo<br>- Bổ sung phân quyền báo cáo cho các nhóm người dùng khác nhau<br>- Nội dung chi tiết và mẫu báo cáo tham khảo nội dung PYC với mã IBM là 4075452 trên hệ<br>thống quản lý sản xuất.||
|**13**||**Chấm điểm cuộc gọi **|||||
|**I**||**HT Chấm điểmgiám sát**|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.1|Mô tả chung HT Chấm điểm<br>giám sát|**- Cho phép chấm**<br>**cho các đơn vị trong**<br>**và ngoài Viettel**<br>**- Với nhân sự chủ**<br>**dịch vụ thì được**<br>**phép tìm kiếm các**<br>**tương tác chỉ của**<br>**đơn vị đó**<br>**- Với nhân sự giám**<br>**sát là người được**<br>**thuê vận hành quản**<br>**lý (outsource ) thì**<br>**được phép tìm kiếm**<br>**tương tác các dịch**<br>**vụ của các đơn vị**<br>**khác nhau theo đơn**<br>**vị được gán**<br>**- Cho phép người**<br>**dùng truy cập hệ**<br>**thống từ ngoài**<br>**internet nếu được**<br>**phân quyền**<br>**- Cho phép cung**<br>**cấp API cho hệ**<br>**thống đánh giá KI,**<br>**chấm công của**<br>**TTCSKH**|Nâng cấp tính năng chấm cuộc gọi test nghiệp vụ và đánh giá cuộc gọi của học viên trước khi<br>lên line, chấm điểm kênh Trực tuyến (chat đa kênh, mạng xã hội), kênh video call và kênh<br>Mail<br>- Hiện tại PMCĐ đang có 03 bất cập ảnh hưởng đến công tác chấm điểm của Giám sát. Cụ<br>thể:<br>+Tính năng gán dữ liệu cuộc gọi cần chấm: Để gán được cuộc gọi theo chủ đề/chủ điểm GSV<br>cần thực hiện thủ công qua 3 bước (1) Xuất dữ liệu nhập thống kê nhu cầu của KH trên<br>BCCS; (2) Lọc danh sách cuộc gọi cần chấm của NVCSKH theo chủ đề/chủ điểm; (3) Gán<br>dữ liệu cuộc gọi cần chấm theo chủ đề/chủ điểm  lên phần mềm chấm điểm (PMCĐ) và  chờ<br>cuộc gọi được đẩy về. Với thời gian đẩy cuộc gọi lâu thường > 3h<br>+ Bất cập: mất nhiều thao tác, chậm, không tìm thấy cuộc gọi<br>+ Theo dõi dữ liệu cuộc gọi đã gán/đã chấm/NVCSKH: toàn bộ dữ liệu cuộc gọi đã gán hoặc<br>đã chấm /NVCSKH  đều phải theo dõi thủ công bằng cách (1) Xuất dữ liệu chi tiết toàn bộ<br>cuộc gọi GSV đã chấm; (2) Đếm cuộc gọi đã gán/đã chấm của từng NVCSKH để theo dõi<br>+ Bất cật: GSV mất thời gian trong khâu đối soát , dễ xảy ra tình trạng sót/trùng dữ liệu chấm<br>+ Phân quyền chấm cuộc gọi: Hiện việc chấm điểm  NVCSKH được chia cho 02 đối tượng<br>GS đánh giá là GS đối tác (GSOS) và GSVT. Tuy nhiên, PMCĐ chỉ hỗ trợ tại một thời điểm<br>chỉ 01 GSV được chấm và   mỗi lần thay đổi GS chấm cần thực hiện thao tác cập nhật lại<br>danh sách GS chấm xong mới có thể chấm điểm được<br>Bất cập:  GSV mất thời gian trong khâu cập nhật danh sách chấm và chờ đợi để chốt đủ cuộc<br>gọi cần chấm/NVCSKH<br>Đề xuất :<br>1.Tính năng gán dữ liệu cuộc gọi cần chấm<br>Xây dựng tính năng lọc cuộc gọi theo chủ đề/chủ điểm trên PMCĐ cho phép GSV lọc theo<br>từ khóa, không cần phải cập nhật file dữ liệu cuộc gọi  cần đẩy như hiện tại (cần có số TB và<br>thời gian KH gọi tổng đài )<br>2.Tính năng theo dõi dữ liệu cuộc gọi đã gán/đã chấm/NVCSKH<br>Xây dựng tính năng xuất dữ liệu báo cáo số lượng CG đã gán/đã chấm theo từng  NVCSKH<br>theo: (1) Tổng cuộc gọi đã gán/đã chấm, (2) số lượng CG đã gán/đã chấm theo chủ đề/chủ<br>điểm.<br>3.Tính năng phân quyền chấm cuộc gọi<br>Xây dựng tính năng cho phép 2 GSV cùng có thể chấm điểm NVCSKH tại một thời điểm<br>gồm: GSOS và GSVT."<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.2|Quản lý Danh sách nhóm chấm|-Upload thông tin<br>NV CSKH cần đánh<br>giá trong tháng, bao<br>gồm:<br>+ Họ tên<br>+ Mã NV CSKH<br>+ Nhóm<br>+ Kênh (line)<br>+ Đối tác (công ty)<br>+ Thâm niên<br>+ User<br>+ Trưởng nhóm<br>+ Giám sát quản lý<br>+ Kiểm định<br>+ Số lượng cuộc gọi<br>cần chấm<br>+ Số điện thoại NV<br>CSKH<br>+ Số điện thoại<br>Trưởng nhóm/Giám<br>sát quản lý<br>+ Ghi chú<br>- Upload dữ liệu lên<br>hệ thống dưới dạng<br>file Excel và có thể<br>lấy dữ liệu từ cơ sở<br>dữ liệu Phần mềm<br>Quản lý nhân sự thê<br>ngoài của TT CSKH.<br>- Tìm kiếm theo các<br>đktrên|- Cho phép quản lý danh sách nhóm chấm: thêm mới, sửa, xóa, import thông tin<br>- Các thông tin tham khảo chức năng quản lý danh sahcs nhóm chấm trên hệ thống cũ<br>- Bổ sung cho phép gán nhóm chấm cho từ 1 đến 2 giám sát<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||13.3|Chức năng lọc cuộc gọi/ lọc<br>mail/ lọc hội thoại chat||-Lọc cuộc gọi theo<br>các điều kiện:<br>+ Độ ngắn dài cuộc<br>gọi<br>+ Theo danh sách<br>NV CSKH<br>+ Theo giám sát quản<br>lý<br>+ Theo đối tác<br>+ Theo khoảng thời<br>gian cài đặt<br>+ Theo kênh<br>+ Theo số thuê bao<br>+ Theo user của KH<br>(áp dụng kênh Trực<br>tuyến: Mạng xã hội,<br>chat đa kênh)<br>+ Mã cuộc gọi /ghi<br>âm/ hình ảnh (áp<br>dụng kênh Video<br>call)<br>+ Địa chỉ email của<br>KH, tiêu đề email (áp<br>dụng với kênh Mail)|- Bổ sung lọc theo mail, lọc theo hội thoại<br>- Mỗi kênh có điều kiện lọc khác nhau<br>- Bổ sung các điều kiện lọc:<br>-Lọc cuộc gọi theo các điều kiện:<br>+ Độ ngắn dài cuộc gọi<br>+ Theo danh sách NV CSKH<br>+ Theo giám sát quản lý<br>+ Theo đối tác<br>+ Theo khoảng thời gian cài đặt<br>+ Theo kênh<br>+ Theo số thuê bao<br>+ Theo user của KH (áp dụng kênh Trực tuyến: Mạng xã hội, chat đa kênh)<br>+ Mã cuộc gọi /ghi âm/ hình ảnh (áp dụng kênh Video call)<br>+ Địa chỉ email của KH, tiêu đề email (áp dụng với kênh Mail)<br>- Các đối tượng cuộc gọi/ mail/ hội thoại được chấm điểm đảm bảo đầy đủ các tiêu chí trên<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||13.4|Chức năng lọc cuộc gọi/ lọc<br>mail/ lọc hội thoại chat||- Lọc cuộc gọi theo<br>mức cảm xúc cuộc<br>gọi gồm các mức<br>cảm xúc (Lấy theo<br>bộ từ khóa của<br>K.CNTT trên hệ<br>thống GSCG, dữ liệu<br>đích có thể thay đổi<br>theo thực tế):<br>+ Cuộc gọi bình<br>thường (OK).<br>+ Cuộc gọi cảnh báo<br>cao (NOK).<br>+ Cuộc gọi cảnh báo<br>trung bình/cần xem<br>xét (NOK).<br>- Lọc cuộc gọi theo<br>Nhu cầu phản ánh<br>khách hàng gồm 05<br>cấp nghiệp vụ (lấy<br>theo bộ từ khóa nhập<br>thống kê nhu cầu KH<br>gọi tổng đài trên web<br>GSCG củaK.CNTT)|- Bổ sung tích hợp với phân tích cảm xúc kênh mail, chat tương tự kênh voice nếu có các<br>công cụ phân tích cảm xúc trên mail và chat.<br>- Lọc cuộc gọi theo mức cảm xúc cuộc gọi gồm các mức cảm xúc (Lấy theo bộ từ khóa của<br>K.CNTT trên hệ thống GSCG, dữ liệu đích có thể thay đổi theo thực tế):<br>+ Cuộc gọi bình thường (OK).<br>+ Cuộc gọi cảnh báo cao (NOK).<br>+ Cuộc gọi cảnh báo trung bình/cần xem xét (NOK).<br>- Lọc cuộc gọi theo Nhu cầu phản ánh khách hàng gồm 05 cấp nghiệp vụ (lấy theo bộ từ khóa<br>nhập thống kê nhu cầu KH gọi tổng đài trên web GSCG của K.CNTT)<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.5|Chức năng lọc cuộc gọi/ lọc<br>mail/ lọc hội thoại chat|- Lọc cuộc gọi theo<br>Nhu cầu phản ánh<br>khách hàng gồm 05<br>cấp nghiệp vụ (lấy<br>theo bộ từ khóa nhập<br>thống kê nhu cầu KH<br>gọi tổng đài trên web<br>GSCG của K.CNTT)<br>+ Cấp 1: Phân loại<br>theo dịch vụ của<br>Viettel (Di động, D-<br>com, Homephone,<br>Internet, PSTN,<br>Truyền hình, SME).<br>+ Cấp 2: Phân loại<br>chi tiết theo nghiệp<br>vụ (DV GTGT,<br>CKTM, Sản<br>phầm…).<br>+ Cấp 3: Phân loại<br>chi tiết theo nhu cầu<br>của KH (cú pháp sử<br>dụng, cách sử dụng,<br>cước sử dụng…).<br>+ Cấp 4: Phân loại<br>chi tiết theo tên sản<br>phẩm/ dịch vụ/ chính<br>sách (Economy,<br>Imuzik, V120…).<br>+ Cấp 5: Phân loại<br>chi tiết theo hành vi<br>sử dụng dịch vụ và<br>nguyên nhân lỗi|- Bổ sung tiêu chí tìm kiếm theo nhu cầu khách hàng theo 5 cấp nhập thống kê của BCCS:<br>+ Cấp 1: Phân loại theo dịch vụ của Viettel (Di động, D-com, Homephone, Internet, PSTN,<br>Truyền hình, SME).<br>+ Cấp 2: Phân loại chi tiết theo nghiệp vụ (DV GTGT, CKTM, Sản phầm…).<br>+ Cấp 3: Phân loại chi tiết theo nhu cầu của KH (cú pháp sử dụng, cách sử dụng, cước sử<br>dụng…).<br>+ Cấp 4: Phân loại chi tiết theo tên sản phẩm/ dịch vụ/ chính sách (Economy, Imuzik,<br>V120…).<br>+ Cấp 5: Phân loại chi tiết theo hành vi sử dụng dịch vụ và nguyên nhân lỗi<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.6|Chức năng chấm điểm|- Ràng buộc theo<br>chức năng Quản lý<br>Danh sách nhóm<br>chấm: 1 Giám sát<br>quản lý 1 nhóm NV<br>CSKH do đó mỗi<br>Giám sát quản lý thì<br>xem và chấm được<br>các cuộc gọi của NV<br>CSKH trong nhóm<br>mà mình quản lý<br>- Cho phép người<br>dùng chấm điểm<br>online/offline, chấm<br>theo chủ đích dưới<br>hình thức đẩy excel<br>và import lên phần<br>mềm (lưu ý: đối với<br>chấm offline, sẽ thực<br>hiện chấm các cuộc<br>gọi đã lọc theo điều<br>kiện tại mục 2).<br>- Cho phép Giám sát<br>được phép sửa trong<br>vòng 24 giờ kể từ lúc<br>chấm lầnđầu|- Bổ sung cho phép có 2 giám sát quản lý giám sát ĐTV, cả 2 giám sát đều có quyền chấm<br>điểm cho ĐTV.<br>- Trên 1 cuộc gọi nếu một giám sát đã chấm điểm cho ĐTV viên rồi thì cán bộ giám sát kia sẽ<br>không được phép chấm (nếu chấm rồi thì phải cảnh báo) trên cuộc gọi.<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.7|Chức năng chấm điểm|- Tại giao diện màn<br>hình chấm cuộc gọi<br>hiển thị đồng thời<br>các thông tin kết quả<br>đánh giá cảm xúc<br>cuộc gọi và Nhu cầu<br>của KH gọi tổng đài<br>trên web GSCG của<br>K.CNTT, dựa vào đó<br>các Giám sát sẽ thực<br>hiện đánh giá thủ<br>công các cuộc gọi,<br>các thông tin hiển thị<br>bao gồm:<br>+ cảm xúc cuộc gọi:<br>mức độ cảnh báo<br>CG, cảm xúc cuộc<br>gọi KH/NV CSKH,<br>hiển thị biểu đồ cảm<br>xúc cuộc gọi theo<br>phân đoạn.<br>+ Nhu cầu phản ánh<br>khách hàng gồm 05<br>cấp nghiệp vụ:<br>o Cấp 1: Phân loại<br>theo dịch vụ của<br>Viettel (Di động, D-<br>com, Homephone,<br>Internet, PSTN,<br>Truyền hình, SME).<br>o Cấp 2: Phân loại<br>chi tiết theo nghiệp<br>vụ (DV GTGT,<br>CKTM, Sản|- Bổ sung kết quả đánh giá Emotion, kết quả cuộc gọi, chủ để cuộc gọi<br>- Tại giao diện màn hình chấm cuộc gọi hiển thị đồng thời các thông tin kết quả đánh giá cảm<br>xúc cuộc gọi và Nhu cầu của KH gọi tổng đài trên web GSCG của K.CNTT, dựa vào đó các<br>Giám sát sẽ thực hiện đánh giá thủ công các cuộc gọi, các thông tin hiển thị bao gồm:<br>+ cảm xúc cuộc gọi: mức độ cảnh báo CG, cảm xúc cuộc gọi KH/NV CSKH, hiển thị biểu đồ<br>cảm xúc cuộc gọi theo phân đoạn.<br>+ Nhu cầu phản ánh khách hàng gồm 05 cấp nghiệp vụ:<br>o Cấp 1: Phân loại theo dịch vụ của Viettel (Di động, D-com, Homephone, Internet, PSTN,<br>Truyền hình, SME).<br>o Cấp 2: Phân loại chi tiết theo nghiệp vụ (DV GTGT, CKTM, Sản phầm…).<br>o Cấp 3: Phân loại chi tiết theo nhu cầu của KH (cú pháp sử dụng, cách sử dụng, giá cước…).<br>o Cấp 4: Phân loại chi tiết theo tên sản phẩm/ dịch vụ/ chính sách (Economy, V120…).<br>o Cấp 5: Phân loại chi tiết theo hành vi sử dụng dịch vụ và nguyên nhân<br>lỗi.<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||phầm…).<br>o Cấp 3: Phân loại<br>chi tiết theo nhu cầu<br>của KH (cú pháp sử<br>dụng, cách sử dụng,<br>giá cước…).<br>o Cấp 4: Phân loại<br>chi tiết theo tên sản<br>phẩm/ dịch vụ/ chính<br>sách (Economy,<br>V120…).<br>o Cấp 5: Phân loại<br>chi tiết theo hành vi<br>sử dụng dịch vụ và<br>nguyên nhân<br>lỗi.||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.8|Chấm điểm Online (chức năng<br>thêm mới vào trong menu Chấm<br>điểm,, hiện menu này đã có chức<br>năng chấm điểm offline, nay bổ<br>xung thêm chấm online)|-cho phép người<br>chấm xem được danh<br>sách các cuộc gọi<br>đang tiếp nhận của<br>nhóm NV CSKH mà<br>mình quản lý. Giám<br>sát được tích chọn<br>bất kỳ cuộc gọi nào<br>cần đánh giá theo<br>thang điểm quy định.<br>- Có chức năng bỏ<br>cuộc gọi không đánh<br>giá và ghi chú được<br>lý do vì sao không<br>đánh giá theo một số<br>đầu mục quy định<br>(cuộc gọi không có<br>nội dung, cuộc gọi<br>test…các đầu mục<br>này sẽ do người dùng<br>tự động cập nhật lên<br>hệ thống).<br>- Yêu cầu:<br>+ Bắt đầu vào chấm -<br>> lưu đánh dấu cuộc<br>gọi ở trạng thái đang<br>chấm.<br>+  Kết thúc chấm và<br>lưu dữ liệu -> chuyển<br>sang trạng thái đã<br>chấm.<br>+ Đối với cuộc gọi<br>được chấm cùng lúc,<br>lấykết quảlưu trước,|- Bổ sung chấm cho kênh: chat, mail, video call.<br>- Cho phép người chấm xem được danh sách các cuộc gọi đang tiếp nhận của nhóm NV<br>CSKH mà mình quản lý. Giám sát được tích chọn bất kỳ cuộc gọi nào cần đánh giá theo<br>thang điểm quy định.<br>- Có chức năng bỏ cuộc gọi không đánh giá và ghi chú được lý do vì sao không đánh giá theo<br>một số đầu mục quy định (cuộc gọi không có nội dung, cuộc gọi test…các đầu mục này sẽ do<br>người dùng tự động cập nhật lên hệ thống).<br>- Yêu cầu:<br>+ Bắt đầu vào chấm -> lưu đánh dấu cuộc gọi ở trạng thái đang chấm.<br>+  Kết thúc chấm và lưu dữ liệu -> chuyển sang trạng thái đã chấm.<br>+ Đối với cuộc gọi được chấm cùng lúc, lấy kết quả lưu trước, người lưu sau sẽ nhận được<br>thông báo “Cuộc gọi này đã chấm”.<br>+ Phần phân loại nghiệp vụ: trường hợp xếp loại TB, Yếu bắt buộc chọn phân loại cấp 4,5.<br>+ Phần kỹ năng: bắt buộc chọn ít nhất một tiêu chí cha. Nếu chọn tiêu chí cha có tiêu chí con<br>thì bắt buộc chọn ít nhất một tiêu chí con.<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||người lưu sau sẽ<br>nhận được thông báo<br>“Cuộc gọi này đã<br>chấm”.<br>+ Phần phân loại<br>nghiệp vụ: trường<br>hợp xếp loại TB, Yếu<br>bắt buộc chọn phân<br>loại cấp 4,5.<br>+ Phần kỹ năng: bắt<br>buộc chọn ít nhất<br>một tiêu chí cha. Nếu<br>chọn tiêu chí cha có<br>tiêu chí con thì bắt<br>buộc chọn ít nhất<br>một tiêu chí con.||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.9|Chấm điểm Offline|- Căn cứ vào danh<br>sách nhóm chấm của<br>Giám sát, hệ thống sẽ<br>cho phép Giám sát<br>xem được danh sách<br>các cuộc gọi đã được<br>gửi ở bước lọc cuộc<br>gọi ngẫu nhiên và<br>Giám sát chọn lần<br>lượt các cuộc gọi cần<br>chấm:<br>+ Danh sách cuộc gọi<br>được sắp xếp cho NV<br>CSKH nào có tỷ lệ<br>cuộc gọi cần chấm<br>nhỏ hơn thì ưu  tiên<br>chấm trước<br>+ Đối với mỗi NV<br>CSKH , ưu tiên chấm<br>cuộc gọi tiếp nhận<br>gần nhất.<br>+ Ngoài ra, các cuộc<br>gọi được đẩy theo<br>file dưới dạng ưu tiên<br>(Cuộc gọi lọc theo<br>file) thì cần được đẩy<br>lên chấm trước sau<br>đó mới đến cuộc gọi<br>của NV CSKH có tỷ<br>lệ cuộc gọi cần chấm<br>nhỏ hơn.<br>- Yêu cầu:<br>+ Bắt đầu vào chấm -<br>> lưu đánhdấu cuộc|- Bổ sung chấm cho kênh: chat, mail, video call.<br>- Căn cứ vào danh sách nhóm chấm của Giám sát, hệ thống sẽ cho phép Giám sát xem được<br>danh sách các cuộc gọi đã được gửi ở bước lọc cuộc gọi ngẫu nhiên và Giám sát chọn lần lượt<br>các cuộc gọi cần chấm:<br>+ Danh sách cuộc gọi được sắp xếp cho NV CSKH nào có tỷ lệ cuộc gọi cần chấm nhỏ hơn<br>thì ưu  tiên chấm trước<br>+ Đối với mỗi NV CSKH , ưu tiên chấm cuộc gọi tiếp nhận gần nhất.<br>+ Ngoài ra, các cuộc gọi được đẩy theo file dưới dạng ưu tiên (Cuộc gọi lọc theo file) thì cần<br>được đẩy lên chấm trước sau đó mới đến cuộc gọi của NV CSKH có tỷ lệ cuộc gọi cần chấm<br>nhỏ hơn.<br>- Yêu cầu:<br>+ Bắt đầu vào chấm -> lưu đánh dấu cuộc gọi ở trạng thái đang chấm.<br>+  Kết thúc chấm và lưu dữ liệu -> chuyển sang trạng thái đã chấm.<br>+ Đối với cuộc gọi được chấm cùng lúc, lấy kết quả lưu trước, người lưu sau sẽ nhận được<br>thông báo “Cuộc gọi này đã chấm”.<br>+ Phần phân loại nghiệp vụ: trường hợp xếp loại TB, Yếu bắt buộc chọn phân loại cấp 4,5.<br>+ Phần kỹ năng: bắt buộc chọn ít nhất một tiêu chí cha. Nếu chọn tiêu chí cha có tiêu chí con<br>thì bắt buộc chọn ít nhất một tiêu chí con.<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||gọi ở trạng thái đang<br>chấm.<br>+  Kết thúc chấm và<br>lưu dữ liệu -> chuyển<br>sang trạng thái đã<br>chấm.<br>+ Đối với cuộc gọi<br>được chấm cùng lúc,<br>lấy kết quả lưu trước,<br>người lưu sau sẽ<br>nhận được thông báo<br>“Cuộc gọi này đã<br>chấm”.<br>+ Phần phân loại<br>nghiệp vụ: trường<br>hợp xếp loại TB, Yếu<br>bắt buộc chọn phân<br>loại cấp 4,5.<br>+ Phần kỹ năng: bắt<br>buộc chọn ít nhất<br>một tiêu chí cha. Nếu<br>chọn tiêu chí cha có<br>tiêu chí con thì bắt<br>buộc chọn ít nhất<br>một tiêu chí con.||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.10|Kiểm định lần 1|- Cho phép người<br>dùng được cấp quyền<br>kiểm định 1 có quyền<br>sửa toàn bộ phần<br>đánh giá của Giám<br>sát/ trưởng nhóm<br>chấm cuộc gọi đó sau<br>24h kề từ khi Giám<br>sát chấm lần đầu.<br>- Chức năng tra cứu<br>tính năng kiểm định<br>1: Cho phép người<br>dùng tìm kiếm cuộc<br>gọi cần kiểm định<br>theo thời gian, theo<br>Giám sát/ Trưởng<br>nhóm, theo NV<br>CSKH, số điện thoại<br>KH gọi tổng đài,<br>theo đối tác, theo<br>ngưỡng xếp loại của<br>cuộc gọi|- Bổ sung kiểm định cho kênh: chat, mail, video call.<br>- Cho phép người dùng được cấp quyền kiểm định 1 có quyền sửa toàn bộ phần đánh giá của<br>Giám sát/ trưởng nhóm chấm cuộc gọi đó sau 24h kề từ khi Giám sát chấm lần đầu.<br>- Chức năng tra cứu tính năng kiểm định 1: Cho phép người dùng tìm kiếm cuộc gọi cần kiểm<br>định theo thời gian, theo Giám sát/ Trưởng nhóm, theo NV CSKH, số điện thoại KH gọi tổng<br>đài, theo đối tác, theo ngưỡng xếp loại của cuộc gọi.<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.11|Kiểm định lần 2 (là chức năng<br>thêm vào trong menu Chấm<br>điểm)|- Cho phép người<br>dùng được cấp quyền<br>kiểm định 1 có quyền<br>sửa toàn bộ phần<br>đánh giá của kiểm<br>định 1 đồng thời sửa<br>được đánh giá  của<br>Giám sát/trưởng<br>nhóm chấm cuộc gọi<br>đó<br>- Tính năng tra cứu<br>chức năng kiểm định<br>2:<br>- Cho phép người<br>dùng tìm kiếm cuộc<br>gọi cần kiểm định<br>theo thời gian, theo<br>kết quả kiểm định 1,<br>theo Giám sát/<br>trưởng nhóm, theo<br>NV CSKH, số điện<br>thoại KH gọi tổng<br>đài, theo đối tác, theo<br>ngưỡng xếp loại của<br>cuộc gọi, theo lỗi<br>đánh giá của kiểm<br>định lần 1 với Giám<br>sát/trưởng nhóm.<br>- Cho phép tra cứu<br>cuộc gọi đã chấm/<br>chưa chấm/ cuộc gọi<br>lỗi theo đơn vị đối<br>tác, theo Giám sát/<br>trưởngnhóm, NV|- Bổ sung kiểm định cho kênh: chat, mail, video call.<br>- Cho phép người dùng được cấp quyền kiểm định 1 có quyền sửa toàn bộ phần đánh giá của<br>kiểm định 1 đồng thời sửa được đánh giá  của Giám sát/trưởng nhóm chấm cuộc gọi đó<br>- Tính năng tra cứu chức năng kiểm định 2:<br>- Cho phép người dùng tìm kiếm cuộc gọi cần kiểm định theo thời gian, theo kết quả kiểm<br>định 1, theo Giám sát/ trưởng nhóm, theo NV CSKH, số điện thoại KH gọi tổng đài, theo đối<br>tác, theo ngưỡng xếp loại của cuộc gọi, theo lỗi đánh giá của kiểm định lần 1 với Giám<br>sát/trưởng nhóm.<br>- Cho phép tra cứu cuộc gọi đã chấm/ chưa chấm/ cuộc gọi lỗi theo đơn vị đối tác, theo Giám<br>sát/ trưởng nhóm, NV CSKH, số điện thoại của KH gọi tổng đài. Đồng thời trong quá trình<br>tra cứu xong có thể thực hiện sửa/ khôi phục cuộc gọi theo yêu cầu.<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||CSKH, số điện thoại<br>của KH gọi tổng đài.<br>Đồng thời trong quá<br>trình tra cứu xong có<br>thể thực hiện sửa/<br>khôi phục cuộc gọi<br>theo yêu cầu||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.12|Hướng dẫn chấm điểm cuộc gọi<br>(Nội dung này là hướng dẫn có<br>tạo thành 1 menu trong chức<br>năng chấm điểm không)?|- Cần xác định cuộc<br>gọi đầu vào -> Chấm<br>điểm từng tiêu chí -<br>>Xác định mức độ<br>lỗi ảnh hưởng (nếu<br>có)_> nhận xét và<br>chọn bộ lỗi -> Điểm.<br>- Xác định cuộc gọi<br>đầu vào: phân dạng<br>loại cuộc gọi<br>- Chấm điểm từng<br>tiêu chí: khung điểm<br>của từng tiêu chí sẽ<br>được đánh giá là n<br>(OK), n+1 (NOK).<br>Đối với tiêu chí<br>không đạt yêu cầu,<br>Giám sát phải chọn<br>mức lỗi tương ứng.<br>- Xác định mức độ<br>lỗi ảnh hưởng đến<br>KH:<br>+ NV CSKH không<br>vi phạm lỗi: mức lỗi<br>trong tham chấm<br>điểm sẽ được để<br>trống và cuộc gọi đạt<br>ngưỡng Xuất sắc.<br>+ NV CSKH  vi<br>phạm lỗi: áp dụng trừ<br>điểm theo mức lỗi<br>đối với từng nhóm<br>lỗi.|Bổ sung màn hình hướng dẫn<br>==> Đề xuất bỏ|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||- Nhận xét và chọn<br>bộ lỗi.||
|13.13|Hướng dẫn cách tính điểm trung<br>bình nghiệp vụ tháng (tạo thành<br>1 menu riêng)|- Điểm trung bình<br>nghiệp vụ của NV<br>CSKH/ tháng = TBC<br>điểm tất cả các cuộc<br>gọi được đánh giá /<br>tháng/ NV CSKH –<br>điểm quy đổi.<br>-điểmquy đổisẽ|Bổ sung màn hình hướng dẫn<br>==> Đề xuất bỏ|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||được cấu hình với<br>điểm trừ.|||
||**II**|**Chức năng cấu hình hệ thống**|||||
|13.14||Danh mục cấu hình thang điểm||- Hệ thống cho phép<br>người dùng khai báo,<br>sửa xóa chỉ tiêu và<br>trọng số tương ứng<br>với từng đầu mục<br>trong khu giải đáp và<br>tỷ trọng.<br>- Hệ thống hiển thị<br>đầy đủ các chức năng<br>sau:<br>+ Dạng cuộc gọi<br>+ Đầu mục cuộc gọi<br>+ Chỉ tiêu đánh giá<br>cuộc gọi (n)/nhóm<br>lỗi(n)/mứclỗi(n).|Xem trong menu quản lý tiêu chí chấm điểm, nếu đã đáp ứng thì bỏ mục này ==> đề xuất bỏ||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|13.15||Danh mục cấu hình điểm quy đổi||Hệ thống cho phép<br>người dùng khai báo,<br>sửa xóa điểm trừ<br>tương ứng với từng<br>điểm quy đổi|- Bổ sung chức năng danh mục cấu hình điểm quy đổi cho phần Đánh giá đa kênh:<br>- Tìm kiếm, sửa xóa, xuất dữ liệu<br>- Cho phép phân quyền chức năng tới admin quản lý cấu hình<br>- Cấu hình theo các tiêu chí : điểm trung bình tất cả các cuộc gọi được đánh giá trên<br>tháng/NV CSKH.<br>- Nội dung chi tiết tham khảo phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý sản xuất.||
|**III**||**Đánhgiá Học viên**|||||
|13.16||Nhập thông tin học viên||Cần trao đổi:<br>- Dữ liệu thông tin<br>học viên: --> Dữ liệu<br>xuất ra fie hay nhập<br>vào?<br>- Cách thức đánh giá<br>và đầy cuộc gọi về<br>hệ thống: sử dụng cơ<br>chế giống cuộc gọi<br>offline đánh giá NV<br>CKSH đang làm việc<br>(giống như là như<br>nào? )<br>1. Nhập thông tin<br>vào<br>2. Cách thức đánh<br>giá và đầy cuộc gọi<br>về hệ thống: sử dụng<br>cơ chế giống cuộc<br>gọioffline đánhgiá|Bổ sung 1 chức năng hoặc 1 tab đánh giá học viên<br>- Chọn học viên (User)<br>- Import danh sách học viên, tìm kiếm, sửa xóa hoạc viên, thêm học viên<br>- Các thông tin chấm điểm tương tự  đánh giá nhân viên<br>- Bổ sung phân quyền admin có thể nhập thông tin hoặc viên<br>- Cách thức đánh giá và đầy cuộc gọi về hệ thống: sử dụng cơ chế giống cuộc gọi offline đánh<br>giá NV CKSH<br>- Tính điểm trung bình các cuộc gọi theo công thức chi tiết tham khảo phiếu yêu cầu mã IBM<br>4075370 trên hệ thống quản lý sản xuất.||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||NV CKSH đang làm<br>việc (gọi dữ liệu từ<br>hệ thống IPCC đẩy<br>lên phần mềm chấm<br>điểm, sử dụng thang<br>điểm chấm offline)||
|13.17|Báo cáo thống kê kết quả|Cần trao đổi<br>- Điểm đạt của học<br>viên là trung bình<br>điểm các cuộc gọi<br>được chấm.<br>- Thống kê kết quả<br>theo nhân sự, đối tác<br>- Biểu mẫu tổng hợp<br>điểm các cuộc gọi<br>của học viên như<br>sau: --> Xuất file<br>excel theo mẫu tại<br>Phiếu yêu cầu|- Điều chỉnh mẫu báo cáo thống kế theo mẫu mới nhất<br>- Điểm đạt của hoặc viên là trung bìn điểm các cuộc gọi được chấm<br>- Thống kê kết quả theo nhân sự, đối tác<br>- Cho phép xuất file excel theo mẫu báo báo<br>- Mẫu báo cáo tham khảo biểu mẫu tại phiếu yêu cầu có mã IBM 4075370 trên hệ thống quản<br>lý sản xuất|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.18|Test nghiệp vụ|- Tạo mục nhập lưu<br>dữ liệu NV CSKH<br>toàn trung tâm (dữ<br>liệu sẽ được cập nhật<br>khi có NV CSKH<br>mới, NV CSKH<br>nghỉ). Dữ liệu NV<br>CSKH được đánh giá<br>theo user VSA<br>- Trên giao diện nhập<br>dữ liệu test nghiệp<br>vụ, Giám sát sẽ nhập<br>user NV CSKH tiếp<br>nhận cuộc gọi test và<br>đánh giá kết quả đạt/<br>không đạt trên các<br>tiêu chí gồm:<br>+ Nghiệp vụ<br>+ Kỹ năng<br>+ Thái độ<br>+ Kết thúc cuộc gọi<br>(chào KH)<br>+ Đánh giá chung<br>+ Phân loại nghiệp<br>vụ<br>+ Ghi chú<br>- Mục thống kê, báo<br>cáo kết quả:<br>- Giám sát chọn thời<br>gian xuất file chi tiết<br>các cuộc gọi test.<br>- Chọn thời gian xuất<br>kết quả theo user NV<br>CKSHvớicác cột:|- Bổ sung Chức năng (tab) nhập dữ liệu kết quả đánh giá test nghiệp vụ<br>- Nhập đơn lẻ (theo lô)<br>- Import theo file<br>- User ĐTV theo VSA quản lý<br>- Sửa tên thành yêu cầu (quản lý kết quả đánh giá test nghiệp vụ)<br>- Bổ sung 1 báo cáo kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||tổng test, tổng đạt về<br>đánh giá chung, cột<br>tỷ lệ đạt (Tỷ lệ đạt<br>=Tổng cuộc gọi đạt/<br>tổng cuộc gọi test).<br>- Thống kê các cuộc<br>gọi không đạt ở các<br>tiêu chí (tùy chọn):<br>trên các tiêu chí<br>Nghiệp vụ, kỹ năng,<br>thái độ, kết thúc cuộc<br>gọi (chào KH), đánh<br>giá chung, phân loại<br>nghiệp vụ…<br>Mẫu tổng hợp: --><br>Xuất file excel theo<br>mẫu tại Phiếu yêu<br>cầu||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|**IV**|**Tab chấm điểm cuộc gọi cho**<br>**kênh chat đa kênh và mạng xã**<br>**hội **|||
|13.19|Chức năng chấm điểm offline<br>(Chức năng chấm điểm offline<br>đã có nhưng chỉ có duy nhất<br>kênh Voice, chưa có các kênh:<br>chat đã kênh và mạng xã hội--><br>Dữ liệu tương tác của KH khác<br>với kênh Voice, đề xuất xây tab<br>riêng. Anh /chị kỹ thuật đánh giá<br>thêm có thể lựa chọn 1 trong 2<br>cách: (1)  bổ sung thêm kênh<br>chat đa kênh và mạng xã hội<br>trong chức năng đã có hoặc (2)<br>xây tab mới)|- Nội dung tương tác<br>của KH:<br>+ Nội dung hội thoại:<br>hiển thị nội dung<br>tương tác của KH<br>dưới dạng hộp hội<br>thoại có kèm thanh<br>cuộn (kéo lên-xuống<br>với các hội thoại có<br>nội dung dài).<br>+ User của KH: hiển<br>thị user tương tác của<br>KH (dữ liệu lấy trên<br>hệ thống Econtact).<br>- Nhu cầu phản ánh<br>khách hàng gồm 05<br>cấp nghiệp vụ:<br>(tương tự như kênh<br>Voice)<br>- Thang điểm đánh<br>giá cuộc gọi: Giữ<br>nguyên tỷ trọng các<br>tiêu chí giống như<br>kênh Voice<br>- Thang điểm gồm<br>các tiêu chí:<br>+ Tiêu chí chính bao<br>gồm: (1) Kiến thức<br>chuyên môn nghiệp<br>vụ, (2) ý thức trách<br>nhiệm/ thái độ.|- Chỉnh sửa Chấm điểm Offline, bổ sung kênh chat, video call, mạng xã hội để chấm<br>- Lấy được ghi âm, hội thoại chat từ hệ thống Econtact<br>- Xem được nội dung tương tác của KH:<br>+ Nội dung hội thoại: hiển thị nội dung tương tác của KH dưới dạng hộp hội thoại có kèm<br>thanh cuộn (kéo lên-xuống với các hội thoại có nội dung dài).<br>+ User của KH: hiển thị user tương tác của KH (dữ liệu lấy trên hệ thống Econtact).<br>- Nhu cầu phản ánh khách hàng gồm 05 cấp nghiệp vụ: (tương tự như kênh Voice)<br>- Thang điểm đánh giá cuộc gọi: Giữ nguyên tỷ trọng các tiêu chí giống như kênh Voice<br>- Thang điểm gồm các tiêu chí:<br>+ Tiêu chí chính bao gồm: (1) Kiến thức chuyên môn nghiệp vụ, (2) ý thức trách nhiệm/ thái<br>độ.<br>+ Tiêu chí điểm trừ bao gồm:<br>+ Kỹ năng nói /viết,<br>+ Kỹ năng lắng nghe/ trình bày<br>+ Kỹ năng tra cứu<br>+ Tiến độ.<br>- Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý<br>sản xuất|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||+ Tiêu chí điểm trừ<br>bao gồm:<br>+ Kỹ năng nói /viết,<br>+ Kỹ năng lắng nghe/<br>trình bày<br>+ Kỹ năng tra cứu<br>+ Tiến độ.||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|13.20||Chấm điểm Online (Chức năng<br>chấm điểm online đã có nhưng<br>chỉ có duy nhất kênh Voice, chưa<br>có các kênh: chat đã kênh và<br>mạng xã hội)||- Lấy được ghi âm,<br>hội thoại chat từ hệ<br>thống Econtact|- Chỉnh sửa Chấm điểm Online, bổ sung kênh chat, video call, mạng xã hội để chấm<br>- Lấy được ghi âm, hội thoại chat từ hệ thống Econtact<br>- Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý<br>sản xuất||
|13.21||Kiểm định 1 (Chức năng kiểm<br>định 1 đã có nhưng chỉ có duy<br>nhất kênh Voice, chưa có các<br>kênh: chat đã kênh và mạng xã<br>hội)||- Lấy được ghi âm,<br>hội thoại chat từ hệ<br>thống Econtact|Chỉnh sửa chức năng kiểm định 1, bổ sung kênh chat, video call để kiểm định<br>- Lấy được ghi âm, hội thoại chat từ hệ thống Econtact<br>- Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý<br>sản xuất||
|13.22||Kiểm định 2(Chức năng kiểm<br>định 2 đã có nhưng chỉ có duy<br>nhất kênh Voice, chưa có các<br>kênh: chat đã kênh và mạng xã<br>hội)||- Lấy được ghi âm,<br>hội thoại chat từ hệ<br>thống Econtact|Chỉnh sửa chức năng kiểm định 2, bổ sung kênh chat, video call để kiểm định<br>- Lấy được ghi âm, hội thoại chat từ hệ thống Econtact<br>- Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý<br>sản xuất||
|**V**||**Tạo tab chấm điểm cuộc gọi**<br>**Videocall**|||||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.23|Chấm điểm Offline (Chức năng<br>chấm điểm offline đã có nhưng<br>chỉ có duy nhất kênh Voice, chưa<br>kênh: Videocall)|- Giữ nguyên các tiêu<br>chí  và tỷ trọng các<br>tiêu chí trong thang<br>điểm như kênh voice<br>+ Nghiệp vụ<br>+ Ý thức/thái độ<br>+ Nói<br>+ Nghe<br>+ Tra cứu.<br>+ Bổ sung tiêu chí<br>điểm trừ.<br>Trường hợp cuộc gọi<br>thoại 1 chiều hoặc 2<br>chiều sẽ download<br>hình ảnh của toàn bộ<br>cuộc gọi lên Phần<br>mềm chấm điểm|- Bổ sung 1 lựa chọn chấm điểm<br>- Giữ nguyên các tiêu chí  và tỷ trọng các tiêu chí trong thang điểm như kênh voice<br>+ Nghiệp vụ<br>+ Ý thức/thái độ<br>+ Nói<br>+ Nghe<br>+ Tra cứu.<br>+ Bổ sung tiêu chí điểm trừ.<br>Trường hợp cuộc gọi thoại 1 chiều hoặc 2 chiều sẽ download hình ảnh của toàn bộ cuộc gọi<br>lên Phần mềm chấm điểm<br>- Nội dung chi tiết tham khảo nội dung Phiếu yêu cầu mã IBM 4075370 trên hệ thống quản lý<br>sản xuất|
|13.24|Kết quả chấm điểm cuộc gọi<br>(Kết quả chấm điểm cuộc gọi<br>(nội dung này sẽ nằm trong<br>Menu Chấm điểm))|- Tổng hợp toàn bộ<br>kết quả chấm của<br>giám sát trong các<br>ngày. Thông tin tìm<br>kiếm tương tự kênh<br>thoại (voice)<br>- Bổ sung thêm loại<br>kênh:Videocall_Myv<br>iettel|- Tổng hợp toàn bộ kết quả chấm của giám sát trong các ngày. Thông tin tìm kiếm tương tự<br>kênh thoại (voice)<br>- Bổ sung thêm loại kênh:Videocall_Myviettel<br>- Bổ sung phân quyền chức năng cho giám sát viên có quyền thao tác<br>- Nội dung chi tiết tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất|
|13.25|Kiểm định 1(Chức năng kiểm<br>định 1 đã có nhưng chỉ có duy<br>nhất kênh Voice, chưa kênh:<br>Videocall)|- Kết quả kiểm định<br>lần 1: Tương tự kênh<br>thoại (Voice)<br>- Bổ sung thêm tiêu<br>chí điểm trừ|- Kết quả kiểm định lần 1: Tương tự kênh thoại (Voice)<br>- Bổ sung thêm tiêu chí điểm trừ<br>- Bổ sung phân quyền chức năng cho giám sát viên có quyền thao tác<br>- Nội dung chi tiết tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|13.26|Kiểm định 2|- Kết quả kiểm định<br>lần 2: Tương tự kênh<br>thoại (Voice)<br>- Bổ sung thêm tiêu<br>chí điểm trừ|- Bổ sung tính năng Kết quả kiểm định lần 2,<br>Tương tự kênh thoại (Voice)<br>- Bổ sung thêm tiêu chí điểm trừ - Nói/Viết|
|**VI**|**Tạo tab chấm điểm cho kênh**<br>**Email**|||
|13.27|Chấm điểm offline (Chức năng<br>chấm điểm offline đã có nhưng<br>chỉ có duy nhất kênh Voice, chưa<br>kênh: Mail)|- Giữ nguyên các tiêu<br>chí và tỷ trọng của<br>các tiêu chí trong<br>thang điểm Email<br>tương tự như kênh<br>voice:<br>+ Nghiệp vụ<br>+ Ý thức/thái độ<br>+ Nói<br>+ Nghe<br>+ Tra cứu.<br>- Bổ sung thêm tiêu<br>chí Viết (cùng tiêu<br>chí Nói trên thang<br>điểm)<br>- Khi chọn chấm<br>email, hệ thống sẽ<br>đẩy toàn bộ nội dung<br>email lên phần mềm<br>chấm điểm của NV<br>CSKH tới KH theo<br>usertrảlời.|- Giữ nguyên các tiêu chí và tỷ trọng của các tiêu chí trong thang điểm Email tương tự như<br>kênh voice:<br>+ Nghiệp vụ<br>+ Ý thức/thái độ<br>+ Nói<br>+ Nghe<br>+ Tra cứu.<br>- Bổ sung thêm tiêu chí Viết (cùng tiêu chí Nói trên thang điểm)<br>- Khi chọn chấm email, hệ thống sẽ đẩy toàn bộ nội dung email lên phần mềm chấm điểm của<br>NV CSKH tới KH theo user trả lời.<br>- Nội dung chi tiết tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|13.28||Kết quả chấm điểm cuộc gọi (nội<br>dung này sẽ nằm trong Menu<br>Chấm điểm)||- Tổng hợp toàn bộ<br>kết quả chấm của<br>giám sát trong các<br>ngày. Thông tin tìm<br>kiếm tương tự kênh<br>thoại (voice)|- Có tính năng kết quả chấm điểm cuộc gọi (nằm trong menu chấm điểm<br>- Tổng hợp toàn bộ kết quả chấm của giám sát trong các ngày.<br>- Thông tin tìm kiếm tương tự kênh thoại (voice)<br>- Bổ sung phân quyền chức năng cho giám sát viên có quyền thao tác<br>- Nội dung chi tiết tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||
|13.29||Kết quả kiểm định lần 1(Chức<br>năng kiểm định 1 đã có nhưng<br>chỉ có duy nhất kênh Voice, chưa<br>kênh: Mail)||- Tương tự kênh<br>thoại (Voice)<br>- Bổ sung thêm tiêu<br>chí điểm trừ -<br>Nói/Viết|- Tương tự kênh thoại (Voice)<br>- Bổ sung thêm tiêu chí điểm trừ - Nói/Viết<br>- Bổ sung phân quyền chức năng cho giám sát viên có quyền thao tác<br>- Nội dung chi tiết tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||
|13.30||Kết quả kiểm định lần 2||- Tương tự kênh<br>thoại (Voice), (tương<br>tự là như thế nào)<br>- Bổ sung thêm tiêu<br>chí điểm trừ -<br>Nói/Viết|- Bổ sung tính năng Kết quả kiểm định lần 2 cho kênh Email,<br>Tương tự kênh thoại (Voice)<br>- Bổ sung thêm tiêu chí điểm trừ - Nói/Viết<br>- Chi tiết nội dung tham khảo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||
|**VII**||**Báo cáo**|||||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|13.31||Báo cáo đánh giá cảm xúc cuộc<br>gọi||- Bổ sung:<br>- Thời gian: Từ ngày<br>xxx- đến ngày xxx<br>- User: chọn 1 hoặc<br>tất cả<br>- Kênh: chọn 1 hoặc<br>tất cả<br>- Đối tác: chọn 1<br>hoặc tất cả<br>- Khu vực: chọn 1<br>hoặc tất cả<br>- Thâm niên: chọn 1<br>hoặc tất cả|Bổ sung báo cáo theo mẫu :<br>- Cho phép tìm kiếm theo tiêu chí:<br>+ Thời gian: Từ ngày xxx- đến ngày xxx<br>+ User: chọn 1 hoặc tất cả<br>+ Kênh: chọn 1 hoặc tất cả<br>+ Đối tác: chọn 1 hoặc tất cả<br>+ Khu vực: chọn 1 hoặc tất cả<br>+ Thâm niên: chọn 1 hoặc tất cả<br>- Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn.<br>- Cho phép thể hiện dữ liệu dưới dạng biểu đồ<br>- Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||
|13.32||Báo cáo “Chi tiết đánh giá cảm<br>xúc cuộc gọi”:||- Bổ sung:<br>- Thời gian: Từ ngày<br>xxx- đến ngày xxx<br>- User: chọn 1 hoặc<br>tất cả<br>- Kênh: chọn 1 hoặc<br>tất cả<br>- Đối tác: chọn 1<br>hoặc tất cả<br>- Khu vực: chọn 1<br>hoặc tất cả<br>- Thâm niên: chọn 1<br>hoặc tất cả|Bổ sung báo cáo theo mẫu :<br>- Cho phép tìm kiếm theo tiêu chí:<br>+ Thời gian: Từ ngày xxx- đến ngày xxx<br>+ User: chọn 1 hoặc tất cả<br>+ Kênh: chọn 1 hoặc tất cả<br>+ Đối tác: chọn 1 hoặc tất cả<br>+ Khu vực: chọn 1 hoặc tất cả<br>+ Thâm niên: chọn 1 hoặc tất cả<br>- Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn.<br>- Cho phép thể hiện dữ liệu dưới dạng biểu đồ<br>- Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|13.33||Báo cáo “Tỉ lệ đánh giá cảm xúc<br>cuộc gọi”||Xem được tỉ lệ đánh<br>giá chính xác cảm<br>xúc cuộc gọi|Bổ sung báo cáo theo mẫu  (như hiện tại đang dùng trên IPCC 1.0 cập nhật biểu mẫu mới<br>nhất):<br>- Cho phép tìm kiếm theo tiêu chí<br>- Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn.<br>- Cho phép thể hiện dữ liệu dưới dạng biểu đồ<br>- Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||
|13.34||Báo cáo Tỷ lệ nhận diện của hệ<br>thống||- Tìm kiếm theo tiêu<br>chí đã chọn và vẽ<br>biểu đồ<br>- Xuất excel<br>- Tỷ lệ cuộc gọi đã<br>đánh giá ngày/ tháng/<br>năm: vẽ biểu đồ hình<br>tròn|Bổ sung báo cáo theo mẫu  (như hiện tại đang dùng trên IPCC 1.0 cập nhật biểu mẫu mới<br>nhất):<br>- Cho phép tìm kiếm theo tiêu chí<br>- Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn.<br>- Cho phép thể hiện Biểu đồ tỷ lệ cuộc gọi đã đánh giá ngày/tháng/năm (biểu đồ hình tròn)<br>- Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|13.35||Báo cáo nhu cầu Phản ánh Khách<br>hàng||- Thời gian: Từ ngày<br>- đến ngày (ngày tiếp<br>nhận PAKH).<br>- User tiếp nhận.<br>- Mã cuộc gọi.<br>- Số điện thoại gọi<br>lên.<br>- Nghiệp vụ các cấp<br>1,2,3,4,5<br>- Nội dung nhu cầu<br>KH<br>- Cho phép xuất dữ<br>liệu ra file excel theo<br>tiêu chí tìm kiếm đã<br>chọn.<br>- Biểu đồ nhu cầu<br>PAKH|Bổ sung báo cáo theo mẫu (như hiện tại đang dùng trên IPCC 1.0)<br>- Thời gian: Từ ngày - đến ngày (ngày tiếp nhận PAKH).<br>+ User tiếp nhận.<br>+ Mã cuộc gọi.<br>+ Số điện thoại gọi lên.<br>+ Nghiệp vụ các cấp 1,2,3,4,5<br>+ Nội dung nhu cầu KH<br>- Cho phép xuất dữ liệu ra file excel theo tiêu chí tìm kiếm đã chọn.<br>- Cho phép thể hiện Biểu đồ nhu cầu PAKH<br>- Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|13.36||Báo cáo kết quả chấm điểm (29<br>mẫu)|||Bổ sung xây dựng 29 mẫu báo cáo theo mẫu báo cáo cập nhật mới nhât:<br>- Danh sách báo cáo:<br>1. Báo cáo chất lượng giải đáp đối tác theo xếp loại<br>2. Báo cáo chất lượng giải đáp đơn vị đối tác theo thâm niên<br>3. Báo cáo chất lượng giải đáp theo thâm niên tổng hợp các đối tác<br>4. Báo cáo so sánh chất lượng giải đáp theo thâm niên của 2 tháng liền nhau<br>5. Báo cáo chất lượng giải đáp theo ngày (không phân biệt đối tác)<br>6. Báo cáo chất lượng giải đáp theo line<br>7. Báo cáo chất lượng giải đáp đối tác theo xếp loại<br>8. Báo cáo chất lượng giải đáp theo dạng cuộc gọi<br>9. Báo cáo chất lượng nhân sự tổng hợp đối tác theo thâm niên<br>10. Báo cáo chất lượng nhân sự theo thâm niên 2 tháng liền nhau theo khu vực<br>11. Báo cáo chất lượng nhân sự theo line<br>12. Báo cáo chất lượng nhân sự đối tác theo thâm niên<br>13. Báo cáo xu hướng Khách hàng và khả năng đáp ứng của ĐTV theo line<br>14. Báo cáo chi tiết lỗi nghiệp vụ theo line<br>15. Báo cáo chi tiết lỗi tiêu chí<br>16. Báo cáo chi tiết cơ cấu chấm điểm theo thời lượng cuộc gọi của từng đối tác<br>17. Báo cáo chi tiết cơ cấu chấm điểm theo dạng cuộc gọi của từng đối tác<br>18. Báo cáo chi tiết cơ cấu chấm điểm trên từng ĐTV<br>19. Báo cáo cơ cấu kiểm định theo dạng cuộc gọi<br>20. Báo cáo cơ cấu kiểm định theo xếp loại cuộc gọi theo đối tác<br>21. Báo cáo cơ cấu kiểm định theo thời lượng cuộc gọi theo đối tác<br>22. Báo cáo cơ cấu kiểm định chi tiết theo ĐTV<br>23. Báo cáo cơ cấu kiểm định theo đối tác (lũy kế)<br>24. Báo cáo chi tiết chất lượng chấm điểm Của kiểm định VT<br>25. Báo cáo chi tiết lỗi sai (nguyên nhân sai) của từng đối tác<br>26. Báo cáo chi tiết lỗi sai của từng giám sát<br>27. Báo cáo chi tiết lỗi sai (nguyên nhân sai) của từng đối tác<br>28. Báo cáo kết quả chấm điểm cuộc gọi kênh Videocall<br>29. Báo cáo tổng hợp chẩm điểm.<br>-Mẫu báo cáo nội dung mã IBM 40875370 trên hệ thống quản lý sản xuất||
|**14**||**Mobile Call(CG tư vấn bán**<br>**hàng)**|||||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||14.1|Bổ sung cung cấp quyền VSA<br>cho quyền chức năng lích sử<br>cuộc gọi|||- GD tra cứu cuộc gói bổ sung thông tin: loại kênh bán, user kênh bán trên chức năng nghe<br>lịch sử cuộc gọi.<br>- Bổ sung ma trận phân quyền cho chức năng gửi VSA để cấp quyền, cấp quyền cho các user<br>có quyền thao tác||
||14.2|Khi login mất kết nối AG server<br>Khi call log CG không có file ghi<br>âm|||- Kiểm tra lỗi khi login mất kết AG Server<br>- Bổ sung trường hiển thị đường link đến file ghi âm<br>- Cho phép kích vào file ghi âm có thể nghe lại||
||14.3|trên GD cuộc gọi tư vấn thể hiện<br>thời gian cuộc gọi bao nhiêu thời<br>gian|||Trên GD cuộc gọi tư vấn thể hiện thời gian cuộc gọi bao nhiêu thời gian||
||14.4|Triển khai trên MAriaDB|||Hệthốngmới sẽ triển khai trên MariaDB||
||14.5|Hiển thị một số các trường thông<br>tin của khách hàng để ông tư vấn<br>biết (như|||Bổ sung màn hình thông tin key KH: đang dùng gói thuê bao gì, có đang dùng VTPay và một<br>số thông tin key khác…<br>trên giao dịch giao diện cuộc gọi||
||**15**|**Video Call Quản lý bán hàng**<br>**mới **|||||
||15.1|Tích hợp với CN giám sát cửa<br>hàng, gám sát điểm bán để gọi<br>được Video  call đến một người<br>trong đó|||- Tích hợp với CN giám sát cửa hàng, gám sát điểm bán để gọi được Video  call đến một<br>người trong đó||
||15.2|Khi gọi videocall đến cửa hàng<br>và điểm bán mà không kết nối có<br>lựa chọn để chuyển cuộc gọi<br>sang số tổng đài và điểm bán|||Khi gọi videocall đến cửa hàng và điểm bán mà không kết nối có lựa chọn để chuyển cuộc<br>gọi sang số tổng đài và điểm bán||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|15.3|Bổ sung các mẫu báo cáo, các<br>màn hìnhgiám sát theo mẫu||- Bổ sung các mẫu báo cáo, các màn hình giám sát theo mẫu|
|**16**|**Video Call xác minh khách**<br>**hàng**|||
|16.1|Bổ sung chức năng đánh giá<br>cuộc gọi|Chưa có chức năng<br>đánh giá cuộc gọi<br>(ĐTV hiện tại phải<br>thống kê thủ công<br>qua file excel rất bất<br>tiện)|- Hệ thống bổ sung báo cáo đánh giá cuộc gọi cho phép xuất dữ liệu ra file excel<br>- Nâng cấp hệ thống cũ bổ sung báo cáo đánh giá cuộc gọi (có nhiều báo cáo)|
|16.2|Chức năng tra cứu lịch sử cuộc<br>gọi|Chưa nghe lại được<br>cuộc gọi có hình ảnh,<br>chỉ nghe đc âm thanh|- Kiểm tra lại trên hệ thống cũ<br>- Trên hệ thống mới phải đáp ứng được vấn đề này|
|16.3|Chức năng tra cứu lịch sử cuộc<br>gọi|**3.      Nhiều cuộc gọi**<br>**ko tìm kiếm lại**<br>**được (NN do đang**<br>**bị đầy bộ nhớ)**|- Hệ thống hiện tại đang bị đầy bộ nhớ ==> thực hiện nâng cấp bộ nhớ theo kế hoạch thống<br>nhất để giải quyết vấn đề này (phụ thuộc vào kế hoạch hạ tầng)<br>- Trên hệ thống mới sẽ tự động đáp ứng vấn đề này|
|16.4|Quản lý cuộc gọi|**4.      Thỉnh thoảng**<br>**tại 1 thời điểm cuộc**<br>**gọi bị rớt nhiều (ví**<br>**dụ 16h ngày 14/6)**|- Kiểm tra tại sao tự dưng rớt và rớt hàng loạt<br>- Khi rớt hàng loạt bên CSKH báo lại cho VTS để phối hợp kiểm tra tìm nguyên nhân|
|16.5|Quản lý cuộc gọi|5.      Lỗi cuộc gọi<br>đang tiếp nhận bị mất<br>tín hiệu (TB tiếp<br>nhận 80c/ngày)|- Hiện tại hệ thống vẫn đáp ứng KPI<br>- Khi có lỗi thì bên CSKH báo lại cho VTS để phối hợp kiểm tra<br>- Trên hệ thống xây mới đảm bảo được KPI và giảm thiểu các lỗi này|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|16.6|Quản lý cuộc gọi|6.      Lỗi cuộc gọi<br>không hiển thị video<br>(TB tiếp nhận<br>40c/ngày)|- Hiện tại hệ thống vẫn đáp ứng KPI<br>- Khi có lỗi thì bên CSKH báo lại cho VTS để phối hợp kiểm tra<br>- Trên hệ thống xây mới đảm bảo được KPI và giảm thiểu các lỗi này|
|16.7|Yêu cầu về giao diện|Bố trí lại màn hình<br>thông tin khách hàng<br>rõ nét hơn, rộng to<br>hơn (hợp lý hơn)|- Tham khảo bố trí giao diện các hệ thống hiện tại (VD: stringee...)<br>- Đảm bảo giao diện thuận tiện dễ dùng hợp lý hơn cho người dung|
|**17**|**Video Call CSKH**|||
|17.1|Tính năng gọi VideoCall|Đây là tính năng cho<br>phép KH thiết lập<br>cuộc gọi hình ảnh<br>với NV CSKH<br>Viettel. Khi KH click<br>vào nút “Gọi Video<br>miễn phí với<br>CSKH”, sẽ có 3<br>Option để KH lựa<br>chọn kết nối với NV<br>CSKH:<br>+ Cuộc gọi hình ảnh<br>2 chiều (KH và NV<br>CSKH nhìn thấy<br>hình ảnh của nhau).<br>+ Cuộc gọi hình ảnh<br>1 chiều nhân viên<br>(chỉ có KH nhìn thấy<br>hình ảnh NV CSKH).<br>+ Cuộc gọi âm thanh<br>(KH và NV CSKH|Đây là tính năng cho phép KH thiết lập cuộc gọi hình ảnh với NV CSKH Viettel. Khi KH<br>click<br>vào nút “Gọi Video miễn phí với CSKH”, sẽ có 3 Option để KH lựa chọn kết nối với NV<br>CSKH:<br>+ Cuộc gọi hình ảnh 2 chiều (KH và NV CSKH nhìn thấy hình ảnh của nhau).<br>+ Cuộc gọi hình ảnh 1 chiều nhân viên (chỉ có KH nhìn thấy hình ảnh NV CSKH).<br>+ Cuộc gọi âm thanh (KH và NV CSKH không nhìn thấy nhau)|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||không nhìn thấy<br>nhau)||
|17.2|Tính năng Chat Online|Cho phép KH tương<br>tác qua chat với NV<br>CSKH Tổng đài<br>video callđakênh|Cho phép KH tương tác qua chat với NV CSKH Tổng đài video call đa kênh|
|17.3|Tính năng Đặt lịch hẹn CSKH<br>gọi lại|- Cho phép KH đặt<br>lịch hẹn NVCSKH<br>gọi lại.<br>- Nội dung đặt lịch<br>gồm: thời gian KH<br>mong muốn NV<br>CSKH gọi lại, nội<br>dung nghiệp vụ KH<br>cần được hỗ trợ, tư<br>vấn.|- Cho phép KH đặt lịch hẹn NVCSKH gọi lại.<br>- Nội dung đặt lịch gồm: thời gian KH mong muốn NV CSKH gọi lại, nội dung nghiệp vụ<br>KH<br>cần được hỗ trợ, tư vấn.|
|17.4|Tính năng gọi 1 chiều|Không hiển thị hình<br>ảnh của khách hàng|- Không hiển thị hình ảnh của khách hàng (Hiển thị hình ảnh 1 chiều)|
|17.5|Chat trongcuộcgọi|Chat trongcuộcgọi|Chat trongcuộcgọi|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||17.6|Transfer sangagent khác|||Transfer sangagent khác(video call)||
||17.7|Chuyển chuyên gia (Professor)|||ĐTV chuyển cuộc gọi video sang chuyển gia (sử dụng MyVietel)||
||17.8|Chuyển sang 1 callflow khác<br>(callflow có thể là: Queue, nhánh<br>phát nhạc, Agent).|||- Cho phép kết thúc cuộc gọi video call => chuyển qua luồng voice, IVR, …||
||17.9|Nghe lén|||Tính năng nghe lén: GS không nghe được tín hiệu gì từ ĐTV và KH. .||
|17.10||Nhắc bài|||Tính năng nhắc bài: ĐTV nói GS nghe được, GS nói ĐTV không nghe được||
|17.11||Cướp cuộc gọi|||Tính năng cướp cuộc gọi: GS nói KH không nghe thấy, KH nói GS vẫn nghe bình thường.||
|17.12||Kết thúc cuộc gọi|||Giám sát chưa thao tác được: điểu chỉnh cho GS thao tác được||
|17.13||Trên My CC cũng  nhận diện<br>được hạng KH|||Trên My CC cũng  nhận diện được hạng KH||
|17.14||Cho phép cấu hình màn hình chờ<br>khi hold cuộc gọi||Thiết kế màn hình<br>chờ để KH nhìn thấy<br>logo Viettel khi ĐTV<br>bấm Hold, tránh hiểu<br>nhầm bị lag hình ảnh<br>--> Amind có thể<br>thay đổi cập nhật<br>màn hình chờ theo<br>YC|Thiết kế màn hình chờ để KH nhìn thấy logo Viettel khi ĐTV bấm Hold, tránh hiểu nhầm bị<br>lag hình ảnh --> Amind có thể thay đổi cập nhật màn hình chờ theo YC<br>Cho phép cấu hình màn hình chờ khi hold cuộc gọi: Video, hình ảnh, slideshow||
|17.15||Hỗ trợ khi ĐTV mute cuộc gọi||Khi ĐTV mute, phía<br>KH thấy màn hình<br>đen ko nhìn thấy<br>ĐTV|- Khi mute cuộc gọi => Vẫn hiển thị video<br>- Vẫn hiển thị hình ảnh của KH||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.16|Login hệ thống MyCC: 1<br>account chỉ được phép đăng nhập<br>duy nhất trên 1 máy tính|Login hệ thống<br>MyCC: 1 account chỉ<br>được phép đăng nhập<br>duy nhất trên 1 máy<br>tính<br>=> Hiện tại 1 user<br>đăng nhập đồng thời<br>trên nhiều vị trí (Khi<br>cg đổ đến acc của<br>ĐTV sẽ đổ đồng thời<br>trên các  thiết bị,<br>ĐTV không thao tác<br>để tiếp nhận, CG rớt)|Login hệ thống MyCC: 1 account chỉ được phép đăng nhập duy nhất trên 1 máy tính<br>=> Hiện tại 1 user đăng nhập đồng thời trên nhiều vị trí (Khi cg đổ đến acc của ĐTV sẽ đổ<br>đồng thời trên các  thiết bị, ĐTV không thao tác để tiếp nhận, CG rớt)|
|17.17|Cuộc gọi đến ĐTV videocall<br>chưa tự link sang BCCS|Cuộc gọi đổ đến<br>ĐTV trên Mycc =><br>Khi ĐTV click nhận<br>sẽ tự bung giao diện<br>BCCS hiển thị thông<br>tinthuê bao|Cuộc gọi đổ đến ĐTV trên Mycc => Khi ĐTV click nhận sẽ tự bung giao diện BCCS hiển thị<br>thông tin thuê bao|
|17.18|hiển thị thông tin cuộc gọi video<br>1 chiều, video 2 chiều, voice|Khi có cuộc gọi đổ<br>đến ĐTV, trên giao<br>diện MyCC hiển thị<br>thông báo loại cuộc<br>gọi của KH là<br>Videocall 1 chiều, 2<br>chiều, voice|Khi có cuộc gọi đổ đến ĐTV, trên giao diện MyCC hiển thị thông báo loại cuộc gọi của KH<br>là Videocall 1 chiều, 2 chiều, voice|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.19|Tool thống kê dữ liệu Agent<br>(dành cho BO): Tổng tiếp nhận,<br>tổng rớt, thời gian nhấc máy, thời<br>gian đàm thoại, thời gian các<br>trạng thái làm việc/ Log chi tiết<br>thay đổi trạng thái của Agent/<br>BC lưu lượng theo khoảng giờ<br>(tổng vào, tổng rớt, tổng gặp)/|TC chưa thực hiện<br>được công tác cảnh<br>báo đánh giá hiệu<br>quả, ý thức làm việc<br>củ NV CSKH|Tool thống kê dữ liệu Agent (dành cho BO): Tổng tiếp nhận, tổng rớt, thời gian nhấc máy,<br>thời gian đàm thoại, thời gian các trạng thái làm việc/ Log chi tiết thay đổi trạng thái của<br>Agent/ BC lưu lượng theo khoảng giờ (tổng vào, tổng rớt, tổng gặp)/|
|17.20|Tool thống kê dữ liệu năng suất,<br>thời gian Avaiable của Agent<br>(dành cho Agent)|TVV không nắm<br>được hiệu suất công<br>việc trong ca để đảm<br>bảo năng suất và thời<br>gian làm việc theo<br>quy định|Tool thống kê dữ liệu năng suất, thời gian Avaiable của Agent (dành cho Agent)|
|17.21|Cấu hình kết thúc cuộc gọi và<br>chat chưa đồng bộ dẫn đến kéo<br>dài thời gian xử lý (KH đã kết<br>thúc call nhưng phiên chat vẫn<br>để thời gian timeout theo cấu<br>hình kênh chat, một số TH khách<br>hàng lại gọi lại khi chat chưa out<br>sẽ làm tăng lưu lượng vào)|Cấu hình khi KH kết<br>thúc Video call hệ<br>thống sẽ kết thúc<br>Chat (đảm bảo đúng<br>tính chất tương tác,<br>rút ngắn thời gian<br>CG)|Cấu hình kết thúc cuộc gọi và chat chưa đồng bộ dẫn đến kéo dài thời gian xử lý (KH đã kết<br>thúc call nhưng phiên chat vẫn để thời gian timeout theo cấu hình kênh chat, một số TH<br>khách hàng lại gọi lại khi chat chưa out sẽ làm tăng lưu lượng vào)|
|17.22|Tình trạng gửi tin báo "Gửi lỗi"<br>do KH đã thoát tính năng Chat,<br>tuy nhiên phía TVV không có<br>nhận biết, phải chờ KH, hết thời<br>gian time out mới được ngắt kết<br>nối|kéo dài thời gian xử<br>lý, YC đối với TH<br>khách hàng tự ngắt<br>phiên chat, thoát khỏi<br>tính năng => Hệ<br>thống cần cấu hình<br>kết thúc phiên chat,<br>có thông báo cho|Tình trạng gửi tin báo "Gửi lỗi" do KH đã thoát tính năng Chat, tuy nhiên phía TVV không có<br>nhận biết, phải chờ KH, hết thời gian time out mới được ngắt kết nối|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||TVV, giải phóng<br>kênh|||
|17.23||Hệ thống chưa hiển thị số thuê<br>bao trên giao diện chat phía KH||Hiển thị số thuê bao<br>trên giao diện chat<br>phía KH theo đúng<br>cấu hình trên kênh<br>chat 4G|Hệ thống chưa hiển thị số thuê bao trên giao diện chat phía KH||
|17.24||Xuất file chi tiết kênh Call me<br>back chưa có thời gian KH đặt<br>lịch hẹn||chưa có số liệu ảnh<br>hưởng đến công tác<br>báo cáo thống kê nhu<br>cầu KH|Xuất file chi tiết kênh Call me back chưa có thời gian KH đặt lịch hẹn||
|17.25||Tính năng tự động gọi ra trên<br>CMB||Ảnh hưởng đến hoạt<br>động giải dápKH|Tính năng tự động gọi ra trên CMB||
|17.26||Tool dành cho BO vận hành thực<br>hiện các thao tác: Add thêm user<br>nghe line cho Agent, user BO;<br>reset mật khẩu đăng nhập hệ<br>thống; gán/thay đổi queue giải<br>đáp cho Agent||Chưa hỗ trợ được kịp<br>thời trong ca trực ảnh<br>hưởng đến hoạt động<br>giải đáp|Tool dành cho BO vận hành thực hiện các thao tác: Add thêm user nghe line cho Agent, user<br>BO;khoá/mở khoá mật khẩu đăng nhập hệ thống ; gán/thay đổi queue giải đáp cho Agent||
|17.27||Tool báo cáo số liệu<br>https://10.60.96.72:8692/report<br>chưa chính xác, tình trạng đăng<br>nhập hệ thống chập chờn thường<br>xuyên báo lỗi||YC hoàn thiện và<br>bàn giao tài liệu cho<br>các tool lấy số liệu,<br>thống nhất cách lấy<br>SL.|Tool báo cáo số liệu https://10.60.96.72:8692/report chưa chính xác, tình trạng đăng nhập hệ<br>thống chập chờn thường xuyên báo lỗi<br>- Bổ sung kiểm tra tình trạng đăng nhập hệ thống báo cáo số liệu<br>- Chỉnh sửa lại các lỗi sau khi xác định được nguyên nhân lỗi||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.28|Hệ thống chưa tối ưu, user của<br>người dùng không vào được đủ<br>các link của hệ thống eContact;<br>hệ thống đang phân quyền 1 user<br>chỉ vào được 1 trong 2 trang<br>eContact Chat đa kênh hoặc<br>Videp call đa kênh => bất cập<br>trong công tác điều hành do nhân<br>sự có thể dùng chung|YC tạo lại quyền truy<br>cập hệ thống|- Trên hệ thống mới sẽ tập trung chức năng và việc phân quyền theo nhóm sẽ đảm bảo được<br>các tài khoản sẽ có đầy đủ các chức năng theo phân quyền.|
|17.29|Bộ đếm thời gian khi chạy clip<br>chờ trên Video call.|KH không nắm được<br>thờigian chờ kết nối|Hiển thị bộ đếm thời gian video chờ|
|17.30|ĐTV, TC phải xác thực 10 link<br>mới vào được hệ thống mỗi lần<br>chuyển máy tính khác hoặc xóa<br>cache lại phải xác thực lại =><br>khó khăn, mới thời gian|Bất cập, mất thời<br>gian|ĐTV, TC phải xác thực 10 link mới vào được hệ thống mỗi lần chuyển máy tính khác hoặc<br>xóa cache lại phải xác thực lại => khó khăn, mới thời gian|
|17.31|Tính năng nghe cuộc gọi Offline<br>hiện file ghi âm đang bị chia<br>thành 2 cửa sổ KH và TVV,<br>giám sát không sử dụng được chế<br>độ tua ghi âm|Tối ưu gộp thành 1<br>cửa sổ để GS thực<br>hiện chế độ tua|Tính năng nghe cuộc gọi Offline hiện file ghi âm đang bị chia thành 2 cửa sổ KH và TVV<br>=> Gộp thành 1 file ghi âm (voice của cả KH và ĐTV)|
|17.32|Hiển thị thời gian phiên chat trên<br>giao diện KH đến giây|ĐTV chưa xác định<br>được thời gian chat.<br>YC hiện thị chính<br>xác đến giây|Hiển thị thời gian phiên chat (giây)|
|17.33|Tính năng Tổng đài 4G chưa<br>được tích hợp lên web Portal|Theo bài toán ban<br>đầu|- Bổ sung tính năng tổng đài 4G lên web Portal<br>- Đưa thành webview (nhúng link web)|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.34|Chưa có tính năng chấm điểm<br>cuộc gọi.|GS chấm thủ công<br>trên file excel, khó<br>kiểm soát => tính<br>năng theo Theo bài<br>toán ban đầu|- Bổ sung chức năng cấu hình chấm điểm cuội gọi<br>- Bổ sung tự động tính điểm cuộc gọi sau khi cuộc gọi kết thúc<br>- Bổ sung giao diện xem thông tin chấm điểm cuộc gọi|
|17.35|Chưa có hệ thống đánh giá hài<br>lòng|Chưa đánh giá được<br>ý kiến của KH. YC<br>bổ sung hiện đã có<br>tính năng này trên<br>Chat đa kênh-<br>eContact|- Bổ sung chức năng đánh giá hài lòng khi kết thúc luồng gọi|
|17.36|Hiện tại hệ thống chưa có tool<br>thống kê các cuộc gọi ĐTV tự<br>kết thúc khi cuộc gọi đã đổ đến<br>agent|YC bổ sung tool<br>thống kê|Bổ sung tool thống kê các cuộc gọi ĐTV tự kết thúc khi cuộc gọi đã đổ đến agent|
|17.37|Khi kết thúc cuộc gọi VideoCall<br>có các chức năng SMS, play<br>quảng cáo…|- Khi kết thúc cuộc<br>gọi VideoCall có các<br>chức năng SMS, play<br>quảng cáo…|- Khi kết thúc cuộc gọi VideoCall có các chức năng SMS, play quảng cáo…<br>- Phát video quảng cáo: Khi ĐTV kết thúc trước<br>- Gửi sms quảng cáo đến thuê bao sau khi kết thúc<br>- Hệ thống tự phát được video/ gửi sms|
|17.38|Giao diện có các khu vực header<br>và footer dành cho quảng cáo,<br>khu vực này có thể cấu hình text<br>chạy hoặc ảnh động hoặc cảnh<br>báo dịch vụ của khách hàng|Cho phép hình text<br>chạy hoặc cảnh báo<br>dịch vụ của KH ở<br>khu vực header và<br>footer dành cho<br>quảng cáo|Giao diện có các khu vực header và footer dành cho quảng cáo, khu vực này có thể cấu hình<br>text chạy hoặc ảnh động hoặc cảnh báo dịch vụ của khách hàng|
|17.39|+   Hiển thị cảnh báo chất lượng<br>sóng trực quan bằng biểu tượng<br>và màu sắc hiển thị realtime, có<br>3-5 mức độ chất lượng.|Hiển thị cảnh báo<br>chất lượng sóng trực<br>quan bằng biểu<br>tượng và màu sắc<br>hiển thị realtime, có<br>3-5 mức độ chất<br>lượng|Hiển thị cảnh báo chất lượng sóng trực quan bằng biểu tượng và màu sắc hiển thị realtime, có<br>3-5 mức độ chất lượng. (Sóng thoại)|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.40||Thời gian chờ trong Queue sẽ do<br>bộ phận kỹ thuật tự cấu hình. Khi<br>KH chờ hết thời gian timeout, hệ<br>thống tự động bật ra cửa sổ Đặt<br>lịch hẹn gọi lại để KH thiết lập<br>lịch hẹn gọi lại sau.||Thời gian chờ trong<br>Queue sẽ do bộ phận<br>kỹ thuật tự cấu hình.<br>Khi KH chờ hết thời<br>gian timeout, hệ<br>thống tự động bật ra<br>cửa sổ Đặt lịch hẹn<br>gọi lại để KH thiết<br>lập lịch hẹn gọi lại<br>sau.|Thời gian chờ trong Queue sẽ do bộ phận kỹ thuật tự cấu hình. Khi KH chờ hết thời gian<br>timeout, hệ thống tự động bật ra cửa sổ Đặt lịch hẹn gọi lại để KH thiết lập lịch hẹn gọi lại<br>sau.||
|17.41||Chức năng cấu hình bắt buộc<br>khách hàng xem hết video chờ<br>trong khoảng x giây mới chuyển<br>đến ĐTV rảnh (ĐTV rảnh cũng<br>ko tiếp nhận ngay mà KH phải<br>xem hết đoạn video)||- chức năng cấu hình<br>bắt buộc khách hàng<br>xem hết video chờ<br>trong khoảng x giây<br>mới chuyển đến<br>ĐTV rảnh (ĐTV<br>rảnh cũng ko tiếp<br>nhận ngay mà KH<br>phải xem hết đoạn<br>video)|- chức năng cấu hình bắt buộc khách hàng xem hết video chờ trong khoảng x giây mới<br>chuyển đến ĐTV rảnh (ĐTV rảnh cũng ko tiếp nhận ngay mà KH phải xem hết đoạn video)||
|||**Nghe offline**|||||
|17.42||Link với phần đánh giá cuộc gọi||Khi nghe lại cuộc<br>gọi, nếu muốn đánh<br>giá chấm điểm cuộc<br>gọi đó GS sẽ tích vào<br>nút Chấm điểm (bên<br>cạnh nút Nghe<br>offline), khi đó hệ<br>thống sẽ link sang<br>phần chấm điểm để<br>đánh giá các tiêu chí<br>như quy định.|Khi nghe lại cuộc gọi, nếu muốn đánh giá chấm điểm cuộc gọi đó GS sẽ tích vào nút Chấm<br>điểm (bên cạnh nút Nghe offline), khi đó hệ thống sẽ link sang phần chấm điểm để đánh giá<br>các tiêu chí như quy định.||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.43|Lưu dữ liệu ghi âm và phiên chat|Cho phép GS/TC<br>xuất và tải file ghi<br>âm (voice call, video<br>call, call back) và dữ<br>liệu chi tiết phiên<br>chát về máy tính.|Cho phép GS/TC xuất và tải file ghi âm (voice call, video call, call back) và dữ liệu chi tiết<br>phiên chát về máy tính.|
|17.44|Nhận diện chế độ hold,mute máy<br>trong cuộc gọi của ĐTV|Khi nghe lại cuộc<br>gọi, GS có thể nhận<br>diện được ĐTV đã<br>hold máy hay mute<br>máy.|Khi nghe lại cuộc gọi, GS có thể nhận diện được ĐTV đã hold máy hay mute máy.|
||**Nghe online**|||
|17.45|Đánh dấu lỗi sai|Khi GS/TC nghe<br>online,GS có thể note<br>vào file ghi âm đoạn<br>ĐTV bị sai. Phần này<br>GS sẽ tích vào nút<br>Nhắc nhở.( cạnh với<br>nút Nghe online và<br>nút Chấm điểm)|Khi GS/TC nghe online,GS có thể note vào file ghi âm đoạn ĐTV bị sai. Phần này GS sẽ tích<br>vào nút Nhắc nhở.( cạnh với nút Nghe online và nút Chấm điểm)<br>Cho phép đánh dấu vào thời điểm cần nhắc nhở => Xuất file biết được thời điểm bị nhắc nhở|
|17.46|Nói thầm với ĐTV|Khi ĐTV trả lời cuộc<br>gọi nhưng cần hỗ trợ,<br>GS/TC nghe online<br>có thể nhắc ĐTV<br>trực tiếp trong cuộc<br>gọi, nội dung nhắc<br>này chỉ ĐTV nghe<br>thấy- không làm ảnh<br>hưởng tới KH|Khi ĐTV trả lời cuộc gọi nhưng cần hỗ trợ, GS/TC nghe online có thể nhắc ĐTV trực tiếp<br>trong cuộc gọi, nội dung nhắc này chỉ ĐTV nghe thấy- không làm ảnh hưởng tới KH|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.47|Đàm thoại nhóm|Khi GS/TC nghe<br>online, nếu KH yêu<br>cầu gặp GS hoặc nội<br>dung cuộc gọi cần<br>can thiệp, GS có thể<br>sử dụng chức năng<br>này để đàm thoại 3<br>bên: KH-ĐTV-GS|- Khi GS/TC nghe online, nếu KH yêu cầu gặp GS hoặc nội dung cuộc gọi cần can thiệp, GS<br>có thể sử dụng chức năng này để đàm thoại 3 bên: KH- ĐTV- GS<br>- ĐTV không thể nói (tự động mute), Không hiển thị hình giám sát|
|17.48|Chat hỗ trợ|Khi ĐTV trả lời cuộc<br>gọi / phiên chat<br>nhưng cần hỗ trợ,<br>GS/TC chat tới ĐTV<br>nội dung cần nhắc<br>nhở. Nội dung này sẽ<br>hiển thị trên màn<br>hình ĐTV|Khi ĐTV trả lời cuộc gọi / phiên chat nhưng cần hỗ trợ, GS/TC chat tới ĐTV nội dung cần<br>nhắc nhở. Nội dung này sẽ hiển thị trên màn hình ĐTV|
|17.49|Gọi điện hỗ trợ|Khi ĐTV trả lời<br>phiên chat nhưng cần<br>hỗ trợ, GS/TC có thể<br>gọi trực tiếp tới ID<br>ĐTV đểnhắcnhở.|Khi ĐTV trả lời phiên chat (Không áp dụng với kênh thoại) nhưng cần hỗ trợ, GS/TC có thể<br>gọi trực tiếp tới ID ĐTV để nhắc nhở (Không cho chiều ngược lại, hoặc ĐTV gọi cho ĐTV)|
|17.50|Add danh sách nghe online|Cho phép GS/TC<br>nghe online toàn bộ<br>nhân viên có trong ca<br>trực, hoặc add danh<br>sách nghe online<br>theo chủ đích( vd:<br>nhân sự yếu,  nhân<br>sự mới lên line, nhân<br>sự viphạmtháiđộ)|Cho phép GS/TC nghe online toàn bộ  nhân viên có trong ca trực, hoặc add danh sách nghe<br>online theo chủ đích( vd: nhân sự yếu,  nhân sự mới lên line, nhân sự vi phạm thái độ)|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.51|Cảnh báo cuộc gọi dài|Trong ca, nếu có<br>cuộc gọi của ĐTV<br>kéo dài >5p, hệ<br>thống sẽ có cảnh báo<br>(cảnh báo dạng pop<br>up hoặc màu sắc) để<br>GS/TC dễ phát hiện,<br>dễ can thiệp cắt cuộc<br>gọi khi cần.|Trong ca, nếu có cuộc gọi của ĐTV kéo dài >5p, hệ thống sẽ có cảnh báo (cảnh báo dạng pop<br>up hoặc màu sắc) để GS/TC dễ phát hiện, dễ can thiệp cắt cuộc gọi khi cần.|
|17.52|Link với phần đánh giá chấm<br>điểm|Khi nghe online CG/<br>xem online phiên<br>chát nếu muốn đánh<br>giá chấm điểm<br>CG/phiên chát đó GS<br>sẽ tích vào nút Chấm<br>điểm (bên cạnh nút<br>Nghe online), khi đó<br>hệ thống sẽ link sang<br>phần chấm điểm để<br>đánh giá các tiêu chí<br>như quy định.|Khi nghe online CG/ xem online phiên chát nếu muốn đánh giá chấm điểm CG/phiên chát đó<br>GS sẽ tích vào nút Chấm điểm (bên cạnh nút Nghe online), khi đó hệ thống sẽ link sang phần<br>chấm điểm để đánh giá các tiêu chí như quy định.|
|17.53|Nhận diện chế độ hold,mute máy<br>trong cuộc gọi của ĐTV|Khi nghe online cuộc<br>gọi, GS có thể nhận<br>diện được ĐTV đã<br>hold máy hay mute<br>máy.|Khi nghe online cuộc gọi, GS có thể nhận diện được ĐTV đã hold máy hay mute máy.|
||**Quản lý cuộc gọi ra của ĐTV**|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.54|Thống kê offline chi tiết cuộc gọi<br>ra|1. Điều kiện chọn:<br>+ Chọn kênh (Không<br>chọn sẽ thống kê tất<br>cả các kênh)<br>+ Chọn thời gian<br>2. Kết quả thống kê:<br>+ Tổng cuộc gọi<br>thành công, Tổng<br>thất bại (nguyên<br>nhân: KH không<br>nghe máy, KH từ<br>chối), Thời gian chờ,<br>Tổng thời gian đàm<br>thoại, Thời gian chờ<br>TBinh, Tổng nhân<br>sự.|1. Điều kiện chọn:<br>+ Chọn kênh (Không chọn sẽ thống kê tất cả các kênh)<br>+ Chọn thời gian<br>2. Kết quả thống kê:<br>+ Tổng cuộc gọi thành công, Tổng thất bại (nguyên nhân: KH không nghe máy, KH từ chối),<br>Thời gian chờ, Tổng thời gian đàm thoại, Thời gian chờ TBinh, Tổng nhân sự.|
|17.55|Theo dõi Online|Tính năng này sẽ<br>theo dõi cả kênh Call<br>back và các cuộc<br>HPC khác trên tổng<br>đài:<br>1. Điều kiện chọn:<br>+ Kênh cần theo dõi:<br>ví dụ Call back/<br>happy call<br>2. Kết quả Online:<br>Kênh, Số thuê bao,<br>thời gian gọi ra thời<br>lượng cuộc gọi|Tính năng này sẽ theo dõi cả kênh Call back và các cuộc HPC khác trên tổng đài:<br>1. Điều kiện chọn:<br>+ Kênh cần theo dõi: ví dụ Call back/ happy call<br>2. Kết quả Online: Kênh, Số thuê bao, thời gian gọi ra thời lượng cuộc gọi|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.56||Thống kê chi tiết theo Agent gọi<br>ra||1. Điều kiện chọn:<br>+ Chọn ĐTV; Chọn<br>kênh (nếu không<br>chọn kênh sẽ xuất chi<br>tiết ĐTV trên tất cả<br>các kênh)<br>+ Ô tìm kiếm nâng<br>cao để search nhiều<br>ĐTV<br>+ Ô nhập thời gian<br>2. Kết quả:<br>+ Xuất chi tiết theo<br>ĐTV gồm: kênh, số<br>TB, thời gian gọi ra<br>+ Trạng thái kết thúc<br>cuộc gọi.|1. Điều kiện chọn:<br>+ Chọn ĐTV; Chọn kênh (nếu không chọn kênh sẽ xuất chi tiết ĐTV trên tất cả các kênh)<br>+ Ô tìm kiếm nâng cao để search nhiều ĐTV<br>+ Ô nhập thời gian<br>2. Kết quả:<br>+ Xuất chi tiết theo ĐTV gồm: kênh, số TB, thời gian gọi ra<br>+ Trạng thái kết thúc cuộc gọi.||
|||**Call me back**|||||
|17.57||Tần suất||Thống kê số lần gọi<br>ra cho các thuê bao|Thống kê số lần gọi ra cho các thuê bao||
|17.58||Thống kê tổng hợp đánh giá chỉ<br>số kết nối của kênh call me back||Thống kê chi tiết<br>tương tác có đánh giá<br>NOK và OK đối với<br>từng tương tác|Thống kê chi tiết tương tác có đánh giá NOK và OK đối với từng tương tác||
|17.59||Thống kê nhu cầu thực KH (căn<br>cứ trên nội dung ĐTV gọi lại cho<br>KH)||Thống kê nhu cầu<br>KH theo nội dung<br>thực tế ĐTV tick khi<br>gọi lại cho KH|Thống kê nhu cầu KH theo nội dung thực tế ĐTV tick khi gọi lại cho KH||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
||17,6|Giao diện ĐTV hiển thị list cuộc<br>gọi, ĐTV không được lựa chọn<br>cuộc gọi ra và theo quy định gọi<br>ra lần lượt theo danh sách||agent/thiết lập cuộc<br>gọi ra, ĐTV có thể<br>pick up trả lời cuộc<br>gọi.|agent/thiết lập cuộc gọi ra, ĐTV có thể pick up trả lời cuộc gọi.<br>- Hệ thống thiết lập cuộc gọi lần 1 nhưng không liên lạc được với KH, sau 30 phút, hệ thống<br>sẽ thiết lập cuộc gọi tới KH thêm 02 lần nữa, mỗi lần cách nhau 30 phút (kể từ lần gọi lại đầu<br>tiên). Như vậy, KH sẽ nhận được tối đa 03 cuộc gọi lại từ tổng đài. Nếu sau 03 lần kết nối, hệ<br>thống vẫn không liên lạc được với KH, Viettel sẽ tự động nhắn tin thông báo để mời KH thiết<br>lập lại lịch hẹn<br>Khi KH đặt lịch hẹn gọi lại thành công, hệ thống sẽ thiết lập thông tin đặt lịch của KH trong<br>queue chờ (hàng đợi) theo nguyên tắc như sau:<br>- Thiết lập cuộc gọi trong hàng đợi theo khung thời gian mà KH đặt lịch. Trường hợp 2 cuộc<br>gọi đặt lịch cùng 1 khung giờ thì KH nào đặt lịch trước sẽ được thiết lập trước.<br>- Trường hợp cùng 1 khung giờ, có quá nhiều lịch hẹn được thiết lập, hệ thống gọi lần lượt.<br>- Nếu KH không chọn khoảng giờ gọi lại, hệ thống sẽ thiết lập thời gian gần nhất, khi có<br>Agent rảnh sẽ kết nối ngay||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.61|Hệ thống kết nối không thành<br>công đến Khách hàng, do: Khách<br>hàng tắt máy, máy bận, không<br>nghe máy, từ chối cuộc gọi…|- Hệ thống thiết lập<br>cuộc gọi lần 1 nhưng<br>không liên lạc được<br>với KH, sau 30 phút,<br>hệ thống sẽ thiết lập<br>cuộc gọi tới KH<br>thêm 02 lần nữa, mỗi<br>lần cách nhau 30<br>phút (kể từ lần gọi lại<br>đầu tiên). Như vậy,<br>KH sẽ nhận được tối<br>đa 03 cuộc gọi lại từ<br>tổng đài. Nếu sau 03<br>lần kết nối, hệ thống<br>vẫn không liên lạc<br>được với KH, Viettel<br>sẽ tự động nhắn tin<br>thông báo để mời<br>KH thiết lập lại lịch<br>hẹn|- Hệ thống thiết lập cuộc gọi lần 1 nhưng không liên lạc được với KH, sau 30 phút, hệ thống<br>sẽ thiết lập cuộc gọi tới KH thêm 02 lần nữa, mỗi lần cách nhau 30 phút (kể từ lần gọi lại đầu<br>tiên). Như vậy, KH sẽ nhận được tối đa 03 cuộc gọi lại từ tổng đài. Nếu sau 03 lần kết nối, hệ<br>thống vẫn không liên lạc được với KH, Viettel sẽ tự động nhắn tin thông báo để mời KH thiết<br>lập lại lịch hẹn|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.62|Cơ chế gọi lại của hệ thống|Khi KH đặt lịch hẹn<br>gọi lại thành công, hệ<br>thống sẽ thiết lập<br>thông tin đặt lịch của<br>KH trong queue chờ<br>(hàng đợi) theo<br>nguyên tắc như sau:<br>- Thiết lập cuộc gọi<br>trong hàng đợi theo<br>khung thời gian mà<br>KH đặt lịch. Trường<br>hợp 2 cuộc gọi đặt<br>lịch cùng 1 khung<br>giờ thì KH nào đặt<br>lịch trước sẽ được<br>thiết lập trước.<br>- Trường hợp cùng 1<br>khung giờ, có quá<br>nhiều lịch hẹn được<br>thiết lập, hệ thống<br>gọi lần lượt.<br>- Nếu KH không<br>chọn khoảng giờ gọi<br>lại, hệ thống sẽ thiết<br>lập thời gian gần<br>nhất, khi có Agent<br>rảnh sẽ kết nối ngay|Khi KH đặt lịch hẹn gọi lại thành công, hệ thống sẽ thiết lập thông tin đặt lịch của KH trong<br>queue chờ (hàng đợi) theo nguyên tắc như sau:<br>- Thiết lập cuộc gọi trong hàng đợi theo khung thời gian mà KH đặt lịch. Trường hợp 2 cuộc<br>gọi đặt lịch cùng 1 khung giờ thì KH nào đặt lịch trước sẽ được thiết lập trước.<br>- Trường hợp cùng 1 khung giờ, có quá nhiều lịch hẹn được thiết lập, hệ thống gọi lần lượt.<br>- Nếu KH không chọn khoảng giờ gọi lại, hệ thống sẽ thiết lập thời gian gần nhất, khi có<br>Agent rảnh sẽ kết nối ngay|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.63||Sau 24h kể từ thời điểm KH đặt<br>lịch, hệ thống không kết nối<br>được với KH do không có Agent<br>rảnh||- Hệ thống sẽ tự động<br>nhắn tin tới KH để<br>thông báo với nội<br>dung như sau: “Xin<br>loi Quy khach, yeu<br>cau goi lai cua Quy<br>khach chua duoc<br>thuc hien. Nhan vien<br>CSKH Viettel se tiep<br>tuc goi lai trong vong<br>24h tiep theo. Tran<br>trong cam on.”. Alias<br>hiển thị:<br>CSKHVIETTEL|- Bổ sung tự động nhắn tin tới KH sau 24h kể từ thời điểm KH đặt lịch, hệ thống không kết<br>nối được với KH do không có Agent rảnh. Với nội dung thông báo như sau: “Xin loi Quy<br>khach, yeu cau goi lai cua Quy khach chua duoc thuc hien. Nhan vien CSKH Viettel se tiep<br>tuc goi lai trong vong 24h tiep theo. Tran trong cam on.”. Alias hiển thị: CSKHVIETTEL||
|17.64||Thống kê chi tiết cuộc gọi theo<br>ĐTV||Thống kê chi tiết<br>cuộc gọi ra trong<br>khoảng giờ cần thống<br>kê theo ĐTV|Thống kê chi tiết cuộc gọi ra trong khoảng giờ cần thống kê theo ĐTV||
|17.65||Thống kê chi tiết cuộc gọi theo<br>số điện thoại KH||Thống kê chi tiết<br>cuộc gọi ra trong<br>khoảng giờ cần thông<br>kê theo số thuê bao|Thống kê chi tiết cuộc gọi ra trong khoảng giờ cần thông kê theo số thuê bao||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.66|Bổ sung các chức năng survey<br>trên MyViettel|Theo y/c của OMNI,<br>tất cả các nghiệp vụ<br>sau khi KH thực hiện<br>sẽ được survey đánh<br>giá mức độ hài lòng.<br>Tuy nhiên còn 1 số<br>nghiệp vụ trên My<br>Viettel (Đăng ký<br>thông tin, mua sim,<br>chuẩn hóa ….) có<br>liên quan đến luồng<br>duyệt đơn hàng qua<br>videocall đang chưa<br>thực hiện được.<br>Nguyên nhân: Do<br>sau khi ĐTV kết thúc<br>cuộc gọi thì SDK của<br>videocall chưa trả ra<br>giá trị (đã hoàn<br>thành/chưa hoàn<br>thành) cho My<br>Viettel. Dẫn đến My<br>Viettel k biết để push<br>survey cho KH.<br>Yêu cầu nâng cấp:<br>Trong lần nâng cấp<br>SDK của video call<br>tới đây, anh bổ sung<br>thêm cho bên em<br>thông tin này để tích<br>hợp lại trên My<br>Viettel nhé.|Yêu cầu nâng cấp :<br>- Bổ sung nâng cấp SDK của video call đảm bảo được khi kết thúc cuộc gọi videocall thì trả<br>ra giá trị (đã hoàn thanh/chưa hoàn thành) cho MyViettel.<br>- MyViettel bổ sung tích hợp nhận diện giá trí nếu cuộc gọi videocall đã hoàn thành thì gửi<br>survey đánh giá mức độ hài lòng cho người dùng vừa kết thúc cuộc gọi videocall.<br>- Bổ sung khảo sát đánh giá mức độ hài lòng trên cá nghiệp vụ của MyViettel như (đăng ký<br>thông tin, mua sim, chuẩn hóa....) có liên quan đến luồng duyệt đơn hàng.|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||**Theo dõi thuê baoquấy rối**|||||
|17.67||Tra cứu lịch sử thuê bao bị chặn<br>vì quấy rối||1. Điều kiện chọn:<br>+ Chọn tool Quấy rối<br>+ Nhập số thuê bao<br>+ Khoảng thời gian<br>muốn tra cứu<br>* Cơ chế chặn QR tự<br>động:<br>+ Thống kê lịch sử<br>thuê bao, thời gian<br>chặn, nguyên nhân<br>chặn (system, hoặc<br>user chặn nếu bị chặn<br>thủ công)|1. Điều kiện chọn:<br>+ Chọn tool Quấy rối<br>+ Nhập số thuê bao<br>+ Khoảng thời gian muốn tra cứu<br>* Cơ chế chặn QR tự động:<br>+ Thống kê lịch sử thuê bao, thời gian chặn, nguyên nhân chặn (system, hoặc user chặn nếu<br>bị chặn thủ công)||
|17.68||Quản lý thuê bao quấy rối||1. Thống kê<br>+ Chọn tool Quấy rối<br>+ Ấn nút thống kê =><br>Hệ thống hiển thị<br>danh sách thuê bao<br>đang bị chặn trên hệ<br>thống gồm cả chặn tự<br>động và chặn thủ<br>công gồm số liệu: Số<br>thuê bao, thời gian<br>chặn, nguyên nhân<br>chặn (system, hoặc<br>user chặn nếu bị chặn<br>thủ công), nút tick để<br>tác động mở. Khi tác<br>động mở chiều hệ<br>thống có trường ghi<br>rõ nguyên nhân).<br>2. Tác động chặn<br>thuê bao quấyrối:|1. Thống kê<br>+ Chọn tool Quấy rối<br>+ Ấn nút thống kê => Hệ thống hiển thị danh sách thuê bao đang bị chặn trên hệ thống gồm<br>cả chặn tự động và chặn thủ công gồm số liệu: Số thuê bao, thời gian chặn, nguyên nhân chặn<br>(system, hoặc user chặn nếu bị chặn thủ công), nút tick để tác động mở. Khi tác động mở<br>chiều hệ thống có trường ghi rõ nguyên nhân).<br>2. Tác động chặn thuê bao quấy rối:<br>+ Chọn tool Quấy rối<br>+ Nhập số thuê bao + import danh sách (chặn/mở)<br>+ Ấn nút tác động chặn, Nhập trường: ghi rõ nguyên nhân chặn||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||+ Chọn tool Quấy rối<br>+ Nhập số thuê bao<br>+ Ấn nút tác động<br>chặn, Nhập trường:<br>ghi rõ nguyên nhân<br>chặn||
|17,69|Tính năng chặn quấy rối|Tình trạng KH quấy<br>rối hình ảnh liên tục<br>xảy ra ảnh hưởng đến<br>tâm lý ĐTV, chưa có<br>hướng xử KH không<br>có nhu cầu thực|Tình trạng KH quấy rối hình ảnh liên tục xảy ra ảnh hưởng đến tâm lý ĐTV, chưa có hướng<br>xử KH không có nhu cầu thực|
||**Nhắn tin**|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.70|nhắn tin cho Agent hoặc 1 nhóm<br>Agent|1. Điều kiện chọn:<br>+ Chọn tool**Nhắn**<br>**tin**<br>+ Ô nhập mã Agent,<br>hoặc danh sách<br>Agent<br>+ Ô chọn nhóm: Hệ<br>thống gom sẵn theo<br>nhóm ĐTV đã được<br>chia sẵn.<br>+ Ô nhập nội dung<br>tin nhắn => Nút gửi,<br>hiển thị Alias<br>+ Trường loại bỏ<br>thuê bao/ nhiều TB<br>ra khỏi danh sách<br>nhắn tin: Nhập số<br>thuê bao => Ấn thực<br>hiện<br>2. Kết quả:<br>+ Trưởng ca nhắn tin<br>thông báo đến nhóm<br>nhân sự ĐTV GS,<br>TC.. điều kiện là số<br>thuê bao đã được add<br>trên hệ thống, không<br>nhắn được các số<br>ngoài DS<br>+ Trưởng ca loại bỏ<br>các số thuê bao ra<br>khỏi danh sách nhắn<br>tin|- Bổ sung Popup cảnh báo IPCC cho Agent hoặc 1 nhóm Agent|
||**Thông tin agent**|||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.71||Tổng hợp thông tin tiếp nhận giải<br>đáp trong ca||ĐTV có thể nhìn<br>được tổng cuộc<br>gọi/phiên chát đã tiếp<br>nhận trong ca trực<br>đó, ví dụ: số cuộc gọi<br>được phục vụ, số<br>cuộc gọi rớt do KH,<br>số cuộc gọi rớt do<br>ĐTV, tổng thời gian<br>trả lời|ĐTV có thể nhìn được tổng cuộc gọi/phiên chát đã tiếp nhận trong ca trực đó, ví dụ: số cuộc<br>gọi được phục vụ, số cuộc gọi rớt do KH, số cuộc gọi rớt do ĐTV, tổng thời gian trả lời||
|||**Nhóm tính năng tiếp nhận giải**<br>**đáp dành cho NV CSKH**|||||
|17.72||Tiếpnhậncuộc gọi||Sau khi cuộc gọi kết<br>nối thành công với<br>NV CSKH, giao diện<br>tiếp nhận cuộc gọi<br>của NV<br>CSKH sẽ có các tính<br>năng sau: Pick up trả<br>lời cuộc gọi<br>vào/Cuộc gọi ra;<br>Hold máy; Mute<br>máy;<br>Tranfer cuộc gọi<br>sang Agent khác;<br>Bật/tắt hình ảnh phía<br>KH; Kết thúc cuộc<br>gọi.|Sau khi cuộc gọi kết nối thành công với NV CSKH, giao diện tiếp nhận cuộc gọi của NV<br>CSKH sẽ có các tính năng sau: Pick up trả lời cuộc gọi vào/Cuộc gọi ra; Hold máy; Mute<br>máy;<br>Tranfercuộc gọisangAgentkhác;Bật/tắthìnhảnhphíaKH;Kết thúc cuộc gọi.||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.73||Chuyển trạng thái Agent và<br>thông tin agent trong ca trực||Đây là tính năng cho<br>phép NV CSKH<br>chọn/chuyển các<br>trạng thái trong ca<br>trực. Trên hệ thống<br>có hiển thị thời lượng<br>của chế độ hiện tại,<br>cảnh báo đỏ khi quá<br>thời gian chế độ cho<br>phép.<br>Hệ thống sẽ có 08<br>trạng thái gồm:<br>Availble; Not<br>Availble; Availble -<br>No ACD; Meeting;<br>Typing; At lunch; No<br>Answer; Go out|Đây là tính năng cho phép NV CSKH chọn/chuyển các trạng thái trong ca trực. Trên hệ thống<br>có hiển thị thời lượng của chế độ hiện tại, cảnh báo đỏ khi quá thời gian chế độ cho phép.<br>Hệ thống sẽ có 08 trạng thái gồm: Availble; Not Availble; Availble - No ACD; Meeting;<br>Typing; At lunch; No Answer; Go out||
|17.74||Tính năng tương tác song song||Cho phép NV CSKH<br>sử dụng song song 2<br>tính năng để hỗ trợ<br>KH. Ví dụ: NV<br>CSKH tiếp nhận<br>cuộc gọi video, trong<br>quá trình tương tác,<br>NV CSKH có thể bật<br>thêm tính năng Chat<br>hoặc ngược lại|Cho phép NV CSKH sử dụng song song 2 tính năng để hỗ trợ KH. Ví dụ: NV CSKH tiếp<br>nhận<br>cuộc gọi video, trong quá trình tương tác, NV CSKH có thể bật thêm tính năng Chat hoặc<br>ngược lại||
|17.75||Gọi ra choKH||Tính năng này cho<br>phép NV CSKH thực<br>hiện cuộc gọi ra cho<br>KH từ hệ thống bằng<br>cách nhập<br>số điệnthoạicầngọi,|Tính năng này cho phép NV CSKH thực hiện cuộc gọi ra cho KH từ hệ thống bằng cách nhập<br>số điệnthoạicầngọi,nhấn nút gọi ra. Cuộc gọi ra sẽ được ghiâm||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||nhấn nút gọi ra. Cuộc<br>gọi ra sẽ được ghi âm|||
|17.76||Hủy lịch hẹn gọi lại khi KH yêu<br>cầu||NV CSKH có nút<br>bấm hủy lịch hẹn cho<br>KH.|NV CSKH có nút bấm hủy lịch hẹn cho KH.||
|17.77||Tổng hợp thông tin tiếp nhận giải<br>đáp||NV CSKH có thể<br>nhìn được tổng cuộc<br>gọi/phiên Chat đã<br>tiếp nhận trong ca<br>trực đó, ví dụ: số<br>cuộc gọi được phục<br>vụ, số cuộc gọi rớt<br>do KH, số cuộc gọi<br>rớt do NV CSKH,<br>tổng thời gian trả lời,<br>thời điểm đăng nhập,<br>tổng cuộc gọi đến,<br>tổng phiên Chat đến|NV CSKH có thể nhìn được tổng cuộc gọi/phiên Chat đã tiếp nhận trong ca trực đó, ví dụ: số<br>cuộc gọi được phục vụ, số cuộc gọi rớt do KH, số cuộc gọi rớt do NV CSKH, tổng thời gian<br>trả lời,<br>thời điểm đăng nhập, tổng cuộc gọi đến, tổng phiên Chat đến||
|||**Nhóm tính năng giám sát và**<br>**đánhgiá chất lượng.**|||||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.78||Giám sát chất lượng online||Tính năng này cho<br>phép giám sát nghe<br>online cuộc gọi<br>VideoCall (1 chiều/2<br>chiều/âm thanh),<br>cuộc gọi<br>Callmeback, xem<br>online phiên Chat và<br>tương tác với NV<br>CSKH và KH trong<br>cuộc gọi.<br>Giám sát có thể<br>online song song 1<br>cuộc gọi và nhiều<br>phiên Chat của các<br>NV CSKH khác<br>nhau|Tính năng này cho phép giám sát nghe online cuộc gọi VideoCall (1 chiều/2 chiều/âm thanh),<br>cuộc gọi Callmeback, xem online phiên Chat và tương tác với NV CSKH và KH trong cuộc<br>gọi.<br>Giám sát có thể online song song 1 cuộc gọi và nhiều phiên Chat của các NV CSKH khác<br>nhau||
|17.79||Giám sát chất lượng offline||Tính năng này cho<br>phép GS tìm kiếm,<br>nghe lại cuộc gọi,<br>xem lại phiên Chat,<br>xuất và lưu dữ liệu<br>chi tiết cuộc<br>gọi/phiên Chat|Tính năng này cho phép GS tìm kiếm, nghe lại cuộc gọi, xem lại phiên Chat, xuất và lưu dữ<br>liệu<br>chi tiết cuộc gọi/phiên Chat||
|17.80||Tính năng đánh giá chất lượng<br>giải đáp của NV CSKH, chất<br>lượng Giám sát viên:|||||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.81||Tính|năng điều hành ca trực.|Theo dõi chỉ số, số<br>liệu Online: cho phép<br>Trưởng ca theo dõi<br>trực tiếp tình trạng,<br>lưu lượng<br>tương tác vào tổng<br>đài, mức độ đáp ứng<br>để có quyết định điều<br>chỉnh nhân sự trong<br>ca, đảm<br>bảo hiệu quả tương<br>tác và chỉ số kết nối<br>toàn tổng đài|Theo dõi chỉ số, số liệu Online: cho phép Trưởng ca theo dõi trực tiếp tình trạng, lưu lượng<br>tương tác vào tổng đài, mức độ đáp ứng để có quyết định điều chỉnh nhân sự trong ca, đảm<br>bảo hiệu quả tương tác và chỉ số kết nối toàn tổng đài||
|17.82||Thống kê số liệu offline||tính năng cho phép<br>thống kê số liệu theo<br>các trường thời gian,<br>kênh<br>tương tác, Agent để<br>phục vụ cho công tác<br>báo cáo phân tích|tính năng cho phép thống kê số liệu theo các trường thời gian, kênh<br>tương tác, Agent để phục vụ cho công tác báo cáo phân tích||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.83||Tính|năng điềuhành khác|Chat: cho phép<br>trưởng ca Chat với<br>nhóm NV CSKH, GS<br>và Trưởng ca khác để<br>thông báo, đưa<br>tin nóng hoặc cảnh<br>báo nhân sự<br>Nhắn tin: cho phép<br>trưởng ca nhắn tin<br>theo số thuê bao đến<br>nhóm NV CSKH, GS<br>và Trưởng ca<br>khác để thông báo,<br>đưa tin nóng hoặc<br>cảnh báo nhân sự,<br>tính năng đảm bảo<br>đối với cả nhân sự<br>không<br>có ca trực.<br>Quản lý thuê bao<br>quấy rối: cho phép<br>trưởng ca theo dõi,<br>tác động chặn/ mở<br>thuê bao quấy rối<br>tổng đài.<br>Quản lý cuộc gọi ra<br>của NV CSKH: cho<br>phép quản lý cuộc<br>gọi ra của NV CSKH|Chat: cho phép trưởng ca Chat với nhóm NV CSKH, GS và Trưởng ca khác để thông báo,<br>đưa<br>tin nóng hoặc cảnh báo nhân sự<br>Nhắn tin: cho phép trưởng ca nhắn tin theo số thuê bao đến nhóm NV CSKH, GS và Trưởng<br>ca<br>khác để thông báo, đưa tin nóng hoặc cảnh báo nhân sự, tính năng đảm bảo đối với cả nhân<br>sự không<br>có ca trực.<br>Quản lý thuê bao quấy rối: cho phép trưởng ca theo dõi, tác động chặn/ mở thuê bao quấy rối<br>tổng đài.<br>Quản lý cuộc gọi ra của NV CSKH: cho phép quản lý cuộc gọi ra của NV CSKH||
|17.84||Dashboard|||Hiển thị các các thông tin giám sát. Call > 5min chưa có dữ liệu||
|17.85||Giám sát queue|||Hiển thị thông tin: Connecting, Avg call length, >5min, <30sec, waiting calls, available/<br>log_in agent||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17,86|Báo cáo kết nối||Bổ sungbáo cáo kết nối theo template mới|
|17.87|Báo cáo năngsuất agent||Bổ sungBáo cáo năngsuất agent theo template mới|
|17.88|Báo cáo trạngthái TVV||Bổ sungBáo cáo trạngthái TVV theo template mới|
|17.89|Báo cáo năng suất và trạng thái<br>agent||Bổ sung Báo cáo năng suất và trạng thái agent theo template mới|
|17.90|Tìm kiếm cuộc gọi||- Tìm kiếm theo khoảng thời gian bất kì<br>- Có nút download file ghi âm hoặc nghe trực tiếp, xem video cuộc gọi theo ứng dụng|
|17.91|Xuất file lịch sử cuộc gọi|1. Làm rõ cột: THỜI<br>LƯỢNG trên báo<br>cáo<br>2. BS thêm cột thời<br>gian hold<br>3. Cột nhiều đầu mục<br>tiếng anh|1. Làm rõ cột: THỜI LƯỢNG trên báo cáo<br>2. BS thêm cột thời gian hold<br>3. Cột nhiều đầu mục tiếng anh|
|17.92|Chi tiết tương tác các kênh Chat|1. Điều kiện chọn:<br>+ Chọn tool Chát<br>+ Ô nhập thời gian<br>cần search<br>2. Kết quả:<br>+ Xuất chi tiết theo<br>số thuê bao, ĐTV<br>tiếp nhận, thời lượng<br>từng tương tác, nội<br>dung chitiết|1. Bổ sung điều kiện chọn tìm kiếm:<br>+ Chọn tool Chát<br>+ Ô nhập thời gian cần search<br>2. Kết quả tìm kiếm bổ sung thêm các thông tin sau:<br>+ Xuất chi tiết theo số thuê bao, ĐTV tiếp nhận, thời lượng từng tương tác, nội dung chi tiết|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.93|Thống kê lịch sử gọi lại cho KH<br>theo lịch hẹn|1. Điều kiện chọn:<br>+ Chọn tool Call me<br>back<br>+ Ô nhập thời gian<br>cần search<br>2. Kết quả:<br>+ Xuất chi tiết theo<br>số thuê bao, ĐTV gọi<br>ra, thời lượng từng<br>tương tác, nội dung/<br>nhu cầu KH, số lần<br>gọi ra (tự động đếm<br>theo thuê bao)|1. Bổ sung điều kiện chọn tìm kiếm:<br>+ Chọn tool Call me back<br>+ Ô nhập thời gian cần search<br>2. Kết quả tìm kiếm bổ sung thêm các thông tin sau:<br>+ Xuất chi tiết theo số thuê bao, ĐTV gọi ra, thời lượng từng tương tác, nội dung/ nhu cầu<br>KH, số lần gọi ra (tự động đếm theo thuê bao)|
|17.94|Chi tiết tương tác theo các kênh<br>Video call|1. Điều kiện chọn:<br>+ Chọn kênh<br>+ Ô nhập thời gian<br>cần search<br>2. Kết quả:<br>+ Xuất chi tiết theo<br>kênh gồm: STB,<br>kênh, ngày, giờ, thời<br>lượng, trạng thái kết<br>thúc, phân biệt tương<br>tác có 2 kênh song<br>song|1. Bổ sung thêm điều kiện chọn tìm kiếm:<br>+ Chọn kênh<br>+ Ô nhập thời gian cần search<br>2. Kết quả tìm kiếm bổ sung thêm các thông tin sau:<br>+ Xuất chi tiết theo kênh gồm: STB, kênh, ngày, giờ, thời lượng, trạng thái kết thúc, phân biệt<br>tương tác có 2 kênh song song|
|17.95|Năng suất ĐTV|1. Điều kiện chọn:<br>+ Chọn kênh<br>+ Ô nhập thời gian<br>cần search<br>2. Kết quả:<br>+ ĐTV, Tổng năng<br>suất - Theo từng<br>kênh, Tổng thời gian<br>trả lời, Năng suất|- Bổ sung thêm điều kiện chọn tìm kiếm:<br>+ Chọn kênh<br>+ Ô nhập thời gian cần search<br>- Kết quả tìm kiếm bổ sung thêm các thông tin sau:<br>+ ĐTV, Tổng năng suất - Theo từng kênh, Tổng thời gian trả lời, Năng suất chuẩn, cảnh bảo<br>nhân sự không đạt năng suất|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||chuẩn, cảnh bảo nhân<br>sự không đạt năng<br>suất|||
|17,96||Báo cáo điểm trung bình nghiệp<br>vụ||Báo cáo điểm trung<br>bình nghiệp vụ<br>'- Cho phép xuất báo<br>cáo chi tiết điểm<br>trung bình nghiệp vụ<br>tháng  theo khu vực,<br>đối tác, phân lớp,<br>theo kênh, theo Giám<br>sát,  theo NV CSKH<br>và theo thời gian<br>(ngày, tuần, tháng,<br>quý, năm) theo biểu<br>mẫu 9_Báo cáo điểm<br>trung bình nghiệp vụ<br>Cách tính điểm trung<br>bình cuộc gọi: theo<br>quy định của thang<br>điểm đánh giá<br>NVCSKH|Báo cáo điểm trung bình nghiệp vụ||
|17,97||Báo cáo chất lượng giải đáp||Báo cáo chất lượng<br>giảiđáp|Bổ sung Báo cáo chất lượng giải đáp||
|17,98||Báo cáo chất lượng nhân sự||Báo cáo chất lượng<br>nhânsự|Bổ sung Báo cáo chất lượng nhân sự||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.99|Báo cáo tổng hợp dữ liệu đã<br>đánh giá theo NV CSKH|Báo cáo tổng hợp dữ<br>liệu đã đánh giá theo<br>NV CSKH|Bổ sung Báo cáo tổng hợp dữ liệu đã đánh giá theo NV CSKH|
|17.100|Cấu hình hệ thống|Cấu hình thang điểm<br>đánh giá<br>'- Hệ thống cho phép<br>người dùng khai báo,<br>sửa, xóa chỉ tiêu và<br>trọng số tương ứng<br>với từng đầu mục<br>trong khung giải đáp<br>và tỷ trọng theo<br>thang điểm áp dụng<br>hiện hành<br>- Hệ thống hiển thị<br>đầy đủ chức năng<br>sau: Dạng cuộc gọi/<br>đầu mục cuộc gọi/chỉ<br>tiêu đánh giá cuộc<br>gọi / nhóm lỗi /mức<br>độ lỗi / kênh giải<br>đáp.<br>Hệ thống cho phép<br>người dùng cấu hình<br>KI nhân sự: khai báo,<br>sửa, xóa công thức<br>tính KI nhân sự;<br>import dạng file các<br>tiêu chí  khác ngoài<br>điểm trung bình cuộc<br>gọi_ Biểu mẫu<br>12_file import KI<br>nhânsự|- Bổ sung Cấu hình thang điểm đánh giá<br>'- Hệ thống cho phép người dùng khai báo, sửa, xóa chỉ tiêu và trọng số tương ứng với từng<br>đầu mục trong khung giải đáp và tỷ trọng theo thang điểm áp dụng hiện hành<br>- Hệ thống hiển thị đầy đủ chức năng sau: Dạng cuộc gọi/ đầu mục cuộc gọi/chỉ tiêu đánh giá<br>cuộc gọi / nhóm lỗi /mức độ lỗi / kênh giải đáp.<br>Hệ thống cho phép người dùng cấu hình KI nhân sự: khai báo, sửa, xóa công thức tính KI<br>nhân sự; import dạng file các tiêu chí  khác ngoài điểm trung bình cuộc gọi_ Biểu mẫu<br>12_file import KI nhân sự|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.101||Báo cáo kết quả đánh giá chất<br>lượng giải đáp||Báo cáo kết quả đánh<br>giá chất lượng giải<br>đáp: ' - Cho phép<br>người dùng xuất chi<br>tiết kết quả dữ liệu<br>đánh giá online/<br>offline theo  Biểu<br>mẫu 4_báo cáo kết<br>quả dữ liệu đánh giá<br>-  Chỉ cho phép Giám<br>sát viên xuất được dữ<br>liệu đã đánh giá của<br>chính mình<br>- Kiểm định 1 xuất<br>được dữ liệu đã đánh<br>giá của tất cả giám<br>sát viên|- Điều chỉnh nâng cấp báo cáo kết quả đánh giá chất lượng giải đáp theo biểu mẫu mới (bổ<br>sung thay đổi các tiếu chí và dữ liệu hiển thị)||
|||**Đánhgiá**|||||
|17.102||Lọc dữ liệu đánh giá||Lọc dữ liệu đánh giá<br>theo điều kiện lọc<br>- Cho phép người<br>dùng lọc dữ liệu<br>đánh giá theo các<br>điều kiện sau: thời<br>lượng phiên tương<br>tác, theo danh sách<br>NV CSKH, theo đối<br>tác, theo khoảng thời<br>gian . Kết quả lọc sẽ<br>đẩy về cho Giám sát<br>quản lý.<br>- Cho phép người<br>dùng lọc dữ liệu<br>đánhgiá theofile dữ|- Bổ sung tiêu chí Lọc dữ liệu đánh giá:<br>..||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|||||liệu dưới dạng<br>import file dữ  liệu (<br>Biểu mẫu 2), kết quả<br>lọc sẽ đẩy về cho<br>giám sát quản lý|||
|17.103||Đánh giá chất lượng giải đáp||Đánh giá offline/<br>Online chất lượng<br>giải đáp|- Đánh giá chất lượng giải đáp bổ sung điều chỉnh lại theo PYC||

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|TD442|
|---|---|---|---|---|---|---|
||||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|||Lần ban hành: 1|
||||||||
||**TT**||**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**||
||**1**|**Tiền**|**xử lý khi vào IVR**||||
|17.104||Kiểm định và báo cáo dữ liệu đã<br>đánh giá||Kiểm định lần 1 (<br>Kiểm định ==> Giám<br>sát)<br>' - Cho phép người<br>dùng được cấp quyền<br>kiểm định 1 có quyền<br>đánh giá chất lượng<br>chấm điểm của giám<br>sát viên:  sửa toàn bộ<br>phần đánh giá của<br>Giám sát đã đánh giá<br>dữ liệu đó. Kết quả<br>của dữ liệu kiểm<br>định 1 đánh giá sẽ<br>thay thế kết quả của<br>Giám sát.<br>- Các điều kiện tìm<br>kiếm dữ liệu kiểm<br>định:  thời gian,<br>Giám sát, NV<br>CSKH, số điện thoại<br>của Khách hàng gọi<br>lên, đối tác,  ngưỡng<br>xếp loại của cuộc gọi<br>( dữ liệu tìm kiếm<br>này không cần chọn<br>đầy đủ các điều kiện)|Kiểm định và báo cáo dữ liệu đã đánh giá||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.105|Kiểm định 2 dữ liệu đã đánh giá|Kiểm định lần 2<br>(Kiểm định lần2<br>==> Kiểm định lần 1<br>==> Giám sát)<br>'- Cho phép người<br>dùng được cấp quyền<br>kiểm định 2 có quyền<br>đánh giá chất lượng<br>chấm điểm của kiểm<br>định 1: sửa toàn bộ<br>phần đánh giá của<br>Kiểm định lần 1<br>đồng thời sửa được<br>đánh giá của Giám<br>sát dữ liệu đó. Kết<br>quả dữ liệu của kiểm<br>định 2 sẽ thay thế kết<br>quả đánh giá của<br>kiểm định 1/ giám sát<br>đã đánh giá trước đó<br>-  Các điều kiện tìm<br>kiếm dữ liệu để kiểm<br>định 2:  thời gian, tài<br>khoản của kiểm định<br>lần 1, tài khoản của<br>Giám sát, NV<br>CSKH, số điện thoại<br>của Khách hàng gọi<br>lên, theo đối tác, theo<br>ngưỡng xếp loại của<br>cuộc gọi, theo lỗi<br>đánh giá của kiểm<br>định lần 1 với Giám<br>sát|<br>Kiểm định 2 dữ liệu đã đánh giá|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|||+ Cho phép tra cứu<br>và xuất cuộc gọi<br>chưa chấm/đã<br>chấm/cuộc gọi lỗi<br>theo đơn vị đối tác,<br>theo Giám sát, NV<br>CSKH, số điện thoại<br>của Khách hàng gọi<br>lên. Đồng thời trong<br>quá trình tra cứu<br>xong có thể thực hiện<br>sửa, khôi phục cuộc<br>gọi theo yêu cầu (lưu<br>ý: khôi phục chỉ<br>dùng khi Giám sát<br>tích bỏ sai cuộc gọi<br>lỗi).||
||**Giám sát Online**|||

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD442|
|---|---|---|
||**TỔNG HỢP KHẢO SÁT HỆ THỐNG IPPC**|Lần ban hành: 1|

|**TT**|**Tên tính năng**|**Mô tả của khách**<br>**hàng**|**Làm rõ yêu cầu**|
|---|---|---|---|
|**1**|**Tiền xử lý khi vào IVR**|||
|17.106|Online nhiều tương tác cùng lúc|Cho phép Giám sát<br>Online cùng lúc 1<br>ĐTV Video và nhiều<br>ĐTV Chat|- Cho phép giám sát online theo nhóm<br>- Video: Cho phép nghe/nhìn cuộc đàm thoại<br>- Chat: Cho phép đọc cuộc hội thoại|
||**Điều hành Online**|||
|17.107|Gán queue cho nhiều ĐTV cùng<br>lúc|1. Điều kiện chọn:<br>+ Chọn kênh cần gán<br>ĐTV<br>+ Chọn ô nhập mã<br>ĐTV có thể nhập<br>nhiều mã ĐTV<br>+ Ô đính kèm danh<br>sách ĐTV cần gán<br>+ Ô nhập thời gian<br>chuyển queue<br>2. Kết quả: ĐTV sẽ<br>được gán sang queue<br>mới khi thao tác<br>hoàn thành, hệ thống<br>định tuyến vào các<br>agent này.|1. Điều kiện chọn:<br>+ Chọn kênh cần gán ĐTV<br>+ Chọn ô nhập mã ĐTV có thể nhập nhiều mã ĐTV<br>+ Ô đính kèm danh sách ĐTV cần gán<br>+ Ô nhập thời gian chuyển queue<br>2. Kết quả: ĐTV sẽ được gán sang queue mới khi thao tác hoàn thành, hệ thống định tuyến<br>vào các agent này.|