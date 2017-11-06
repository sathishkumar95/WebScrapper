str = raw_input("Enter the string :")
rev = ''.join(reversed(str))
if str==rev:
    print("Plaindrome")
else:
    print("Not a plaindrome")