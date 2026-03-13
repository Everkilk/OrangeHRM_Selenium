# Dự Án Kiểm Thử OrangeHRM – Tóm Tắt Báo Cáo Kiểm Thử Phần Mềm

**Mô tả:** Thực hiện kiểm thử toàn diện cho hệ thống quản lý nhân sự, tập trung vào kiểm thử thủ công, kiểm thử hộp đen và kiểm thử tự động bằng Selenium WebDriver và pytest.

**Công nghệ sử dụng:** Python, Selenium WebDriver, pytest, Page Object Model (POM), Microsoft Excel, pytest-html, Kiểm thử hộp đen, Phân vùng tương đương, Phân tích giá trị biên

**Trách nhiệm:**
- Thực hiện kiểm thử thủ công và kiểm thử hộp đen trên 6 mô-đun (Đăng nhập, Bảng điều khiển, Nghỉ phép, Quản lý nhân viên, Quản trị và Thông tin cá nhân) nhằm phát hiện lỗi và đảm bảo chất lượng phần mềm.
- Xây dựng và thực thi 65 test case tự động bằng Selenium WebDriver và pytest theo mô hình thiết kế Page Object Model (POM) để kiểm tra giao diện người dùng và hành vi chức năng.
- Lập tài liệu kịch bản kiểm thử, test case và tạo báo cáo kiểm thử dạng HTML bằng pytest-html để theo dõi kết quả kiểm thử và ghi nhận lỗi.

---

## Kịch Bản Kiểm Thử Thủ Công & Test Case

### Mô-đun 1 – Đăng nhập

| # | Kịch bản | Test Case |
|---|----------|-----------|
| 1 | Kiểm tra đầu vào form đăng nhập | Nhập tên đăng nhập, để trống mật khẩu → kỳ vọng hiển thị thông báo lỗi |
| 2 | Kiểm tra đầu vào form đăng nhập | Nhập email sai định dạng vào ô tên đăng nhập → kỳ vọng hiển thị lỗi xác thực |
| 3 | Kiểm tra đầu vào form đăng nhập | Để trống cả tên đăng nhập và mật khẩu → kỳ vọng hiển thị thông báo lỗi |
| 4 | Kiểm tra đầu vào form đăng nhập | Nhập tên đăng nhập hợp lệ nhưng mật khẩu sai → kỳ vọng hiển thị lỗi "Thông tin đăng nhập không hợp lệ" |
| 5 | Xác thực đăng nhập thành công | Nhập tên đăng nhập và mật khẩu hợp lệ → kỳ vọng chuyển hướng đến Bảng điều khiển |
| 6 | Điều hướng Quên mật khẩu | Nhấp vào liên kết "Quên mật khẩu" → kỳ vọng điều hướng đến trang Đặt lại mật khẩu |
| 7 | Hủy Quên mật khẩu | Nhấp "Hủy" trên trang Quên mật khẩu → kỳ vọng quay về trang Đăng nhập |
| 8 | Luồng đặt lại mật khẩu | Gửi tên đăng nhập hợp lệ trên trang Quên mật khẩu → kỳ vọng hiển thị thông báo xác nhận |
| 9 | Hiển thị giao diện | Mở trang Đăng nhập → kỳ vọng logo OrangeHRM hiển thị |
| 10 | Hiển thị giao diện | Mở trang Đăng nhập → kỳ vọng tiêu đề trang hiển thị đúng nội dung |
| 11 | Hiển thị giao diện | Mở trang Đăng nhập → kỳ vọng phần tử tiêu đề trang hiển thị |
| 12 | Liên kết mạng xã hội | Mở trang Đăng nhập → kỳ vọng biểu tượng LinkedIn hiển thị và liên kết đúng |
| 13 | Liên kết mạng xã hội | Mở trang Đăng nhập → kỳ vọng biểu tượng Facebook hiển thị và liên kết đúng |
| 14 | Liên kết mạng xã hội | Mở trang Đăng nhập → kỳ vọng biểu tượng Twitter hiển thị và liên kết đúng |
| 15 | Liên kết mạng xã hội | Mở trang Đăng nhập → kỳ vọng biểu tượng YouTube hiển thị và liên kết đúng |
| 16 | Phân vùng tương đương | Cung cấp thông tin đăng nhập không hợp lệ từ bộ dữ liệu → kỳ vọng đăng nhập thất bại với mọi phân vùng không hợp lệ |
| 17 | Tính toàn vẹn liên kết | Quét tất cả liên kết trên trang Đăng nhập → kỳ vọng không có liên kết bị hỏng (HTTP 200) |

