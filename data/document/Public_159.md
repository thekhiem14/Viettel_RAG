**VIETTEL AI RACE** TD159 **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

## **1. CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG** 

## **1.1 Khái quát về mã hóa khóa bất đối xứng** 

Mã hóa khóa bất đối xứng, đôi khi được gọi là mã hóa khóa công khai sử dụng một cặp khóa cho quá trình mã hóa và giải mã. Trong cặp khóa, khóa công khai được sử dụng cho mã hóa và khóa riêng được sử dụng cho giải mã. Chỉ khóa riêng cần giữ bí mật, còn khóa công khai có thể phổ biến rộng rãi, nhưng phải đảm bảo tính toàn vẹn và xác thực chủ thể của khóa. 

Hình 3.27 minh họa quá trình mã hóa (Encrypt) và giải mã (Decrypt) sử dụng mã hóa khóa bất đối xứng. Theo đó, người gửi (Sender) sử dụng khóa công khai (Public key) của người nhận (Recipient) để mã hóa bản rõ (Plaintext) thành bản mã (Ciphertext) và gửi nó cho người nhận. Người nhận nhận được bản mã sử dụng khóa riêng (Private key) của mình để giải mã khôi phục bản rõ. 

Đặc điểm nổi bật của các hệ mã hóa khóa bất đối xứng là kích thước khóa lớn, lên đến hàng ngàn bit. Do vậy, các hệ mã hóa dạng này thường có tốc độ thực thi chậm hơn nhiều lần so với các hệ mã hóa khóa đối xứng với độ an toàn tương đương. Mặc dù vậy, các hệ mã hóa khóa bất đối xứng có khả năng đạt độ an toàn cao và ưu điểm nổi bật nhất là việc quản lý và phân phối khóa đơn giản hơn do khóa công khai có thể phân phối rộng rãi. 

**==> picture [307 x 210] intentionally omitted <==**

_Hình 3.27. Mã hóa và giải mã trong hệ mã hóa bất đối xứng_ 

Các giải thuật mã hóa khóa bất đối xứng điển hình bao gồm: RSA, Rabin, ElGamal, McEliece và Knapsack. Trong mục tiếp theo chúng ta tìm hiểu về giải thuật mã hóa RSA – một trong các giải thuật mã hóa khóa đối xứng được sử dụng rộng rãi nhất trên thực tế. 

**VIETTEL AI RACE** TD159 **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

**==> picture [52 x 71] intentionally omitted <==**

## **1.2 Giải thuật mã hóa RSA** 

## **1.2.1 Giới thiệu** 

Giải thuật mã hóa RSA được 3 nhà khoa học người Mỹ là Ronald Rivest, Adi Shamir và Leonard Adleman phát minh năm 1977, và tên giải thuật RSA lấy theo chữ cái đầu của tên 3 đồng tác giả. Độ an toàn của RSA dựa trên tính khó của việc phân tích số nguyên rất lớn, với độ lớn cỡ hàng trăm chữ số thập phân. Giải thuật RSA sử dụng một cặp khóa, trong đó khóa công khai dùng để mã hóa và khóa riêng dùng để giải mã. Chỉ khóa riêng RSA cần giữ bí mật. Khóa công khai có thể công bố rộng rãi. Hiện nay, các khóa RSA có kích thước nhỏ hơn 1024 bit được coi là không an toàn do tốc độ các hệ thống máy tính tăng nhanh. Để đảm bảo an toàn, khuyến nghị sử dụng khóa 2048 bit trong giai đoạn 2010-2020. Trong tương lai, cần sử dụng khóa RSA có kích thước lớn hơn, chẳng hạn 3072 bit. 

## **1.2.2 Sinh khóa** 

RSA cung cấp một thủ tục sinh cặp khóa (khóa công khai và khóa riêng) tương đối đơn giản. Cụ thể, thủ tục sinh khóa gồm các bước như sau: 

   - Tạo 2 số nguyên tố _p_ và _q_ ; 

   - Tính modulo _n_ = _p_ × _q_ 

- Tính  ( _n_ ) = ( _p_ -1) × ( _q_ -1) 

   - Chọn số _e_ sao cho 0 < _e_ <  ( _n_ ) và gcd( _e_ ,  ( _n_ )) = 1, trong đó hàm gcd() tính ước số chung lớn nhất của 2 số nguyên. Nếu gcd( _e_ ,  ( _n_ )) = 1 thì _e_ và  ( _n_ ) là 2 số nguyên tố cùng nhau. 

   - Chọn số _d_ sao cho _d_  _e_[-1] mod  ( _n_ ), 

