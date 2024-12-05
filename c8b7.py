print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


def write_list_to_file(fname, content):
    with open(fname, 'w') as f:
        for item in content:
            f.write(f"{item}\n") 
my_list = ['Hello', 'Python', 'File operations']
write_list_to_file('output.txt', my_list)
