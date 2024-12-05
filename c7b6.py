print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


class Circle:
    # Hàm khởi tạo nhận bán kính r
    def __init__(self, r):
        self.radius = r

    # Phương thức tính diện tích hình tròn
    def area(self):
        return 3.14 * (self.radius ** 2)

    # Phương thức tính chu vi hình tròn
    def circumference(self):
        return 2 * 3.14 * self.radius

# Tạo đối tượng Circle với bán kính là 5
circle = Circle(5)

# In ra diện tích và chu vi của hình tròn
print("Diện tích:", circle.area())           # Kết quả: 78.5
print("Chu vi:", circle.circumference())      # Kết quả: 31.400000000000002
