Public 610 

**VIETTEL AI RACE HƯỚNG DẪN KIỂM TRA BẢO TRÌ BẢO DƯỠNG HỆ THỐNG MẠNG** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

## **1. Bảo trì bảo dưỡng thiết bị** 

## **1.1 Lên lịch rà soát, bảo dưỡng thiết bị mạng** 

- ✓ Bảo dưỡng thiết bị theo tháng 

- Tần suất: 1 lần/tháng. 

**==> picture [64 x 89] intentionally omitted <==**

- Nội dung thực hiện: Rà soát và xóa các cảnh báo lỗi tồn, khai báo rác. 

- Backup dữ liệu hệ thống (database/ file cấu hình) ra server ngoài và ra đĩa quang hoặc USB nếu có. 

- Với thiết bị tại tổng trạm khu vực/ quốc gia: vệ sinh tại nơi đặt thiết bị và quanh khu vực đặt thiết bị, trên sàn và dưới sàn phòng máy tổng trạm khu vực/quốc gia. 

- ✓ Bảo dưỡng thiết bị theo quý. 

- Tần suất: 1 lần/quý/3 tháng 

- Rà soát và xóa các logfile, file database cũ, các file rác trên thiết bị lưu trữ. 

- Cập nhật thời gian hệ thống, trạng thái đồng bộ (nếu có sai khác). 

- Với thiết bị tại tổng trạm khu vực/quốc gia: kiểm tra và siết lại các cáp kết nối (nguồn/ tín hiệu/ nối đất/...), bulong, ốc-vít bị hỏng,... đảm bảo chắc chắn; bó buộc các loại cáp (nguồn, tín hiệu) nếu đang không gọn gàng. 

- ✓ Bảo dưỡng thiết bị theo 06 tháng 

- Tần suất: 6 tháng/lần 

- Audit các hệ thống thuộc lớp mạng lõi, hội tụ và cập nhật tham số theo bộ tham số chuẩn (nếu có sai khác) 

- Switchover các cặp thiết bị có dự phòng active/standby: 

   - +  Các cặp card/module điều khiển, chuyển mạch active/standby thuộc các thiết bị chuyển mạch, định tuyến trung tâm của mạng (các thiết bị lớp Core và Distribute) 

   - + Trong trường hợp 6 tháng đã có tác động dẫn đến switchover cho thiết 

   - bị active/standby thì coi như đã thực hiện switchover đinh kỳ, và tính chu kỳ mới bắt đầu từ thời điểm switchover thiết bị lần trước đó. 

- ✓ Bảo dưỡng thiết bị theo năm 

- Tần suất: 1 lần/năm. 

- Switchover các phần tử kết nối có dự phòng active/standby standby: + Thiết bị mạng: switchover các cặp node active/standby trên mạng. 

   - + Trường hợp trong 1 năm đã có tác động dẫn đến switchover cho các node active/standby thì coi như đã thực hiện switchover định kỳ, và tính chu kỳ mới bắt đầu từ thời điểm switchover node. 

## **1.2 Hướng dẫn switchover thiết bị mạng** 
**VIETTEL AI RACE** Public 610 **HƯỚNG DẪN KIỂM TRA BẢO TRÌ BẢO DƯỠNG HỆ THỐNG MẠNG** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

**==> picture [477 x 650] intentionally omitted <==**

**----- Start of picture text -----**<br>
Loại  Lớp thiết<br>STT  Hãng  Các bước thực hiện<br>thiết bị  bị<br>1. Backup cấu hình thiết bị trước khi thực<br>hiện<br>2. Log vào thiết bị kiểm tra trang thái hoat<br>động của card SUP (SUPERVISOR),<br>xem card SUP nào đang là active, card<br>SUP nào đang là standby show mô-đun<br>3. Thực hiện lấy thông tin route, trạng thái<br>các phiên BGP và OSPF để so sánh sau<br>khi thực hiện switchover<br>4. Đứng trên thiết bị đang có card SUP ở<br>1  N9K  Cisco  Core<br>trạng thái active, thực hiện switchover<br>sang card SUP standy làm active<br>-<br>Ngắt nguồn card SUP active để<br>switchover sang card SUP standby để<br>card standby chuyển sang trạng thái<br>Sactive.<br>#poweroff module "số lượng module<br>đang hoạt động"<br>-<br>Card SUP standby chuyển lên làm active,<br>thực hiện show module để kiểm tra lại.<br>-<br>Cấp nguồn lại cho card Standby vừa ngắt<br>để làm dự phòng.<br>1. 1. Backup cấu hình thiết bị trước khi thực<br>hiên<br>2. Login vào thiết bị kiểm tra trạng thái<br>hoạt động và xem card RP (route<br>2  NCS560 Cisco  Core  processor) nào đang là active, RP nào<br>đang là standby. Hiển thị ngay khi login<br>vào thiết bị #show platform<br>#show redundancy<br>Để lấy thông tin RP active-standby chi<br>tiết trên cặp thiết bị switchover<br>**----- End of picture text -----**<br>
**VIETTEL AI RACE** Public 610 **HƯỚNG DẪN KIỂM TRA BẢO TRÌ BẢO DƯỠNG HỆ THỐNG MẠNG** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

