print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


# Nhập chuỗi các số nhị phân từ người dùng
binary_numbers = input("Nhập chuỗi các số nhị phân 4 chữ số, phân tách bởi dấu phẩy: ").split(',')

# Lưu trữ các số nhị phân chia hết cho 5
result = []

# Kiểm tra từng số nhị phân
for binary in binary_numbers:
    if int(binary, 2) % 5 == 0:  # Chuyển nhị phân sang thập phân và kiểm tra chia hết cho 5
        result.append(binary)

# In ra kết quả
print(",".join(result))
