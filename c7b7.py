print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


def count_lines_in_file(fname):
    with open(fname, 'r') as f:
        lines = f.readlines()
        print(f"Number of lines: {len(lines)}")
        
count_lines_in_file('test.txt')
