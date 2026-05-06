**VIETTEL AI RACE** Public 501 **HỆ TÌM KIẾM ẢNH THEO NGỮ NGHĨA** Lần ban hành: 1 **DỰA TRÊN ONTOLOGY** 

**==> picture [39 x 47] intentionally omitted <==**

**==> picture [35 x 43] intentionally omitted <==**

## **1. Khung ontology** 

Ontology được xây dựng, phát triển dựa trên tập ảnh đối tượng và mối quan hệ giữa các đối tượng. Các hình ảnh đa đối tượng ban đầu được phân đoạn thành ảnh đối tượng; trích xuất các thành phần của ảnh đối tượng và xây dựng mối quan hệ giữa các đối tượng. Từ đó ontology được xây dựng và bổ sung thuộc tính ảnh đối tượng và mối quan hệ này. Trong luận án, ảnh đối tượng được xây dựng từ kỹ thuật dò tìm và phân đoạn đối tượng bằng mạng R-CNN. Trong phạm vi luận án, mỗi hình ảnh thực nghiệm có số đối tượng khác nhau, do đó mô hình mạng R-CNN được sử dụng để nhận diện, phân đoạn ảnh gốc thành các ảnh đối tượng. Quá trình ứng dụng mạng R-CNN được thực hiện trên cơ sở kế thừa mô hình đã có để từ đó nhận diện, phân đoạn các đối tượng khác nhau trên mỗi hình ảnh gốc [99]. Mục đích chính của ontology là biểu diễn hình ảnh theo cách ngữ nghĩa. Do đó, hình ảnh được biểu diễn theo cách dễ hiểu của máy, điều này dẫn đến việc tìm kiếm ảnh sẽ dễ dàng hơn. 

**==> picture [97 x 204] intentionally omitted <==**

Hình ảnh trong tập dữ liệu được biểu diễn ở cấp độ cao, chú thích bằng tập danh mục (vị trí hoặc nhãn) mô tả chúng. Tìm kiếm bắt đầu từ nút gốc _**Owl: Thing**_ . Mỗi lớp được kết nối với nút gốc thông qua quan hệ kế thừa. Ý nghĩa của hình ảnh được xác định bằng cách lập chỉ mục cho lớp. Các truy vấn được chuyển đổi sang cấu trúc hình thức tương đương của nó (RDF) bằng cách sử dụng mối quan hệ (vị ngữ). Các truy vấn này sau đó được so sánh với cấu trúc ontology đã được xây dựng. Từ đó, hình ảnh có cùng danh mục sẽ dễ dàng được xác định và truy xuất. 

Mô hình khung ontology được xây dựng từ tập MS-COCO kế thừa từ công trình [100], có quan hệ và phân cấp giữa các lớp (taxonomy). Các bước xây dựng gồm: 

1. Kế thừa và bổ sung phân lớp từ MS-COCO; 

2. Thêm chú thích, mô tả phân lớp; 

3. Lấy URI, định nghĩa, định danh lớp từ WWW, WordNet, bổ sung cho 

**==> picture [104 x 37] intentionally omitted <==**

**==> picture [60 x 41] intentionally omitted <==**

**VIETTEL AI RACE** Public 501 **HỆ TÌM KIẾM ẢNH THEO NGỮ NGHĨA** Lần ban hành: 1 **DỰA TRÊN ONTOLOGY** 

**==> picture [39 x 47] intentionally omitted <==**

## tập ImageCLEF; 

## 4. Tạo khung ontology từ MS-COCO và thông tin bổ sung từ WWW. 

Ontology ảnh xây dựng trên Protégé được lưu dưới dạng tập tin OWL hoặc RDF/XML. Tuy nhiên, Protégé chỉ trực quan hóa ontology, không quản lý hiệu quả cơ sở tri thức lớn và thường xuyên cập nhật như dữ liệu ảnh. Do đó, cần phương pháp hiệu quả để quản lý cơ sở dữ liệu ảnh lớn. 

**==> picture [97 x 204] intentionally omitted <==**