hoặc ( _d_ × _e_ ) mod  ( _n_ ) = 1 

hay _d_ là modulo nghịch đảo của _e_ . 

- Ta có ( _n_ , _e_ ) là khóa công khai, ( _n_ , _d_ ) là khóa riêng và _n_ còn được gọi là modulo. 

**==> picture [78 x 49] intentionally omitted <==**

## **1.2.3 Mã hóa và giải mã** 

- Mã hóa 

`+` Thông điệp bản rõ _m_ đã được chuyển thành số, với _m_ < _n_ . Nếu thông điệp bản rõ _m_ có kích thước lớn thì được chia thành các khối _mi_ , với _mi_ < _n_ . 

- `+` Bản mã _c_ = _m[e]_ mod _n_ 

   - Giải mã 

- `+` Bản mã _c_ , với _c_ < _n_ 

**VIETTEL AI RACE** TD159 

**==> picture [38 x 47] intentionally omitted <==**

## **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

Lần ban hành: 1 

`+` Bản rõ _m_ = _c[d]_ mod _n_ 

**1.2.4 Ví dụ** 

   - Sinh khóa: 

- `+` Chọn 2 số nguyên tố _p_ = 3 và _q_ = 11 

- `+` Tính _n_ = _p_ × q = 3 × 11 = 33 

- `+` Tính  ( _n_ ) = ( _p_ -1) × ( _q_ -1) = 2 × 10 = 20 

`+` Chọn số _e_ sao cho 0 < _e_ < 20, và _e_ và  ( _n_ ) là số nguyên tố cùng nhau 

(  ( _n_ ) không chia hết cho _e_ ). Chọn _e_ = 7 

- `+` Tính ( _d_ x e) mod  (n) → ( _d_ × 7) mod 20 = 1 

- _d_ = (20 × _k_ +1)/7 → _d_ = 3 ( _k_ =1) 

- `+` Ta có: khóa công khai là (33, 7) và khóa riêng là (33, 3) 

   - Mã hóa: 

- `+` Với bản rõ _m_ = 6, 

`+` _c_ = _m[e]_ mod _n_ = 6[7] mod 33 = 279936 mod 33 = 30 

`+` Vậy bản mã _c_ = 30 

   - Giải mã: 

- `+` Với bản mã _c_ = 30 

- `+` _m_ = _c[d]_ mod _n_ = 30[3] mod 33 = 27000 mod 33 = 6 

- `+` Vậy bản rõ _m_ = 6. 

## **1.2.5 Một số yêu cầu với quá trình sinh khóa** 

Dưới đây liệt kê các yêu cầu đặt ra với các tham số sinh khóa và khóa để đảm bảo sự an toàn cho cặp khóa RSA. Các yêu cầu cụ thể gồm: 

- Yêu cầu với các tham số sinh khóa _p_ và _q_ : 

`+` Các số nguyên tố _p_ và _q_ phải được chọn sao cho việc phân tích _n_ ( _n_ = _p_ × _q_ ) là không khả thi về mặt tính toán. _p_ và _q_ nên có cùng độ lớn (tính bằng bit) và phải là các số đủ lớn. Nếu _n_ có kích thước 2048 bit thì _p_ và _q_ nên có kích thước khoảng 1024 bit. 

`+` Hiệu số _p – q_ không nên quá nhỏ, do nếu _p – q_ quá nhỏ, tức _p_  _q_ và _p_  √𝑛. Như vậy, có thể chọn các số nguyên tố ở gần √𝑛 và thử. Khi có được _p_ , có thể tính _q_ và tìm ra _d_ là khóa bí mật từ khóa công khai _e_ và  ( _n_ ) = ( _p_ - 1)( _q_ - 1). Nếu _p_ và _q_ được chọn ngẫu nhiên và _p_ – _q_ đủ lớn, khả năng hai số này bị phân tích từ _n_ giảm đi. 

- Vấn đề sử dụng số mũ mã hóa ( _e_ ) nhỏ: Khi sử dụng số mũ mã hóa ( _e_ ) nhỏ, chẳng hạn 

**VIETTEL AI RACE** TD159 **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

