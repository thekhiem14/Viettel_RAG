**VIETTEL AI RACE** TD888 **HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG LỌC SỐ VÀ THIẾT KẾ BỘ LỌC SỐ** 

Lần ban hành: 1 

**==> picture [38 x 47] intentionally omitted <==**

## **1. GIỚI THIỆU VỀ LỌC SỐ SỐ** 

**==> picture [40 x 44] intentionally omitted <==**

Lọc số (Digital Filtering) là kỹ thuật xử lý tín hiệu rời rạc nhằm triệt tiêu hoặc giảm thiểu thành phần nhiễu, tăng cường thành phần mong muốn. 

Trong lĩnh vực xử lý tín hiệu, thiết kế bộ lọc số chiếm vai trò then chốt với các ứng dụng từ âm thanh, hình ảnh đến thông tin vô tuyến và điều khiển tự động. 

MATLAB cung cấp nhiều công cụ mạnh mẽ như Signal Processing Toolbox để xây dựng, mô phỏng và đánh giá hiệu năng của các bộ lọc FIR và IIR. 

## **2. NỘI DUNG CHI TIẾT HƯỚNG DẪN MÔ PHỎNG** 

## **2.1 Yêu cầu trước khi thực hành** 

Một số yêu cầu bao gồm: 

- Nắm bắt kiến thức cơ bản về tín hiệu rời rạc và hệ thống LTI. 

- Hiểu khái niệm biến đổi z và biến đổi Fourier rời rạc. 

- Sử dụng thành thạo MATLAB và Signal Processing Toolbox. 

- Có kinh nghiệm đọc đồ thị đáp ứng tần số và nhóm pha. 

## **2.2 Mục đích của phần thực hành** 

- Xây dựng và so sánh bộ lọc FIR và IIR cho bài toán loại bỏ nhiễu. 

- Thiết kế cửa sổ Hamming, Kaiser và thuật toán Parks–McClellan. 

- Đánh giá đáp ứng tần số, đáp ứng bước và độ ổn định của bộ lọc. 

- Phân tích ảnh hưởng của tham số thiết kế lên đặc tính lọc. 

## **2.3 Tóm tắt lý thuyết** 

Bộ lọc số được chia thành hai họ chính: FIR (Finite Impulse Response) và IIR (Infinite Impulse Response). 

FIR có đáp ứng xung hữu hạn, dễ đạt pha tuyến tính; IIR có đáp ứng xung vô hạn, đạt đặc tính biên dải sắc với bậc thấp nhưng pha thường không tuyến tính. 

Quy trình thiết kế tiêu chuẩn gồm xác định yêu cầu phổ, lựa chọn loại bộ lọc (thấp, cao, băng, dừng), xác lập tần số cắt và gợn râu, sau đó chọn phương pháp thiết kế phù hợp và kiểm chứng ổn định, thực thi. 
**VIETTEL AI RACE** 

**HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG LỌC SỐ VÀ THIẾT KẾ BỘ LỌC SỐ** 

Lần ban hành: 1 

**==> picture [38 x 47] intentionally omitted <==**

**==> picture [390 x 100] intentionally omitted <==**

**----- Start of picture text -----**<br>
Định nghĩa các hệ thống lọc cơ bản<br>FIR (đáp ứng hữu hạn):<br>[CT1]  𝑀<br>𝑦[𝑛] = 𝑏𝑘 · 𝑥[𝑛−𝑘]<br>∑<br>𝑘=0<br>**----- End of picture text -----**<br>

## **2.4 Định nghĩa các hệ thống lọc cơ bản** 

- FIR (đáp ứng hữu hạn): 

- IIR (đáp ứng vô hạn): 

**==> picture [385 x 54] intentionally omitted <==**

**----- Start of picture text -----**<br>
[CT2]<br>𝑏𝑘 𝑎𝑘 · 𝑦[𝑛−𝑘]<br>𝑦[𝑛] = ∑𝑘= 0 [𝑀] · 𝑥[𝑛−𝑘] −∑𝑘= 1 [𝑁]<br>**----- End of picture text -----**<br>

- Bộ lọc thấp (Low-pass): Cho phép tần số ≤fc. 

- Bộ lọc cao (High-pass): Cho phép tần số ≥ 𝑓𝑐. 

- Bộ lọc băng (Band-pass): Cho phép f₁ ≤ f ≤ f₂. 

- Bộ lọc dừng (Band-stop): Chặn f₁ ≤ f ≤ f₂. 

## **2.5 Phân loại hệ thống lọc số** 

**==> picture [426 x 258] intentionally omitted <==**

**----- Start of picture text -----**<br>
Loại lọc  Đặc điểm  Minh họa  Ứng dụng  Tính  Tính<br>chính  chính  nhân  ổn định<br>quả<br>FIR  Pha tuyến  Xử lý âm  Có  Luôn<br>tính; đáp ứng  thanh, đo  ổn định<br>nhanh  lường<br>IIR  Tiết kiệm bậc;  Điều khiển,  Có hoặc  Tùy hệ<br>pha không  liên lạc  không  số<br>tuyến tính<br>Thấp (Low- Chặn thành  Làm mượt  Có  Luôn<br>pass)  phần tần số  tín hiệu, khử  ổn định<br>cao  nhiễu<br>**----- End of picture text -----**<br>
**VIETTEL AI RACE** TD888 **HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG LỌC SỐ VÀ THIẾT KẾ BỘ LỌC SỐ** 

Lần ban hành: 1 

**==> picture [38 x 47] intentionally omitted <==**

