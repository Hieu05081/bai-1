print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


# Nhập câu từ người dùng
sentence = input("Nhập câu: ")

# Khởi tạo bộ đếm chữ hoa và chữ thường
uppercase_count = 0
lowercase_count = 0

# Duyệt qua từng ký tự trong câu
for char in sentence:
    if char.isupper():  # Kiểm tra nếu là chữ hoa
        uppercase_count += 1
    elif char.islower():  # Kiểm tra nếu là chữ thường
        lowercase_count += 1

# In kết quả
print("Chữ hoa:", uppercase_count)
print("Chữ thường:", lowercase_count)
