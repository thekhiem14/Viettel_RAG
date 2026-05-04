|---|---|---|
||**VIETTEL AI RACE**|Public 103|
||**HUẤN LUYỆN VÀ SUY LUẬN LINEAR-**<br>**CHAIN CRFS**|Lần ban<br>hành: 1|

**==> picture [34 x 38] intentionally omitted <==**

## **1. Giải thích:** 

Tương tự CRFs, Linear-Chain CRFs phân loại chuỗi dựa trên xác suất 𝑃(𝑌|𝑋). Với chuỗi x cho trước, CRFs sẽ tìm ra chuỗi y sao cho xác suất 𝑃(𝑌= 𝑦|𝑋=  𝑥) là lớn nhất. 

## 𝑦̂ = 𝑎𝑟𝑔𝑚𝑎𝑥𝑦 𝑃(𝑦|𝑥) 

Xác suất 𝑃(𝑌|𝑋) được xây dựng thông qua việc định nghĩa các hàm đặc trưng 𝑓𝑘và 𝑔𝑘 và xác định giá trị 𝜆𝑘, 𝜇𝑘. Các trọng số  được tối ưu trong quá trình huấn huyện với tập dữ liệu huấn luyện. Nói cách khác, quá trình huấn luyện CRFs là quá trình học phân phối xác suất 𝑃(𝑌|𝑋) của tập dữ liệu huấn luyện. 

**==> picture [67 x 93] intentionally omitted <==**

Việc tối ưu hóa các trọng số 𝜃= (𝜆1, … , 𝜆𝑘; 𝜇1, … , 𝜇𝑘) tương đương với việc tìm kiếm hàm năng lượng tối ưu cho mô hình. Mô hình CRFs sẽ điều chỉnh các trọng số để hàm đặc trưng phản ánh chính xác mối quan hệ giữa chuỗi quan sát và chuỗi nhãn, từ đó đưa ra dự đoán chính xác nhất. Do đó, hàm đặc trưng đóng vai trò then chốt trong việc xác định mối quan hệ giữa chuỗi quan sát x và chuỗi nhãn y. Việc lựa chọn và thiết kế hàm đặc trưng phù hợp với bài toán cụ thể là rất quan trọng để đảm bảo mô hình có thể học được các mẫu quan trọng từ dữ liệu và đưa ra dự đoán chính xác. 

## **2. Huấn luyện** 

Việc huấn luyện thường sử dụng phương pháp MLE (Maximum Likelihood Estimation) để tối ưu hóa các trọng số 𝜃= (𝜆1, … , 𝜆𝑘; 𝜇1, … , 𝜇𝑘) từ tập huấn 𝑁 luyện 𝐷= {(𝑥[(ⅈ)] , 𝑦[(ⅈ)] )}ⅈ=1. Mục tiêu của quá trình huấn luyện là tìm ra bộ trọng số 𝜃 để hàm mục tiêu log-likelihood 𝐿(𝜃) là lớn nhất. 

𝑁 𝐿(𝜃) = ∑𝑙𝑜𝑔(𝑃𝜃(𝑦[(ⅈ)] |𝑥[(ⅈ)] )) ⅈ=1 

**==> picture [437 x 224] intentionally omitted <==**

Việc tối ưu hóa hàm mục tiêu có thể sử dụng các phương pháp tối ưu dựa trên việc tính gradient như Gradient Descent, Stochastic Gradient Descent (SGD), L- BFGS (Limited-memory BFGS). Do đó chúng ta cần tính gradient của 𝐿(𝜃). 

**==> picture [67 x 93] intentionally omitted <==**

**==> picture [428 x 425] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 103|
||**HUẤN LUYỆN VÀ SUY LUẬN LINEAR-**<br>**CHAIN CRFS**|Lần ban<br>hành: 1|

Gọi 𝐸𝑥(𝑓𝑘) là kì vòng hàm đặc trưng 𝑓𝑘 theo phân phối xác suất 𝑃(𝑦|𝑥): 

**==> picture [316 x 114] intentionally omitted <==**

Tương tự ta cũng có gradient cho 𝜇𝑘: 

**==> picture [271 x 114] intentionally omitted <==**

**==> picture [139 x 163] intentionally omitted <==**

Nếu tính trực tiếp kì vọng của các hàm đặc trưng từ công thức trên thì độ phức tạp tính toán sẽ là hàm mũ (𝑂(𝑛× |𝒴|[𝑛] )). Do đó không khả thi khi số lượng nhãn và bộ dữ liệu lớn. Để giảm độ phức tạp tính toán ta biến đổi công thức trên thành dạng sau: 

**==> picture [290 x 61] intentionally omitted <==**

**==> picture [348 x 65] intentionally omitted <==**

**==> picture [126 x 41] intentionally omitted <==**

