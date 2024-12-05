print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")



input_file = open('D:/a.txt', 'r')
for line in input_file:
    l = len(line)
    s = ''
    while l > 1:
        s += line[l - 1]
        l -= 1
    print(s)
input_file.close()
