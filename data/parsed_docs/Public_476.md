**VIETTEL AI RACE** Public 476 **HƯỚNG DẪN THỰC HÀNH TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY BẰNG** Lần ban hành: 1 **PYTHON** 

**==> picture [39 x 47] intentionally omitted <==**

## **1. GIỚI THIỆU VỀ PYTHON VÀ AI** 

**==> picture [44 x 54] intentionally omitted <==**

Python là ngôn ngữ lập trình phổ biến cho nghiên cứu và ứng dụng trí tuệ nhân tạo (AI) và học máy (Machine Learning). Trong tài liệu này, chúng ta sẽ tìm hiểu cách mô phỏng và thực hành các mô hình AI cơ bản bằng Python, với mục tiêu giúp học viên hiểu và áp dụng lý thuyết vào thực tế. 

## **2. DỮ LIỆU VÀ MÔ HÌNH HỌC MÁY** 

## **2.1 Yêu cầu trước khi làm thí nghiệm** 

- Có kiến thức cơ bản về Python. 

- Hiểu các khái niệm thống kê: trung bình, phương sai, độ lệch 

- chuẩn. 

   - Cài đặt thư viện: numpy, pandas, scikit-learn, matplotlib. 

## **2.2 Mục đích của phần thí nghiệm** 

Dùng MATLAB mô phỏng các nội dung sau: 

- Làm quen với quy trình xử lý dữ liệu và huấn luyện mô hình. 

- Hiểu cách áp dụng các thuật toán cơ bản và đánh giá kết quả 

## **2.3 Tóm tắt lý thuyết** 

## **2.3.1 Định nghĩa cơ bản** 

Công thức Định nghĩa ŷ =  𝑤ᵀ𝑥 +  𝑏 Hồi quy tuyến tính 𝑀𝑆𝐸 = (1/𝑛) 𝛴 (𝑦ᵢ − ŷᵢ)² (Linear Regression): tìm tham số w, b để tối thiểu hóa MSE 
Public 476 

**VIETTEL AI RACE** 

**==> picture [39 x 47] intentionally omitted <==**

**HƯỚNG DẪN THỰC HÀNH TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY BẰNG PYTHON** 

Lần ban hành: 1 

Hồi quy logistic (Logistic Regression): phân loại nhị phân với hàm sigmoid 

ŷ =  𝜎(𝑧) =  1 / (1 +  𝑒^(−𝑧)), 𝑧 =  𝑤ᵀ𝑥 +  𝑏 𝐿𝑜𝑠𝑠 = −(1/𝑛) 𝛴 [𝑦ᵢ 𝑙𝑜𝑔(ŷᵢ) + (1 −𝑦ᵢ) 𝑙𝑜𝑔(1 −ŷᵢ)] 

Mạng nơ-ron (Neural Networks): nhiều tầng tuyến tính kết hợp hàm kích hoạt 

**==> picture [156 x 49] intentionally omitted <==**

𝑎^(𝑙) =  𝑓(𝑊^(𝑙) 𝑎^(𝑙−1) +  𝑏^(𝑙)) 

**==> picture [217 x 204] intentionally omitted <==**

Chuẩn hóa dữ liệu (Standardization) 

**==> picture [108 x 14] intentionally omitted <==**

**----- Start of picture text -----**<br>
𝑧 = (𝑥 − 𝜇) / 𝜎<br>**----- End of picture text -----**<br>

**==> picture [217 x 75] intentionally omitted <==**

Đánh giá mô hình 

**==> picture [75 x 52] intentionally omitted <==**

𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 = (𝑇𝑃 +  𝑇𝑁) / (𝑇𝑃 +  𝑇𝑁 +  𝐹𝑃 +  𝐹𝑁) 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 =  𝑇𝑃 / (𝑇𝑃 +  𝐹𝑃) 𝑅𝑒𝑐𝑎𝑙𝑙 =  𝑇𝑃 / (𝑇𝑃 +  𝐹𝑁) 𝐹1 −𝑠𝑐𝑜𝑟𝑒 =  2 ∗ (𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 ∗ 𝑅𝑒𝑐𝑎𝑙𝑙) / (𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛 +  𝑅𝑒𝑐𝑎𝑙𝑙) 
**VIETTEL AI RACE** Public 476 **HƯỚNG DẪN THỰC HÀNH TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY BẰNG PYTHON** 

**==> picture [39 x 47] intentionally omitted <==**

## **2.3.2 Một số định nghĩa khác** 

Lần ban hành: 1 

**==> picture [52 x 71] intentionally omitted <==**

|Gradient Descent: thuật toán<br>tối ưu để cập nhật tham số|𝜃∶=  𝜃 − 𝛼 𝛻𝐽(𝜃)|
|---|---|
|Chuẩn hóa L2 (Ridge<br>Regression)|𝜃∶=  𝜃 − 𝛼 𝛻𝐽(𝜃)|
|Chuẩn hóa L1 (Lasso<br>Regression)|𝐽(𝑤) = (1/𝑛) 𝛴 (𝑦ᵢ − ŷᵢ)² +  𝜆 ||𝑤||₁|
|Phân tích thành phần chính<br>(Principal Component<br>Analysis - PCA)|𝑚𝑎𝑥_{𝑤} 𝑉𝑎𝑟(𝑤ᵀ𝑋), 𝑣ớ𝑖 𝑟à𝑛𝑔 𝑏𝑢ộ𝑐 ||𝑤||<br>=  1|
|K-Means Clustering: gom<br>cụm dữ liệu|𝐽 =  𝛴 𝛴 ||𝑥ᵢ<br>− 𝜇_𝑘||², 𝑣ớ𝑖 𝜇_𝑘 𝑙à 𝑡â𝑚 𝑐ụ𝑚|
|Naive Bayes Classifier: áp<br>dụng định lý Bayes với giả<br>định độc lập|𝑃(𝑦|𝑥) ∝ 𝑃(𝑦) 𝛱 𝑃(𝑥ᵢ|𝑦)|
|Support Vector Machine<br>(SVM): tìm siêu phẳng tối<br>ưu|𝑚𝑖𝑛_{𝑤, 𝑏} (1<br>/2)||𝑤||², 𝑣ớ𝑖 𝑟à𝑛𝑔 𝑏𝑢ộ𝑐 𝑦ᵢ(𝑤ᵀ𝑥ᵢ +  𝑏)<br>≥ 1|

## **2.3.3 Hệ thống** 

**==> picture [97 x 60] intentionally omitted <==**

_2.3.3.1. Cross-Entropy Loss (Entropy chéo cho phân loại đa lớp)_ 

**[CT1]** 𝐿 = − 𝛴 𝑦ᵢ 𝑙𝑜𝑔(ŷᵢ) 
**==> picture [39 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 476 **HƯỚNG DẪN THỰC HÀNH TRÍ TUỆ NHÂN TẠO VÀ HỌC MÁY BẰNG** Lần ban hành: 1 **PYTHON** 

_2.3.3.2. Softmax Function: chuẩn hóa xác suất cho phân loại đa lớp_ **[CT2]**[𝜎(𝑧)_𝑗 =  𝑒^{𝑧_𝑗} / 𝛴 𝑒^{𝑧_𝑘} ] 

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**