Trong đó 𝑃(𝑌𝑡−1 = 𝑦[′] , 𝑌𝑡 = 𝑦′′|𝑥[(ⅈ)] ) là xác xuất biên của 𝑌𝑡−1 = 𝑦[′] , 𝑌𝑡 = 𝑦′′ khi biết chuỗi quan sát 𝑥[(ⅈ)] , tức xác suất để cặp nhãn (𝑦′, 𝑦′′) được gán tại vị trí 

|---|---|---|
||**VIETTEL AI RACE**|Public 103|
||**HUẤN LUYỆN VÀ SUY LUẬN LINEAR-**<br>**CHAIN CRFS**|Lần ban<br>hành: 1|

t-1 và t khi biết 𝑥[(ⅈ)] mà không quan tâm đến các nhãn còn lại. Xác suất biên này có thể được tính trong thời gian đa thức bằng thuật toán Forward-Backward. 

Tương tự cho 𝜇𝑘: 

**==> picture [108 x 132] intentionally omitted <==**

**==> picture [279 x 47] intentionally omitted <==**

## **3. Thuật toán Forward-Backward áp dụng trong tính gradient** 

**==> picture [482 x 184] intentionally omitted <==**

_Hình 3.1. Minh họa thuật toán Forward-Backward trong việc xác suất biên tại 1 nút_ 

Ý tưởng của thuật toán Forward-Backward là tính xác suất biên dựa vào việc tính xác suất tiến 𝛼ⅈ(𝑥) và xác suất lùi 𝛽ⅈ(𝑥). Hình 8 mô tả ý tưởng tính xác suất biên 𝑃(𝑌2 =  𝑣|𝑥) và hình 9 mô tả ý tưởng cách tính xác suất biên 𝑃(𝑌𝑡−1 = 𝑦[′] , 𝑌𝑡 = 𝑦′′|𝑥) cho bài toán POS. Mỗi một đường đi từ <S> đến <T> là 1 trường hợp của chuỗi Y. Trọng số của của mỗi cạnh được tính theo công thức 𝑀ⅈ(𝐶𝑗, 𝐶𝑘|𝑥) đã trình bày ở phần trước thể hiện khả năng nhãn của từ liền kề khi biết trước nhãn, trọng số của 1 đường đi là tích các trọng số cạnh mà đường đi qua. 

**==> picture [376 x 35] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 103|
||**HUẤN LUYỆN VÀ SUY LUẬN LINEAR-**<br>**CHAIN CRFS**|Lần ban<br>hành: 1|

Xác suất biên 𝑃(𝑌2 =  𝑣|𝑥) sẽ là tổng xác suất của tất cả các đường đi đi qua v tại 𝑌2 hay tổng trọng số các đường đi đó. Ta có thể phân tích tổng này thành tích của 2 tổng 𝛼2(𝑣|𝑥) và 𝛽2(𝑣|𝑥). 

𝑃(𝑌2 =  𝑣|𝑥) = 𝛼2(𝑣|𝑥) × 𝛽2(𝑣|𝑥) 

Trong đó 𝛼2(𝑣|𝑥) là tổng trọng số tất cả các đường đi từ <S> đến v tại 𝑌2, 𝛽2(𝑣|𝑥) là tổng trọng số tất cả các đường đi từ v tại 𝑌2 đến <T>. 

Để tính 𝛼2(𝑣|𝑥) ta sẽ tính 𝛼1 của tất cả các giá trị của Y1 rồi nhân với trọng số chuyển đổi thành nhãn v tương ứng với từng giá trị (v => v, n => v, p => v, d => v). Như vậy thì 𝛼ⅈ sẽ được tính dựa theo 𝛼ⅈ−1 và quá trình này là quá trình tiến của thuật toán Forward-Backward. Tương tự 𝛽ⅈ cũng được tính toán dựa trên quy hoạch động và quá trình này là quá trình lùi. 

**==> picture [67 x 93] intentionally omitted <==**

Tổng quát, ta có chuỗi 𝑌= (𝑌0, … , 𝑌𝑛), gọi 𝑌ⅈ:𝑗 = (𝑌ⅈ, … , 𝑌𝑗) 𝑣ớ𝑖 0 ≤𝑖< 𝑗≤𝑛. 

**==> picture [391 x 207] intentionally omitted <==**

Ta chứng minh 𝛼𝑡(𝑌𝑡 = 𝑦[′] |𝑥) = ∑𝑦[′] 𝑡−1∈𝒴 𝛼𝑡−1(𝑌𝑡−1 = 𝑦[′] 𝑡−1[|𝑥)] × 𝑀𝑡(𝑦[′] 𝑡−1[, 𝑦][′][|𝑥)][ với ][ 1 < 𝑡≤𝑛][, thật vậy: ] 

|---|---|---|
||**VIETTEL AI RACE**|Public 103|
||**HUẤN LUYỆN VÀ SUY LUẬN LINEAR-**<br>**CHAIN CRFS**|Lần ban<br>hành: 1|

**==> picture [524 x 274] intentionally omitted <==**

**==> picture [411 x 77] intentionally omitted <==**

Tương tự, với 1 ≤𝑡< 𝑛−1ta cũng có: 

