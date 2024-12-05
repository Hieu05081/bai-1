import math

def Tinh(R):
    if R <= 0:
        return "Bán kính không hợp lệ!"
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    return chu_vi, dien_tich

R = float(input("Nhập bán kính R: "))
result = Tinh(R)
print("Chu vi và diện tích của hình tròn là:", result)
