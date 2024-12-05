print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


# Khởi tạo số dư ban đầu
balance = 0

# Nhập nhật ký giao dịch từ người dùng
while True:
    transaction = input("Nhập giao dịch (D <số tiền> hoặc W <số tiền>), hoặc bấm Enter để dừng: ")
    if not transaction:  # Nếu không có đầu vào, thoát khỏi vòng lặp
        break
    
    # Tách lệnh và số tiền
    type_, amount = transaction.split()
    amount = int(amount)
    
    # Kiểm tra loại giao dịch và cập nhật số dư
    if type_ == 'D':
        balance += amount
    elif type_ == 'W':
        balance -= amount

# In ra số dư cuối cùng
print("Số dư tài khoản là:", balance)
