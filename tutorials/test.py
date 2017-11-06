with open('primenumbers.txt', 'r') as open_file:
    content = open_file.readline()
    lst=[]
    while content:
        lst.append(int(content))
        content = open_file.readline()
    print lst