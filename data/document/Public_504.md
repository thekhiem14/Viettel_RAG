|---|---|---|
||**VIETTEL AI RACE**|Public 504|
||**XÂY DỰNG MÔ HÌNH THỰC NGHIỆM**<br>**THIẾT BỊ TỰ ĐỘNG PHÁT HIỆN VÀ**<br>**NỐI NGẮN MẠCH PHA CHẠM ĐẤT**<br>**TRONG PHÒNG THÍ NGHIỆM**|Lần ban hành: 1|

## **1. Thiết kế và mô phỏng mô hình thiết bị thực nghiệm trong phòng thí nghiệm** 

Quá trình thiết kế và mô phỏng được thực hiện nhằm đảm bảo mô hình hoạt động chính xác, đồng thời giảm thiểu rủi ro trước khi chế tạo thực tế. Các bước triển khai bao gồm: 

- Xác định yêu cầu kỹ thuật: Mạch phải phát hiện nhanh hiện tượng chạm đất với độ nhạy cao, thời gian đáp ứng nhỏ hơn 10 ms và đảm bảo độ tin cậy khi vận hành trong môi trường phòng thí nghiệm. 

- Lựa chọn cấu hình mô hình: Hệ thống được thiết kế trên cơ sở mạng điện 3 pha quy đổi từ điện áp 6 kV sang 400 VAC, bảo đảm an toàn khi thử nghiệm. 

- Mô phỏng trên phần mềm: Sử dụng phần mềm chuyên dụng (như MATLAB/Simulink, Proteus hoặc Multisim) để xây dựng mô hình lý thuyết. Các thành phần chính gồm nguồn xoay chiều 3 pha, tải, mạch phát hiện chạm đất, và khối hiển thị kết quả. 

- Phân tích kết quả mô phỏng: Các dạng sóng điện áp và dòng điện được theo dõi để xác định sự khác biệt giữa trạng thái bình thường và khi có sự cố chạm đất. Tín hiệu ngõ ra được kiểm chứng nhằm đánh giá khả năng tác động của mạch. 

**==> picture [32 x 51] intentionally omitted <==**

Mục tiêu của giai đoạn này là đảm bảo thiết kế có tính khả thi, đồng thời cung cấp cơ sở dữ liệu cho bước chế tạo thực nghiệm. 

## **2. Thử nghiệm tại phòng thí nghiệm** 

Sơ đồ nguyên lý đóng vai trò then chốt trong việc quyết định khả năng phát hiện sự cố của thiết bị. Việc lựa chọn được tiến hành theo các tiêu chí: 

- **Nguyên tắc phát hiện** : Dựa trên việc so sánh điện áp các pha với điểm trung tính hoặc với nhau để phát hiện sự mất cân bằng khi xảy ra chạm đất. 

- **Cấu trúc mạch** : Bao gồm bộ chỉnh lưu tín hiệu điện áp, mạch lọc, mạch so sánh và rơ le tác động. Sơ đồ được thiết kế sao cho tín hiệu ra có độ trễ nhỏ nhất, đồng thời giảm thiểu ảnh hưởng của nhiễu. 

- **Độ nhạy và an toàn** : Các linh kiện chọn phải có khả năng chịu điện áp và dòng điện phù hợp, đồng thời vẫn đảm bảo an toàn khi thử nghiệm trong phòng thí nghiệm. 

|---|---|---|
||**VIETTEL AI RACE**|Public 504|
||**XÂY DỰNG MÔ HÌNH THỰC NGHIỆM**<br>**THIẾT BỊ TỰ ĐỘNG PHÁT HIỆN VÀ**<br>**NỐI NGẮN MẠCH PHA CHẠM ĐẤT**<br>**TRONG PHÒNG THÍ NGHIỆM**|Lần ban hành: 1|

- **Khả năng mở rộng** : Sơ đồ cho phép tích hợp thêm các module hiển thị hoặc kết nối máy tính để giám sát và ghi nhận dữ liệu. 

Qua quá trình phân tích, sơ đồ nguyên lý được lựa chọn nhằm đáp ứng đầy đủ yêu cầu kỹ thuật, vừa đơn giản trong chế tạo, vừa hiệu quả trong phát hiện sự cố. 

Các kết quả thử nghiệm 

## **Mô phỏng Thực nghiệm** 

**==> picture [157 x 99] intentionally omitted <==**

**==> picture [138 x 47] intentionally omitted <==**

