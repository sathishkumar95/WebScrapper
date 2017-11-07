grid=[[0,0,0],[0,0,0],[0,0,0]]

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

    return 0


def check(count, grid):
    if count > 4:
        res = findwinner(grid)

        if res != 0:
            print("The winner is " + str(res))
            exit(0)


def play(grid):
    count = 0
    for i in range(3):

        x, y = map(int, raw_input("Player 1 :").split())
        count += 1
        grid[x-1][y-1] = 1
        check(count, grid)
        print(grid)
        x, y = map(int, raw_input("Player 2 :").split())
        grid[x - 1][y - 1] = 2
        count += 1
        check(count, grid)
        print(grid)




play(grid)