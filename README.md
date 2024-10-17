# Thông tin nhóm
Bài tập lớn môn "Lưu trữ và xử lý dữ liệu lớn" - Nhóm 17 - 20241.1

Đại học Bách Khoa Hà Nội

Môn học: Lưu trữ và xử lý dữ liệu lớn (IT4391)

GVHD: TS. Trần Việt Trung

Nhóm: 17

| STT | Họ và Tên           | Mã Sinh Viên | Email                             |
|-----|---------------------|--------------|-----------------------------------|
| 1   | Nguyễn Văn Trường    | 20215495     | truong.nv215495@sis.hust.edu.vn   |
| 2   | Nguyễn Đình Khải     | 20215400     | khai.nd215400@sis.hust.edu.vn     |
| 3   | Đỗ Xuân Trọng        | 20210865     | trong.dx210865@sis.hust.edu.vn    |
| 4   | Lê Tấn Đạt           | 20215339     | dat.lt215339@sis.hust.edu.vn      |
| 5   | Vũ Phương Thanh      | 20210790     | thanh.vp210790@sis.hust.edu.vn    |

# Về Bài tập lớn: 
## Mục tiêu của hệ thống
Hệ thống này nhằm phân tích giá thời gian thực của các loại tiền điện tử, ví dụ như Bitcoin và Litecoin. Dự án được thiết kế để xử lý lượng giao dịch khổng lồ xảy ra mỗi giây bằng cách sử dụng các framework big data như HBase, Kafka, và Spark. Mục đích là xây dựng một pipeline hiệu quả để theo dõi giá tiền tệ số theo thời gian thực.

## Kiến trúc:
Các thành phần chính:
![image](https://github.com/user-attachments/assets/35f686b7-586a-478d-a4c1-d9ded1f62bc4)

### Data-producer:

Thành phần này có nhiệm vụ lấy dữ liệu thời gian thực về giá giao dịch cuối cùng (LastTradePrice) từ API của gdax (một sàn giao dịch tiền điện tử).
Cứ mỗi giây, dữ liệu này sẽ được lấy và đưa vào Kafka để xử lý tiếp.
### Data-storage:

Dữ liệu từ Kafka được lưu trữ vào HBase để phục vụ việc phân tích sau này.
### Data-stream:

Dữ liệu được truyền qua Kafka sẽ được xử lý bằng Spark Streaming, một công cụ xử lý dữ liệu theo thời gian thực.
Trong quá trình này, hệ thống sẽ tính toán các chỉ số như giá trung bình, giá mở cửa (open), giá đóng cửa (close), giá thấp nhất (low), và giá cao nhất (high) cho mỗi chu kỳ thời gian.
### Publish and display:

Sau khi dữ liệu được xử lý, nó sẽ được đẩy vào Redis để phục vụ việc hiển thị trên user dashboard.

User dashboard sẽ được xây dựng bằng Node.js


