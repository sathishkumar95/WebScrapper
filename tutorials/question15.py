def processstring(str1):
    return ' '.join(str1.split(' ')[::-1])
str1 = raw_input("Enter the String :")
w=processstring(str1)
print(w)
