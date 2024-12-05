print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


k = open('D:/a.txt', 'r')
char, wc, lc = 0, 0, 0
for line in k:
    for k in range(0, len(line)):
        char += 1
        if line[k] == ' ':
            wc += 1
        if line[k] == '\n':
            wc, lc = wc + 1, lc + 1
print("The no. of chars is %d\nThe no. of words is %d\nThe no. of lines is %d" % (char, wc, lc))