_e_ = 3 có thể tăng tốc độ mã hóa. Kẻ tấn công có thể nghe lén và lấy được bản mã, từ đó phân tích bản mã để khôi phục bản rõ. Do số mũ mã hóa nhỏ nên chi phí cho phân tích, hoặc vét cạn không quá lớn. Do vậy, nên sử dụng số mũ mã hóa _e_ đủ lớn và thêm chuỗi ngẫu nhiên vào khối rõ trước khi mã hóa để giảm khả năng bị vét cạn hoặc phân tích bản mã. 

   - Vấn đề sử dụng số mũ giải mã ( _d_ ) nhỏ: Khi sử dụng số mũ giải mã ( _d_ ) nhỏ, có thể tăng tốc độ giải mã. Nếu _d_ nhỏ và gcd( _p_ -1, _q_ -1) cũng nhỏ thì _d_ có thể tính được tương đối dễ dàng từ khóa công khai ( _n_ , _e_ ). Do vậy, để đảm bảo an toàn, nên sử dụng số mũ giải mã _d_ đủ lớn. 

**2. Các hàm băm** 

## **2.1 Khái quát về hàm băm** 

## **2.1.1 Giới thiệu** 

Hàm băm (hash function) là một hàm toán học _h_ có tối thiểu 2 thuộc tính: 

- Nén (Compression): _h_ là một ánh xạ từ chuỗi đầu vào _x_ có chiều dài bất kỳ sang một chuỗi đầu ra _h_ ( _x_ ) có chiều dài cố định _n_ bit; 

- Dễ tính toán (Ease of computation): cho trước hàm _h_ và đầu vào _x_ , việc tính toán 

_h_ ( _x_ ) là dễ dàng. 

**==> picture [226 x 200] intentionally omitted <==**

_Hình 3.28. Mô hình nén thông tin của hàm băm_ 

Hình 3.28 minh họa mô hình nén thông tin của hàm băm, theo đó thông điệp (Message) đầu vào với chiều dài tùy ý đi qua nhiều vòng xử lý của hàm băm để tạo chuỗi rút gọn, hay chuỗi đại diện (Digest) có kích thước cố định ở đầu ra. 

**VIETTEL AI RACE** TD159 **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

**==> picture [38 x 47] intentionally omitted <==**

## **2.1.2 Phân loại** 

Lần ban hành: 1 

**==> picture [36 x 43] intentionally omitted <==**

Có thể phân loại các hàm băm theo khóa sử dụng hoặc theo chức năng. Theo khóa sử dụng, các hàm băm gồm 2 loại: hàm băm không khóa (unkeyed) và hàm băm có khóa (keyed), như biểu diễn trên Hình 3.29. Trong khi hàm băm không khóa nhận đầu vào chỉ là thông điệp (dạng _h_ ( _x_ ), với hàm băm _h_ và thông điệp _x_ ), hàm băm có khóa nhận đầu vào gồm thông điệp và khóa bí mật (theo dạng _h_ ( _x_ , _K_ ), với hàm băm _h_ và thông điệp _x_ và _K_ là khóa bí mật). Trong các hàm băm không khóa, các mã phát hiện sửa đổi (MDC – Modification Detection Code) được sử dụng rộng rãi nhất, bên cạnh một số hàm băm không khóa khác. Tương tự, trong các hàm băm có khóa, các mã xác thực thông điệp (MAC - Message Authentication Code) được sử dụng rộng rãi nhất, bên cạnh một số hàm băm có khóa khác. 

**==> picture [109 x 39] intentionally omitted <==**

**==> picture [296 x 140] intentionally omitted <==**

_Hình 3.29. Phân loại các hàm băm theo khóa sử dụng_ 

Theo chức năng, có thể chia các hàm băm thành 2 loại chính: 

- Mã phát hiện sửa đổi (MDC - Modification Detection Code): MDC thường được sử dụng để tạo chuỗi đại diện cho thông điệp và dùng kết hợp với các kỹ thuật khác (như chữ ký số) để đảm bảo tính toàn vẹn của thông điệp. MDC thuộc loại hàm băm không khóa. MDC gồm 2 loại nhỏ: 

`+` Hàm băm một chiều (OWHF - One-way hash functions): Với hàm băm một chiều, việc tính giá trị băm là dễ dàng, nhưng việc khôi phục thông điệp từ giá trị băm là rất khó khăn; 

`+` Hàm băm chống đụng độ (CRHF - Collision resistant hash functions): Với hàm băm chống đụng độ, sẽ là rất khó để tìm được 2 thông điệp khác nhau nhưng có cùng giá trị băm. 

