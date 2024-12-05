print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


import datetime as dt

# Định dạng thời gian
format = '%Y-%m-%dT%H:%M:%S'

# Tạo đối tượng datetime từ chuỗi theo định dạng trên
t1 = dt.datetime.strptime('2008-10-12T14:45:52', format)
print('Day ' + str(t1.day))       # In ra ngày của t1
print('Month ' + str(t1.month))    # In ra tháng của t1
print('Minute ' + str(t1.minute))  # In ra phút của t1
print('Second ' + str(t1.second))  # In ra giây của t1

# Định nghĩa ngày và giờ hiện tại
t2 = dt.datetime.now()

# Tính khoảng cách ngày giữa t2 và t1
diff = t2 - t1
print('How many days difference? ' + str(diff.days))
