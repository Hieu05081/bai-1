print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


import numpy as np

def find_max_min(arr):
    max_element = np.max(arr)
    min_element = np.min(arr)
    return max_element, min_element

def main():
    n = int(input("Nhập số lượng phần tử của mảng: "))
    arr = np.zeros(n, dtype=int)
    for i in range(n):
        element = int(input(f"Nhập phần tử thứ {i+1}: "))
        arr[i] = element
    
    max_element, min_element = find_max_min(arr)
    print("Phần tử lớn nhất:", max_element)
    print("Phần tử nhỏ nhất:", min_element)

if __name__ == '__main__':
    main()
