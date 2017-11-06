
def printbox(size):
    for i in range(size):
        print(" ---"*(size))
        print("|   "*(size+1))

    print(' ---' * (size))

size = int(raw_input("Enter the size of box : "))
printbox(size)