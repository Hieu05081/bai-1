print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")

# File: mymath.py

def square(n):
    return n * n

def cube(n):
    return n * n * n

def average(values):
    nvals = len(values)
    total = 0.0
    for v in values:
        total += v
    return float(total) / nvals
