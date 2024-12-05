print("Sinh Vien : Nguyen Phuong Hieu")
print("Ma so SV : 235752021610040")


def find_longest_words(fname):
    with open(fname, 'r') as f:
        words = f.read().split()
        max_length = max(len(word) for word in words) 
    longest_words = [word for word in words if len(word) == max_length] 
    print(f"Longest words: {longest_words}")

find_longest_words('test.txt')