---

### Mô-đun 2 – Bảng điều khiển

| # | Kịch bản | Test Case |
|---|----------|-----------|
| 1 | Nhận diện trang | Điều hướng đến Bảng điều khiển → kỳ vọng tiêu đề trang hiển thị "Dashboard" |
| 2 | Điều hướng widget | Nhấp vào widget Chấm công → kỳ vọng trang Đồng hồ mở ra |
| 3 | Điều hướng widget | Nhấp vào widget Hiệu suất → kỳ vọng trang Hiệu suất mở ra |
| 4 | Điều hướng widget | Nhấp vào phím tắt "Phân công nghỉ phép" → kỳ vọng trang Phân công nghỉ phép mở ra |
| 5 | Điều hướng widget | Nhấp vào phím tắt "Danh sách nghỉ phép" → kỳ vọng trang Danh sách nghỉ phép mở ra |
| 6 | Điều hướng widget | Nhấp vào phím tắt "Bảng chấm công" → kỳ vọng trang Bảng chấm công mở ra |
| 7 | Điều hướng widget | Nhấp vào phím tắt "Đăng ký nghỉ phép" → kỳ vọng trang Đăng ký nghỉ phép mở ra |
| 8 | Điều hướng widget | Nhấp vào phím tắt "Nghỉ phép của tôi" → kỳ vọng trang Nghỉ phép của tôi mở ra |
| 9 | Điều hướng widget | Nhấp vào phím tắt "Bảng chấm công của tôi" → kỳ vọng trang Bảng chấm công của tôi mở ra |
| 10 | Điều hướng widget | Mở Cài đặt nghỉ phép nhân viên từ Bảng điều khiển → kỳ vọng trang cài đặt đúng |
| 11 | Điều hướng widget | Nhấp vào widget Buzz → kỳ vọng trang Buzz mở ra |
| 12 | Chụp màn hình | Chụp ảnh màn hình tất cả các phần của Bảng điều khiển → kỳ vọng không có lỗi hiển thị |
| 13 | Hiển thị biểu đồ | Kiểm tra biểu đồ Phân bổ nhân viên → kỳ vọng biểu đồ hiển thị với dữ liệu |
| 14 | Điều hướng thanh bên | Nhấp từng mục trong thanh bên Admin từ Bảng điều khiển → kỳ vọng tất cả liên kết hoạt động |
| 15 | Tính toàn vẹn liên kết | Quét tất cả liên kết trên Bảng điều khiển → kỳ vọng không có liên kết bị hỏng |

---

### Mô-đun 3 – Nghỉ phép

| # | Kịch bản | Test Case |
|---|----------|-----------|
| 1 | Truy cập menu | Nhấp vào mục Nghỉ phép trong thanh bên → kỳ vọng trang Nghỉ phép tải thành công |
| 2 | Hiển thị danh sách nghỉ phép | Mở menu con Danh sách nghỉ phép → kỳ vọng bảng dữ liệu nghỉ phép xuất hiện |
| 3 | Đặt lại tìm kiếm | Nhấp nút Đặt lại trên form bộ lọc Danh sách nghỉ phép → kỳ vọng tất cả trường bộ lọc được xóa |
| 4 | Kiểm tra xác thực trường | Gửi bộ lọc với trường Từ ngày bị trống → kỳ vọng hiển thị lỗi xác thực |
| 5 | Kiểm tra xác thực trường | Gửi bộ lọc với trường Đến ngày bị trống → kỳ vọng hiển thị lỗi xác thực |
| 6 | Kiểm tra xác thực trường | Gửi bộ lọc với trường Trạng thái bị trống → kỳ vọng hiển thị lỗi xác thực |
| 7 | Kiểm tra xác thực trường | Gửi bộ lọc với tất cả các trường bị trống → kỳ vọng hiển thị lỗi xác thực trên các trường bắt buộc |

---

### Mô-đun 4 – Quản lý nhân viên (PIM)

