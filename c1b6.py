print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


class Circle(object):
    # Hàm khởi tạo nhận bán kính r
    def __init__(self, r):
        self.radius = r

    # Phương thức tính diện tích hình tròn
    def area(self):
        return self.radius ** 2 * 3.14

# Tạo một đối tượng Circle với bán kính là 2
aCircle = Circle(2)

# In ra diện tích của hình tròn
print(aCircle.area())
