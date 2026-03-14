## Tổng quan các scenario sẽ manual test
Cụ thể các test case sẽ được liệt kê trong file OrangeHRM_TestCase.xlsx

```
Module 1: Xác thực (Authentication)
Scenario ID | Mô tả
SC-001 | Xác minh đăng nhập với thông tin hợp lệ
SC-002 | Xác minh đăng nhập với tên người dùng không hợp lệ
SC-003 | Xác minh đăng nhập với mật khẩu không hợp lệ
SC-004 | Xác minh đăng nhập khi để trống trường tên người dùng
SC-005 | Xác minh đăng nhập khi để trống trường mật khẩu
SC-006 | Xác minh đăng nhập khi để trống cả hai trường
SC-007 | Xác minh chức năng đăng xuất
SC-008 | Xác minh chức năng “Quên mật khẩu”

Module 2: Quản lý nhân viên (PIM)
Scenario ID | Mô tả
SC-009 | Xác minh thêm nhân viên mới với dữ liệu hợp lệ
SC-010 | Xác minh thêm nhân viên khi thiếu các trường bắt buộc
SC-011 | Xác minh thêm nhân viên với định dạng dữ liệu không hợp lệ
SC-012 | Xác minh chỉnh sửa thông tin nhân viên hiện có
SC-013 | Xác minh xóa một nhân viên hiện có
SC-014 | Xác minh tìm kiếm nhân viên theo tên
SC-015 | Xác minh tìm kiếm nhân viên theo mã (ID)
SC-016 | Xác minh giá trị biên của mã nhân viên (độ dài tối thiểu/tối đa)
SC-017 | Xác minh giá trị biên của tên nhân viên (độ dài tối thiểu/tối đa)

Module 3: Quản lý nghỉ phép (Leave Management)
Scenario ID | Mô tả
SC-018 | Xác minh tạo yêu cầu nghỉ phép với dữ liệu hợp lệ
SC-019 | Xác minh tạo yêu cầu nghỉ phép với ngày trong quá khứ
SC-020 | Xác minh tạo yêu cầu nghỉ phép khi để trống các trường
SC-021 | Xác minh chuyển trạng thái nghỉ phép (Đang chờ → Được duyệt)
SC-022 | Xác minh chuyển trạng thái nghỉ phép (Đang chờ → Bị từ chối)
SC-023 | Xác minh chuyển trạng thái nghỉ phép (Được duyệt → Đã hủy)
SC-024 | Xác minh số dư nghỉ phép sau khi được duyệt
SC-025 | Xác minh admin có thể xem tất cả yêu cầu nghỉ phép

Module 4: Quản lý người dùng (Admin)
Scenario ID | Mô tả
SC-026 | Xác minh tạo người dùng hệ thống mới với dữ liệu hợp lệ
SC-027 | Xác minh tạo người dùng với tên đăng nhập bị trùng
SC-028 | Xác minh tạo người dùng khi để trống các trường bắt buộc
SC-029 | Xác minh chỉnh sửa thông tin người dùng hiện có
SC-030 | Xác minh xóa một người dùng hiện có
SC-031 | Xác minh tìm kiếm người dùng theo tên đăng nhập
SC-032 | Xác minh phân quyền vai trò người dùng (Admin vs Nhân viên)

Module 5: Thông tin của tôi (Quản lý hồ sơ/My Info)
Scenario ID | Mô tả
SC-033 | Xác minh cập nhật thông tin cá nhân
SC-034 | Xác minh cập nhật thông tin liên hệ với dữ liệu hợp lệ
SC-035 | Xác minh cập nhật thông tin liên hệ với định dạng số điện thoại không hợp lệ
SC-036 | Xác minh giá trị biên của số điện thoại (số chữ số tối thiểu/tối đa)
SC-037 | Xác minh đổi mật khẩu với dữ liệu hợp lệ
SC-038 | Xác minh đổi mật khẩu khi nhập sai mật khẩu hiện tại
SC-039 | Xác minh đổi mật khẩu khi mật khẩu mới không khớp

Module 6: Tìm kiếm & Lọc (Search & Filter)
Scenario ID | Mô tả
SC-040 | Xác minh tìm kiếm trả về kết quả chính xác
SC-041 | Xác minh tìm kiếm không có kết quả khớp
SC-042 | Xác minh tìm kiếm khi để trống đầu vào
SC-043 | Xác minh lọc theo trạng thái nhân viên (Đang làm việc/Tạm nghỉ)
SC-044 | Xác minh lọc theo chức danh công việc
