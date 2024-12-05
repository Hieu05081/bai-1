class StringReverser:
    def reverse_words(self, s):
        return ' '.join(s.split()[::-1])

# Tạo đối tượng và đảo ngược chuỗi từ
reverser = StringReverser()
print(reverser.reverse_words('hello .py'))  # Kết quả là '.py hello'
