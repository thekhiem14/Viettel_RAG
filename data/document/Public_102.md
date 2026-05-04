|---|---|---|
||**VIETTEL AI RACE**|Public 102|
||**LINEAR-CHAIN CRFS**|Lần ban hành: 1|

**==> picture [39 x 47] intentionally omitted <==**

**==> picture [51 x 69] intentionally omitted <==**

## **1. Định nghĩa** 

**==> picture [482 x 138] intentionally omitted <==**

_Hình 1. Linear-Chain CRFs dạng factor với các ô vuông là các hàm phụ thuộc giữa các nút_ 

Gọi X là biến ngẫu nhiên đại diện cho chuỗi dữ liệu đầu vào cần được gán nhãn, Y là biến ngẫu nhiên đại diện cho chuỗi nhãn tương ứng với chuỗi dữ liệu X. Tất cả các thành phần 𝑌𝑖 của Y thuộc một tập nhãn hữu hạn 𝒴 (tập các nhãn có thể có). 𝛺𝑥 là các trường hợp có thể có của chuỗi X, 𝛺𝑦 là các trường hợp có thể có của chuỗi nhãn Y. 

Giả định cả X và Y đều được coi là biến ngẫu nhiên phân phối chung (jointly distributed), nghĩa là chúng có mối liên hệ xác suất với nhau, và xác suất 𝑃(𝑋, 𝑌) là dương nghiêm ngặt (𝑃(𝑋=  𝑥, 𝑌= 𝑦) > 0, ∀ 𝑥, 𝑦). 

CRFs [8] là một mô hình phân biệt, tập trung vào việc xây dựng mô hình xác suất có điều kiện P(Y|X). CRFs dự đoán chuỗi nhãn Y dựa trên chuỗi dữ liệu X đã cho. CRFs không cố gắng mô hình hóa xác suất của X (tức là P(X)), mà chỉ quan tâm đến xác suất của Y khi biết X. 

Định nghĩa: Cho đồ thị 𝐺= (𝑉, 𝐸) sao cho 𝑌= (𝑌𝑣)𝑣 ∈ 𝑉, nghĩa là 𝑌 được chỉ mục hóa theo các đỉnh của đồ thị 𝐺. Khi đó, cặp (𝑋, 𝑌) là một trường ngẫu nhiên điều kiện (conditional random fields - CRFs) trong trường hợp, khi biết 𝑋, các biến ngẫu nhiên 𝑌𝑣 thỏa mãn tính chất Markov đối với đồ thị: 

𝑃(𝑌𝑣|𝑋, 𝑌𝑤, 𝑤≠𝑣) =  𝑃(𝑌𝑣|𝑋, 𝑌𝑤, 𝑤~𝑣) 

**VIETTEL AI RACE** Public 102 **LINEAR-CHAIN CRFS** Lần ban hành: 1 

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

trong đó 𝑤~𝑣 có nghĩa là 𝑤 và 𝑣 là các đỉnh kề nhau trong đồ thị 𝐺. Hay nói cách khác trạng thái của các đỉnh trong đồ thị chỉ phụ thuộc vào các điểm lân cận. 

=> CRFs là một trường hợp đặc biệt của MRF, trong có các nút có thể chia thành 2 tập riêng biệt X, Y. Và xác suất của chuỗi nhãn Y được xác định dựa trên toàn bộ chuỗi quan sát X. Do X là các biến quan sát lên cấu trúc đồ thị của X là ∈ tùy ý và Y và các biến y Y có thể phụ thuộc vào bất kì biến nào trong X. 

Trong trường hợp CRFs có X, Y  là các chuỗi X = (X1, …, Xn), Y = (Y1,…, Yn) và đồ thị G là cây mà các đỉnh có bậc không quá 2 (chuỗi tuyến tính) thì được gọi là trường ngẫu nhiên có điều kiện tuyến tính (Linear-Chain CRFs). 

**==> picture [67 x 93] intentionally omitted <==**

**==> picture [482 x 133] intentionally omitted <==**

_Hình 2. Ví dụ minh họa Linear-Chain CRFs trong bài toán gán nhãn thực thể có tên_ 

Hình 2 là một ví dụ về Linear-Chain CRFs được sử dụng trong bài toán gán nhãn thực thể có tên (tìm xem từ nào là tên riêng – PER, từ nào là tên địa danh – LOC). Ở đây, các từ trong câu đầu vào cần được gán nhãn sẽ có vai trò là chuỗi X, các nhãn cần được gán cho từng từ trong câu đầu vào sẽ là chuỗi Y. Các nhãn này sẽ nhận một trong các giá trị: PER-Tên riêng, LOC-Địa điểm, O-Không xác định. Theo tích chất Markov thì nhãn của từ hiện tại chỉ phụ thuộc vào nhãn trước, nhãn sau và câu đầu vào. 

## **2. Xây dựng mô hình xác suất P(Y|X)** 

Với giả định 𝑃(𝑋=  𝑥, 𝑌= 𝑦) là dương nghiêm ngặt, theo định lý Hammersley–Clifford [9], ta có: 

**VIETTEL AI RACE** Public 102 **LINEAR-CHAIN CRFS** 

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

**==> picture [394 x 145] intentionally omitted <==**

**==> picture [67 x 93] intentionally omitted <==**

**==> picture [140 x 40] intentionally omitted <==**

