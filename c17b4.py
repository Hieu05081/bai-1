print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


n = int(input('Nhap n: '))
for i in range(1, n):
    if sum([j for j in range(1, i + 1) if i % j == 0]) > i:
        print(i)
