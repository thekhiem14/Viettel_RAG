Public 516 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

# **TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ PHỎNG ĐỘNG HỌC** 

Lần ban hành: 1 

**==> picture [56 x 72] intentionally omitted <==**

## **1. Trình tự lắp ráp** 

## **1.1 Lập kế hoạch làm việc** 

Thứ tự tạo các chi tiết và các cụm lắp phụ thuộc vào việc ta trả lời các câu hỏi sau ra 

- Ta chỉnh sửa một lắp ráp có sẵn hay bắt đầu một lắp ráp mới? 

- Ta có thể đập vỡ một lắp ráp lớn thành các cụm lắp con được không? 

- Ta có thể dùng các chi tiết có sẵn và các phần tử thiết kế không? 

- Ràng buộc nào sẽ ảnh hưởng đến chức năng của thiết kế? 

## **1.2 Tạo hoặc chèn thành phần lắp ráp đầu tiên** 

Chọn một chi tiết hoặc một cụm lắp cơ sở (ví dụ như một khung hoặc tấm kim loại) làm thành phần lắp ráp đầu tiên của lắp ráp. Ta có thể chèn một thành phần lắp ráp có sẵn hoặc tạo mới một thành phần lắp ráp mới trong lắp ráp. Thành phần lắp ráp đầu tiên này cần được gán cố định (tất cả các bậc tự do đều bị hạn chế). Gốc tọa độ và các trục tọa độ của nó được căn theo gốc và các trục tọa độ của lắp ráp. 

**==> picture [89 x 201] intentionally omitted <==**

- Tạo một thành phần lắp ráp: Chọn Assemble → Create. Trong hộp thoại Create In-Place Component ta nhập tên file mới và kiểu file. Khi đó sẽ tạo ra thành phần lắp ráp đầu tiên. 

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [141 x 47] intentionally omitted <==**

Public 516 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ PHỎNG ĐỘNG HỌC** 

Lần ban hành: 1 

**==> picture [379 x 185] intentionally omitted <==**

_Hình 2.16. Hộp thoại Create In-Place Component_ 

- Chèn một thành phần lắp ráp có sẵn: Chọn Assemble → Place. Duyệt qua các file cần mở trong hộp thoại Open. Kích chuột vào cửa sổ đồ họa để chèn thành phần lắp ráp, có thể chèn nhiều bản một lúc, kết thúc kích chuột phải và chọn Ok. Các bản chèn không có các ràng buộc lắp ráp. 

**==> picture [89 x 201] intentionally omitted <==**

## **1.3 Định vị các thành phần lắp ráp** 

Có nhiều cách để di chuyển các thành phần lắp ráp. Nếu một thành phần lắp ráp không phải là cố định hoặc không bị ràng buộc hoàn toàn, ta có thể di chuyển nó trong vùng lắp ráp. Các ràng buộc sẽ xóa một vài bậc tự do của thành phần lắp ráp này. Có thể dịch chuyển một thành phần lắp ráp theo các bậc tự do còn lại. 

Khi một chi tiết hoặc một cụm lắp ráp được cố định nó sẽ được cố định trong hệ tọa độ lắp ráp. Chi tiết cố định này sẽ được mô tả bằng một biểu tượng riêng trên cửa sổ duyệt. Bất kỳ thành phần lắp ráp nào trong một lắp ráp cũng có thể được cố định. Thành phần lắp ráp đầu tiên của lắp ráp được tự động cố định tuy nhiên ta có thể hủy bỏ trạng thái cố định của nó. 

Một thành phần lắp ráp cố định thì không giống như các thành phần lắp ráp ràng buộc khác. Một thành phần lắp ráp cố định được cố định vào hệ trục tọa độ lắp ráp. Một thành phần lắp ráp ràng buộc thì có quan hệ với các thành phần lắp ráp khác mà 

