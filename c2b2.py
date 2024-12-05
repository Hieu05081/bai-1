import math

# Nhập tọa độ điểm thứ nhất
x1 = int(input("Enter x1 ---> "))
y1 = int(input("Enter y1 ---> "))

# Nhập tọa độ điểm thứ hai
x2 = int(input("Enter x2 ---> "))
y2 = int(input("Enter y2 ---> "))

# Tính khoảng cách
d1 = (x2 - x1) ** 2  # Bình phương khoảng cách theo trục x
d2 = (y2 - y1) ** 2  # Bình phương khoảng cách theo trục y
res = math.sqrt(d1 + d2)  # Căn bậc hai tổng bình phương

# Hiển thị kết quả
print("Distance between two points:", res)
