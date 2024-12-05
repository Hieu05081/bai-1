print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


ds = input('Nhap chuoi: ').split(',')
ds = [bin(int(s, 2))[4:] for s in ds]
ds = [s for s in ds if s[-1] in ('0', '5')]
print(','.join(ds))
