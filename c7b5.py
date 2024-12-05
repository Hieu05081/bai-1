print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")




import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sắp xếp theo chiều cao tăng dần, nếu chiều cao bằng nhau thì sắp xếp theo id
indices = np.lexsort((student_id, student_height))

# In các chỉ số mô tả thứ tự sắp xếp
print("Chỉ số:")
print(indices)

# In dữ liệu đã sắp xếp
print("Dữ liệu sắp xếp:")
for index in indices:
    print(student_id[index], student_height[index])
