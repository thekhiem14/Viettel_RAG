Public 273 

**VIETTEL AI RACE** 

Lần ban hành: 1 

**Cách đọc Wireshark TCP/HTTP log** 

**==> picture [38 x 47] intentionally omitted <==**

Trong phần này, bạn sẽ học cách đọc **Wireshark TCP/HTTP log** cho lưu lượng mạng giữa khách truy cập website nội bộ và web server của công ty. Hầu hết các công cụ phân tích **network protocol/traffic analyzer** dùng để bắt gói tin đều cung cấp thông tin tương tự. 

## **1. Số thứ tự log và thời gian** 

|**No.**|**Time**|
|---|---|
|47|3.144521|
|48|3.195755|
|49|3.246989|

Phần log của **Wireshark TCP** này bắt đầu tại log số 47, tức là sau 3.144521 giây kể từ khi công cụ ghi nhận bắt đầu hoạt động. Điều này cho thấy có khoảng 47 thông điệp được gửi và nhận bởi web server trong 3.1 giây đầu. Tốc độ này diễn ra rất nhanh nên công cụ phải đo bằng **milliseconds** . 

## **2. Địa chỉ IP nguồn và đích** 

|**Source**|**Destination**|
|---|---|
|198.51.100.23|192.0.2.1|
|192.0.2.1|198.51.100.23|
|198.51.100.23|192.0.2.1|

Cột **Source** và **Destination** thể hiện địa chỉ IP nguồn gửi gói tin và địa chỉ IP đích nhận gói tin. Trong file log này, **192.0.2.1** là web server của công ty, còn dải **198.51.100.0/24** thuộc về máy tính nhân viên. 

## **3. Loại protocol và thông tin liên quan** 

|**Protocol**|**Info**|
|---|---|
|TCP|42584->443 [SYN] Seq=0 Win-5792 Len=120...|
|TCP|443->42584 [SYN, ACK] Seq=0 Win-5792 Len=120...|
|TCP|42584->443 [ACK] Seq=1 Win-5792 Len=120...|
**VIETTEL AI RACE** Public 273 

**Cách đọc Wireshark TCP/HTTP log** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

- Cột **Protocol** cho biết các gói tin đang được gửi bằng **TCP protocol** (thuộc transport layer trong mô hình **TCP/IP** ). Sau khi kết nối thành công, protocol sẽ chuyển sang **HTTP** (application layer). 

- Cột **Info** liệt kê port nguồn và port đích. Ở đây **port 443** là của web server, thường dùng cho web traffic mã hóa. 

## **Ba bước bắt tay TCP (three-way handshake):** 

- **[SYN]** : Máy nhân viên gửi yêu cầu kết nối đến web server. 

- **[SYN, ACK]** : Web server phản hồi chấp nhận yêu cầu và dự trữ tài nguyên. 

- • **[ACK]** : Máy nhân viên xác nhận, hoàn tất kết nối TCP. 

## **4. Lưu lượng website bình thường** 

Ví dụ một giao dịch bình thường 

|**No.**|**Time**|**Source**|**Destination**|**Protocol**|**Info**|
|---|---|---|---|---|---|
|47|3.144521|198.51.100.23|192.0.2.1|TCP|42584->443 [SYN] Seq=0 Win=5792<br>Len=120...|
|48|3.195755|192.0.2.1|198.51.100.23|TCP|443->42584 [SYN, ACK] Seq=0 Win-<br>5792 Len=120...|
|49|3.246989|198.51.100.23|192.0.2.1|TCP|42584->443 [ACK] Seq=1 Win-5792<br>Len=120...|
|50|3.298223|198.51.100.23|192.0.2.1|HTTP|GET /sales.html HTTP/1.1|
|51|3.349457|192.0.2.1|198.51.100.23|HTTP|HTTP/1.1 200 OK (text/html)|

## **5. Cuộc tấn công** 

Kẻ tấn công có thể lợi dụng TCP bằng cách gửi **SYN flood** (rất nhiều gói SYN) khiến web server không còn tài nguyên để phản hồi. Đây là **DoS attack** (tấn công từ chối dịch vụ) ở mức **network layer** . 

- Nếu từ một nguồn duy nhất: **DoS direct attack** . 

- Nếu từ nhiều nguồn: **DDoS attack** , khó phát hiện hơn. 
**VIETTEL AI RACE** Public 273 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 **Cách đọc Wireshark TCP/HTTP log** 

