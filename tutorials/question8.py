ch ='y'
user1name = raw_input("PLayer 1 play and enter your name :")
user2name = raw_input("PLayer 2 play and enter your name :")
while ch=='y':


    user1choice = raw_input("PLayer 1 play and enter your choice :")

    user2choice = raw_input("PLayer 2 play and enter your choice :")

    if user1choice=='scissors'and user2choice=='paper':
        print("%s wins" %user1name)

    elif user2choice=='scissors'and user1choice=='paper':
        print("%s wins" %user2name)

    elif user1choice=='paper'and user2choice=='rock':
        print("%s wins" %user1name)

    elif user2choice=='paper'and user1choice=='rock':
        print("%s wins" %user2name)

    elif user1choice=='rock'and user2choice=='scissors':
        print("%s wins" %user1name)

    elif user2choice=='rock'and user1choice=='scissors':
        print("%s wins" %user2name)

    print("Play again by pressing y or press n")
    ch = raw_input('')