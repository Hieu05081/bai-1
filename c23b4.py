print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


# Nhập câu từ người dùng
sentence = input("Nhập câu: ")

# Khởi tạo bộ đếm chữ cái và chữ số
letters = 0
digits = 0

# Duyệt qua từng ký tự trong câu
for char in sentence:
    if char.isalpha():  # Kiểm tra nếu là chữ cái
        letters += 1
    elif char.isdigit():  # Kiểm tra nếu là chữ số
        digits += 1

# In kết quả
print("Số chữ cái là:", letters)
print("Số chữ số là:", digits)
