def findwinner(grid):
    #row winner
    for i in range(3):
        val = set([grid[i][0],grid[i][1],grid[i][2]])
        if len(val) == 1 and val!=0:
            return val.pop()

    #col winner
    for i in range(3):
        val = set([grid[0][i], grid[1][i], grid[2][i]])
        if len(val) == 1 and val != 0:
            return val.pop()

    #diagonal winner

    val = set([grid[0][0],grid[1][1],grid[2][2]])
    val2 = set([grid[2][0],grid[1][1],grid[0][2]])
    if len(val) == 1 and val != 0:
        return val.pop()
    elif len(val2) == 1 and val != 0:
        return val2.pop()

winner_is_2 = [[2, 2, 0],[2, 1, 0],[2, 1, 1]]
winner_is_1 = [[1, 2, 0],[2, 1, 0],[2, 1, 1]]
winner_is_also_1 = [[0, 1, 0],[2, 1, 0],[2, 1, 1]]
no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 2]]
also_no_winner = [[1, 2, 0],[2, 1, 0],[2, 1, 0]]

print("The winner is "+str(findwinner(winner_is_2)))