- Mã xác thực thông điệp (MAC - Message Authentication Code): MAC cũng được dùng để đảm bảo tính toàn vẹn của thông điệp mà không cần một kỹ thuật bổ sung nào khác. MAC là loại hàm băm có khóa như đã 

**VIETTEL AI RACE** TD159 **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

đề cập ở trên, với đầu vào là thông điệp và một khóa bí mật. 

## **2.1.3 Mô hình xử lý dữ liệu** 

Hình 3.30 biểu diễn mô hình tổng quát xử lý dữ liệu của các hàm băm. Theo đó, thông điệp đầu vào với độ dài tùy ý (arbitrary length input) đi qua hàm nén lặp nhiều vòng (iterated compression function) để tạo chuỗi đầu ra có kích thước cố định (fixed length output). Chuỗi này đi qua một khâu chuyển đổi định dạng tùy chọn (optional output transformation) để tạo ra chuỗi băm kết quả (output). 

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [140 x 198] intentionally omitted <==**

_Hình 3.30. Mô hình tổng quát xử lý dữ liệu của hàm băm_ 

Hình 3.31 mô tả chi tiết quá trình xử lý dữ liệu của các hàm băm. Theo đó, quá trình xử lý gồm 3 bước chính: (1) tiền xử lý (preprocessing), (2) xử lý lặp (iterated processing) và (3) chuyển đổi định dạng. Trong bước tiền xử lý, thông điệp đầu vào _x_ trước hết được nối đuôi thêm một số bit và kích thước khối, sau đó chia thành các khối có kích thước xác định. Kết quả của bước này là _t_ khối dữ liệu có cùng kích thước có dạng _x_ = _x1x2…xt_ làm đầu vào cho bước 2. Trong bước 2, từng khối dữ liệu _xi_ được xử lý thông qua hàm nén _f_ 

để tạo đầu ra là _Hi_ . Kết quả của bước 2 là chuỗi đầu ra _Ht_ và _Ht_ được chuyển đổi định dạng bởi hàm _g_ để tạo chuỗi giá trị băm hết quả _h_ ( _x_ ). 

**==> picture [146 x 86] intentionally omitted <==**

