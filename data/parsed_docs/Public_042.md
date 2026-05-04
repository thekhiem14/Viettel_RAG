**==> picture [80 x 62] intentionally omitted <==**

**==> picture [161 x 68] intentionally omitted <==**

**==> picture [60 x 61] intentionally omitted <==**

## **VIETTEL AI RACE** TD042 **GIỚI THIỆU NEURAL NETWORK** Lần ban hành: 1 

**==> picture [35 x 43] intentionally omitted <==**

## **1. Neural network là gì** 

**==> picture [66 x 66] intentionally omitted <==**

Con chó có thể phân biệt được người thân trong gia đình và người lạ hay đứa trẻ có thể phân biệt được các con vật. Những việc tưởng chừng như rất đơn giản nhưng lại cực kì khó để thực hiện bằng máy tính. Vậy sự khác biệt nằm ở đâu? Câu trả lời nằm ở cấu trúc bộ não với lượng lớn các nơ-ron thần kinh liên kết với nhau. Liệu máy tính có thể mô phỏng lại cấu trúc bộ não để giải các bài toán trên ??? 

Neural là tính từ của neuron (nơ-ron), network chỉ cấu trúc, cách các nơ-ron đó liên kết với nhau, nên neural network (NN) là một hệ thống tính toán lấy cảm hứng từ sự hoạt động của các nơ-ron trong hệ thần kinh. 

## **1.1 Hoạt động của các nơ-ron** 

Nơ-ron là đơn vị cơ bản cấu tạo hệ thống thần kinh và là thành phần quan trọng nhất của não. Đầu chúng ta gồm khoảng 10 triệu nơ-ron và mỗi nơ-ron lại liên kết với tầm 10.000 nơ-ron khác. 

Ở mỗi nơ-ron có phần thân (soma) chứa nhân, các tín hiệu đầu vào qua sợi nhánh (dendrites) và các tín hiệu đầu ra qua sợi trục (axon) kết nối với các nơ-ron khác. Hiểu đơn giản mỗi nơ-ron nhận dữ liệu đầu vào qua sợi nhánh và truyền dữ liệu đầu ra qua sợi trục, đến các sợi nhánh của các nơ-ron khác. 

Mỗi nơ-ron nhận xung điện từ các nơ-ron khác qua sợi nhánh. Nếu các xung điện này đủ lớn để kích hoạt nơ-ron, thì tín hiệu này đi qua sợi trục đến các sợi nhánh của các nơ-ron khác. 

**==> picture [384 x 212] intentionally omitted <==**

**==> picture [110 x 37] intentionally omitted <==**

**==> picture [81 x 210] intentionally omitted <==**

Hình 5.1: Tế bào thần kinh [14] 

=> Ở mỗi nơ-ron cần quyết định có kích hoạt nơ-ron đấy hay không. Tương tự các hoạt động của hàm sigmoid bài trước. 

**==> picture [96 x 63] intentionally omitted <==**

**==> picture [60 x 61] intentionally omitted <==**

**==> picture [161 x 68] intentionally omitted <==**

## **VIETTEL AI RACE** 

**==> picture [35 x 47] intentionally omitted <==**

Lần ban hành: 1 

## **GIỚI THIỆU NEURAL NETWORK** 

Tuy nhiên NN chỉ là lấy cảm hứng từ não bộ và cách nó hoạt động, chứ không phải bắt chước toàn bộ các chức năng của nó. Việc chính của chúng ta là dùng mô hình đấy đi giải quyết các bài toán chúng ta cần. 

## **2. Mô hình neural network** 

**==> picture [35 x 35] intentionally omitted <==**

## **2.1 Logistic regression** 

Logistic regression là mô hình neural network đơn giản nhất chỉ với input layer và output layer. 

**==> picture [105 x 229] intentionally omitted <==**

Mô hình của logistic regression từ bài trước là: _y_ ˆ= _σ_ ( _w_ 0+ _w_ 1∗ _x_ 1+ _w_ 2∗ _x_ 2). Có 2 bước: 

Tính tổng linear: _z_ =1∗ _w_ 0+ _x_ 1∗ _w_ 1+ _x_ 2∗ _w_ 2 

Áp dụng sigmoid function: _y_ ˆ= _σ_ ( _z_ ) 

Để biểu diễn gọn lại ta sẽ gộp hai bước trên thành một trên biểu đồ như hình 5.2. 

**==> picture [284 x 211] intentionally omitted <==**

**==> picture [116 x 39] intentionally omitted <==**

Hình 5.2: Mô hình logistic regression 

Hệ số _w_ 0 được gọi là bias. Để ý từ những bài trước đến giờ dữ liệu khi tính toán luôn được thêm 1 để tính hệ số bias _w_ 0 . Tại sao lại cần hệ số bias? Quay lại với bài 1, phương trình đường thẳng sẽ thế nào nếu bỏ _w_ 0, phương trình giờ có dạng: _y_ = _w_ 1∗ _x_ , sẽ luôn đi qua gốc tọa độ và nó không tổng quát hóa phương trình đường thẳng nên có thể không tìm được phương trình mong muốn. => Việc thêm bias (hệ số tự do) là rất quan trọng. 

