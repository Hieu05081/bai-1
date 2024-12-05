print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


ds = input('Nhap dãy các từ: ').split()
max_length = 0
longest_words = []
for word in ds:
    if len(word) >= max_length:
        longest_words.append(word)
        max_length = len(word)
print('Từ dài nhất trong dãy: ', longest_words)