**==> picture [477 x 644] intentionally omitted <==**

**----- Start of picture text -----**<br>
3. Thực hiện lấy thông tin route, trạng thái<br>các phiên BGP và OSPF để so sánh sau<br>khi thực hiện switchover<br>4. Xác định được RP nào đang là active, RP<br>nào đang là standby<br>-<br>Đứng trên thiết bị, chuyển card active<br>sang standby và kiểm tra<br>#redundancy switchover #show platform<br>-<br>Card RP standby chuyển lên làm active<br>#show platform #show redundancy để<br>kiểm tra lại trạng thái active-standby trên<br>card RP<br>1. 1. Backup cấu hình thiết bị trước khi thực<br>hiện.<br>2. Login vào thiết bị kiểm tra trạng thái<br>hoạt động của thiết bị và xem card RSP<br>(route switch processors) nào đang là<br>active, RSP nào đang là standby. Hiên thị<br>ngay khi login vào thiết bị #show<br>platform #show redundancy<br>Để lấy thông tin RSP active-standby chi<br>tiết trên cặp thiết bị switchover<br>3  ASR9K  Cisco  Core  3. Thực hiện lấy thông tin route, trạng thái<br>các phiên BGP và OSPF để so sánh sau<br>khi thực hiện switchover<br>4. Xác định được RSP nào đang là active,<br>RSP nào đang là standby<br>-<br>Đứng trên thiết bị, chuyển card active<br>sang standby và kiểm tra # edundancy<br>switchover<br>5. Card RSP standby chuyển lên làm active,<br>thực hiện #show platform #show<br>redundancy để kiểm tra lại trạng thái<br>active-standby trên card RSP<br>**----- End of picture text -----**<br>
Public 610 

**VIETTEL AI RACE** 

**HƯỚNG DẪN KIỂM TRA BẢO TRÌ BẢO DƯỠNG HỆ THỐNG MẠNG** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

**==> picture [477 x 635] intentionally omitted <==**

**----- Start of picture text -----**<br>
1. Login vào thiêt bị kiêm tra trạng thái<br>hoạt động của thiết bị và trạng thái của<br>RE.<br>#show chassis hardware<br>Các  #show system switchover<br>#request chassis routing-engine master<br>dòng<br>thiết bị  switch check<br>Juniper  2. Thực hiện lấy thông tin route, trạng<br>hỗ trợ<br>thái các phiên BGP và OSPF để so sánh<br>4  RE  Juniper Core<br>sau khi thực hiện switchover<br>(Routing<br>3. Tiến hành rút nguồn chassis RE<br>Engine)<br>primary, thiết bị switchover sang RE<br>backup hoặc thực hiện câu lệnh #system<br>switchover<br>Sau khi switchover, thiết bị Backup trước<br>đó chuyển lên làm Primary.<br>4. Kiểm tra trạng thái các kết nối qua<br>thiết bị<br>1. Đối với các cặp switch DS chạy các giao<br>thức dự phòng VRRP, HSRP,...<br>Với trường hợp sử dụng giao thức<br>VRRP.<br>Các<br>1.1. Thực hiện lật mặt trạng thái<br>switch  VRRP từ thiết bị Master sang<br>dòng  Backup, xác định thiết bị  nào<br>Cisco hỗ<br>5  Cisco  Distritube  đang là master<br>trợ giao  1.2. Thực hiện shutdown các uplink từ<br>thức  iết bị Master lên CR để switchover<br>VRRP,  các vlan chạy trên thiết bị Master<br>HRRP  sang thiết bị Backup. Kiểm tra<br>trạng thái các vlan chạy trên thiết<br>bị Backup. Lúc này thiết bị<br>Backup sẽ thành Master.<br>#show vrrp brief<br>**----- End of picture text -----**<br>
Public 610 

