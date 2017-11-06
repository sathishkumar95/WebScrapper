from random import *

def calc(guess,num):
    cow=0
    bull=0

    for i in range(len(guess)):
        if guess[i]==num[i]:
            cow+=1
        elif guess[i] in num:
            bull+=1

    print("Your Cows were :%d \nBulls :%d"%(cow, bull))
    return cow


count=0
guess = 0
cow=0
print("WECOME TO THE COWS AND BULLS GAME ")
num = str(randint(1000, 9999))
print(num)
while cow!=4:
    guess = raw_input("Enter your best guess :")
    cow = calc(guess,num)









