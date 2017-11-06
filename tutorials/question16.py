password=''
def generate(strength):
    lst=['ganesha','krishna','jesus','shiva']
    if strength=='strong':
        password = str(randint(11,99))
        password+=lst[randint(0,3)]
        password += str(randint(11, 99))
    elif strength=='normal':
        password=str(randint(111111111,999999999))

    elif strength=='weak':
        password=lst[randint(0,3)]
    else:
        print("Try again")

    return password

from random import *
user_ip= raw_input("Enter how strong you want the password(strong,normal,weak):")
print(generate(user_ip))
