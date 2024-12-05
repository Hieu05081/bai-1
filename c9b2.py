# Nhập chuỗi từ bàn phím
string = input("Nhập một chuỗi: ")

# Khởi tạo từ điển rỗng
char_count = {}

# Duyệt qua từng ký tự trong chuỗi
for char in string:
    if char in char_count:
        char_count[char] += 1  # Tăng số đếm nếu ký tự đã tồn tại
    else:
        char_count[char] = 1  # Thêm ký tự mới vào từ điển

# In kết quả
print("Số lần xuất hiện của các ký tự:", char_count)
