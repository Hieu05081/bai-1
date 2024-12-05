class InputOutputString:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Nhập một chuỗi: ")

    def print_String(self):
        print(self.s.upper())

# Tạo đối tượng và sử dụng các phương thức
string_object = InputOutputString()
string_object.get_String()
string_object.print_String()
