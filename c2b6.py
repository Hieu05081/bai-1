print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


class Hinhchunhat:
    # Hàm khởi tạo nhận chiều dài và chiều rộng
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    # Phương thức tính diện tích hình chữ nhật
    def dientich(self):
        return self.dai * self.rong

# Tạo một đối tượng Hinhchunhat với chiều dài là 5 và chiều rộng là 3
hcn = Hinhchunhat(5, 3)

# In ra diện tích của hình chữ nhật
print(hcn.dientich())
