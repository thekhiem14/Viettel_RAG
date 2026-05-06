**VIETTEL AI RACE** TD566 **RCE** Lần ban hành: 1 

**==> picture [39 x 46] intentionally omitted <==**

## **1. Định cấu hình cho RCE** 

Cấu hình cơ bản nhất của RCE được nêu ở hình vẽ 2. Với cấu hình này, thiết bị RCE được sử dụng để KSVKL điều khiển một tần số đơn (VHF hoặc UHF). Trong cấu hình này, các máy phát và máy thu được đặt cùng nhau. Một RCE sẽ đưa ra 02 giao tiếp trung kế (trunk), trunk A thường được nối với đường truyền mặt đất (cáp quang, Viba...) và trunk B được nối với đường truyền dự phòng mặt đất hoặc vệ tinh. 

Khi khởi động, các RCE sẽ bắt đầu từ trunk A, nếu đường này tốt sẽ hoạt động bình thường. Nếu trunk A hỏng, RCE sẽ chuyển sang trunk B (trong vòng 15-30s). RCE ở đầu xa nhận được tín hiệu trên đầu vào trunk B sẽ tự chuyển sang trunk B, hai RCE sẽ bắt đầu các thủ tục đồng bộ và bắt ta làm việc cùng nhau. Tại đầu điều khiển, 6 tín hiệu vào (PTT Main, PTT Standby, Tx Main/Standby, Rx Main/Standby, Rx Mute, Remote Over-ride) có thể được đưa vào RCE. Tại đầu xa, các tín hiệu điều khiển tương ứng (PTT Main, PTT Standby, Tx Main/Standby, Rx Main/Standby, Rx Mute, Remote Over-ride) sẽ sẵn sàng để đưa vào hoạt động. các tín hiệu vào này sử dụng opto-coupler và được kích hoạt bởi một công tắc chập nhả ở ngoài. Nếu các tín hiệu confirm ngoài không sẵn sàng có thể sử dụng cá tín hiệu nội tại của RCE (xem phần cài đặt DIP-Switch). Tại đầu điều khiển, các tín hiệu vào (PTT Main Confirm, PTT Standby Confirm, Tx Main/Standby Confirm, Rx Main/Standby Confirm, Rx Mute Main, Rx Mute Standby) ở dạng công tác chập nhả. 

## **2. Yêu cầu về nguồn cung cấp** 

Thiết bị RCE chế tạo để hoạt động với nguồn AC từ 100 đến 265 V, 47-63 Hz, và/hoặc nguồn DC +24V. Yêu cầu về nguồn cụ thể như trong bảng dưới đây. Khi hoạt động với nguồn AC, nguồn DC có thể sử dụng như nguồn dự phòng. Không cần bất cứ điều chỉnh nào với nguồn cung cấp trong dải cho phép cấp vào máy. Trong điều kiện nguồn điện không ổn định, khuyến cáo dùng thiết bị ổn áp hoặc UPS để bảo vệ thiết bị. 

**==> picture [39 x 46] intentionally omitted <==**

||**VIETTEL AI RACE**|TD566|
|---|---|---|
||**RCE**|Lần ban hành: 1|

**==> picture [460 x 250] intentionally omitted <==**

Hình 1. Cấu hình hoạt động cơ bản của RCE 

Bảng 1. Yêu cầu về nguồn cho RCE 

|Stt|Điện áp|Dòng thông thường|Dòng cực đại|
|---|---|---|---|
|1|+24 VDC|1.0 A|1.5 A|
|2|110 VAC|0.375 A|0.50 A|
|3|230 VAC|0.200 A|0.250|

## **3. Sơ đồ chân giao tiếp** 

Tất cả các giao tiếp vào/ra được đưa ra chân cắm 25 đôi phía sau máy. Hình vẽ 3 mô tả mặt sau RCE với tất cả các đầu giắc cắm. 

**==> picture [496 x 71] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|TD571|
||**CẤU HÌNH KHAI THÁC VÀ BẢO TRÌ**<br>**THIẾT BỊ ĐIỀU KHIỂN XA VHF**|Lần ban hành: 1|

Bảng 2. Sơ đồ chân nguồn DC J6 (5-Pin Circular DIN) 

|Bảng2. Sơ đồ chân nguồn DC|J6 (5-PinCircular DIN)|
|---|---|
|Tên chân|Điện áp|
|Chân 1 và 2|DC Ground/RTN|
|Chân 3|+5 VDC|
|Chân 4|-12 VDC|
|Chân 5|+12 VDC|

Chú ý: Không được nối tắt bất cứ chân nào trên đây. Giắc này chỉ cho phép cấp nguồn vào thiết bị. 

Bảng 3. Chân nguồn TB1 

