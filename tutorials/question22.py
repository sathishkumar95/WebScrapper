with open('NewyorkTimes.txt', 'r') as open_file:
    content = open_file.readline()
    while content:
        print(content)
        content = open_file.readline()