def prime(num):
    for i in range(2, num/2+1):
        if num % i == 0:
            return True
    return False

num = int(raw_input("Enter the number to check :"))
if prime(num):
    print("Number is not a prime")
else:
    print("Number is a prime")

