**VIETTEL AI RACE** Public 496 **GIỚI THIỆU VỀ HỌC TĂNG CƯỜNG (** Lần ban hành: 1 **REINFORCEMENT LEARNING – RL )** 

**==> picture [38 x 47] intentionally omitted <==**

## **1. GIỚI THIỆU VỀ HỌC TĂNG CƯỜNG - RL** 

**==> picture [40 x 44] intentionally omitted <==**

Học tăng cường (Reinforcement Learning – RL) là một lĩnh vực quan trọng trong trí tuệ nhân tạo, tập trung vào việc huấn luyện một tác nhân (agent) học cách đưa ra chuỗi hành động trong môi trường để tối đa hóa phần thưởng tích lũy. RL được ứng dụng trong nhiều lĩnh vực: chơi game (AlphaGo, Dota2 AI), robot tự hành, tối ưu chuỗi sản xuất, tài chính, y học cá nhân hóa… 

Khác với học có giám sát (supervised learning), RL không có nhãn cố định cho từng dữ liệu. Thay vào đó, agent phải khám phá (exploration) và khai thác (exploitation) thông tin trong môi trường để cải thiện chính sách hành động. 

## **2. MẠNG NƠ-RON NHÂN TẠO** 

## **2.1 Yêu cầu trước khi làm thí nghiệm** 

Yêu cầu trước khi thực hành: 

- Kiến thức nền tảng: đại số tuyến tính, xác suất – thống kê, học có giám sát. 

- Kỹ năng lập trình: Python, NumPy, hiểu cơ bản TensorFlow/PyTorch. 

- Công cụ: Python 3.x, Jupyter Notebook, thư viện gym (OpenAI Gym). 

**==> picture [92 x 35] intentionally omitted <==**

- Dữ liệu / môi trường: sử dụng các môi trường RL chuẩn như CartPole, MountainCar, Atari. 

## **2.2 Mục đích của phần thí nghiệm** 

Mục đích của phần thí nghiệm: 

- Hiểu rõ khái niệm Markov Decision Process (MDP). 

- Nắm được các hàm giá trị 𝑉[𝜋] (s), 𝑄[𝜋] (s,a) 

- Làm quen với các phương trình Bellman và ý nghĩa tối ưu. 

- Áp dụng các thuật toán Q-learning, SARSA, Policy Gradient, ActorCritic. 

- Biết các kỹ thuật regularization và exploration trong RL. 

## **2.3 Tóm tắt lý thuyết** 

## **2.3.1 Định nghĩa** 
Public 496 

**VIETTEL AI RACE** 

**GIỚI THIỆU VỀ HỌC TĂNG CƯỜNG ( REINFORCEMENT LEARNING – RL )** 

Lần ban hành: 1 

**==> picture [38 x 47] intentionally omitted <==**

Công thức Định nghĩa 𝑀𝐷𝑃= (𝑆, 𝐴, 𝑃, 𝑅, γ) Mô hình RL được mô tả dưới dạng Markov Decision Process: tập trạng thái S, tập hành động A, xác suất chuyển trạng thái P, phần thưởng R, hệ số chiết khấu γ. Hàm giá trị trạng thái: kỳ vọng phần 𝑉[𝜋] (𝑠) = 𝐸𝜋[∑∞𝑡=0 𝛾[𝑡] 𝑅𝑡+1 | 𝑆0 = 𝑠] thưởng tích lũy khi bắt đầu từ trạng thái sss và theo chính sách π. Hàm giá trị hành động: kỳ vọng 𝑄[π] (𝑠, 𝑎) = 𝐸π[∑∞𝑡=0 γ[𝑡] 𝑅𝑡+1 | 𝑆0 = 𝑠, 𝐴0 = 𝑎] phần thưởng tích lũy khi bắt đầu từ trạng thái s, chọn hành động aaa và theo chính sách π. 

## **2.3.2 Thuật toán RL** 

**==> picture [86 x 33] intentionally omitted <==**

Cập nhật Q- 𝑄(𝑠[′] , 𝑎[′] learning: học 𝑄(𝑠, 𝑎) ←𝑄(𝑠, 𝑎) + 𝛼[𝑟+ 𝛾𝑚𝑎𝑥𝑎[′] ) −𝑄(𝑠, 𝑎)] chính sách tối ưu bằng cách cập nhật giá trị Q. Cập nhật 𝑄(𝑠, 𝑎) ←𝑄(𝑠, 𝑎) + 𝛼[𝑟+ 𝛾𝑄(𝑠[′] , 𝑎[′] ) −𝑄(𝑠, 𝑎)] SARSA: học theo chính sách đang thực hiện, 
Public 496 

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