Trong đó C là tập tất cả các nhóm đầy đủ của đồ thị G (một **nhóm đầy đủ** trong đồ thị vô hướng là một tập hợp các đỉnh mà giữa tất cả các cặp đỉnh trong tập hợp đó đều tồn tại một cạnh), 𝑓𝑖 là hàm năng lượng của cụm 𝑐𝑖 chỉ ra khả năng xảy ra các mối quan hệ trong cụm. Z là hằng số chuẩn hóa để tạo phân phối xác suất hợp lệ (<1). 𝐸(𝑥, 𝑦) là hàm năng lượng được sử dụng để đánh giá mức độ "tốt" của một cặp giá trị (𝑥, 𝑦) cụ thể của các biến ngẫu nhiên X, Y. Cặp giá trị (𝑥, 𝑦) có 𝐸(𝑥, 𝑦) thấp hơn được coi là tốt hơn. 

Dựa vào công thức trên kết hợp định lý Bayes, ta suy ra phân phối của chuỗi nhãn Y khi biết X có dạng sau: 

**==> picture [349 x 174] intentionally omitted <==**

**VIETTEL AI RACE** Public 102 **LINEAR-CHAIN CRFS** Lần ban hành: 1 

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

**==> picture [394 x 105] intentionally omitted <==**

Với Linear-Chain CRFs, tập các cụm là 2 đỉnh của các cạnh và các đỉnh lẻ, khi đó, ta có: 

**==> picture [334 x 62] intentionally omitted <==**

**==> picture [67 x 93] intentionally omitted <==**

Để đơn giản, ta thêm 2 nhãn vào đầu và cuối chuỗi nhãn: Y0 = <Start>. Trong Linear-Chain CRFs, hàm năng lượng cho các cạnh là tổng hợp các hàm đặc trưng cạnh 𝑓𝑘 và hàm năng lượng cho đỉnh là tổng hợp các hàm đặc trưng của đỉnh 𝑔𝑘. 

**==> picture [384 x 45] intentionally omitted <==**

**==> picture [106 x 15] intentionally omitted <==**

**==> picture [434 x 117] intentionally omitted <==**

Các hàm đặc trưng 𝑓𝑘và 𝑔𝑘 được cho trước và cố định, thường là chỉ báo cho 1 đặc trưng ví dụ 1 hàm đặc trưng sẽ trả về giá trị 1 khi 𝑋𝑖 viết hoa chữ cái đầu và 𝑌𝑖 có nhãn là “N” ngược lại sẽ trả về 0. 

Trọng số 𝜆𝑘, 𝜇𝑘 của hàm đặc trưng là một hệ số điều chỉnh mức độ ảnh hưởng của hàm đặc trưng đến năng lượng của cấu hình. Trọng số càng cao, hàm đặc trưng càng có ảnh hưởng lớn đến xác suất của chuỗi nhãn. 

**VIETTEL AI RACE** Public 102 **LINEAR-CHAIN CRFS** 

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

## **3. Linear-Chain CRFs dạng ma trận** 

**==> picture [43 x 53] intentionally omitted <==**

Lần ban hành: 1 

Giả sử, 𝒴= {𝐶1, … , 𝐶𝑙}, 𝒴[′] =  𝒴∪{< 𝑆𝑡𝑎𝑟𝑡>}. Xác xuất có điều kiện của chuỗi Y có thể được biểu diễn dưới dạng ma trận. Tại mỗi vị trí i trong chuỗi quan sát x, ta định nghĩa một ma trận biến ngẫu nhiên kích thước |𝒴′| × |𝒴′|, 𝑀𝑖(𝑥) = [𝑀𝑖(𝐶𝑗, 𝐶𝑘|𝑥)], 𝐶𝑗, 𝐶𝑘 ∈ 𝒴. 

Mỗi phần tử 𝑀𝑖(𝐶𝑗, 𝐶𝑘|𝑥) đại diện cho một giá trị xác suất chưa chuẩn hóa. 𝑀𝑖(𝑥) là biến ngẫu nhiên mà giá trị phụ thuộc vào chuỗi quan sát X. 

**==> picture [311 x 117] intentionally omitted <==**

Với cách biểu diễn trên, 𝑍𝜃(𝑥) có thể viết lại dưới dạng sau với 1|𝒴′|×1 là ma trận kích thước |𝒴′| hàng và 1 cột có các giá trị bằng 1: 

**==> picture [299 x 22] intentionally omitted <==**

Công thức xác suất có điều kiện có thể biểu diễn dưới dạng ma trận: 

**==> picture [291 x 57] intentionally omitted <==**

Biểu diễn này hữu ích trong việc huấn luyện và suy luận mô hình CRFs. 

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [146 x 82] intentionally omitted <==**

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 102 **LINEAR-CHAIN CRFS** Lần ban hành: 1 

**==> picture [482 x 285] intentionally omitted <==**

_Hình 3. Linear-Chain CRFs biều diễn dưới dạng factor với các factor được coi là ma trận chuyển đổi_ 

Hình 3 là một ví dụ mình họa của linear-Chain CRFs biểu diễn dưới dạng factor cho bài toán POS tiếng Việt (gán nhãn động từ - v, danh từ - n, đại từ - p, trạng từ - d). Ở đây, câu đầu vào có 5 từ và mỗi 1 từ sẽ được gán nhãn từ loại tương ứng. Chuỗi từ loại chính là chuỗi Y. Giữa mỗi cặp nhãn cần gán kề nhau sẽ có một ma trận thể hiện khả năng mà giá trị nhán được gán khi biết nhãn của từ liền kề. 

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [156 x 49] intentionally omitted <==**