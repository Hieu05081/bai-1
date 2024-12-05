print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


n = int(input('Nhap n: '))
for i in range(1, n + 1):
  print('(n - i) + '.join([str(j) for j in range(1, i + 1)]))
