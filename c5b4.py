input_list = input("Nhập danh sách các từ: ").split()
reversed_list = input_list[::-1]
for word in reversed_list:
    print(word, end=' ')