| # | Kịch bản | Test Case |
|---|----------|-----------|
| 1 | Điều hướng menu | Nhấp vào mục PIM → kỳ vọng trang Danh sách nhân viên tải thành công |
| 2 | Thêm nhân viên | Nhấp nút Thêm → kỳ vọng trang form Thêm nhân viên mở ra |
| 3 | Tìm kiếm theo tên | Nhập tên nhân viên vào ô tìm kiếm → kỳ vọng danh sách nhân viên phù hợp xuất hiện |
| 4 | Tìm kiếm theo mã | Nhập mã nhân viên vào ô tìm kiếm → kỳ vọng nhân viên tương ứng xuất hiện |
| 5 | Lọc theo chức danh | Chọn chức danh từ dropdown Chức danh → kỳ vọng danh sách lọc theo chức danh đó |
| 6 | Lọc theo trạng thái | Chọn trạng thái hợp đồng từ dropdown Trạng thái → kỳ vọng danh sách lọc theo trạng thái đó |
| 7 | Lọc theo tùy chọn bao gồm | Chọn tùy chọn từ dropdown Bao gồm → kỳ vọng danh sách phản ánh lựa chọn |
| 8 | Lọc theo phòng ban | Chọn phòng ban từ dropdown Đơn vị con → kỳ vọng danh sách lọc theo phòng ban đó |
| 9 | Tìm kiếm quản lý | Nhập tên quản lý vào trường Tên quản lý → kỳ vọng kết quả phù hợp xuất hiện |
| 10 | Đặt lại bộ lọc | Nhấp nút Đặt lại → kỳ vọng tất cả trường bộ lọc tìm kiếm được xóa |

---

### Mô-đun 5 – Quản trị

| # | Kịch bản | Test Case |
|---|----------|-----------|
| 1 | Truy cập trang Quản trị | Đăng nhập và điều hướng đến trang Quản trị → kỳ vọng bảng Quản lý người dùng hiển thị |
| 2 | Tìm kiếm người dùng | Nhập tên đăng nhập vào trường tìm kiếm → kỳ vọng người dùng hệ thống phù hợp xuất hiện |
| 3 | Lọc theo vai trò | Chọn vai trò hệ thống từ dropdown → kỳ vọng danh sách lọc theo vai trò đó |
| 4 | Lọc theo tên nhân viên | Nhập tên nhân viên → kỳ vọng người dùng liên kết với nhân viên đó xuất hiện |
| 5 | Lọc theo trạng thái | Chọn Đang hoạt động hoặc Không hoạt động từ dropdown Trạng thái → kỳ vọng danh sách lọc phù hợp |
| 6 | Nút thêm người dùng | Nhấp nút Thêm → kỳ vọng form Thêm người dùng mở ra |
| 7 | Thêm người dùng mới | Điền form Thêm người dùng với dữ liệu hợp lệ và gửi → kỳ vọng người dùng mới xuất hiện trong danh sách |

---

### Mô-đun 6 – Thông tin cá nhân (My Info)

| # | Kịch bản | Test Case |
|---|----------|-----------|
| 1 | Truy cập trang | Đăng nhập và điều hướng đến My Info → kỳ vọng form Thông tin cá nhân hiển thị |
| 2 | Chỉnh sửa tên | Xóa và nhập giá trị mới vào trường Tên → kỳ vọng trường chấp nhận dữ liệu nhập |
| 3 | Chỉnh sửa tên đệm | Xóa và nhập giá trị mới vào trường Tên đệm → kỳ vọng trường chấp nhận dữ liệu nhập |
| 4 | Chỉnh sửa họ | Xóa và nhập giá trị mới vào trường Họ → kỳ vọng trường chấp nhận dữ liệu nhập |
| 5 | Ngày sinh | Chọn ngày từ bộ chọn ngày Ngày sinh → kỳ vọng ngày đã chọn được hiển thị |
| 6 | Lựa chọn dropdown | Chọn giá trị từ dropdown Giới tính / Quốc tịch → kỳ vọng giá trị được chọn |
| 7 | Nút thao tác form | Nhấp nút Lưu → kỳ vọng hiển thị thông báo lưu thành công |
| 8 | Nhóm máu | Chọn nhóm máu từ dropdown Nhóm máu → kỳ vọng giá trị được lưu |
| 9 | Gửi form | Điền tất cả trường bắt buộc và nhấp Lưu → kỳ vọng form gửi thành công |