**==> picture [88 x 32] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 516|
||**TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ**<br>**PHỎNG ĐỘNG HỌC**|Lần ban hành: 1|

định nghĩa vị trí của nó. Đây là sự tác động lẫn nhau giữa các thành phần lắp ráp. Ví dụ: Nếu ta dùng công cụ Move hoặc Rotate để tạm thời định vị lại một thành phần lắp ráp được ràng buộc khi Update, thành phần lắp ráp này sẽ trở lại vị trí ràng buộc của nó. 

Khi dịch chuyển một thành phần lắp ráp cố định bằng công cụ Move hoặc Rotate, bất kỳ thành phần lắp ráp nào mà có ràng buộc tới nó sẽ cùng dịch chuyển tới vị trí mới của thành phần lắp ráp cố định. 

**==> picture [106 x 201] intentionally omitted <==**

**==> picture [213 x 183] intentionally omitted <==**

**==> picture [147 x 47] intentionally omitted <==**

_Hình 2.17. Biểu tượng chi tiết định vị trên cửa sổ duyệt_ 

**==> picture [166 x 148] intentionally omitted <==**

_Hình 2.18. Chế độ Degrees of Freedom OnS_ 

**==> picture [110 x 38] intentionally omitted <==**

Hiển thị các bậc tự do có sẵn: Kích chuột phải vào chi tiết trong cửa sổ duyệt hoặc cửa sổ 

|---|---|---|
||**VIETTEL AI RACE**|Public 516|
||**TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ**<br>**PHỎNG ĐỘNG HỌC**|Lần ban hành: 1|

đồ họa sau đó chọn Properties. Trong hộp hội thoại Properties chọn nút Occurrence, đánh dấu vào hộp kiểm Degrees of Freedom sau đó kích chuột OK. Để tắt chế độ hiển thị bậc tự do ta bỏ đánh dấu trong hộp kiểm trên. Ta cũng có thể sử dụng tùy chọn Degrees of Freedom trong menu View. 

**==> picture [147 x 47] intentionally omitted <==**

**==> picture [178 x 414] intentionally omitted <==**

**==> picture [106 x 201] intentionally omitted <==**

_Hình 2.19. Thay đổi trạng thái cố định của một thành phần lắp ráp_ 

Di chuyển hoặc quay thành phần lắp ráp cố định: Kích chuột vào công cụ Move Component hoặc Rotate Component trên thanh công cụ Assembly. Sau đó, kéo rê 

**==> picture [60 x 41] intentionally omitted <==**

**==> picture [88 x 32] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 516|
||**TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ**<br>**PHỎNG ĐỘNG HỌC**|Lần ban hành: 1|

thành phần lắp ráp cố định tới vị trí mới. Khi kích chuột vào Update bất kỳ các thành phần lắp ráp ràng buộc nào sẽ được định vị lại tới vị trí mới. 

- Di chuyển một thành phần lắp ráp với một khoảng cách xác định: Kích chuột phải vào thành phần lắp ráp cần di chuyển sau đó chọn Properties → Occurrence. Ta có thể nhập số cho các giá trị dịch chuyển theo các trục tọa độ X, Y, Z. Ta cũng có thể bật tắt trạng thái cố định của thành phần lắp ráp cố định. 

**==> picture [106 x 201] intentionally omitted <==**

**==> picture [323 x 455] intentionally omitted <==**

**==> picture [117 x 42] intentionally omitted <==**

**==> picture [121 x 41] intentionally omitted <==**

_Hình 2.20. Di chuyển một thành phần lắp ráp với khoảng cách xác định_ 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** Public 516 **TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ** Lần ban hành: 1 **PHỎNG ĐỘNG HỌC** 

- Di chuyển hoặc quay tạm thời các thành phần lắp ráp ràng buộc: Kích chuột vào công cụ Move Component hoặc Rotate Component trên thanh công cụ Assembly. Dùng các công cụ này để di chuyển hoặc quay tạm thời các thành phần lắp ráp mà không xóa mất ràng buộc. Thành phần lắp ráp ràng buộc sẽ trở thành vị trí ban đầu của nó khi ta kích chuột vào Update. 

