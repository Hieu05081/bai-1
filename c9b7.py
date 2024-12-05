print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


def copy_file_content(source, destination):
    with open(source, 'r') as src:
        content = src.read()  
    with open(destination, 'w') as dest:
        dest.write(content)
copy_file_content('source.txt', 'destination.txt')
