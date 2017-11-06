from random import*

var = randint(0,9)
guess = int(raw_input("Choose any number between 0 to 9 :"))
if guess == var:
    print("You were right")
else:
    print("You entered :%d \nCorrect number was :%d"%(guess,var))