## **1.4 Bổ sung thành phần lắp ráp** 

Trong môi trường lắp ráp ta có thể tạo một cụm lắp, một chi tiết mới hoặc chèn một chi tiết hay một cụm lắp có sẵn. Khi tạo một Component In-Place mới ta có thể gán mặt phác thảo trong mặt quan sát hiện hành hay ràng buộc nó tới một mặt của thành phần lắp ráp có sẵn. Ta có thể chèn nó vào vùng lắp ráp sau đó bổ sung các ràng buộc. 

Khi một thành phần lắp ráp được kích hoạt thì các thành phần lắp ráp còn lại sẽ bị mờ đi trong cửa sổ duyệt. Chỉ có một thành phần lắp ráp có thể được kích hoạt tại một thời điểm. Bộ phận lắp ráp tự nó phải được kích hoạt khi tạo hoặc chèn một thành phần lắp ráp. 

**==> picture [89 x 201] intentionally omitted <==**

- Kích hoạt chi tiết: Kích đúp vào tên chi tiết trong cửa sổ duyệt. Các chi tiết còn lại sẽ bị mờ đi. 

- Kích hoạt một cụm lắp: Kích đúp vào tên của của cụm lắp ráp trong cửa sổ duyệt hoặc kích chuột phải trong cửa sổ đồ họa và chọn Finish Edit. 

Chú ý: Finish Edit sẽ bị ẩn trên menu ngữ cảnh trong khi đối tượng hình học được chọn trong cửa sổ đồ họa. 

- Tạo một Component In-Place: Kích chuột vào công cụ Create Component. Nếu cần tạo ràng buộc giữa mặt phác thảo và một mặt của chi tiết có sẵn thì chọn Constrain Sketch Plance to Selected Face trong hộp thoại Create In-Place Component. 

Cách khác có thể kích chuột vào một vị trí trong cửa sổ đồ họa để xác định mặt phác thảo. 

**==> picture [88 x 32] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 516|
||**TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ**<br>**PHỎNG ĐỘNG HỌC**|Lần ban hành: 1|

- Tạo một chi tiết hoặc một cụm lắp dẫn xuất: Duyệt và mở file Part (.ipt) đối với Feature cơ sở. Trong thanh công cụ Feature kích chuột vào nút Derived Component. Xác định hệ số tỷ lệ, mặt đối xứng và kích OK. Nếu ta chỉnh sửa Feature của chi tiết dẫn xuất kích chuột phải và chọn Update Derived Feature. Để phá hủy liên kết và không cập nhật sự thay đổi của chi tiết gốc, kích chuột phải vào Feature dẫn xuất trong cửa sổ duyệt và kích chuột vào Break link. 

**==> picture [89 x 201] intentionally omitted <==**

- Chèn một chi tiết hoặc một cụm lắp: Kích chuột vào công cụ Place Component sau đó chỉ rõ file cần chèn. Kích chuột vào cửa sổ đồ họa để định vị thành phần lắp ráp khi chèn. Mỗi lần kích chuột vào cửa sổ đồ họa sẽ chèn một bản của chi tiết hoặc cụm chi lắp cần chèn. Không có ràng buộc nào được gán khi dùng công cụ Place Component. 

## **1.5 Tạo mảng các thành phần lắp ráp** 

Bạn có thể tạo mảng chi tiết, nhóm chi tiết, cụm lắp. Các thành phần lắp ráp được tạo mảng có thể bao gồm các ràng buộc và là các đối tượng lắp ráp duy nhất với các đặc tính không có trong các thành phần lắp ráp chèn thông thường. Ta có thể tạo các thành phần lắp ráp được tạo mảng và có liên kết tới mảng các Feature chi tiết. Ví dụ: Một mảng các lỗ có thể tồn tại cùng các bulong mà có mối liên hệ với mảng các lỗ. Nếu số lỗ thay đổi thì số bulong cũng thay đổi theo. 

