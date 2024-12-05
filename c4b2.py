# Nhập khoảng (a, b)
a = int(input("Nhập giá trị a: "))
b = int(input("Nhập giá trị b: "))

print("Số nghịch đảo và kết quả thập phân trong khoảng (a, b):")
for i in range(a + 1, b):
    reciprocal = 1 / i
    print(f"Số {i}: nghịch đảo là {reciprocal}")