**==> picture [235 x 30] intentionally omitted <==**

**----- Start of picture text -----**<br>
GIỚI THIỆU VỀ HỌC TĂNG CƯỜNG (<br>REINFORCEMENT LEARNING – RL )<br>**----- End of picture text -----**<br>

Lần ban hành: 1 

**==> picture [426 x 339] intentionally omitted <==**

**----- Start of picture text -----**<br>
khác với Q-<br>learning .<br>Actor-Critic:<br>sai số TD<br>𝛻𝐽(𝜃) = 𝐸𝜋[𝛻𝜃 𝑙𝑜𝑔𝜋𝜃 (𝑎|𝑠) 𝑄 [𝜋] (𝑠, 𝑎)]<br>(Temporal<br>Difference) để<br>cập nhật Critic.<br>Hàm  𝛿𝑡 = 𝑟𝑡 + 𝛾𝑉(𝑠𝑡+1) −𝑉(𝑠𝑡)<br>Advantage:<br>đo lường<br>mức độ tốt<br>hơn trung<br>bình của<br>hành động a<br>tại trạng thái<br>s.<br>**----- End of picture text -----**<br>

## **2.3.3 REGULARIZATION & EXPLORATION** 

## _2.3.3.1. Entropy Regularization:_ 

**[CT1]** 𝐻(𝜋(𝑠)) = −∑𝜋(𝑎|𝑠) 𝑙𝑜𝑔𝜋(𝑎|𝑠) 𝑎 

**==> picture [192 x 116] intentionally omitted <==**
**VIETTEL AI RACE** Public 496 

**GIỚI THIỆU VỀ HỌC TĂNG CƯỜNG ( REINFORCEMENT LEARNING – RL )** 

Lần ban hành: 1 

**==> picture [38 x 47] intentionally omitted <==**

**==> picture [384 x 253] intentionally omitted <==**

## _2.3.3.2. Epsilon-Greedy Policy_ 

π(𝑎|𝑠) = (1 −ϵ +\𝑡𝑓𝑟𝑎𝑐ϵ|𝐴|)1 [𝑎= arg max𝑎 𝑄(𝑠, 𝑎)] +\𝑡𝑓𝑟𝑎𝑐ϵ|𝐴| 

**==> picture [92 x 35] intentionally omitted <==**

## _2.3.3.3. Softmax Exploration:_ 

**==> picture [113 x 32] intentionally omitted <==**

**[CT2]** 

## _2.3.3.4. Weight Decay (L2)_ 

𝜃𝑡+1 = (1 −𝜂𝜆)𝜃𝑡 −𝜂∇𝜃𝐿(𝜃𝑡) **[CT3]** 

**==> picture [56 x 45] intentionally omitted <==**

## **2.3.4. Phương pháp học nâng cao trong RL** 

hàm advantage: đo lường mức 𝐴[𝜋] (𝑠, 𝑎) = 𝑄[𝜋] (𝑠, 𝑎) −𝑉[𝜋] (𝑠) độ “tốt hơn trung bình” của hành động a tại trạng thái s. được dùng trong actor-critic và policy gradient. 
Public 496 

**VIETTEL AI RACE** 

**GIỚI THIỆU VỀ HỌC TĂNG CƯỜNG ( REINFORCEMENT LEARNING – RL )** 

Lần ban hành: 1 

**==> picture [38 x 47] intentionally omitted <==**

sai số td (temporal difference): 𝛻𝐽(𝜃) = 𝐸𝑠,𝑎∼𝜋𝜃[𝛻𝜃 𝑙𝑜𝑔𝜋𝜃 (𝑎|𝑠) 𝐴[𝜋] (𝑠, 𝑎)] dùng để cập nhật critic trong actor-critic. hàm mất mát trong proximal policy optimization (ppo): giới 𝐿[𝑝𝑝𝑜] (𝜃) = 𝐸𝑡[𝑚𝑖𝑛! (𝑟𝑡(𝜃)𝐴𝑡,  clip(𝑟𝑡(𝜃), 1 −𝜖, 1 hạn cập nhật chính sách để + 𝜖)𝐴𝑡)] tránh bước nhảy quá lớn. _MSE_ thường dùng cho hồi 𝑁 quy; nhạy cảm với ngoại lai do 𝐿=[1] 𝑖 −𝑦̂)𝑖[2] 𝑁 ∑(𝑦 bình phương sai số. 𝑖=1 _Hinge loss_ dùng trong 𝑁 SVM/NN phân biệt biên cứng; 𝑖𝑦̂)𝑖 𝐿= ∑𝑚𝑎𝑥(0,1 −𝑦 khuyến khích lề phân tách lớn. 𝑖=1 

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**