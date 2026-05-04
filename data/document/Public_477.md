Public 477 

**VIETTEL AI RACE HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG NĂNG LƯỢNG MẶT TRỜI VÀ LƯU TRỮ PIN BẰNG PYTHON** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

## **1. GIỚI THIỆU VỀ PYTHON** 

Python là ngôn ngữ lập trình mạnh mẽ, hỗ trợ nhiều thư viện khoa học như NumPy , Pandas , Matplotlib , SciPy . Trong lĩnh vực năng lượng tái tạo, Python được sử dụng để: 

- Mô phỏng sản lượng điện mặt trời theo dữ liệu bức xạ. 

- Tính toán hiệu suất hệ thống lưu trữ pin. 

- Phân tích dữ liệu vận hành và tối ưu hóa cấu hình hệ thống. 

## **2. HỆ THỐNG NĂNG LƯỢNG MẶT TRỜI Ở MIỀN THỜI GIAN (t)** 

## **2.1 Yêu cầu trước khi làm thí nghiệm** 

Nắm vững kiến thức về: 

- Bức xạ mặt trời và các yếu tố ảnh hưởng. 

- Nguyên lý hoạt động của tấm pin quang điện (PV). 

- Cách tính dung lượng và hiệu suất pin lưu trữ. 

## **2.2 Mục đích của phần thí nghiệm** 

Dùng Python mô phỏng các nội dung sau: 

- Công suất phát của hệ thống PV theo giờ trong ngày. 

- Chu kỳ sạc/xả của pin lưu trữ. 

- Hiệu suất tổng thể của hệ thống PV + pin. 

## **2.3 Tóm tắt lý thuyết** 

## **2.3.1 Mô hình nguồn pin mặt trời PV** 

Pin mặt trời PV (Photovoltaic cell) gồm các lớp bán dẫn chịu tác dụng của quang học để biến đổi các năng lượng phôton bức xạ mặt trời thành năng lượng điện. Theo quan điểm năng lượng điện tử, pin mặt trời có thể được coi là những 

**==> picture [265 x 114] intentionally omitted <==**
Public 477 

**VIETTEL AI RACE** 

**HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG NĂNG LƯỢNG MẶT TRỜI VÀ LƯU TRỮ PIN BẰNG PYTHON** 

**==> picture [39 x 47] intentionally omitted <==**

nguồn dòng biểu diễn mối quan hệ phi tuyến I-V. 

Hiệu suất của tấm pin mặt trời sẽ lớn nhất khi pin mặt trời cung cấp cho ta công suất cực đại. Theo đặc tính phi tuyến trên hình 2, nó sẽ xảy ra khi P-V là cực đại, tức là P-V = Pmax tại thời điểm (Imax ,Vmax ) được gọi là điểm cực đại MPP (Maximum Point Power). Hệ bám điểm công suất cực đại MPPT (Maximum Point Power Tracking) được sử dụng để đảm bảo rằng pin mặt trời sẽ luôn luôn làm việc ở điểm MPP bất chấp tải được nối vào pin. 

Lần ban hành: 1 

**==> picture [64 x 89] intentionally omitted <==**

## **2.3.2 Định nghĩa một số đại lượng cơ bản** 

|Đại<br>lượng|Ký hiệu|Công thức|Đơn<br>vị|Ý nghĩa|
|---|---|---|---|---|
|Bức xạ<br>mặt trời|𝐺𝑡||W/m²|Năng lượng bức xạ tới bề<br>mặt tấm pin|
|Hiệu<br>suất tấm<br>pin|η𝑝𝑣||%|Tỉ lệ chuyển đổi bức xạ<br>thành điện năng|
|Công<br>suất PV|Ppv|Ppv<br>= Gt⋅A ⋅ηpv|W|Công suất tức thời của hệ<br>PV. Phụ thuộc vào bức xạ<br>mặt trời, diện tích tấm pin<br>và hiệu suất tấm pin|
|Dung<br>lượng<br>pin|Cbat||kWh|Lượng điện năng pin có thể<br>lưu trữ|
Public 477 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG NĂNG LƯỢNG MẶT TRỜI VÀ LƯU TRỮ PIN BẰNG PYTHON** 

Lần ban hành: 1 