**VIETTEL AI RACE** 

**HƯỚNG DẪN KIỂM TRA BẢO TRÌ BẢO DƯỠNG HỆ THỐNG MẠNG** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

   - 1.3. Mở lại các port vừa shutdown trên thiết bị Master cũ để trạng thái vrrp về Backup 

2. Với trường hợp sử dụng giao thức HSRP 

   - 2.1. Thực hiện lật mặt trạng thái HSRP từ thiết bị Active sang thiết bị Standby, xác định thiết bị nào đang chạy là thiết bị Active trước. 

   - 2.2. Thực hiên shutdown các uplink của thiết bị Active, hoặc rút nguồn thiết bị Active traffic đổ qua thiết bị Standby, lúc này các route ảo sẽ được chuyến sang thiết bị Standby để chuyển tiếp dữ liệu. 2.3. Kiểm tra trạng thái thiết bị Standby #show stanby 

**==> picture [156 x 49] intentionally omitted <==**

- 2.4. Mở lại các port vừa shutdown hoặc cấp nguồn lại cho thiết bị. Lúc này thiết nào có priority lớn hơn thì thiết bị đó sẽ là thiết bị Active và ngược lại. 

## **1.3 Kiểm tra và vệ sinh hệ thống làm mát** 

   - Kiểm tra quạt tản nhiệt: Kiểm tra xem tất cả các quạt trên CPU, GPU, nguồn, và vỏ thiết bị có hoạt động bình thường không. Nghe kỹ xem có mạnh có thể chỉ ra quạt tiếng ồn bất thường không (tiếng gầm hoặc rung 4 bị hỏng hoặc mất cân bằng). 

   - Nếu phát hiện quạt hoạt động kém hiệu quả, quá ồn hoặc không hoạt động, hãy thay thế chúng ngay lập tức. 

- **1.4 Kiểm tra và vệ sinh lỗ thông gió và bộ lọc khí** 

   - Kiểm tra các lỗ thông gió của thiêtt bị, đảm bảo không có bụi bẩn hoặc các Kiểm tra các lỗ thông gió của thiết bị, đảm bảo vật thể lạ gây cản trở luồng không khí. 

   - Nếu thiết bị sử dụng bộ lọc không khí, vệ sinh hoặc thay thế bộ lọc thường xuyên. Bộ lọc không khí có thể bị tắc nghẽn bụi bẩn, khiến quạt phải làm việc với cường độ cao hơn, từ từ đó làm tăng nhiệt độ của thiết bị. 

## **1.5 Lên kế hoạch bảo trì định kỳ hệ thống làm mát** 
**VIETTEL AI RACE** Public 610 **HƯỚNG DẪN KIỂM TRA BẢO TRÌ** Lần ban hành: 1 **BẢO DƯỠNG HỆ THỐNG MẠNG** 

**==> picture [39 x 47] intentionally omitted <==**

- Kiểm tra hàng tháng: Thực hiện kiểm tra hàng tháng các quạt và hệ thống làm mát của thiết bị. Đảm bảo không có dấu hiệu bất thường nào xảy ra và nhiệt độ của các thành phần luôn ổn định. 

- Bảo dưỡng hàng quý: Thực hiện vệ sinh định kỳ hệ thống làm mát hàng quý, bao gồm làm sạch quạt, lỗ thông gió,... 

- Bảo trì hệ thống điều hòa không khí hàng năm: Định kỳ bảo trì hệ thống điều hòa không khí, đảm bảo chúng hoạt động hiệu quả để hỗ trợ làm mát cho toàn bộ hệ thống. 

## **2. Vệ sinh và bảo trì vật lý** 

## **2.1 Vệ sinh bên ngoài thiết bị** 

Làm sạch vỏ ngoài của thiết bị: Sử dụng khăn mềm hoặc các chất liệu không dẫn điện để lau sạch vỏ ngoài, tránh làm hư hỏng hoặc trầy xước. Bụi bẩn có thể tích tụ trên bề mặt và dẫn đến các vấn đề về tản nhiệt hoặc ảnh hưởng đến hiệu suất. 

