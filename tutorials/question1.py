#first question on input
name = raw_input("Enter the name :")
age = raw_input("Enter the age :")
#calculating year
year = 2017+(100-int(age))
copies = raw_input("Enter the number of times to print :")
#typecasting
copies = int(copies)
for i in range(copies):
    print("you will be 100 in this year : %d" %year)

