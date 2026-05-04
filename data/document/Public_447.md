**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Test case|Mô tả|Input|Expected<br>Output|Phương<br>pháp|Ghi chú|
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năngcủa hệthống,|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||bao gồm kịch bản<br>thành công và thất<br>bại.||sự cố|||
|---|---|---|---|---|---|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|---|---|---|---|---|---|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>baogồm kịch bản|network<br>disconnect|User<br>login<br>thành<br>công|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thành công và thất<br>bại.||trong <1s|||
|---|---|---|---|---|---|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|API stress|Thực hiện API stress<br>test để kiểm thử|invalid|User<br>login|JMeter|Gửi báo cáo|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||PDF hàng ngày<br>Test môi<br>trường Pre-<br>Prod<br>Gửi báo cáo<br>PDF hàng ngày<br>Gửi báo cáo<br>PDF hàng ngày<br>Theo chuẩn<br>ISTQB|
||test||chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|data|thành<br>công<br>trong <1s|script||PDF hàng ngày|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|invalid<br>data|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium||Test môi<br>trường Pre-<br>Prod|
||Security<br>scan||Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script||Gửi báo cáo<br>PDF hàng ngày|
||Security<br>scan||Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan||Gửi báo cáo<br>PDF hàng ngày|
||Login test||Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan||Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||công và thất bại.|||||
|---|---|---|---|---|---|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năngcủa hệ|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thống, bao gồm kịch<br>bản thành công và<br>thất bại.||gián đoạn|||
|---|---|---|---|---|---|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Theo chuẩn<br>ISTQB|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|DB<br>corruption|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|Test môi<br>trường Pre-<br>Prod|
|Database|Thực hiện Database|DB|Hệthống|Automation|So sánh|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|recovery<br>test|recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|corruption|chịu tải<br>20k TPS<br>không<br>gián đoạn|Selenium|benchmark với<br>release trước|
|---|---|---|---|---|---|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, baogồm kịch|invalid<br>data|User<br>login<br>thành<br>công|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||bản thành công và<br>thất bại.||trong <1s|||
|---|---|---|---|---|---|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|Theo chuẩn<br>ISTQB|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|invalid<br>data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|Theo chuẩn<br>ISTQB|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năngcủa hệ|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thống, bao gồm kịch<br>bản thành công và<br>thất bại.||sự cố|||
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|API stress|Thực hiện API stress|network|Không|JMeter|Theo chuẩn|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|test|test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|disconnect|phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|script|ISTQB|
|---|---|---|---|---|---|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|invalid<br>data|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, baogồm kịch|invalid<br>data|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||So sánh<br>benchmark với<br>release trước<br>So sánh<br>benchmark với<br>release trước<br>Theo chuẩn<br>ISTQB<br>Test môi<br>trường Pre-<br>Prod<br>Phải log toàn|
||||bản thành công và<br>thất bại.||||||
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan||So sánh<br>benchmark với<br>release trước|
||API stress<br>test||Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible||So sánh<br>benchmark với<br>release trước|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script||Theo chuẩn<br>ISTQB|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan||Test môi<br>trường Pre-<br>Prod|
||Data<br>consistency||Thực hiện Data<br>consistencytest để|network|Hệ thống<br>chịu tải|Manual test||Phải log toàn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||bộ kết quả<br>Theo chuẩn<br>ISTQB<br>So sánh<br>benchmark với<br>release trước<br>Theo chuẩn<br>ISTQB<br>Theo chuẩn<br>ISTQB|
||test||kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|disconnect|20k TPS<br>không<br>gián đoạn|plan||bộ kết quả|
||Failover<br>test||Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|JMeter<br>script||Theo chuẩn<br>ISTQB|
||Failover<br>test||Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium||So sánh<br>benchmark với<br>release trước|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium||Theo chuẩn<br>ISTQB|
||Login test||Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium||Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|Theo chuẩn<br>ISTQB|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành côngvà thất|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||bại.|||||
|---|---|---|---|---|---|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|DB<br>corruption|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Cluster<br>failover<br>tự động<br>trong 5s|JMeter<br>script|Theo chuẩn<br>ISTQB|
|Security|Thực hiện Security<br>scan để kiểm thử|valid data|Dữ liệu<br>được khôi|Manual test|Test môi<br>trườngPre-|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|scan|chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.||phục toàn<br>vẹn sau<br>sự cố|plan|Prod|
|---|---|---|---|---|---|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Test môi<br>trường Pre-<br>Prod|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||công và thất bại.||sự cố|||
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery|Thực hiện Database<br>recoverytest để|valid data|User<br>login|JMeter|Theo chuẩn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||ISTQB<br>So sánh<br>benchmark với<br>release trước<br>So sánh<br>benchmark với<br>release trước<br>Gửi báo cáo<br>PDF hàng ngày<br>Phải log toàn<br>bộ kết quả|
||test||kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.||thành<br>công<br>trong <1s|script||ISTQB|
||Failover<br>test||Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium||So sánh<br>benchmark với<br>release trước|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium||So sánh<br>benchmark với<br>release trước|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script||Gửi báo cáo<br>PDF hàng ngày|
||API stress<br>test||Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible||Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năngcủa hệthống,|valid data|User<br>login<br>thành<br>công|Automation<br>Selenium|Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||bao gồm kịch bản<br>thành công và thất<br>bại.||trong <1s|||
|---|---|---|---|---|---|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Test môi<br>trường Pre-<br>Prod|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Data|Thực hiện Data|DB|User|Kịch bản|Test môi|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|consistency<br>test|consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|corruption|login<br>thành<br>công<br>trong <1s|Ansible|trường Pre-<br>Prod|
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Theo chuẩn<br>ISTQB|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||công và thất bại.||Top 10|||
|---|---|---|---|---|---|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||công và thất bại.||Top 10|||
|---|---|---|---|---|---|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|invalid<br>data|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệthống,bao|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||gồm kịch bản thành<br>công và thất bại.||trong <1s|||
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|Theo chuẩn<br>ISTQB|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|DB<br>corruption|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|DB<br>corruption|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|Theo chuẩn<br>ISTQB|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năngvà hiệu năng|stress load<br>> 10k|Không<br>phát hiện<br>lỗ hổng|JMeter<br>script|So sánh<br>benchmark với|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|TPS|bảo mật<br>OWASP<br>Top 10||release trước|
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Test môi<br>trường Pre-<br>Prod|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|Data|Thực hiện Data|invalid|User|Automation|So sánh|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|consistency<br>test|consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|data|login<br>thành<br>công<br>trong <1s|Selenium|benchmark với<br>release trước|
|---|---|---|---|---|---|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|invalid<br>data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||công và thất bại.||Top 10|||
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|
|Database<br>recovery|Thực hiện Database<br>recoverytest để|network|Cluster<br>failover|Manual test|So sánh<br>benchmark với|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||release trước<br>Theo chuẩn<br>ISTQB<br>Phải log toàn<br>bộ kết quả<br>Gửi báo cáo<br>PDF hàng ngày<br>So sánh<br>benchmark với<br>release trước|
||test||kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|disconnect|tự động<br>trong 5s|plan||release trước|
||Security<br>scan||Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Cluster<br>failover<br>tự động<br>trong 5s|JMeter<br>script||Theo chuẩn<br>ISTQB|
||Failover<br>test||Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium||Phải log toàn<br>bộ kết quả|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible||Gửi báo cáo<br>PDF hàng ngày|
||API stress<br>test||Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành côngvà thất|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium||So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||bại.|||||
|---|---|---|---|---|---|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Test môi<br>trường Pre-<br>Prod|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năngvà hiệu năng|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn|JMeter<br>script|Test môi<br>trường Pre-|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.||vẹn sau<br>sự cố||Prod|
|---|---|---|---|---|---|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Data<br>consistency|Thực hiện Data<br>consistencytest để|API call<br>batch|Không<br>phát hiện|Kịch bản|Theo chuẩn|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|test|kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|1000<br>request|lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Ansible|ISTQB|
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Theo chuẩn<br>ISTQB|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|Theo chuẩn<br>ISTQB|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|invalid<br>data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, baogồm kịch|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau|JMeter<br>script|Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||bản thành công và<br>thất bại.||sự cố|||
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|API call<br>batch<br>1000<br>request|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Failover|Thực hiện Failover<br>test để kiểm thử|DB|Không<br>phát hiện|Automation|Theo chuẩn|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|test|chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|corruption|lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Selenium|ISTQB|
|---|---|---|---|---|---|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|Theo chuẩn<br>ISTQB|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||bại.|||||
|---|---|---|---|---|---|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Database<br>recovery|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn|Kịch bản<br>Ansible|Test môi<br>trường Pre-|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||Prod<br>Gửi báo cáo<br>PDF hàng ngày<br>So sánh<br>benchmark với<br>release trước<br>Phải log toàn<br>bộ kết quả<br>Test môi<br>trường Pre-<br>Prod|
||test||và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.||vẹn sau<br>sự cố|||Prod|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible||Gửi báo cáo<br>PDF hàng ngày|
||Security<br>scan||Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script||So sánh<br>benchmark với<br>release trước|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible||Phải log toàn<br>bộ kết quả|
||Security<br>scan||Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script||Test môi<br>trường Pre-<br>Prod|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||công và thất bại.||Top 10|||
|---|---|---|---|---|---|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Theo chuẩn<br>ISTQB|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năngvà hiệu|network<br>disconnect|Cluster<br>failover<br>tựđộng|Manual test<br>plan|So sánh<br>benchmark với|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||release trước<br>So sánh<br>benchmark với<br>release trước<br>Gửi báo cáo<br>PDF hàng ngày<br>So sánh<br>benchmark với<br>release trước<br>Test môi<br>trường Pre-<br>Prod|
||||năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.||trong 5s|||release trước|
||Data<br>consistency<br>test||Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium||So sánh<br>benchmark với<br>release trước|
||Failover<br>test||Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible||Gửi báo cáo<br>PDF hàng ngày|
||Data<br>consistency<br>test||Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|invalid<br>data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible||So sánh<br>benchmark với<br>release trước|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành côngvà|API call<br>batch<br>1000<br>request|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium||Test môi<br>trường Pre-<br>Prod|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thất bại.|||||
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Theo chuẩn<br>ISTQB|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Security|Thực hiện Security<br>scan để kiểm thử|invalid|Hệ thống<br>chịu tải|Kịch bản|Test môi<br>trườngPre-|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|scan|chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|data|20k TPS<br>không<br>gián đoạn|Ansible|Prod|
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành côngvà|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thất bại.|||||
|---|---|---|---|---|---|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năngcủa hệ|valid data|User<br>login<br>thành<br>công|Manual test<br>plan|Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thống, bao gồm kịch<br>bản thành công và<br>thất bại.||trong <1s|||
|---|---|---|---|---|---|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||công và thất bại.|||||
|---|---|---|---|---|---|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năngvà hiệu năng|stress load<br>> 10k|User<br>login<br>thành|JMeter<br>script|So sánh<br>benchmark với|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||release trước<br>Phải log toàn<br>bộ kết quả<br>Gửi báo cáo<br>PDF hàng ngày<br>Theo chuẩn<br>ISTQB<br>Test môi<br>trường Pre-<br>Prod|
||||của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|TPS|công<br>trong <1s|||release trước|
||Security<br>scan||Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan||Phải log toàn<br>bộ kết quả|
||Login test||Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script||Gửi báo cáo<br>PDF hàng ngày|
||Failover<br>test||Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible||Theo chuẩn<br>ISTQB|
||API stress<br>test||Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible||Test môi<br>trường Pre-<br>Prod|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||Theo chuẩn<br>ISTQB<br>Gửi báo cáo<br>PDF hàng ngày<br>Gửi báo cáo<br>PDF hàng ngày<br>Phải log toàn<br>bộ kết quả<br>Test môi<br>trường Pre-<br>Prod|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script||Theo chuẩn<br>ISTQB|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|API call<br>batch<br>1000<br>request|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan||Gửi báo cáo<br>PDF hàng ngày|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible||Gửi báo cáo<br>PDF hàng ngày|
||Data<br>consistency<br>test||Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible||Phải log toàn<br>bộ kết quả|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành côngvà|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium||Test môi<br>trường Pre-<br>Prod|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thất bại.|||||
|---|---|---|---|---|---|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năngvà hiệu|API call<br>batch<br>1000|User<br>login<br>thành|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|request|công<br>trong <1s|||
|---|---|---|---|---|---|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|---|---|---|---|---|---|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành côngvà thất|invalid<br>data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||Test môi<br>trường Pre-<br>Prod<br>So sánh<br>benchmark với<br>release trước<br>Theo chuẩn<br>ISTQB<br>Phải log toàn<br>bộ kết quả<br>Phải log toàn|
||||bại.||||||
||Data<br>consistency<br>test||Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible||Test môi<br>trường Pre-<br>Prod|
||API stress<br>test||Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan||So sánh<br>benchmark với<br>release trước|
||Data<br>consistency<br>test||Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan||Theo chuẩn<br>ISTQB|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium||Phải log toàn<br>bộ kết quả|
||Load test||Thực hiện Load test<br>để kiểm thử chức|stress load<br>> 10k|Hệ thống<br>chịu tải|Automation||Phải log toàn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||bộ kết quả<br>Gửi báo cáo<br>PDF hàng ngày<br>Phải log toàn<br>bộ kết quả<br>Gửi báo cáo<br>PDF hàng ngày<br>Phải log toàn<br>bộ kết quả|
||||năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|TPS|20k TPS<br>không<br>gián đoạn|Selenium||bộ kết quả|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible||Gửi báo cáo<br>PDF hàng ngày|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Cluster<br>failover<br>tự động<br>trong 5s|JMeter<br>script||Phải log toàn<br>bộ kết quả|
||Failover<br>test||Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Cluster<br>failover<br>tự động<br>trong 5s|Kịch bản<br>Ansible||Gửi báo cáo<br>PDF hàng ngày|
||Login test||Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script||Phải log toàn<br>bộ kết quả|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||Phải log toàn<br>bộ kết quả<br>Test môi<br>trường Pre-<br>Prod<br>Phải log toàn<br>bộ kết quả<br>Theo chuẩn<br>ISTQB<br>Theo chuẩn<br>ISTQB|
||Login test||Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|stress load<br>> 10k<br>TPS|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script||Phải log toàn<br>bộ kết quả|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible||Test môi<br>trường Pre-<br>Prod|
||Login test||Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Automation<br>Selenium||Phải log toàn<br>bộ kết quả|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan||Theo chuẩn<br>ISTQB|
||Data<br>consistency<br>test||Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành côngvà|invalid<br>data|Cluster<br>failover<br>tự động<br>trong 5s|JMeter<br>script||Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thất bại.|||||
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Theo chuẩn<br>ISTQB|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức|invalid|Hệ thống<br>chịu tải|Kịch bản|Phải log toàn|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||bộ kết quả<br>Phải log toàn<br>bộ kết quả<br>Gửi báo cáo<br>PDF hàng ngày<br>Theo chuẩn<br>ISTQB<br>So sánh<br>benchmark với<br>release trước|
||||năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|data|20k TPS<br>không<br>gián đoạn|Ansible||bộ kết quả|
||API stress<br>test||Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible||Phải log toàn<br>bộ kết quả|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan||Gửi báo cáo<br>PDF hàng ngày|
||Login test||Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script||Theo chuẩn<br>ISTQB|
||Load test||Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible||So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|---|---|---|---|---|---|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|Phải log toàn<br>bộ kết quả|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>baogồm kịch bản|invalid<br>data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thành công và thất<br>bại.||Top 10|||
|---|---|---|---|---|---|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|So sánh<br>benchmark với<br>release trước|
|Login test|Thực hiện Login test<br>để kiểm thử chức|API call<br>batch|Cluster<br>failover|Kịch bản|So sánh<br>benchmark với|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|1000<br>request|tự động<br>trong 5s|Ansible|release trước|
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành côngvà|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thất bại.|||||
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năngvà hiệu|valid data|Không<br>phát hiện<br>lỗ hổng|Manual test<br>plan|So sánh<br>benchmark với|