Để tạo mảng các thành phần lắp ráp: Kích chuột vào công cụ Pattern Component sau đó chọn nút Rectangular hoặc Circular. Ta có thể chọn các thành phần lắp ráp cần tạo mảng trong cửa sổ duyệt hoặc trong cửa sổ đồ họa. Sau đó, chọn các cạnh của thành phần lắp ráp, các trục làm việc hoặc các trục tọa độ để xác định hướng của các hàng và các cột hoặc trục quay. Nhập số phần tử và khoảng cách giữa các phần tử. 

Chú ý: Mỗi lần chèn một thành phần lắp ráp hoặc tạo một mảng từ một thành phần lắp ráp, Autodesk Inventor liên kết nó tới tất cả các cá thể khác của thành phần lắp ráp đó. Thay đổi một mô hình đơn sẽ làm thay đổi tất cả các cá thể khác. Để tạo 

**==> picture [88 x 32] intentionally omitted <==**

**==> picture [60 x 41] intentionally omitted <==**

**VIETTEL AI RACE** Public 516 **TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ PHỎNG ĐỘNG HỌC** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

một thành phần lắp ráp mới dựa trên thành phần lắp ráp khác, ghi phiên bản với tên chi tiết và chèn phiên bản vào trong lắp ráp. 

**==> picture [188 x 172] intentionally omitted <==**

**==> picture [97 x 201] intentionally omitted <==**

_Hình 2.22. Hộp thoại Pattern Component_ 

## **1.6 Thay đổi các thành phần lắp ráp** 

Việc các nhà thiết kế thay đổi một chi tiết trong lắp ráp là việc thường xuyên diễn ra. Autodesk Inventor chèn chi tiết mới với các trục tọa độ của nó được căn theo các trục tọa độ của chi tiết có sẵn. Ta phải gán bất kỳ ràng buộc nào cho nó. 

Để thay đổi một thành phần lắp ráp: Kích chuột vào công cụ Replace Component trên thanh công cụ Assembly sau đó chọn thành phần lắp ráp cần thay đổi sau đó tìm đến thành phần lắp ráp mới. Tất cả các ràng buộc trên thành phần lắp ráp có sẵn sẽ bị mất trong khi thay đổi. 

## **1.7 Bổ sung các ràng buộc tới các thành phần lắp ráp** 

Ta có thể bổ sung 4 kiểu ràng buộc tới các thành phần lắp ráp: mate, angle, tangent và insert. Mỗi kiểu của ràng buộc có nhiều phương án. Các phương án được định nghĩa bởi hướng của các vector vuông góc với thành phần lắp ráp. Ta có thể Mate các thành phần lắp ráp bằng cách nhấn phím Alt và kéo rê chi tiết vào vị trí Mate. Phương pháp này thì nhanh bởi vì không cần nhập lệnh tạo ràng buộc. Một số bậc tự do sẽ bị mất khi ta thêm các ràng buộc. Các bậc tự do có thể vẫn có sẵn nhưng 

**==> picture [88 x 32] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 516|
||**TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ**<br>**PHỎNG ĐỘNG HỌC**|Lần ban hành: 1|

bị hạn chế. Ví dụ: Nếu ta gán một ràng buộc Tangent tới 2 quả cầu thì tất cả sáu bậc tự do vẫn còn nhưng ta không thể dịch chuyển một quả cầu dù chỉ là theo một hướng. Thử dựng một vài chi tiết để xem các ràng buộc hạn chế chuyển động của chúng như thế nào. 

**==> picture [374 x 196] intentionally omitted <==**

**==> picture [106 x 201] intentionally omitted <==**

**==> picture [147 x 47] intentionally omitted <==**

