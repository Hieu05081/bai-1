print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


n = int(input('Nhap n: '))
fib = []
for i in range(1, n):
    if i <= 1:
        fib.append(i)
    else:
        fib.append(fib[-1]+fib[-2])
print(fib)