Kiểm tra cổng kết nối và khe cắm: Các cổng kết nối như USB, Ethernet, và các khe cắm mở rộng có thể bị oxy hóa hoặc hư hỏng sau thời gian dài sử dụng. Kiểm tra xem các cổng này có bị rỉ sét hoặc hư hại không, đồng thời làm sạch bằng dung dịch chuyên dụng nếu cần. 

## **2.2 Kiểm tra và vệ sinh các cổng kết nối vật lý** 

Kiểm tra tình trạng cáp: Các cáp kết nối nguồn và dữ liệu cần được kiểm tra định kỳ. Đảm bảo chúng không bị gấp khúc, đứt hoặc quá căng, điều này có thể gây ra sự cố cho hệ thống. 

Kiểm tra các cổng kết nối: Đảm bảo các cổng kết nối giữa thiết bị và các thiết bị ngoại vi không bị lỏng lẻo. Nếu phát hiện cổng bị mòn, cần thay thế hoặc sửa chữa kịp thời để tránh mất kết nối. 

## **3. Bảo trì hệ thống cáp và kết nối mạng** 

## **3.1 Kiểm tra hệ thống cáp mạng** 

Kiểm tra cáp mạng Ethernet: Cáp Ethernet là xương sống của hệ thống mạng. Bạn cần kiểm tra các dây cáp xem có dấu hiệu bị mòn, đứt hoặc gấp khúc không. Nếu cáp bị hỏng, hãy thay thế bằng cáp mới đạt tiêu chuẩn Cat5e, Cat6 hoặc cao hơn tùy nhu cầu sử dụng. 

Kiểm tra cáp quang (fiber optic): Nếu sử dụng kết nối quang, cần kiểm tra định kỳ các dây cáp quang để đảm bảo không có hiện tượng đứt gãy hoặc suy giảm tín 
**VIETTEL AI RACE** Public 610 **HƯỚNG DẪN KIỂM TRA BẢO TRÌ** Lần ban hành: 1 **BẢO DƯỠNG HỆ THỐNG MẠNG** 

**==> picture [39 x 47] intentionally omitted <==**

hiệu. Các kết nối quang cần được giữ sạch sẽ để tránh ảnh hưởng đến chất lượng truyền tải. 

Đảm bảo quản lý cáp tốt: Cáp mạng cần cần được quản lý một cách gọn gàng và khoa học, tránh việc gấp khúc hoặc kéo căng quá mức. Điều này giúp duy trì trì hiệu suất của mạng và giảm thiểu rủi ro hỏng hóc. 

## **3.2 Kiểm tra tình trạng hoạt động của cổng mạng:** 

Bị hư hại sau thời gian dài sử dụng. Hãy đảm bảo rằng các cổng mạng hoạt động ổn định và không có sự cố như mất kết nối hay giảm băng thông. 

**4. Kiểm tra và bảo trì hệ thống giá đỡ và bố trí thiết bị** 

- **4.1 Kiểm tra và quản lý hệ thống giá đỡ (rack)** 

   - Đảm bảo sự chắc chắn của thiết bị trong giá đỡ: Các thiết bị cần được gắn chắc chắn vào hệ thống giá đỡ để tránh rung lắc hoặc di chuyển không mong muốn, có thể gây ảnh hưởng đến các kết nối và hoạt động của thiết bị. Sử dụng ốc vít hoặc kẹp chặt để đảm bảo sự ổn định. 

   - Quản lý cáp trong giá đỡ: Cáp nguồn và cáp mạng cần được bố trí gọn gàng trong giá đỡ để tránh cản trở hoặc gây khó khăn khi bảo trì. Bạn nên sử dụng các phụ kiện quản lý cáp như dây rút, khay cáp hoặc tấm chắn cáp để giữ cáp gọn gàng và dễ quản lý. 

## **4.2 Kiểm tra bố trí các thiết bị** 

- Bố trí thiết bị khoa học: Các thiết bị trong giá đỡ cần được bố trí sao cho đảm bảo luồng không khí tản nhiệt hiệu quả. Tránh đặt các thiết bị quá sát nhau hoặc chặn luồng khí giữa các thiết bị. 

- Dễ dàng tiếp cận các thiết bị: Khí bố trí các thiết bị trong phòng server, bạn cần đảm bảo rằng tất cả các thiết bị có thể dễ dàng tiếp cận để thực hiện kiểm tra và bảo trì. Điều này giúp giảm thời gian bảo trì và đảm bảo rằng hệ thống luôn hoạt hoạt động liên tục. 

**==> picture [192 x 116] intentionally omitted <==**