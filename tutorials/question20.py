#binary search
lst = [1,1,2,2,3,4,4,5,6,7,8,9,10]

def binarysearch(low, high, item):

    while low<=high:
        mid = (low + high) / 2
        if lst[mid]==item:
            return mid
        elif item>lst[mid]:
            low = mid+1
        elif item<lst[mid]:
            high = mid-1

    return False

num = int(raw_input("Enter the number : "))
status = binarysearch(0,len(lst)-1,num)
if status:
    print("The value is present at %d position" %(status+1))
else:
    print("NOt present")



