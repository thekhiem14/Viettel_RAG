|---|---|---|
||**VIETTEL AI RACE**|Public 105|
||**THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN**<br>**MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG**<br>**DỤNG VÀO POS TAGGING**|Lần ban hành: 1|

## **1. Thuật toán liên quan đến Hidden Markov Model (HMM)** 

Các thuật toán liên quan đến HMM là trung tâm của việc áp dụng mô hình trong các bài toán thực tiễn. Dưới đây là ba thuật toán quan trọng, mỗi thuật toán giải quyết một trong ba bài toán cơ bản của HMM. 

**==> picture [93 x 113] intentionally omitted <==**

## 1.1. **Thuật toán Forward và Backward** 

## **1.1.1. Mục đích:** 

Tính xác suất của một chuỗi quan sát O={O1,O2,…,OT} dựa trên một mô hình HMM λ=(A,B,π). 

## **1.1.2. Thuật toán Forward** 

Forward algorithm tính xác suất P(O ∣ λ) bằng cách sử dụng đệ quy. 

- **Biến forward** αt(i): Xác suất của chuỗi quan sát một phần O1,O2,…,Ot và hệ thống ở trạng thái Si tại thời điểm t: 

**==> picture [199 x 14] intentionally omitted <==**

## • **Quy trình tính toán:** 

## 1. **Khởi tạo:** 

**==> picture [359 x 107] intentionally omitted <==**

## 2. **Đệ quy:** 

3. **Kết thúc:** 

**==> picture [123 x 46] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 105|
||**THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN**<br>**MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG**<br>**DỤNG VÀO POS TAGGING**|Lần ban hành: 1|

- **Độ phức tạp:** O(N[2] T). 

## **1.1.3. Thuật toán Backward** 

Backward algorithm hỗ trợ tính toán tương tự nhưng từ cuối chuỗi quan sát trở về đầu. 

- **Biến backward** βt(i): Xác suất của chuỗi quan sát từ Ot+1,Ot+2,…,OT, với trạng thái qt=Si tại thời điểm t: 

**==> picture [191 x 14] intentionally omitted <==**

- **Quy trình tính toán:** 

   1. **Khởi tạo:** 

**==> picture [109 x 14] intentionally omitted <==**

2. **Đệ quy:** 

**==> picture [277 x 48] intentionally omitted <==**

3. **Kết thúc:** Tính xác suất tổng quát: 

**==> picture [172 x 57] intentionally omitted <==**

## • **Độ phức tạp:** O(N[2] T). 

**==> picture [60 x 43] intentionally omitted <==**

## 1.2. **Thuật toán Viterbi** 

**==> picture [156 x 49] intentionally omitted <==**

## **1.2.1. Mục đích:** 

Tìm chuỗi trạng thái ẩn tối ưu Q[∗] ={q1[∗] ,q2[∗] ,…,qT[∗] } giải thích tốt nhất chuỗi quan sát O. 

**==> picture [45 x 47] intentionally omitted <==**