**==> picture [362 x 126] intentionally omitted <==**

## **TCP log đánh dấu màu** 

Trong log có hai tab: 

- Một tab bình thường. 

- Một tab **Color coded TCP log** : hiển thị tương tác giữa server và IP attacker **203.0.113.0** (đánh dấu màu đỏ). 

|**Color**<br>**as text**|**No.**|**Time**|**Source**<br>**(x= redacted)**|**Destination**<br>**(x = redacted)**|**Protocol**|**Info**|
|---|---|---|---|---|---|---|
||<br>52|||||54770->443<br>[SYN]<br>Seq=0|
|red||3.390692|203.0.113.0|192.0.2.1|TCP|<br> <br>Win=5792 Len=0...|
||<br>53|||||443->54770<br>[SYN,<br>ACK]|
|red||3.441926|192.0.2.1|203.0.113.0|TCP|<br> <br>Seq=0 Win-5792 Len=120...|
||<br>54|||||54770->443<br>[ACK<br>Seq=1|
|red||3.493160|203.0.113.0|192.0.2.1|TCP|<br> <br>Win=5792 Len=0...|
||<br>55|||||14785->443<br>[SYN]<br>Seq=0|
|green||3.544394|198.51.100.14|192.0.2.1|TCP|<br> <br>Win-5792 Len=120...|
||<br>56|||||443->14785<br>[SYN,<br>ACK]|
|green||3.599628|192.0.2.1|198.51.100.14|TCP|<br> <br>Seq=0 Win-5792 Len=120...|
||<br>57|||||54770->443<br>[SYN]<br>Seq=0|
|red||3.664863|203.0.113.0|192.0.2.1|TCP|<br> <br>Win=5792 Len=0...|
||<br>58|||||14785->443<br>[ACK]<br>Seq=1|
|green||3.730097|198.51.100.14|192.0.2.1|TCP|<br> <br>Win-5792 Len=120...|
||<br>59|||||54770->443<br>[SYN]<br>Seq=0|
|red||3.795332|203.0.113.0|192.0.2.1|TCP|<br> <br>Win-5792 Len=120...|
|green|<br>60|3.860567|198.51.100.14|192.0.2.1|HTTP|GET /sales.html HTTP/1.1|
|red|<br>61|3.939499|203.0.113.0|192.0.2.1|TCP|54770->443<br>[SYN]<br>Seq=0|
**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|Public 273|
|---|---|---|
||**Cách đọc Wireshark TCP/HTTP log**|Lần ban hành: 1|

|||||||Win-5792 Len=120...|
|---|---|---|---|---|---|---|
|green|<br>62<br>|4.018431|192.0.2.1|198.51.100.14|HTTP|HTTP/1.1 200 OK (text/html)|

|**Color**<br>**as text**|**No.**|**Time**|**Source**|**Destination**|**Protocol**|**Info**|
|---|---|---|---|---|---|---|
|||4.097363||||33638->443 [SYN] Seq=0|
|green|<br>63||198.51.100.5|192.0.2.1|TCP|<br>Win-5792 Len=120...|
|||4.176295||||443->54770 [SYN, ACK]|
|red|<br>64||192.0.2.1|203.0.113.0|TCP|<br>Seq=0 Win-5792 Len=120...|
|||4.255227||||443->33638 [SYN, ACK]|
|green|<br>65||192.0.2.1|198.51.100.5|TCP|<br>Seq=0 Win-5792 Len=120...|
|||4.256159||||54770->443 [SYN] Seq=0|
|red|<br>66||203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||5.235091||||33638->443 [ACK] Seq=1|
|green|<br>67||198.51.100.5|192.0.2.1|TCP|<br>Win-5792 Len=120...|
|||5.236023||||54770->443 [SYN] Seq=0|
|red|<br>68||203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||5.236955||||32641->443 [SYN] Seq=0|
|green|<br>69||198.51.100.16|192.0.2.1|TCP|<br>Win-5792 Len=120...|
|||5.237887||||54770->443 [SYN] Seq=0|
|red|<br>70||203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|green|<br>71|6.228728|198.51.100.5|192.0.2.1|HTTP|GET /sales.html HTTP/1.1|
|||6.229638||||54770->443 [SYN] Seq=0|
|red|<br>72||203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||6.230548||||443->32641 [RST, ACK]|
|yellow|<br>73||192.0.2.1|198.51.100.16|TCP|<br>Seq=0 Win-5792 Len=120...|
|||6.330539||||54770->443 [SYN] Seq=0|
|red|<br>74||203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||6.330885||||42584->443 [SYN] Seq=0|
|green|<br>75||198.51.100.7|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||6.331231||||54770->443 [SYN] Seq=0|
|red|<br>76||203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
**VIETTEL AI RACE** Public 273 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 **Cách đọc Wireshark TCP/HTTP log** 

|||||||HTTP/1.1<br>504<br>Gateway|
|---|---|---|---|---|---|---|
|yellow|<br>77|7.330577|192.0.2.1|198.51.100.5|TCP|<br>Time-out (text/html)|
|||||||54770->443 [SYN] Seq=0|
|red|<br>78|7.331323|203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||||||6345->443 [SYN] Seq=0|
|green|<br>79|7.340768|198.51.100.22|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||||||443->42584 [RST, ACK]|
|yellow|<br>80|7.340773|192.0.2.1|198.51.100.7|TCP|<br>Seq=1 Win-5792 Len=120...|
|||||||54770->443 [SYN] Seq=0|
|red|<br>81|7.340778|203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||||||54770->443 [SYN] Seq=0|
|red|<br>82|7.340783|203.0.113.0|192.0.2.1|TCP|<br>Win=5792 Len=0...|
|||||||443->54770 [RST, ACK]|
|red|<br>83|7.439658|192.0.2.1|203.0.113.0|TCP|<br>Seq=1 Win=5792 Len=0...|

|**Color**<br>**as text**|**No.**|**Time**|**Source**<br>**(x = redacted)**|**Destination**<br>**(x = redacted)**|**Protoco**<br>**l**|**Info**|
|---|---|---|---|---|---|---|
|||19.198705||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>119||203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||19.521718||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>120||203.0.113.0|192.0.2.1|TCP||
|||||||Len=0...|
|||19.844731||||443->4631 [RST, ACK]|
|||||||Seq=1<br>Win=5792|
|yellow|<br>121||192.0.2.1|198.51.100.9|TCP|<br>Len=0...|
|||20.167744||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>122||203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||20.490757||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>123||203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|Public 273|
|---|---|---|
||**Cách đọc Wireshark TCP/HTTP log**|Lần ban hành: 1|

|||||||443->54770<br>[RST,|
|---|---|---|---|---|---|---|
|||||||ACK] Seq=1 Win=5792|
|red|<br>124|20.81377|192.0.2.1|203.0.113.0|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>125|21.136783|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>126|21.459796|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>127|21.782809|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>128|22.105822|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>129|22.428835|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>130|22.751848|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>131|23.074861|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>132|23.397874|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>133|23.720887|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>134|24.0439|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|red|<br>135|24.366913|203.0.113.0|192.0.2.1|TCP|<br>Seq=0<br>Win=5792|
**VIETTEL AI RACE** Public 273 Lần ban hành: 1 **Cách đọc Wireshark TCP/HTTP log** 

**==> picture [38 x 47] intentionally omitted <==**

|||||||Len=0...|
|---|---|---|---|---|---|---|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>136|24.689926|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>137|25.012939|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>138|25.335952|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>139|25.658965|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>140|25.981978|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>141|26.304991|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>142|26.628004|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>143|26.951017|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>144|27.27403|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>145|27.597043|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>146|27.920056|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|red|<br>147|28.243069|203.0.113.0|192.0.2.1|TCP|54770->443<br>[SYN]|
**VIETTEL AI RACE** Public 273 Lần ban hành: 1 **Cách đọc Wireshark TCP/HTTP log** 

**==> picture [38 x 47] intentionally omitted <==**

|||||||Seq=0<br>Win=5792|
|---|---|---|---|---|---|---|
|||||||Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>148|28.566082|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>149|28.889095|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>150|29.212108|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>151|29.535121|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|
|||||||54770->443<br>[SYN]|
|||||||Seq=0<br>Win=5792|
|red|<br>152|29.858134|203.0.113.0|192.0.2.1|TCP|<br>Len=0...|

Từ log số 125 trở đi, web server không còn phản hồi traffic hợp lệ nữa, chỉ ghi nhận các gói **SYN** từ attacker. Vì chỉ có một IP tấn công, đây là **direct DoS SYN flood attack** .