||||**VIETTEL AI RACE**|**VIETTEL AI RACE**||||TD447|
|---|---|---|---|---|---|---|---|---|
||||**KỊCH BẢN KIỂM THỬ**||**QA**|||Lần ban hành: 1|
|||||||||release trước<br>So sánh<br>benchmark với<br>release trước<br>So sánh<br>benchmark với<br>release trước<br>Test môi<br>trường Pre-<br>Prod<br>So sánh<br>benchmark với<br>release trước|
||||năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.||bảo mật<br>OWASP<br>Top 10|||release trước|
||Database<br>recovery<br>test||Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|invalid<br>data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan||So sánh<br>benchmark với<br>release trước|
||Failover<br>test||Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium||So sánh<br>benchmark với<br>release trước|
||API stress<br>test||Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|JMeter<br>script||Test môi<br>trường Pre-<br>Prod|
||Data<br>consistency<br>test||Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành côngvà|network<br>disconnect|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|JMeter<br>script||So sánh<br>benchmark với<br>release trước|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thất bại.|||||
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Gửi báo cáo<br>PDF hàng ngày|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|invalid<br>data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Security|Thực hiện Security<br>scan để kiểm thử|API call<br>batch|Hệ thống<br>chịu tải|Manual test|So sánh<br>benchmark với|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|scan|chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|1000<br>request|20k TPS<br>không<br>gián đoạn|plan|release trước|
|---|---|---|---|---|---|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|Theo chuẩn<br>ISTQB|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|DB<br>corruption|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|API stress|Thực hiện API stress|invalid|Không|Kịch bản|Gửi báo cáo|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|test|test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|data|phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Ansible|PDF hàng ngày|
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Cluster<br>failover<br>tự động<br>trong 5s|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Automation<br>Selenium|So sánh<br>benchmark với<br>release trước|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Data<br>consistency<br>test|Thực hiện Data<br>consistency test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành côngvà|valid data|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||thất bại.|||||
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|invalid<br>data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|JMeter<br>script|So sánh<br>benchmark với<br>release trước|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|Cluster<br>failover<br>tự động<br>trong 5s|JMeter<br>script|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành côngvà thất|invalid<br>data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP|JMeter<br>script|Phải log toàn<br>bộ kết quả|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

