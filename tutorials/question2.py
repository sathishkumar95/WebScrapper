num = raw_input("Enter the number :")
check = raw_input("Enter the other number :")
num = int(num)
check = int(check)
if(num%check==0): print("Hey %d is divisible by %d" %(num,check))
else :
    if(num%2 == 0):
        print("Its even!!")
        if(num%4==0):
          print(" Hey Its divisible by 4!!")
    else : print("Its ODD!!")
