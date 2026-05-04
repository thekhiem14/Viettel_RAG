**VIETTEL AI RACE** Public 368 **XÁC ĐỊNH LỖI ĐỐI VỚI LUỒNG PDH** Lần ban hành: 1 

**==> picture [39 x 47] intentionally omitted <==**

## **1. Kích cỡ khối để thử luồng PDH** 

Kích cỡ khối để thử luồng PDH trong hệ thống đang khai thác được cho trong Bảng 6. 

**Bảng 6 - Kích cỡ khối PDH** 

|Tốc độ bit của luồng<br>PDH kbit/s|Kích cỡ khối PDH bit|EDC/không có EDC|
|---|---|---|
|2048<br>8448<br>34368<br>139264|2048<br>4224<br>4296<br>17408|CRC-4<br>Không có EDC<br>Không có EDC<br>Không có EDC|

## **2. Các bất bình thường (Anomatics)** 

Hai trạng thái bất bình thường trong hệ thống đang khai thác được sử dụng để xác định chỉ tiêu lỗi bit của luồng PDH. 

a1: Một tín hiệu đồng bộ khung bị lỗi (an errored frame alignment signal). 

a2: Một khối bị lỗi (EB) được chỉ thị bằng mã phát hiện lỗi (EDC). 

## **3. Các sai hỏng** 

Ba trạng thái sai hỏng của tín hiệu lối vào trong hệ thống đang khai thác được sử dụng để xác định chỉ tiêu lỗi bit của luồng PDH. 

d1: Mất khung (Loss of frame). 

d2: Tín hiệu chỉ thị cảnh báo (Alarm Indication Signal). 

d3: Mất đồng bộ khung (Loss of frame alignment). 

## **4. Các kiểu luồng PDH** 

**==> picture [39 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|Public 368|
|---|---|---|
||**XÁC ĐỊNH LỖI ĐỐI VỚI LUỒNG PDH**|Lần ban hành: 1|

Tùy theo thiết bị thử ISM liên quan đối với luồng PDH sẽ có 4 loại cấu trúc luồng như sau: 

- Kiểu 1: Luồng được cấu trúc bởi khung và khối 

Một tập hợp đầy đủ chỉ thị sai hỏng d1, d2, d3 và các chỉ thị bất bình thường a1, a2 do thiết bị kiểm tra cung cấp khi hệ thống đang khai thác (ISM). 

- Kiểu 2: Luồng được cấu trúc bởi khung 

Một tập hợp đầy đủ chỉ thị sai hỏng d1, d2, d3 và bất bình thường a1 do thiết bị kiểm tra cung cấp khi hệ thống đang khai thác. 

- Kiểu 3: Các luồng được cấu trúc khung khác 

Một loạt các giới hạn của chỉ thị sai hỏng d1, d2 và bất bình thường a1 do thiết bị kiểm tra cung cấp khi hệ thống đang khai thác. Ngoài ra ISM còn chỉ thị cả số lượng chuỗi tín hiệu đồng bộ khung bị lỗi trong mỗi giây. 

- Kiểu 4: Các luồng không định dạng khung 

Một loạt các giới hạn của chỉ thị sai hỏng d1, d2 do thiết bị kiểm tra cung cấp khi hệ thống đang khai thác. 

## **5. Các thông số và tiêu chuẩn đo luồng PDH** 

**Bảng 7 - Các thông số và tiêu chuẩn đo** 

|**Kiểu luồng**|**Các thông số**|**Tiêu chuẩn đo**|
|---|---|---|
|1|ESR|Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1hoặc a2<br>hoặc một sai hỏng d1đến d3xảy ra.|
||SESR|Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có ‘x’ bất bình thường a1<br>hoặc a2, hoặc một sai hỏng d1đến d3xảy ra.|

|||**VIETTEL AI RACE**|**VIETTEL AI RACE**|**VIETTEL AI RACE**|Public 368|
|---|---|---|---|---|---|
|||**XÁC ĐỊNH LỖI ĐỐI**||**VỚI LUỒNG PDH**|Lần ban hành: 1|
||||BBER|Một lỗi khối cơ bản quan sát được khi: một bất<br>bình thường a1hoặc a2xảy ra trong một khối<br>nhưng không thuộc phần giây bị lỗi nghiêm<br>trọng.||
||2||ESR|Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1hoặc một<br>sai hỏng d1đến d3xảy ra||
||||SESR|Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có ‘x’ bất bình thường a1<br>hoặc một sai hỏng d1hoặc d2xảy ra.||
||3||ESR|Một giây bị lỗi quan sát được khi trong một<br>giây ít nhất có một bất bình thường a1hoặc một<br>sai hỏng d1hoặc d2xảy ra.||
||||SESR|Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây có ít nhất ‘x’ bất bình thường a1<br>hoặc một sai hỏng d1hoặc d2xảy ra||
||4|||Một giây bị lỗi nghiêm trọng quan sát được khi<br>trong một giây ít nhất có một sai hỏng d1hoặc<br>d2xảy ra.||

## **6. Tiêu chuẩn cho việc phát hiện một giây bị lỗi nghiêm trọng trong luồng PDH** 

Bảng 8 liệt kê giá trị ‘x’ gây ra một giây bị lỗi nghiêm trọng (SES) trong khi kiểm tra hệ thống đang khai thác. 

**Bảng 8 - Tiêu chuẩn có SES trên các tuyến PDH** 

**==> picture [39 x 47] intentionally omitted <==**

**VIETTEL AI RACE** Public 368 **XÁC ĐỊNH LỖI ĐỐI VỚI LUỒNG PDH** Lần ban hành: 1 

Tốc độ bit (kbit/s) 2 048 Kiểu EDC CRC-4 Số khối/1 giây 1 000 Số bit/1 khối 2 048 Ngưỡng SES trước Khuyến nghị G.826 x = 805 Ngưỡng ISM dựa trên SES của Khuyến x = 30% khối bị lỗi nghị G.826