||bại.||Top 10|||
|---|---|---|---|---|---|
|Security<br>scan|Thực hiện Security<br>scan để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|So sánh<br>benchmark với<br>release trước|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|DB<br>corruption|User<br>login<br>thành<br>công<br>trong <1s|Manual test<br>plan|Test môi<br>trường Pre-<br>Prod|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Cluster<br>failover<br>tự động<br>trong 5s|Automation<br>Selenium|Gửi báo cáo<br>PDF hàng ngày|
|Database<br>recovery|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng|valid data|Cluster<br>failover<br>tựđộng|Kịch bản<br>Ansible|Gửi báo cáo<br>PDF hàng ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|test|và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.||trong 5s|||
|---|---|---|---|---|---|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|API call<br>batch<br>1000<br>request|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|Kịch bản<br>Ansible|Test môi<br>trường Pre-<br>Prod|
|Database<br>recovery<br>test|Thực hiện Database<br>recovery test để<br>kiểm thử chức năng<br>và hiệu năng của hệ<br>thống, bao gồm kịch<br>bản thành công và<br>thất bại.|stress load<br>> 10k<br>TPS|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Phải log toàn<br>bộ kết quả|
|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|Theo chuẩn<br>ISTQB|
|API stress<br>test|Thực hiện API stress<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|stress load<br>> 10k<br>TPS|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Manual test<br>plan|Gửi báo cáo<br>PDF hàng ngày|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|