**==> picture [38 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 105 **THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG** Lần ban hành: 1 **DỤNG VÀO POS TAGGING** 

**==> picture [34 x 38] intentionally omitted <==**

## **1.2.2. Quy trình tính toán:** 

- **Biến trạng thái** δt(i): Xác suất lớn nhất của chuỗi trạng thái dẫn đến Si tại thời điểm t: 

**==> picture [139 x 163] intentionally omitted <==**

**==> picture [326 x 22] intentionally omitted <==**

## • **Bước thực hiện:** 

## 1. **Khởi tạo:** 

**==> picture [167 x 44] intentionally omitted <==**

## 2. **Đệ quy:** 

**==> picture [373 x 43] intentionally omitted <==**

**==> picture [235 x 44] intentionally omitted <==**

## 3. **Kết thúc:** 

**==> picture [170 x 101] intentionally omitted <==**

**==> picture [126 x 41] intentionally omitted <==**

## 4. **Truy vết trạng thái tối ưu:** 

**==> picture [230 x 15] intentionally omitted <==**

## • **Độ phức tạp:** O(N[2] T). 

|---|---|---|
||**VIETTEL AI RACE**|Public 105|
||**THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN**<br>**MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG**<br>**DỤNG VÀO POS TAGGING**|Lần ban hành: 1|

## **2. Các giả định của Hidden Markov Model (HMM)** 

Hidden Markov Model (HMM) dựa trên hai giả định cơ bản, giúp đơn giản hóa việc mô hình hóa và tính toán xác suất trong các bài toán thực tế. Mặc dù những giả định này có thể không hoàn toàn chính xác trong mọi trường hợp, chúng vẫn đủ mạnh để mô tả nhiều hệ thống thực tế một cách hiệu quả. 

**==> picture [93 x 113] intentionally omitted <==**

## 2.1. **Giả định Markov (Markov Assumption)** 

## **2.1.1. Định nghĩa:** 

Giả định Markov phát biểu rằng trạng thái hiện tại qtq_tqt chỉ phụ thuộc vào trạng thái ngay trước đó qt−1, không phụ thuộc vào các trạng thái trước đó trong chuỗi. 

P(qt∣qt−1,qt−2,…,q1) = P(qt ∣ qt−1) 

## **2.1.2. Ý nghĩa:** 

- Giả định này giảm độ phức tạp của mô hình, chỉ yêu cầu xét mối quan hệ giữa hai trạng thái liên tiếp thay vì toàn bộ chuỗi trạng thái. 

- Trong thực tế, giả định Markov có thể hiểu là một hệ thống "có trí nhớ ngắn hạn", nơi trạng thái hiện tại chứa đủ thông tin để dự đoán trạng thái tiếp theo. 

## **2.1.3. Hạn chế:** 

- Hệ thống thực tế có thể bị ảnh hưởng bởi nhiều trạng thái trong quá khứ, không chỉ bởi trạng thái ngay trước đó. Tuy nhiên, việc tăng bậc của mô hình Markov (Markov bậc cao hơn) có thể giúp giảm bớt hạn chế này, nhưng làm tăng độ phức tạp tính toán. 

## 2.2. **Giả định độc lập quan sát (Independence Assumption)** 

## **2.2.1. Định nghĩa:** 

Giả định này cho rằng mỗi quan sát OtO_tOt tại thời điểm ttt chỉ phụ thuộc vào trạng thái hiện tại qtq_tqt, không phụ thuộc vào các quan sát khác hoặc các trạng thái khác trong chuỗi. 

|---|---|---|
||**VIETTEL AI RACE**|Public 105|
||**THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN**<br>**MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG**<br>**DỤNG VÀO POS TAGGING**|Lần ban hành: 1|

P(Ot ∣ qt,qt−1,Ot−1,… ) = P(Ot ∣ qt) 

## **2.2.2. Ý nghĩa:** 

**==> picture [108 x 132] intentionally omitted <==**

- Giả định này cho phép ta mô hình hóa mối quan hệ giữa trạng thái ẩn và quan sát một cách độc lập, giảm đáng kể độ phức tạp khi tính toán xác suất. 

- Đây là một trong những lý do HMM được áp dụng rộng rãi trong các bài toán như nhận dạng giọng nói và gắn thẻ từ loại. 

## **2.2.3. Hạn chế:** 

- Trong thực tế, các quan sát thường có mối liên hệ phụ thuộc với nhau, đặc biệt trong các chuỗi dữ liệu có tính chất tuần tự cao. Giả định này có thể không hoàn toàn chính xác, nhưng thường được chấp nhận để đơn giản hóa mô hình. 

Hai giả định Markov và độc lập quan sát là nền tảng của Hidden Markov Model, giúp mô hình này trở thành một công cụ đơn giản nhưng mạnh mẽ để mô tả các chuỗi dữ liệu tuần tự. Mặc dù có những hạn chế nhất định, chúng cho phép HMM áp dụng hiệu quả trong các bài toán thực tế với độ phức tạp tính toán thấp. 

**3. Ứng dụng của Hidden Markov Model (HMM) vào Gắn thẻ từ loại (POS Tagging)** 

Gắn thẻ từ loại (Part-of-Speech Tagging - POS Tagging) là một bài toán quan trọng trong xử lý ngôn ngữ tự nhiên (NLP), nhằm gán nhãn ngữ pháp (danh từ, động từ, tính từ,...) cho từng từ trong câu. Hidden Markov Model (HMM) là một phương pháp phổ biến để giải quyết bài toán này nhờ khả năng mô hình hóa chuỗi trạng thái ẩn (các nhãn từ loại) dựa trên chuỗi quan sát (các từ trong câu). 

## 3.1. **Mô hình HMM cho POS Tagging** 

Để áp dụng HMM vào bài toán POS Tagging, chúng ta cần xác định các thành phần của mô hình: 

|---|---|---|
||**VIETTEL AI RACE**|Public 105|
||**THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN**<br>**MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG**<br>**DỤNG VÀO POS TAGGING**|Lần ban hành: 1|

- **Tập trạng thái ẩn (S):** 

`o` Là tập các nhãn từ loại (POS tags), ví dụ: S={NN (danh từ),VB (động từ),JJ (tính từ),… }. 

## • **Tập quan sát (O):** 

- Là tập các từ trong câu, ví dụ: O={The, cat, runs, fast} 

- **Phân phối xác suất ban đầu (π):** 

**==> picture [93 x 113] intentionally omitted <==**

- Xác suất một từ trong câu bắt đầu với một từ loại cụ thể: πi=P(S1=i) Ví dụ: Một câu thường bắt đầu bằng các nhãn như DT (mạo từ) hoặc NN (danh từ). 

## • **Ma trận chuyển trạng thái (A):** 

- Xác suất chuyển từ nhãn từ loại này sang nhãn từ loại khác: aij=P(St+1=j∣St=i) 

   - Ví dụ: Sau một danh từ (NN), khả năng cao sẽ là một động từ (VB) hoặc mạo từ (DT). 

## • **Ma trận xác suất phát xạ (B):** 

- Xác suất một nhãn từ loại phát sinh một từ cụ thể: bj(Ot)=P(Ot∣St=j) Ví dụ: Xác suất từ "runs" thuộc nhãn động từ (VB) sẽ cao hơn các nhãn khác. 

## 3.2. **Thuật toán Viterbi để giải bài toán POS Tagging** 

POS Tagging sử dụng thuật toán Viterbi để tìm chuỗi nhãn từ loại tối ưu S[∗] ={S1[∗] ,S2[∗] ,…,ST[∗] } tương ứng với chuỗi quan sát O={O1,O2,…,OT}. 

## **Quy trình thực hiện:** 

**B1: Khởi tạo:** Tại thời điểm t=1: 

⋅ δ1(i)=πi bi(O1), ψ1(i)=0 

|---|---|---|
||**VIETTEL AI RACE**|Public 105|
||**THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN**<br>**MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG**<br>**DỤNG VÀO POS TAGGING**|Lần ban hành: 1|

`o` δ1(i): Xác suất lớn nhất khi bắt đầu với trạng thái Si. 

`o` ψ1(i): Truy vết trạng thái trước đó, tại thời điểm khởi đầu, giá trị này bằng 0. 

**B2: Đệ quy:** Từ t=2 đến T (số lượng từ trong câu): 

𝛿𝑡(𝑗) = max 𝑖[[𝛿][𝑡−1][(𝑖) ∙𝑎][𝑖𝑗][∙𝑏][𝑗][(𝑂][𝑡][)], ψ][𝑡][(𝑗) =  𝑎𝑟𝑔max] 𝑖[[𝛿][𝑡−1][(𝑖) ∙𝑎][𝑖𝑗][]] 

`o` δt(j): Xác suất lớn nhất dẫn đến trạng thái Sj tại thời điểm t. `o` ψt(j): Truy vết trạng thái Si tốt nhất trước Sj. 

**B3: Kết thúc:** Tại thời điểm cuối T: 

**==> picture [121 x 19] intentionally omitted <==**

**B4: Truy vết:** Từ t=T−1 đến t=1: 

**==> picture [101 x 14] intentionally omitted <==**

St∗=ψt+1(St+1∗)S_t^* = \psi_{t+1}(S_{t+1}^*)St∗=ψt+1(St+1∗) 

**==> picture [337 x 17] intentionally omitted <==**

**==> picture [71 x 45] intentionally omitted <==**

## 3.3. **Ví dụ minh họa** 

**Đề bài:** Cho câu quan sát: 

**==> picture [68 x 47] intentionally omitted <==**

O={"The", "cat", "runs"} 

**==> picture [156 x 49] intentionally omitted <==**

Với tập nhãn từ loại: 

S={DT (mạo từ),NN (danh từ),VB (động từ)} 

**VIETTEL AI RACE** 

**==> picture [54 x 69] intentionally omitted <==**

**==> picture [38 x 47] intentionally omitted <==**

Public 105 

**THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG DỤNG VÀO POS TAGGING** 

Lần ban hành: 1 

**==> picture [34 x 38] intentionally omitted <==**

## Các tham số mô hình: 

- π={P(DT)=0.6,P(NN)=0.3,P(VB)=0.1}. 

- Ma trận chuyển trạng thái: 

𝑃(𝐷𝑇→ 𝐷𝑇) 𝑃(𝐷𝑇→ 𝑁𝑁) 𝑃(𝐷𝑇→ 𝑉𝐵) 𝑃(𝑁𝑁→ 𝐷𝑇) 𝑃(𝑁𝑁→ 𝑁𝑁) 𝑃(𝑁𝑁→ 𝑉𝐵) 𝐴= [𝑃(𝑉𝐵→ 𝐷𝑇) 𝑃(𝑉𝐵→ 𝑁𝑁) 𝑃(𝑉𝐵→ 𝑉𝐵)] = 0 0.7 0.3 0.1 0.4 0.5 [0.6 0.3 0.1] 

- Ma trận phát xạ: 

**==> picture [139 x 163] intentionally omitted <==**

**==> picture [311 x 106] intentionally omitted <==**

## **Giải:** 

- **Khởi tạo:** 

**==> picture [265 x 37] intentionally omitted <==**

**==> picture [279 x 38] intentionally omitted <==**

**==> picture [93 x 65] intentionally omitted <==**

**==> picture [275 x 29] intentionally omitted <==**

**==> picture [93 x 31] intentionally omitted <==**

- **Đệ quy (tại** t=2 **):** 

|---|---|---|
||**VIETTEL AI RACE**|Public 105|
||**THUẬT TOÁN LIÊN QUAN ĐẾN HIDDEN**<br>**MARKOV MODEL (HMM), CÁC GIẢ ĐỊNH & ỨNG**<br>**DỤNG VÀO POS TAGGING**|Lần ban hành: 1|

𝛿2(𝑁𝑁) =  𝑚𝑎𝑥[𝛿1(𝐷𝑇) ∙𝑎𝐷𝑇→𝑁𝑁, 𝛿1(𝑁𝑁) ∙𝑎𝑁𝑁→𝑁𝑁, 𝛿1(𝑉𝐵) ∙𝑎𝑉𝐵→𝑁𝑁] 

∙𝑏𝑁𝑁("𝑐𝑎𝑡") 

- **Tiếp tục:** 

Lặp lại các bước trên cho đến t=3 để tìm chuỗi nhãn tối ưu. 

**==> picture [139 x 163] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [156 x 49] intentionally omitted <==**