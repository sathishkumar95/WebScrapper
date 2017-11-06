lst = [1,2,1,3,4,2,3,3,4,3,43,4,5,5,6,6,6,6,6,6,7,8]

def setlist(lst):
    return set(lst)

def looplst(lst):
    new_lst=[]
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)

    return  new_lst

temp = looplst(lst)
temp2 = setlist(lst)
print("Loop elimination : %s" %temp)
print("Set :%s" %temp2)