Public 114 

**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

## **1. Giới thiệu** 

**==> picture [45 x 49] intentionally omitted <==**

**CONTRAST ENHANCEMENT BASED ON LAYERED DIFFERENCE** Lần ban hành: 1 **REPRESENTATION OF 2D HISTOGRAMS** 

**==> picture [45 x 53] intentionally omitted <==**

Mặc dù công nghệ xử lý hình ảnh đã có nhiều tiến bộ, các hình ảnh thu được vẫn thường không thể hiện đầy đủ chi tiết cảnh hoặc có độ tương phản thấp do giới hạn dải động. Các phương pháp tăng cường tương phản (Contrast Enhancement - CE) đã được phát triển nhằm khắc phục vấn đề này. Tuy nhiên, các phương pháp truyền thống như Histogram Equalization - HE thường tập trung vào phân phối mức xám tuyệt đối, dẫn đến hạn chế trong việc xử lý tương phản cục bộ và dễ gây hiện tượng quá làm nổi bật ở một số vùng ảnh. 

Phương pháp được đề xuất là một thuật toán tăng cường tương phản toàn cục mới, dựa trên khung lý thuyết Layered Difference Representation - LDR. Điểm khác biệt chính của phương pháp này so với các thuật toán truyền thống là việc sử dụng lược đồ 2D để biểu diễn mối quan hệ mức xám giữa các điểm ảnh liền kề, thay vì chỉ xét đến phân phối mức xám đơn lẻ. Điều này cho phép phương pháp tận dụng sự nhạy cảm tự nhiên của hệ thống thị giác con người (Human Visual System - HVS) đối với sự khác biệt mức xám, mang lại kết quả cải thiện tương phản phù hợp hơn với nhận thức thị giác. 

**==> picture [61 x 85] intentionally omitted <==**

Phương pháp LDR kế thừa từ các nghiên cứu sử dụng lược đồ 2D trước đó, chẳng hạn như thuật toán Contextual Visual Contrast (CVC). Tuy nhiên, thay vì chỉ khai thác thông tin biên và cạnh vật thể, phương pháp LDR thiết lập mối quan hệ chặt chẽ giữa lược đồ 2D của ảnh đầu vào và sự khác biệt mức xám trong ảnh đầu ra. Phương pháp này nhấn mạnh các sự khác biệt xuất hiện thường xuyên, qua đó cải thiện tương phản cục bộ và tận dụng tối đa dải động. Điều này giúp LDR vượt qua các hạn chế của HE và CVC, mang lại hình ảnh đầu ra có độ tương phản cao hơn và chất lượng thị giác tốt hơn. 

## **2. Mô tả thuật toán** 

Thuật toán tăng cường tương phản toàn cục được đề xuất dựa trên Layered Difference Representation – LDR. Thuật toán gồm hai thành phần chính: intralayer optimization và inter-layer aggregation. Các bước chính được mô tả lần lượt dưới đây. 

Public 114 

**VIETTEL AI RACE** 

**==> picture [38 x 47] intentionally omitted <==**

**==> picture [45 x 49] intentionally omitted <==**

**CONTRAST ENHANCEMENT BASED ON LAYERED DIFFERENCE** Lần ban hành: 1 **REPRESENTATION OF 2D HISTOGRAMS** 

**==> picture [453 x 86] intentionally omitted <==**

_Hình minh họa quy trình, thể hiện các bước từ việc trích xuất lược đồ 2D, tối ưu hóa trong lớp, tổng hợp giữa các lớp, đến tái cấu trúc ảnh đầu ra_ . 

## **2.1. Trích Xuất Lược Đồ 2D** 

- Bước đầu tiên là xây dựng lược đồ 2D h(k, k+l) từ ảnh đầu vào. Lược đồ này đếm số lượng các cặp điểm ảnh liền kề với mức xám k và k+l, biểu diễn sự khác biệt mức xám giữa các điểm ảnh trong không gian ảnh. 

ℎ(𝑘, 𝑘+ 𝑙) =  𝑡ầ𝑛 𝑠ố 𝑐á𝑐 𝑐ặ𝑝 đ𝑖ể𝑚 ả𝑛ℎ 𝑐ó 𝑚ứ𝑐 𝑥á𝑚 (𝑘, 𝑘+ 𝑙) - Lược đồ 2D cung cấp thông tin phong phú về sự thay đổi mức xám, giúp phát hiện các đặc điểm cục bộ quan trọng để cải thiện tương phản. 

**==> picture [61 x 85] intentionally omitted <==**

## **2.2. Intra-Layer Optimization** 

- Lược đồ h(k, k+l) được phân tách thành các lớp (layers), mỗi lớp đại diện cho một khoảng chênh lệch mức xám cụ thể l. 

- Với mỗi lớp l, một vector lược đồ hl được tính toán. Vector này được sử dụng để thiết lập một hệ phương trình tuyến tính, từ đó giải ra vector sự khác biệt dl cho lớp l. 

𝐷∙𝑑𝑙 = 𝑠𝑙, 

với D là ma trận chênh lệch, sl là tổng của hl . 

- Quá trình tối ưu này đảm bảo rằng các sự khác biệt mức xám xuất hiện thường xuyên sẽ được làm nổi bật trong ảnh đầu ra. 

**==> picture [50 x 35] intentionally omitted <==**

## **2.3. Inter-Layer Aggregation** 

- Các vector khác biệt dl từ tất cả các lớp được tổng hợp lại thành một vector sự khác biệt hợp nhất d, sử dụng một vector trọng số w để xác định mức độ đóng góp của mỗi lớp. 

**==> picture [38 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 114 **CONTRAST ENHANCEMENT BASED ON LAYERED DIFFERENCE** Lần ban hành: 1 **REPRESENTATION OF 2D HISTOGRAMS** 

**==> picture [45 x 53] intentionally omitted <==**

**==> picture [84 x 47] intentionally omitted <==**

**----- Start of picture text -----**<br>
255<br>𝑙 ∙𝑑𝑙<br>𝑑= ∑𝑤<br>𝑙=1<br>**----- End of picture text -----**<br>

- Quá trình tổng hợp này giúp kết hợp thông tin từ tất cả các lớp, tạo ra một biểu diễn toàn diện cho toàn bộ ảnh. 

## **2.4. Tái Cấu Trúc Hàm Biến Đổi** 

- Vector d được sử dụng để tái cấu trúc hàm biến đổi x, ánh xạ mức xám đầu vào thành mức xám đầu ra. 

**==> picture [188 x 14] intentionally omitted <==**

- Hàm biến đổi này được áp dụng để biến đổi ảnh đầu vào, tạo ra ảnh đầu ra với độ tương phản được cải thiện. 

## **2.5. Kết Quả** 

- Hàm biến đổi x được áp dụng lên ảnh đầu vào: 

**==> picture [84 x 33] intentionally omitted <==**

𝑜𝑢𝑡=  𝑥[𝑖𝑚𝑔] 

- Phương pháp tập trung vào việc tăng cường các sự khác biệt mức xám thường xuất hiện trong ảnh đầu vào. Điều này giúp cải thiện đáng kể độ tương phản so với các phương pháp truyền thống, đồng thời tận dụng toàn bộ dải động của ảnh. 

**==> picture [61 x 85] intentionally omitted <==**

**==> picture [192 x 116] intentionally omitted <==**

**==> picture [124 x 43] intentionally omitted <==**