Các phân lớp trong bộ dữ liệu ảnh được xây dựng phân cấp, với từ điển ngữ nghĩa từ WordNet định nghĩa cho các phân lớp. Mỗi hình ảnh là một cá thể của một hoặc nhiều phân lớp trong ontology. Hình 4.8 minh họa ontology xây dựng trên Protégé cho dữ liệu MS-COCO. Các phương pháp xây dựng ontology bao gồm: Thủ công, Tự động và Bán tự động. 

- Phương pháp thủ công: Sử dụng công cụ Protégé và dữ liệu chọn lọc, đảm bảo độ tin cậy cao nhưng tốn nhiều thời gian và nhân lực, không phù hợp với cơ sở dữ liệu lớn. 

**==> picture [93 x 36] intentionally omitted <==**

- Phương pháp tự động: Nhanh chóng, không cần con người tham gia, nhưng dữ liệu phân tán, không đồng nhất dễ gây sai sót, giảm độ tin cậy. 

- Phương pháp bán tự động: Kết hợp thủ công và tự động, với chuyên gia kiểm tra thông tin trước khi cập nhật, phù hợp cho cơ sở dữ liệu lớn, đảm bảo tin cậy, tiết kiệm thời gian và nhân lực. 

Trong luận án này, một khung ontology bán tự động được đề xuất dựa trên RDF và OWL, có khả năng mở rộng khi dữ liệu ảnh tăng. 

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [141 x 47] intentionally omitted <==**

|---|---|---|
||**VIETTEL AI RACE**|Public 501|
||**HỆ TÌM KIẾM ẢNH THEO NGỮ NGHĨA**<br>**DỰA TRÊN ONTOLOGY**|Lần ban hành: 1|

**==> picture [446 x 241] intentionally omitted <==**

**Hình 4.8.** Một ví dụ về ontology áp dụng trên bộ dữ liệu ảnh MS-COCO 

## **2. Xây dựng khung ontology** 

Khung ontology bán tự động được xây dựng như trong mô tả **Hình 4.9,** bao gồm các bước: 

- Sử dụng tập dữ liệu ảnh ban đầu và ảnh từ WWW làm đầu vào cho quá trình học ontology. 

- Phân lớp tự động các thể từ bộ dữ liệu dựa trên mô hình học máy GPTree/Graph- GPTree/SgGP-Tree. 

- Định nghĩa lớp được tạo thủ công hoặc tự động từ WordNet. 

- Ảnh từ WWW được kết xuất định danh và URL, bổ sung vào dữ liệu đầu vào. 

- Dữ liệu được cập nhật và chỉnh sửa với sự tham gia của chuyên gia.Khung 

|---|---|---|
||**VIETTEL AI RACE**|Public 501|
||**HỆ TÌM KIẾM ẢNH THEO NGỮ NGHĨA**<br>**DỰA TRÊN ONTOLOGY**|Lần ban hành: 1|

ontology được tạo bán tự động từ dữ liệu chuẩn hóa. 

**==> picture [526 x 233] intentionally omitted <==**

**----- Start of picture text -----**<br>
Các phân lớp  Phân lớp<br>tập ảnh  của tập ảnh<br>Tập ảnh từ<br>Bộ dữ liệu ảnh bổ  Các thông tin  Các thuộc<br>WWW<br>sung vào Ontology  Literal  tính<br>Từ điển<br>Các cá thể<br>Tự động  Bán tự động<br>WWW (WordNet,<br>Phân lớp ảnh  Wiki,…)  Mẫu dữ liệu<br>Ontology<br>Cập nhật,<br>Bổ sung<br>chỉnh sửa<br>**----- End of picture text -----**<br>

**==> picture [147 x 47] intentionally omitted <==**

**Hình 4.9.** Mô hình xây dựng khung ontology bán tự động 

Khung ontology có thể mở rộng, bổ sung thêm cá thể hình ảnh, thuộc tính, và phân lớp mới. Định nghĩa lớp được lấy từ WordNet. **Hình 4.10** minh họa việc bổ sung khái niệm cho phân lớp mới vào ontology, và **Hình 4.11** ví dụ về phân cấp lớp ảnh trước và sau khi làm giàu ontology. 

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [141 x 47] intentionally omitted <==**

