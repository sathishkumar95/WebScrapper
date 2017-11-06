def genfib(num):
    a=1
    b=1
    if num==1:
        print(a)
    else :
        print(" ")

    for i in range(3,num):
        c = a + b
        print("  %d" %c)
        a=b
        b=c

num = int(raw_input("Enter the limit :"))
genfib(num)