Hàm sigmoid ở đây được gọi là activation function. 

## **2.2 Mô hình tổng quát** 

Layer đầu tiên là input layer, các layer ở giữa được gọi là hidden layer, layer cuối cùng được gọi là output layer. Các hình tròn được gọi là node. 

Mỗi mô hình luôn có 1 input layer, 1 output layer, có thể có hoặc không các hidden layer. Tổng số layer trong mô hình được quy ước là số layer - 1 (không tính input layer). 

**==> picture [59 x 40] intentionally omitted <==**

**==> picture [161 x 68] intentionally omitted <==**

**==> picture [60 x 61] intentionally omitted <==**

## **VIETTEL AI RACE** 

**==> picture [35 x 47] intentionally omitted <==**

Lần ban hành: 1 

## **GIỚI THIỆU NEURAL NETWORK** 

Ví dụ như ở hình trên có 1 input layer, 2 hidden layer và 1 output layer. Số lượng layer của mô hình là 3 layer. 

**==> picture [66 x 66] intentionally omitted <==**

Mỗi node trong hidden layer và output layer : 

Liên kết với tất cả các node ở layer trước đó với các hệ số w riêng. 

Mỗi node có 1 hệ số bias b riêng. 

Diễn ra 2 bước: tính tổng linear và áp dụng activation function. 

**==> picture [105 x 229] intentionally omitted <==**

## **2.3 Kí hiệu** 

Số node trong hidden layer thứ i là _l_[(] _[i]_[)] . 

Ma trận _W_[(] _[k]_[)] kích thước _l_[(] _[k]_[−1) ] ∗ _l_[(] _[k]_[)] là ma trận hệ số giữa layer (k-1) và layer k, trong đó _w_[(] _ij[k]_[) ] là hệ số kết nối từ node thứ i của layer k-1 đến node thứ j của layer k. 

**==> picture [323 x 265] intentionally omitted <==**

**==> picture [116 x 39] intentionally omitted <==**

Hình 5.3: Mô hình neural network 

Vector 𝑏[(𝑘)] kích thước 𝑙[𝑘] ∗1 là hệ số bias của các node trong layer k, trong đó _b_[(] _i[k]_[) ] là bias của node thứ i trong layer k. 

## ( _l_ ) 

Với node thứ i trong layer l có bias _bi[(l)]_ thực hiện 2 bước: 

- Tính tổng tất cả các node trong layer trước nhân với hệ số w tương ứng, rồi cộng với bias b. 

Áp dụng activation function: _ai[(l)]_ = _σ_ ( _zi[(l)]_ ) 

Vector _z_[(] _[k]_[)] kích thước _l_[(] _[k]_[)] ∗1 là giá trị các node trong layer k sau bước tính tổng linear. 

**==> picture [94 x 33] intentionally omitted <==**

**==> picture [59 x 40] intentionally omitted <==**

TD042 Lần ban hành: 1 

**==> picture [161 x 68] intentionally omitted <==**

**==> picture [60 x 61] intentionally omitted <==**

## **VIETTEL AI RACE** 

**==> picture [35 x 47] intentionally omitted <==**

## **GIỚI THIỆU NEURAL NETWORK** 

Vector _a_[(] _[k]_[) ] kích thước _l_[(] _[k]_[)] ∗1 là giá trị của các node trong layer k sau khi áp dụng hàm activation function. 

**==> picture [66 x 66] intentionally omitted <==**

**==> picture [399 x 262] intentionally omitted <==**

**==> picture [105 x 210] intentionally omitted <==**

Mô hình neural network trên gồm 3 layer. Input layer có 2 node ( _l_[(0) ] =2), hidden layer 1 có 3 node, hidden layer 2 có 3 node và output layer có 1 node. 

Do mỗi node trong hidden layer và output layer đều có bias nên trong input layer và hidden layer cần thêm node 1 để tính bias (nhưng không tính vào tổng số node layer có). 

**==> picture [86 x 34] intentionally omitted <==**

## **3. Feedforward** 

Để nhất quán về mặt ký hiệu, gọi input layer là _a_[(0)] (= _x_ ) kích thước 2*1. 

**==> picture [426 x 134] intentionally omitted <==**

**==> picture [128 x 79] intentionally omitted <==**

Tương tự ta có: 

**==> picture [156 x 49] intentionally omitted <==**

_z_ (2) =( _W_ (2)) _T_ ∗ _a_ (1) + _b_ (2) 

_a_ (2) = _σ_ ( _z_ (2)) 

_z_ (3) =( _W_ (3)) _T_ ∗ _a_ (2) + _b_ (3) 

**==> picture [80 x 62] intentionally omitted <==**

**==> picture [153 x 63] intentionally omitted <==**

**==> picture [462 x 136] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE TD042<br>GIỚI THIỆU NEURAL NETWORK Lần ban hành: 1<br>y ˆ=  a (3) = σ ( z (3))<br>**----- End of picture text -----**<br>