|Cao (High-<br>pass)|Chặn thành<br>phần tần số<br>thấp||Phát hiện<br>cạnh, phân<br>tích|Có|Tùy<br>thiết kế|
|---|---|---|---|---|---|
|Băng thông<br>(Band-<br>pass)|Cho phép dải<br>tần xác định||Xử lý vô<br>tuyến, phân<br>tích|Có|Tùy<br>thiết kế|
|Băng dừng<br>(Band-<br>stop)|Chặn dải tần<br>xác định||Loại bỏ tạp<br>âm cụ thể|Có|Tùy<br>thiết kế|

## **2.6 Phương pháp thiết kế bộ lọc số** 

Trong MATLAB, thường sử dụng ba nhóm phương pháp: 

- Cửa sổ (Window Method): Hamming, Hanning, Kaiser. 

- Equiripple (Parks–McClellan): Tối ưu theo Chebyshev. 

- Thiết kế IIR cổ điển: Butterworth, Chebyshev I/II, Elliptic. 

|**Phương**<br>**pháp**<br>**thiết**<br>**kế**|**Băng**<br>**thông**<br>**cắt**|**Độ gợn**<br>**râu**<br>**trong**<br>**(dB)**|**Độ**<br>**gợn**<br>**râu**<br>**dừng**<br>**(dB)**|**Độ**<br>**dốc**<br>**(dB/oct)**|**Độ**<br>**phức**<br>**tạp**<br>**tính**<br>**toán**|**Ghi chú**|
|---|---|---|---|---|---|---|
|Window<br>Hamming|Xác<br>định<br>thủ<br>công|~0.02|~50|Trung<br>bình|Thấp|Dễ cài đặt,<br>pha gần tuyến<br>tính|
|Window<br>Kaiser|Điều<br>chỉnh β|Tùy β|Tùy β|Cao|Trung<br>bình|Linh<br>hoạt,<br>cân bằng gợn<br>râu–độdốc|
|Parks–<br>McClellan|Tùy<br>yêu<br>cầu|Thiết<br>lập rõ<br>ràng|Thiết<br>lập rõ<br>ràng|Cao|Cao|Equiripple,<br>tối ưu chặt<br>chẽ|
|Butterworth<br>(IIR)|Tự<br>nhiên|–3|~20|Thấp|Thấp|Pha<br>không<br>tuyến tính|
|Chebyshev I<br>(IIR)|Tự<br>nhiên|0|~65||||
||||||||

- **2.7 Quy trình thiết kế chi tiết** 
**VIETTEL AI RACE** TD888 

**HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG LỌC SỐ VÀ THIẾT KẾ BỘ LỌC SỐ** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

**==> picture [64 x 89] intentionally omitted <==**

## **2.7.1 Đặc tả yêu cầu phổ:** 

   - **Loại:** Thấp, cao, băng thông, băng dừng. 

   - **Tần số:** Chỉ rõ ωp, ωs(hoặc fp, fs). 

   - **Độ gợn râu:** Đặt 𝐴𝑝(dB) và 𝐴𝑠(dB). 

   - **Ràng buộc pha/độ trễ:** Xác định yêu cầu tuyến tính pha nếu có. 

- **2.7.2 Chọn họ bộ lọc:** 

   - **FIR** nếu cần pha tuyến tính, ổn định vô điều kiện, chấp nhận bậc cao. 

   - **IIR** nếu cần biên sắc với bậc thấp, chấp nhận méo pha. 

- **2.7.3 Chọn phương pháp thiết kế:** 

   - **FIR–Window:** 

      - **Ưu tiên:** Triển khai nhanh, dễ điều chỉnh; dùng Hamming/Hann cho gợn râu thấp, Kaiser khi cần tinh chỉnh. 

      - **Bước tính:** Ước lượng bậc từ suy hao dải dừng và vùng chuyển tiếp; tiền xử lý chuẩn hóa tần số; tạo bộ hệ số. 

   - **FIR–Equiripple:** 

      - **Ưu tiên:** Tối ưu hóa cao, bậc tối thiểu; chỉ định trọng số từng dải để cân bằng lỗi. 

   - **IIR–Prototype:** 

      - **Butterworth/Chebyshev/Elliptic:** Xác định bậc từ (𝐴𝑝, 𝐴𝑠, ω𝑝, ω𝑠); tiền biến dạng tần số; dùng biến đổi song tuyến tính; phân rã thành biquad. 

## **2.7.4 Kiểm chứng miền tần số:** 

   - **Biên độ:** Đáp ứng dải thông trong [−𝐴𝑝,+ 𝐴𝑝] dB; dải dừng dưới −𝐴𝑠 dB. 

   - **Pha/độ trễ nhóm:** Với FIR tuyến tính pha, xác minh τg gần hằng trên dải thông. 

- **2.7.5 Đánh giá miền thời gian:** 

   - **Đáp ứng bước/xung:** Kiểm tra vượt đỉnh, gợn sóng, thời gian xác lập. 

   - **Tín hiệu thực tế:** Áp dụng trên dữ liệu để đánh giá nhiễu tồn dư, méo biên dạng. 

- **2.7.6 Ràng buộc thực thi:** 

   - **Độ dài/độ trễ:** FIR dài gây trễ; cân nhắc decimation hoặc cấu trúc phân pha (polyphase). 
**VIETTEL AI RACE** TD888 

**HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG** Lần ban hành: 1 **LỌC SỐ VÀ THIẾT KẾ BỘ LỌC SỐ** 

**==> picture [38 x 47] intentionally omitted <==**

   - **Số học cố định:** Dùng biquad, chuẩn hóa thang, chống tràn; lượng tử hóa hệ số. 

- **2.7.7 Tinh chỉnh tham số:** 

   - **FIR:** Điều chỉnh bậc, loại cửa sổ, trọng số equiripple. 

   - **IIR:** Điều chỉnh bậc, gợn râu, tần số cắt; chọn cấu trúc trực tiếp II– transposed/biquad để ổn định số học. 

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**