|Load test|Thực hiện Load test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|invalid<br>data|User<br>login<br>thành<br>công<br>trong <1s|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|---|---|---|---|---|---|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Hệ thống<br>chịu tải<br>20k TPS<br>không<br>gián đoạn|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|valid data|Không<br>phát hiện<br>lỗ hổng<br>bảo mật<br>OWASP<br>Top 10|Kịch bản<br>Ansible|Theo chuẩn<br>ISTQB|
|Failover<br>test|Thực hiện Failover<br>test để kiểm thử<br>chức năng và hiệu<br>năng của hệ thống,<br>bao gồm kịch bản<br>thành công và thất<br>bại.|network<br>disconnect|Dữ liệu<br>được khôi<br>phục toàn<br>vẹn sau<br>sự cố|JMeter<br>script|Phải log toàn<br>bộ kết quả|
|Login test|Thực hiện Login test<br>để kiểm thử chức<br>năng và hiệu năng<br>của hệ thống, bao<br>gồm kịch bản thành<br>công và thất bại.|network<br>disconnect|User<br>login<br>thành<br>công<br>trong <1s|Automation<br>Selenium|Theo chuẩn<br>ISTQB|

**==> picture [38 x 47] intentionally omitted <==**

||**VIETTEL AI RACE**|TD447|
|---|---|---|
||**KỊCH BẢN KIỂM THỬ QA**|Lần ban hành: 1|