**==> picture [38 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

Lần ban hành: 1 

**==> picture [188 x 309] intentionally omitted <==**

_Hình 3.31. Mô hình chi tiết xử lý dữ liệu của hàm băm_ 

## **2.2 Một số hàm băm thông dụng** 

Các hàm băm thông dụng giới thiệu trong mục này đều là các hàm băm không khóa, gồm các họ hàm băm chính như sau: 

- Họ hàm băm MD (Message Digest) gồm các hàm băm MD2, MD4, MD5 và MD6. 

- Họ hàm băm SHA (Secure Hash Algorithm) gồm các hàm băm SHA0, SHA1, SHA2 và SHA3. 

- Một số hàm băm khác, gồm CRC (Cyclic redundancy checks), Checksums,... 

Các mục con tiếp theo của mục này giới thiệu 2 hàm băm đã và đang được sử dụng rộng rãi nhất là hàm băm MD5 và SHA1. 

**==> picture [71 x 49] intentionally omitted <==**

## **2.2.1 Hàm băm MD5** 

## * Giới thiệu 

MD5 (Message Digest) là hàm băm không khóa được Ronald Rivest thiết kế năm 1991 để thay thế MD4. Chuỗi giá trị băm đầu ra của MD5 là 128 bit (16 byte) và thường được biểu diễn thành 32 số hexa. MD5 được sử dụng khá rộng rãi trong nhiều ứng dụng, như tạo chuỗi đảm bảo tính toàn vẹn thông điệp, tạo chuỗi kiểm 

**VIETTEL AI RACE** TD159 **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

tra lỗi, hoặc kiểm tra tính toàn vẹn dữ liệu (Checksum) và mã hóa mật khẩu trong các hệ điều hành và các ứng dụng. MD5 hiện nay được khuyến nghị không nên sử dụng do nó không còn đủ an toàn. 

Nhiều điểm yếu của MD5 đã bị khai thác, như điển hình MD5 bị khai thác bởi mã độc Flame vào năm 2012. 

* Quá trình xử lý thông điệp 

Quá trình xử lý thông điệp của MD5 gồm 2 khâu là _tiền xử lý_ và _các vòng lặp xử lý_ . 

Cụ thể, chi tiết về các khâu này như sau: 

   - Tiền xử lý: Thông điệp được chia thành các khối 512 bit (16 từ 32 bit). Nếu kích thước thông điệp không là bội số của 512 thì nối thêm số bit còn thiếu. 

   - Các vòng lặp xử lý: Phần xử lý chính của MD5 làm việc trên _state_ 128 bit, chia thành 4 từ 32 bit (A, B, C, D): 

- `+` Các từ A, B, C, D được khởi trị bằng một hằng cố định; 

- `+` Từng phần 32 bit của khối đầu vào 512 bit được đưa dần vào để thay đổi _state_ ; 

- `+` Quá trình xử lý gồm 4 vòng, mỗi vòng gồm 16 thao tác tương tự nhau. 

- `+` Mỗi thao tác gồm: Xử lý bởi hàm F (4 dạng hàm khác nhau cho mỗi vòng), Cộng modulo và Quay trái. Hình 3.32 biểu diễn lưu đồ xử lý của một thao tác của MD5, trong đó A, B, C, D là các từ 32 bit của _state_ , Mi: khối 32 bit thông điệp đầu vào, Ki là 32 bit hằng khác nhau cho mỗi thao tác, <<<s là thao tác dịch trái _s_ bit, biểu diễn phép cộng modulo 32 bit và F là hàm phi tuyến tính. 

**==> picture [227 x 251] intentionally omitted <==**

**VIETTEL AI RACE** TD159 **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM BĂM** 

**==> picture [38 x 47] intentionally omitted <==**

Lần ban hành: 1 

_Hình 3.32. Lưu đồ xử lý một thao tác của MD5_ 

Hàm F gồm 4 dạng được dùng cho 4 vòng lặp. Cụ thể, F có các dạng như 

sau: F(B, C, D) = (B  C)  (  B  D) 

G(B, C, D) = (B  D)  (C   D) 

H(B, C, D) = B  C  D 

I(B, C, D) = C  (B   D) 

trong đó, các ký hiệu  ,  ,  ,  biểu diễn các phép toán lô gíc XOR, AND, OR và NOT tương ứng. 

## **2.2.2 Hàm băm SHA1** 

## * Giới thiệu 

SHA1 (Secure Hash Function) được Cơ quan mật vụ Mỹ thiết kế năm 1995 để thay thế cho hàm băm SHA0. Chuỗi giá trị băm đầu ra của SHA1 có kích thước 160 bit và thường được biểu diễn thành 40 số hexa. Tương tự MD5, SHA1 được sử dụng rộng rãi để đảm bảo tính xác thực và toàn vẹn thông điệp. 

* Quá trình xử lý thông điệp 

SHA1 sử dụng thủ tục xử lý thông điệp tương tự MD5, cũng gồm 2 khâu là _tiền xử lý_ 

và _các vòng lặp xử lý_ . Cụ thể, chi tiết về các khâu này như sau: 

   - Tiền xử lý: Thông điệp được chia thành các khối 512 bit (16 từ 32 bit). Nếu kích thước thông điệp không là bội số của 512 thì nối thêm số bit còn thiếu. 

   - Các vòng lặp xử lý: Phần xử lý chính của SHA1 làm việc trên _state_ 160 bit, chia thành 5 từ 32 bit (A, B, C, D, E): 

- `+` Các từ A, B, C, D, E được khởi trị bằng một hằng cố định; 

- `+` Từng phần 32 bit của khối đầu vào 512 bit được đưa dần vào để thay đổi _state_ ; 

- `+` Quá trình xử lý gồm 80 vòng, mỗi vòng gồm các thao tác: add, and, or, xor, rotate, mod. 

`+` Mỗi vòng xử lý gồm: Xử lý bởi hàm phi tuyến tính F (có nhiều dạng hàm khác nhau), Cộng modulo và Quay trái. Hình 3.33 biểu diễn lưu đồ một vòng xử lý của SHA1, trong đó A, B, C, D, E là các từ 32 bit của _state_ , Wt: khối 32 bit thông điệp đầu vào, Kt là 32 bit hằng khác nhau cho mỗi vòng, <<<n là thao tác dịch trái _n_ bit, biểu diễn phép cộng modulo 32 bit và F là hàm phi tuyến tính. 

**==> picture [38 x 47] intentionally omitted <==**

**VIETTEL AI RACE** TD159 **CÁC GIẢI THUẬT MÃ HÓA KHÓA BẤT ĐỐI XỨNG VÀ CÁC HÀM** Lần ban hành: 1 **BĂM** 

**==> picture [236 x 242] intentionally omitted <==**

_Hình 3.33. Lưu đồ một vòng xử lý của SHA1_ 

**==> picture [156 x 49] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**