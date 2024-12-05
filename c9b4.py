print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


ds = input('Nhap chuoi: ').split()

ds = [1, 2, 3, 4, 5]
x = list(zip(ds[1:], ds[:-1]))
for c in x:
    print(c)
