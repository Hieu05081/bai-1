print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


class py_solution:
    def roman_to_int(self, s):
        # Tạo từ điển ánh xạ các ký tự La Mã và giá trị tương ứng
        rom_val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        int_val = 0  # Khởi tạo giá trị số nguyên là 0

        # Lặp qua từng ký tự trong chuỗi La Mã
        for i in range(len(s)):
            # Nếu ký tự hiện tại nhỏ hơn ký tự kế tiếp, trừ giá trị của ký tự hiện tại
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        
        return int_val

# Tạo đối tượng của lớp py_solution
solution = py_solution()

# Thử nghiệm chuyển đổi số La Mã thành số nguyên
print(solution.roman_to_int('MMMM'))     # Kết quả mong đợi: 4000
print(solution.roman_to_int('MCMLIV'))   # Kết quả mong đợi: 1954
print(solution.roman_to_int('C'))        # Kết quả mong đợi: 100
