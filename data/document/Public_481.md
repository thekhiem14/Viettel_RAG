**VIETTEL AI RACE** Public 481 **GIỚI THIỆU VỀ MẠNG NORON NHÂN TẠO** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

**==> picture [40 x 44] intentionally omitted <==**

## **1. GIỚI THIỆU VỀ MẠNG NƠ-RON NHÂN TẠO** 

Mạng nơ-ron nhân tạo (Artificial Neural Networks – ANN) là nền tảng cốt lõi của trí tuệ nhân tạo hiện đại. Ý tưởng dựa trên cách bộ não sinh học xử lý thông tin thông qua các nơ-ron liên kết. 

## **2. MẠNG NƠ-RON NHÂN TẠO** 

## **2.1 Yêu cầu trước khi làm thí nghiệm** 

Yêu cầu trước khi thực hàn 

## **2.2 Mục đích của phần thí nghiệm** 

Mục đích của phần thí nghiệm: 

- Hiểu nguyên lý hoạt động của ANN. 

- Làm quen với các công thức toán học mô tả quá trình huấn luyện. 

- Ứng dụng ANN trong bài toán thực tế: phân loại, dự đoán, xử lý ảnh, ngôn ngữ. 

## **2.3 Tóm tắt lý thuyết** 

**==> picture [86 x 33] intentionally omitted <==**

## **2.3.1 Nơ-ron nhân tạo** 

Định nghĩa 

## Công thức 

𝑛 Nơ-ron nhân tạo thực hiện phép biến 𝑖𝑥𝑖 + 𝑏 đổi tuyến tính–tịnh tiến trên vector 𝑧= ∑𝑤 đặc trưng đầu vào, sau đó qua hàm 𝑖=1 kích hoạt phi tuyến để tăng năng lực biểu diễn; bias giúp dịch chuyển biên 𝑦= 𝑓(𝑧) quyết định. 

1 Sigmoid nén giá trị về (0,1), thường 𝜎(𝑧) = dùng cho đầu ra nhị phân; nhưng dễ 1 + 𝑒[−𝑧] bão hòa gradient ở vùng biên. 

**==> picture [87 x 59] intentionally omitted <==**
Public 481 

**GIỚI THIỆU VỀ MẠNG NORON NHÂN TẠO** 

Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

**==> picture [226 x 142] intentionally omitted <==**

Tanh là phiên bản tịnh tiến/scale của Sigmoid, đầu ra (-1,1), trung bình bằng 0 giúp hội tụ tốt hơn trong một số mạng 

ReLU giữ thành phần dương, triệt tiêu âm, giúp mạng sâu hội tụ nhanh; có biến thể Leaky ReLU khắc phục “neuron chết”. 

𝑡𝑎𝑛ℎ(𝑧) =[𝑒][𝑧][−𝑒][−𝑧] 𝑒[𝑧] + 𝑒[−𝑧] 

ReLU(𝑧) = 𝑚𝑎𝑥(0, 𝑧) ,  LeakyReLU(𝑧) = 𝑚𝑎𝑥(𝛼𝑧, 𝑧) 

## **2.3.2 Mất mát và phân phối** 

**==> picture [426 x 239] intentionally omitted <==**
Public 481 

**VIETTEL AI RACE** 

**GIỚI THIỆU VỀ MẠNG NORON NHÂN TẠO** 

**==> picture [39 x 47] intentionally omitted <==**

## Lần ban hành: 1 

**==> picture [244 x 152] intentionally omitted <==**

**==> picture [426 x 222] intentionally omitted <==**

**----- Start of picture text -----**<br>
MSE  thường dùng cho hồi  𝑁<br>quy; nhạy cảm với ngoại lai  𝐿= [1] 𝑖 −𝑦̂)𝑖 [2]<br>𝑁 ∑(𝑦<br>do bình phương sai số.  𝑖=1<br>Hinge loss  dùng trong  𝑁<br>SVM/NN phân biệt biên  𝑖𝑦̂)𝑖<br>𝐿= ∑𝑚𝑎𝑥(0,1 −𝑦<br>cứng; khuyến khích lề phân  𝑖=1<br>tách lớn.<br>**----- End of picture text -----**<br>

## **2.3.3 Tối ưu hoá** 

## _2.3.3.1. Gradient Descent/SGD_ 

**[CT1]** 𝜃𝑡+1 = 𝜃𝑡 −𝜂𝛻𝜃𝐿(𝜃𝑡) 

## _2.3.3.2. Gradient Descent/SGD_ 

𝑣𝑡 = μ𝑣𝑡−1 + η∇θ𝐿𝑡,   θ𝑡+1 = θ𝑡 −𝑣𝑡 

**==> picture [67 x 48] intentionally omitted <==**
Public 481 

**VIETTEL AI RACE** 

**GIỚI THIỆU VỀ MẠNG NORON NHÂN TẠO** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

**==> picture [426 x 122] intentionally omitted <==**

## _2.3.3.4. Weight Decay (L2)_ 

𝜃𝑡+1 = (1 −𝜂𝜆)𝜃𝑡 −𝜂∇𝜃𝐿(𝜃𝑡) **[CT3]** 

## **2.3.4. Regularization & Normalization** 

L1/L2 Regularization lần lượt khuyến khích thưa (sparsity) và nhỏ hoá tham số; tác động khác nhau lên giải pháp tối ưu. 

**==> picture [426 x 384] intentionally omitted <==**
Public 481 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **GIỚI THIỆU VỀ MẠNG NORON NHÂN TẠO** 

Lần ban hành: 1 

_Hinge loss_ dùng trong SVM/NN phân biệt biên cứng; khuyến khích lề phân tách lớn. 

**==> picture [269 x 149] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑁<br>𝑖𝑦̂)𝑖<br>𝐿= ∑𝑚𝑎𝑥(0,1 −𝑦<br>𝑖=1<br>**----- End of picture text -----**<br>

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**