Với cách biểu diễn dưới dạng ma trận công thức 𝛼𝑡(𝑌𝑡 = 𝑦[′] |𝑥) và 𝛽𝑡(𝑌𝑡 = 𝑦[′] |𝑥) có thể biểu diễn dưới dạng tích ma trận và vector với 𝑀ⅈ(𝑥)<𝑆𝑡𝑎𝑟𝑡> là vetor hàng ứng vói nhãn < 𝑆𝑡𝑎𝑟𝑡>, 1|𝒴′|×1 là ma trận các giá trị 1 kích thước |𝒴′| × 1: 

**==> picture [406 x 168] intentionally omitted <==**

Công thức xác xuất biên biểu diễn bằng xác suất tiến và lùi có dạng: 

**==> picture [273 x 34] intentionally omitted <==**

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 103 **HUẤN LUYỆN VÀ SUY LUẬN LINEAR-** Lần ban **CHAIN CRFS** hành: 1 

**==> picture [482 x 156] intentionally omitted <==**

_Hình 3.2. Minh họa thuật toán Forward-Backward trong việc xác suất biên tại 1 cạnh_ 

Tương tự với xác suất biên 𝑃(𝑌𝑡−1 = 𝑦[′] , 𝑌𝑡 = 𝑦′′|𝑥), ta có: 

**==> picture [139 x 15] intentionally omitted <==**

**==> picture [47 x 51] intentionally omitted <==**

**==> picture [312 x 35] intentionally omitted <==**

Bằng phương pháp quy hoạch động, ta có thể tính các xác suất biên với độ phức tạp 𝑂(𝑛× |𝒴|[2] ) và chính là độ phức tạp khi tính kì vọng của các hàm đặc trưng. 

## **4. Thuật toán Viterbi áp dụng trong suy luận Linear-Chain CRFs** 

Xác định chuỗi 𝑦̂ có xác suất xảy ra cao nhất khi biết x: 

**==> picture [324 x 41] intentionally omitted <==**

Vì 𝑍𝜃(𝑥) là hằng số khi biết nên việc xác định chuỗi 𝑦̂ có xác suất xảy ra cao nhất khi biết x tương đương với xác định chuỗi 𝑦̂ để ∏𝑛ⅈ=1 𝑀ⅈ(𝑦ⅈ−1, 𝑦ⅈ|𝑥) lớn nhất: 

**==> picture [87 x 59] intentionally omitted <==**

**==> picture [220 x 53] intentionally omitted <==**

Việc tìm 𝑦̂ có thể tính trong thời gian 𝑂(𝑛× |𝒴|[2] ) với thuật toán quy hoạch động Viterbi. Thuật toán Viterbi được mô tả bằng mã giả trong hình 10. 

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 103 **HUẤN LUYỆN VÀ SUY LUẬN LINEAR-** Lần ban **CHAIN CRFS** hành: 1 

**==> picture [331 x 518] intentionally omitted <==**

**==> picture [139 x 163] intentionally omitted <==**

_Hình 4.1: Thuật toán Viterbi cho suy luận Linear-chain CRFs_ 

𝑀ⅈ(𝑥) là ma trận đã được trình bày trong phần 3 với hàng 0 và cột 0 tương ứng với nhãn <Start>. 

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 103 **HUẤN LUYỆN VÀ SUY LUẬN LINEAR-** Lần ban **CHAIN CRFS** hành: 1 _Hình 4.2: Hình minh họa thuật toán Viterbi cho POS_ 

Hình 4.2 là minh họa quá trình suy luận Viterbi cho POS. Giả sử sau khi huấn luyện ta đã có được trọng số của các đường đi 𝑀ⅈ. Với đầu câu đầu vào có 4 từ, và cần gán nhãn cho 4 từ này một nhãn từ loại là 1 trong 4 giá trị: v, n, p, d. Ở đây, mỗi một miền tương đương với 1 từ cần được gán nhãn và số đỉnh trong miền là nhãn có thể có của từ, ví dụ, miền Y1 có 4 đỉnh là v, n, p, d tương đương với 4 giá trị có thể gán cho từ đầu tiên của câu. Một đường đi hợp lệ là đường đi đi qua duy nhất một đỉnh trong mỗi miền. Thuật toán Viterbi sẽ tìm đường sao cho trọng số là lớn nhất (tương đương với xác suất chuỗi nhãn là lớn nhất. 

Ý tưởng của Viterbi là đường đi lớn nhất đến một đỉnh sẽ bao gồm đường đi lớn nhất đến đỉnh trước nó. Xuất phát từ ý tưởng này, để tìm đường đi lớn nhất đến miền Y4, ta sẽ tính đường đi lớn nhất đến các đỉnh của miền Y3, sau đó từ các đỉnh của Y3 ta tính trọng số đến các đỉnh của Y4 và chọn ra đường đi có trọng số lớn nhât. Tương tự đường đi có trọng số lớn nhất đến các đỉnh trong Y3 có thể tính qua đường đi có trọng số lớn nhất đến các đỉnh trong Y2, ….