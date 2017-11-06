num = int(raw_input("Enter a number :"))
lst = []
for i in range(2,num/2+1):
    if num%i==0:
        lst.append(i)

print(lst)