**==> picture [35 x 35] intentionally omitted <==**

Hình 5.4: Feedforward 

## **4. Logistic regression với toán tử XOR** 

**==> picture [105 x 229] intentionally omitted <==**

Phần này không bắt buộc, nó giúp giải thích việc có nhiều layer hơn thì mô hình sẽ giải quyết được các bài toán phức tạp hơn. Cụ thể là mô hình logistic regression bài trước không biểu diễn được toán tử XOR nhưng nếu thêm 1 hidden layer với 2 node ở giữa input layer và output layer thì có thể biểu diễn được toán tử XOR. 

AND, OR, XOR là các phép toán thực hiện phép tính trên bit. Thế bit là gì? bạn không cần quan tâm, chỉ cần biết mỗi bit nhận 1 trong 2 giá trị là 0 hoặc 1. 

## **4.1 NOT** 

Phép tính NOT của 1 bit cho ra giá trị ngược lại. 

|A|NOT(A)|
|---|---|

## **4.2 AND** 

**==> picture [86 x 34] intentionally omitted <==**

Phép tính AND của 2 bit cho giá trị 1 nếu cả 2 bit bằng 1 và cho giá trị bằng 0 trong các trường hợp còn lại. Bảng chân lý 

**==> picture [111 x 111] intentionally omitted <==**

## **4.3 OR** 

Phép tính OR của 2 bit cho giá trị 1 nếu 1 trong 2 bit bằng 1 và cho giá trị bằng 0 trong các trường hợp còn lại. Bảng chân lý 

**==> picture [96 x 63] intentionally omitted <==**

**==> picture [101 x 69] intentionally omitted <==**

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [60 x 61] intentionally omitted <==**

## **4.4 XOR** 

**==> picture [384 x 127] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE TD042<br>GIỚI THIỆU NEURAL NETWORK Lần ban hành: 1<br>**----- End of picture text -----**<br>

**==> picture [51 x 71] intentionally omitted <==**

1 0 1 1 1 1 

Phép tính XOR của 2 bit cho giá trị 1 nếu đúng 1 trong 2 bit bằng 1 và cho giá trị bằng 0 trong các trường hợp còn lại. Bảng chân lý 

|A|B|A XOR B|
|---|---|---|

Khi thiết lập bài toán logistic regression, ta có đồ thị 

**==> picture [284 x 215] intentionally omitted <==**

**==> picture [116 x 39] intentionally omitted <==**

**==> picture [105 x 229] intentionally omitted <==**

Rõ ràng là không thể dùng một đường thẳng để phân chia dữ liệu thành 2 miền. Nên khi bạn dùng gradient descent vào bài toán XOR thì bất kể bạn chạy bước 2 bao nhiêu lần hay chỉnh learning_rate thế nào thì vẫn không ra được kết quả như mong muốn. Logistic regression như bài trước không thể giải quyết được vấn đề này, giờ cần một giải pháp mới !!! 

Áp dụng các kiến thức về bit ở trên lại, ta có: 

**==> picture [417 x 80] intentionally omitted <==**

**==> picture [94 x 33] intentionally omitted <==**

**==> picture [47 x 36] intentionally omitted <==**

**==> picture [80 x 62] intentionally omitted <==**

**==> picture [153 x 63] intentionally omitted <==**

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**||TD042|
|---|---|---|---|---|---|---|---|---|
||||**GIỚI THIỆU NEURAL NETWORK**|||||Lần ban hành: 1|
|||||||||1<br>1<br>0|
||0|1|1|0|1|1||1|
||1|0|1|0|1|1||1|
||1|1|0|1|0|1||0|

**==> picture [35 x 35] intentionally omitted <==**

Do đó: A XOR B = (NOT(A AND B) AND (A OR B)), vậy để tính được XOR ta kết hợp NOT(AND) và OR sau đó tính phép tính AND. 

**==> picture [105 x 229] intentionally omitted <==**

**==> picture [320 x 180] intentionally omitted <==**

Hình 5.12: Mô hình XOR 

Nhìn có vẻ rối nhỉ, cùng phân tích nhé: 

node NOT( _x_ 1 AND _x_ 2) chính là từ hình 5.10, với 3 mũi tên chỉ đến từ 1 _,x_ 1 _,x_ 2 với hệ số _w_ 0 _,w_ 1 _,w_ 2 tương ứng là 1.5, -1, -1. 

**==> picture [86 x 34] intentionally omitted <==**

node tính _x_ 1 OR _x_ 2 là từ hình 5.11 

node trong output layer là phép tính AND từ 2 node của layer trước, giá trị hệ số từ hình 1 mang xuống. 

Nhận xét: mô hình logistic regression không giải quyết được bài toán XOR nhưng mô hình mới thì giải quyết được bài toán XOR. Đâu là sự khác nhau: 

Logistic regression chỉ có input layer và output layer 

Mô hình mới có 1 hidden layer có 2 node ở giữa input layer và output layer. 

Càng nhiều layer và node thì càng giải quyết được các bài toán phức tạp hơn. 

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [156 x 49] intentionally omitted <==**