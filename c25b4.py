print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


# Nhập chuỗi các số từ người dùng, tách thành danh sách
numbers = input("Nhập các số, phân tách bởi dấu phẩy: ").split(',')

# Lọc các số lẻ
odd_numbers = [num for num in numbers if int(num) % 2 != 0]

# In kết quả, các số lẻ được phân tách bởi dấu phẩy
print(",".join(odd_numbers))