|Bảng3. Chân nguồn TB1||
|---|---|
|Tên chân|Điện áp<br>|
|Chân 1|Đầu vào +24 VDC Input|
|Chân 2|Ground Return Single Point Ground|
|Chân 3|RCE Fault (Active Low, Open Collector<br>Output)|
|Chân 4|Multi-point Ground(Rack Ground)|

**==> picture [34 x 51] intentionally omitted <==**

## **4. Quy trình cài đặt** 

- Tháo vỏ thiết bị một cách cần thận, tuân thủ các yêu cầu về tĩnh điện. 

- Kiểm tra cẩn thận các chân cắm phía sau (XA1-XA3) để đảm bảo không có chân nào bị cong và bị nối chập nhau. 

- Trượt thiết bị lên rack từ phía trước mặt và vặn chặt 04 ốc phía trước. 

- Đặt các switch và các jumper theo đúng ứng dụng cần dùng. 

- Cắm các giắc tín hiệu vào/ra cho RCE. (xem các bảng 1-4 các hình vẽ 2- 6 cho 

- Kết nối nguồn cung cấp chặt chẽ cho RCE 

- Dùng trói cáp để cố định các cáp nguồn và cáp tín hiệu vào phía sau rack máy. 

- Kết nối đất cho thiết bị, yêu cầu dùng dây dẫn kích thước 12-16 AWG nối với điểm tiếp mát của các rack máy và toà nhà. 

- Nối chân 4 của TB-1 vào điểm GND để đảm bảo chống nhiễu. 

- Kiểm tra cẩn thận nguồn cung cấp cho thiết bị trước khi bật nguồn. 

- Khi thiết bị khởi tạo, đèn Status sẽ nháy vàng trong vài giây, sau đó sẽ nháy xanh với tốc độ nhanh để bắt đầu tìm đồng bộ. 

- Nếu thiết bị đầu xa cũng hoạt động tốt, hai đầu sẽ bắt tay tại trunk A trước, khi đó đèn LED SYN A sẽ nháy sáng xanh. Việc này sẽ diễn ra trong 1030 giây tuỳ thuộc vào điều kiện đường truyền, khi hai thiết bị bắt tay thành 

**==> picture [92 x 35] intentionally omitted <==**
**==> picture [39 x 47] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|TD571|
||**CẤU HÌNH KHAI THÁC VÀ BẢO TRÌ**<br>**THIẾT BỊ ĐIỀU KHIỂN XA VHF**|Lần ban hành: 1|

công, đèn SYN A sẽ sáng cố định. Đèn Status sẽ nháy sáng chậm (1 giây/lần) 

- Nếu trunk A lỗi, thiết bị RCE đầu gần sẽ chuyển sang trunk B để tìm đồng bộ, RCE đầu xa cũng chuyển theo. khi đó đèn LED SYN B sẽ nháy sáng xanh. Việc này sẽ diễn ra trong 10-30 giây tuỳ thuộc vào điều kiện đường truyền, khi hai thiết bị bắt tay thành công, đèn SYN B sẽ sáng cố định. 

- Nếu vì một lý do nào đó thiết bị không hoạt động đúng, reset RCE bằng cách ấn nút RESET tại mặt trước. 

- Nếu chưa khắc phục được, kiểm tra lại card xử lý và bật nguồn. 

- Nếu thiết bị hoạt động tốt, vặn chặt 3 vít nhỏ tại mặt trước và không được nới lỏng 3 vít này trong quá trình hoạt động. 

- Thiết bị sẵn sàng cho hoạt động. 

## **5. Quy trình kiểm tra** 

Thiết bị RCE kết nối với nhau thông qua đường truyền và kết nối với VCCS, máy thu phát ở mỗi đầu. Để kiểm tra tình trạng hoạt động, tuân theo các bước sau: 

- Kiểm tra mức âm tần thu và phát ở 2 đầu cho phù hợp toàn hệ thống. 

**==> picture [34 x 51] intentionally omitted <==**

- Kiểm tra tình trạng tín hiệu PTT và âm tần phát tại đầu xa. 

- Kiểm tra tín hiệu PTT Confirmation tại đầu điều khiển (nếu hệ thống được đấu nối để sử dụng tính năng này). 

- Kiểm tra tín hiệu điều khiển Select máy phát Main/Stdby tại đầu xa 

- Kiểm tra tín hiệu Select Confirmation tại đầu điều khiển (nếu hệ thống được đấu nối để sử dụng tính năng này) 

- Kiểm tra tín hiệu Squelch Break và âm tần thu tại đầu điều khiển. 

- Kiểm tra tín hiệu Receiver Mute và sự tắt âm tần tại đầu điều khiển. 

- Ngắt kết nối 

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [92 x 35] intentionally omitted <==**