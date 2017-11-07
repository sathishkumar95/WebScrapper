from collections import Counter

import json


with open('info.json', 'r') as f:
    #use load in file handling
    #use loads when json is a element
    data = json.load(f)
lst=[]
print("we have the following data :")
for i in data:
    print(" "+i)
    #preparing data for the counter
    var  = data[i].split('/')
    lst.append(var[1])
#takes the lst and shows the frequency
c = Counter(lst)
print c



choice = input("Do you want to view(press 0) or add birthday (press 1) or print all(press 2) :")
if choice == 0:
    name = raw_input("Enter the name of the person :")
    try:
        if data[name]:
            print("{} has birthday on {}".format(name,data[name]))
    except:
        print("{} IS NOT IN THE LIST ".format(name))
elif choice == 1:
    name = raw_input("Enter the name of the person :")
    birth = raw_input("Enter the birthday :")
    data[name]= birth
    for i in data:
        print(" "+i)
    with open('info.json', 'w') as f:
        json.dump(data,f)


elif choice == 2:
    for i in data:
        print(" {} has birthday on {}" .format(i,data[i]))