**==> picture [139 x 96] intentionally omitted <==**

**==> picture [32 x 51] intentionally omitted <==**

**Hình 4.11.** Tín hiệu trước chỉnh lưu 

**==> picture [409 x 148] intentionally omitted <==**

**----- Start of picture text -----**<br>
Mô phỏng  Thực nghiệm<br>**----- End of picture text -----**<br>

**==> picture [90 x 35] intentionally omitted <==**

**Hình 4.12.** Tín hiệu sau chỉnh lưu của mỗi pha 

**==> picture [38 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 504 **XÂY DỰNG MÔ HÌNH THỰC NGHIỆM THIẾT BỊ TỰ ĐỘNG PHÁT HIỆN VÀ** Lần ban hành: 1 **NỐI NGẮN MẠCH PHA CHẠM ĐẤT TRONG PHÒNG THÍ NGHIỆM** 

**==> picture [398 x 169] intentionally omitted <==**

**----- Start of picture text -----**<br>
Mô phỏng  Thực nghiệm<br>**----- End of picture text -----**<br>

**Hình 4.13.** Tín hiệu hiệu điện áp giữa các pha khi không có sự cố 

**==> picture [32 x 51] intentionally omitted <==**

**==> picture [149 x 48] intentionally omitted <==**

**==> picture [295 x 226] intentionally omitted <==**

**Hình 4.15.** Hình ảnh thể hiện chạm đất pha B 

**==> picture [60 x 41] intentionally omitted <==**

**==> picture [90 x 35] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 504|
||**XÂY DỰNG MÔ HÌNH THỰC NGHIỆM**<br>**THIẾT BỊ TỰ ĐỘNG PHÁT HIỆN VÀ**<br>**NỐI NGẮN MẠCH PHA CHẠM ĐẤT**<br>**TRONG PHÒNG THÍ NGHIỆM**|Lần ban hành: 1|

**Hình 4.16.** Dạng sóng đo được khi thử chạm đất pha A 

**==> picture [108 x 39] intentionally omitted <==**

|**STT**|**Điện**<br>**trở**<br>**rò**<br>**(Ω)**|**Đồ thị dạng sóng**|**Đồ thị dạng sóng**|**Thời**<br>**gian**<br>**phát**<br>**hiện**<br>**(ms);**<br>**kết**<br>**luận**|
|---|---|---|---|---|
|||Mô phỏng<br>Yêu cầu thời<br>gian tác động ≤<br>2ms do trong mô<br>phỏng không có<br>phần tử Rơ le|Thực<br>nghiệm Yêu cầu<br>thời gian tác<br>động của Rơ le ≤<br>10ms||
|1|10|||10<br>Đạt|
|2|20||||
|3|26||||
|4|27|||10<br>Tác<br>động<br>không<br>chắc|

**==> picture [32 x 51] intentionally omitted <==**

**==> picture [90 x 35] intentionally omitted <==**

**==> picture [438 x 360] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE  Public 504<br>XÂY DỰNG MÔ HÌNH THỰC NGHIỆM<br>THIẾT BỊ TỰ ĐỘNG PHÁT HIỆN VÀ<br>Lần ban hành: 1<br>NỐI NGẮN MẠCH PHA CHẠM ĐẤT<br>TRONG PHÒNG THÍ NGHIỆM<br>chắn<br>5  30  Không<br>phát<br>hiện<br>được<br>pha<br>chạm<br>đất<br>**----- End of picture text -----**<br>

**Bảng 4.3.** Kết quả thực nghiệm xác định thời gian phát hiện pha chạm đất 

**==> picture [125 x 44] intentionally omitted <==**

**==> picture [32 x 51] intentionally omitted <==**

## **3. Nhận xét** 

- Các dạng sóng mô phỏng và thực nghiệm là tương tự. Sự sai lệch do sai số linh kiện, các điện trở và tụ điện trong thực tế có sai số ±5%, trong khi đó các linh kiện mô phỏng là lý tưởng. 

- Mạch có khả năng phát hiện pha chạm đất. 

- Đối với mạng quy đổi từ điện áp 6kV sang 400VAC, mạch có khả năng phát hiện pha rò với điện trở rò không quá 26.6Ω và tác động đến rơ le với tổng thời gian không vượt quá 10m. 

**==> picture [90 x 35] intentionally omitted <==**

**==> picture [97 x 64] intentionally omitted <==**