Hiệu ηbat % Tỉ lệ điện năng thu hồi so suất pin với khi sạc 

## **2.3.2 Một số công thức quan trọng** 

_2.3.2.1 Công suất PV tức thời:_ 

**[CT1]** 𝑃𝑝𝑣(𝑡) = 𝐺𝑡(𝑡) ⋅𝐴⋅𝜂𝑝𝑣 

## _2.3.2.2 Năng lượng PV trong một ngày:_ 

**==> picture [478 x 45] intentionally omitted <==**

## _2.3.2.3 Trạng thái sạc pin (SOC):_ 

**==> picture [92 x 35] intentionally omitted <==**

**==> picture [478 x 65] intentionally omitted <==**

## **2.3.3 Một số định nghĩa khác** 

|Cộng hai nguồn năng lượng:|Nếu có hai hệ PV độc lập:<br>𝑃𝑡𝑜𝑡𝑎𝑙(𝑡) = 𝑃𝑝𝑣1(𝑡) + 𝑃𝑝𝑣2(𝑡)|
|---|---|
|Nhân với hằng số (tăng công suất):|𝑃′(𝑡) = 𝑘⋅𝑃𝑝𝑣(𝑡)|
|Dịch thời gian (mô phỏng múi giờ khác):|𝑃′(𝑡) = 𝑃𝑝𝑣(𝑡 − 𝛥𝑡)|
Public 477 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **HƯỚNG DẪN MÔ PHỎNG HỆ THỐNG NĂNG LƯỢNG MẶT TRỜI VÀ LƯU TRỮ PIN BẰNG PYTHON** 

Lần ban hành: 1 

**==> picture [426 x 191] intentionally omitted <==**

**----- Start of picture text -----**<br>
Đảo thời gian (mô phỏng ngược dữ liệu):  𝑃 [′] (𝑡) = 𝑃𝑝𝑣(−𝑡 )<br>Năng lượng lưu trữ:   𝐸𝑠𝑡𝑜𝑟𝑒𝑑 𝑐ℎ𝑎𝑟𝑔𝑒(𝑡) ⋅𝜂𝑏𝑎𝑡<br>= ∑𝑃<br>𝑡<br>Công suất trung bình:  𝑇<br>𝑃 = [1]<br>𝑎𝑣𝑔<br>𝑇 ∑𝑃(𝑡)<br>𝑡=1<br>**----- End of picture text -----**<br>

## **2.3.4 Hệ thống PV + Pin** 

_**Hệ thống bất biến theo thời gian:**_ Nếu điều kiện bức xạ và nhiệt độ không đổi, công suất PV không đổi theo thời gian. 

_**Hệ thống nhân quả:**_ Công suất tại thời điểm t chỉ phụ thuộc vào dữ liệu bức xạ và SOC trước đó. 

_**Hệ thống ổn định:**_ SOC luôn nằm trong khoảng [0, 1]. 

Phương trình cân bằng năng lượng: 

𝑃𝑙𝑜𝑎𝑑(𝑡) = 𝑃𝑝𝑣(𝑡) + 𝑃𝑑𝑖𝑠𝑐ℎ𝑎𝑟𝑔𝑒(𝑡) −𝑃𝑐ℎ𝑎𝑟𝑔𝑒(𝑡) 

## **2.3.5 Bảng dữ liệu mô phỏng (ví dụ 1 ngày)** 

|**Giờ**|𝐆𝐭<br>**(W/m²)**|𝐏𝐩𝐯<br>**(kW)**|**SOC**<br>**(%)**|𝐏𝐜𝐡𝐚𝐫𝐠𝐞(𝐤𝐖)|𝐏𝐝𝐢𝐬𝐜𝐡𝐚𝐫𝐠𝐞(𝐤𝐖)|𝐏𝐥𝐨𝐚𝐝(𝐤𝐖)|
|---|---|---|---|---|---|---|
|0|0|0.00|65|0.00|0.50|0.50|
|1|0|0.00|62|0.00|0.45|0.45|
|2|0|0.00|60|0.00|0.40|0.40|
|...|...|...|...|...|...|...|
|12|850|2.55|80|1.00|0.00|1.55|
|...|...|...|...|...|...|...|
|23|0|0.00|68|0.00|0.55|0.55|
||||||||