_Hình 2.23. Gán ràng buộc cho các chi tiết lắp ráp_ 

- Tạo ràng buộc 2 mặt, cạnh, điểm hoặc các Work Feature với nhau: Trong hộp thoại Place Constraint kích chuột vào Mate. Ta có hai phương án trong lệnh Mate là Mate và Flush như minh họa hình 2.24. Nếu ta muốn các mũi tên vuông góc hướng vào nhau thì ta chọn Mate. Nếu ta muốn các đối tượng hình học đặt cạnh nhau và các mũi tên theo cùng một hướng ta chọn Flush. Nếu muốn tạo khe hở nhập giá trị hở vào hộp offset. 

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [141 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** Public 516 **TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ** Lần ban hành: 1 **PHỎNG ĐỘNG HỌC** 

**==> picture [327 x 218] intentionally omitted <==**

_Hình 2.24. Ràng buộc Mate trong hộp thoại Place Constraint_ 

- Tạo ràng buộc hai mặt hoặc hai cạnh hợp với nhau một góc nhất định: Trong hộp thoại Place Constraint kích chuột vào Angle. Ta có thể chọn các vector vuông góc với các mặt hoặc các cạnh riêng. Có 4 giải pháp cho mỗi cặp lắp ráp. Các mặt được lựa chọn của chi tiết sẽ được ràng buộc theo góc. 

**==> picture [89 x 201] intentionally omitted <==**

**==> picture [322 x 215] intentionally omitted <==**

_Hình 2.25. Ràng buộc Angle trong hộp thoại Place Constraint_ 

**==> picture [141 x 47] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 516|
||**TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ**<br>**PHỎNG ĐỘNG HỌC**|Lần ban hành: 1|

- Tạo ràng buộc của một mặt cong với một mặt phẳng hoặc một mặt cong khác: 

Trong hộp thoại Place Constraint kích chuột vào Tangent. Trong trường hợp này ta có hai phương án là tiếp xúc trong và tiếp xúc ngoài như hình dưới đây: 

**==> picture [301 x 200] intentionally omitted <==**

_Hình 2.26. Ràng buộc Tangent trong hộp thoại Place Constraint_ 

**==> picture [106 x 201] intentionally omitted <==**

- Tạo ràng buộc ngang bằng giữa lỗ và mặt trụ: Trong hộp thoại Place Constraint kích chuột vào Insert. Lệnh này sẽ gán đồng tâm của các cung trong hoặc đường tròn được chọn để tạo ràng buộc. Để gán ràng buộc ta chọn đường tròn trên hình trụ và trên lỗ mà ta muốn ràng buộc. 

Chú ý: Các ràng buộc Insert được hạn chế bởi các bề mặt phẳng mà vuông góc với đường trục của hình trụ và của lỗ. 

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [141 x 47] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 516 

## **TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ PHỎNG ĐỘNG HỌC** 

Lần ban hành: 1 

**==> picture [292 x 195] intentionally omitted <==**

**==> picture [97 x 201] intentionally omitted <==**

_Hình 2.27. Ràng buộc Insert trong hộp thoại Place Constraint_ 

## **1.8 Bổ sung ràng buộc cho các chi tiết thích nghi** 

Có thể tạo các chi tiết đặt dưới sự ràng buộc mà được thích nghi theo ràng buộc đó trong lắp ráp. Bằng cách này, chức năng thiết kế sẽ điều khiển hình dạng của các thành 

phần lắp ráp. Ví dụ, ta có thể tạo một miếng đệm và gán ràng buộc sao cho nó sẽ kéo dãn hoặc thu nhỏ để điền đầy khe hở giữa hai chi tiết. 

Một số yêu cầu để thích nghi: 

- Phác thảo phải được ràng buộc đúng cả về hình học và kích thước. Nếu phác thảo đã bị gán toàn bộ các kích thước thì Autodesk Inventor sẽ không thể thay đổi kích thước. Nếu có nhiều kích thước còn thiếu thì Autodesk Inventor có thể thay đổi sai đối tượng hình học; 

- Chi tiết phải được gán thích nghi trong lắp ráp. Kích chuột phải vào chi tiết trong 

- cửa sổ duyệt của lắp ráp sau đó chọn Adaptive; 

   - Feature phải được đặt thích nghi trong file chi tiết. Kích hoạt chi tiết sau đó kích 

**==> picture [88 x 32] intentionally omitted <==**

**==> picture [60 x 41] intentionally omitted <==**

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** Public 516 **TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ** Lần ban hành: 1 **PHỎNG ĐỘNG HỌC** 

chuột phải vào Feature trong cửa sổ duyệt và chọn Adaptive; 

- Chỉ có một cá thể của chi tiết có thể được thích nghi. Nếu một chi tiết đã được thích nghi thì tùy chọn Adaptivity sẽ bị mờ đi trên menu ngữ cảnh. 

Các ràng buộc thích nghi được gán sau khi thành phần lắp ráp đã được ràng buộc về vị trí. Trước tiên Autodesk Inventor định vị lại chi tiết để đảm bảo theo ràng buộc. Nếu thành phần lắp ráp không thể dịch chuyển, hệ thống sẽ thích nghi chi tiết đó để điều chỉnh khoảng trống. Nếu thành phần lắp ráp đã bị ràng buộc hoàn toàn, dòng nhắc nhắc ta đang tạo các ràng buộc thừa trên chi tiết. 

**==> picture [44 x 88] intentionally omitted <==**

## **2. Các công cụ lắp ráp** 

**==> picture [533 x 383] intentionally omitted <==**

**----- Start of picture text -----**<br>
Khi tạo hoặc chỉnh sửa một chi tiết trong lắp ráp, thanh công cụ lắp ráp không<br>được kích họa trong khi thanh công cụ Part Model được kích hoạt.<br>Loại  Nút lệnh  Công cụ  Chức năng<br>Component  Chèn một chi tiết hoặc một cụm<br>lắp có sẵn<br>Place Component<br>Tạo một cụm lắp hoặc một<br>Create Component  chi tiết mới trong môi trường<br>lắp ráp<br>Cho phép dịch chuyển tạm thời<br>một thành phần lắp ráp đã được<br>Move Component  ràng buộc. Thành phần lắp ráp<br>sẽ trở lại vị trí cũ khi ta Update<br>**----- End of picture text -----**<br>

Khi tạo hoặc chỉnh sửa một chi tiết trong lắp ráp, thanh công cụ lắp ráp không được kích họa trong khi thanh công cụ Part Model được kích hoạt. 

**==> picture [75 x 52] intentionally omitted <==**

**==> picture [540 x 425] intentionally omitted <==**

**----- Start of picture text -----**<br>
VIETTEL AI RACE  Public 516<br>TRÌNH TỰ, CÔNG CỤ LẮP RÁP VÀ MÔ<br>Lần ban hành: 1<br>PHỎNG ĐỘNG HỌC<br>Cho phép quay tạm thời một<br>Rotate Component  thành phần lắp ráp đã được ràng<br>buộc. Thành phần lắp ráp sẽ trở<br>lại vị trí cũ khi ta Update<br>Thay một chi tiết trong một<br>Replace Component<br>lắp ráp bằng một chi tiết khác<br>Pattern Component  Tạo mảng các chi tiết lắp ráp<br>Constraint<br>Gán ràng buộc giữa các mặt,<br>Place Constraint  các cạnh hoặc các Work<br>Feature. Các ràng buộc có thể<br>được thích nghi<br>All  Thay nhiều chi tiết trong lắp ráp<br>Replace All<br>bằng một chi tiết khác<br>**----- End of picture text -----**<br>

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [141 x 47] intentionally omitted <==**