Public 501 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **HỆ TÌM KIẾM ẢNH THEO NGỮ NGHĨA DỰA TRÊN ONTOLOGY** 

Lần ban hành: 1 

**==> picture [453 x 247] intentionally omitted <==**

**----- Start of picture text -----**<br>
Dữ liệu  Các phân lớp ảnh trong ontology<br>ảnh<br>Các phân<br>WordNet<br>lớp ảnh<br>Tập ảnh từ<br>WWW<br>Từ điển ontology<br>**----- End of picture text -----**<br>

**Hình 4.10.** Bổ sung khái niệm cho phân lớp mới vào từ điển ontology 

**==> picture [147 x 47] intentionally omitted <==**

**==> picture [142 x 300] intentionally omitted <==**

**==> picture [143 x 207] intentionally omitted <==**

**Hình 4.11.** Ví dụ về ontology trước và sau khi làm giàu 

**==> picture [141 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 501 **HỆ TÌM KIẾM ẢNH THEO NGỮ NGHĨA DỰA TRÊN ONTOLOGY** 

**==> picture [39 x 47] intentionally omitted <==**

Lần ban hành: 1 

## • Truy vấn SPARQL 

Trong phần này, câu truy vấn SPARQL được xây dựng bởi hai phép toán hội 

(UNION), phép toán và (AND) dựa trên tên phân lớp của ảnh truy vấn đã phân lớp. 

**==> picture [147 x 47] intentionally omitted <==**

**==> picture [308 x 224] intentionally omitted <==**

**Hình 4.12.** Tập hình ảnh minh hoạ cho truy vấn SPARQL 

**==> picture [106 x 204] intentionally omitted <==**

Bằng cách đưa ra một hình ảnh làm truy vấn, công cụ này sẽ tìm kiếm với tập các ảnh được gắn nhãn hiện có. Hình ảnh truy vấn phải được đặt trong số các danh mục hiện có. Truy vấn có thể ở dạng hình ảnh, dựa trên văn bản hoặc kết hợp của hai hoặc nhiều danh mục, giai đoạn tạo câu truy vấn sẽ được thực hiện tự động. Cho dữ liệu mẫu được mô tả như **Hình 4.12** , các câu truy vấn SPARQL nhằm tìm kiếm các ảnh được trình bày trong **Bảng 4.7** 

**Bảng 4.7.** Ví dụ truy vấn SPARQL 

|---|---|---|---|
|**STT**|**Yêu cầu**|**Truy vấn**|**Kết quả**|
|1|Tìm kiếm các<br>phân lớp con của<br>**Bird**|SELECT ?x<br>WHERE { ?x rdfs:subClassOf<br>:Bird}|Duck, Eagle, Peacock, Swan|

Public 501 

**==> picture [39 x 47] intentionally omitted <==**

## **VIETTEL AI RACE** 

## **HỆ TÌM KIẾM ẢNH THEO NGỮ NGHĨA DỰA TRÊN ONTOLOGY** 

## Lần ban hành: 1 

**==> picture [455 x 324] intentionally omitted <==**

**----- Start of picture text -----**<br>
SELECT ?x ?y<br>Tìm kiếm các  WHERE {  ?x<br>2<br>hình ảnh của  Bird  rdfs:subClassOf :Bird .<br>?y rdf:type ?x }<br>SELECT ?y ?x<br>Tìm các hình ảnh<br>WHERE {  ?x<br>3  của phân lớp  Bird<br>rdfs:subClassOf :Bird .<br>có màu trắng<br>?y :Color "White" }<br>SELECT DISTINCT ?name<br>Tìm người tạo các  Magesh<br>4  WHERE { ?x rdf:type :Swan<br>ảnh  Swan  Aswinth<br>.  ?x :Creator ?name }<br>5  Tìm các ảnh về  SELECT ?x<br>Swan  WHERE { ?x rdf:type :Swan }<br>Tìm các hình ảnh  SELECT ?x<br>6  Car có màu  Red WHERE { ?x rdf:type :Swan }<br>**----- End of picture text -----**<br>

**==> picture [117 x 42] intentionally omitted <==**

**==> picture [77 x 204] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [141 x 47] intentionally omitted <==**