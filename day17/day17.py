f = open('adventofcode/day17/data.txt', 'r')
jets = list(f.read())
trocks = 0
cur_p = 0
start = (0, 2)
grid = [[0 for j in range(7)] for i in range(4)]
rows = len(grid)
cols = len(grid[0])
cur_highest = 999
cur_j = 0
pieces = [
    
    [[1,1,1,1],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0]],

    [[0,1,0,0],
    [1,1,1,0],
    [0,1,0,0],
    [0,0,0,0]],

    [[0,0,1,0],
    [0,0,1,0],
    [1,1,1,0],
    [0,0,0,0]],

    [[1,0,0,0],
    [1,0,0,0],
    [1,0,0,0],
    [1,0,0,0]],

    [[1,1,0,0],
    [1,1,0,0],
    [0,0,0,0],
    [0,0,0,0]],  
]

def draw(x, y):
    pheight = maxheight()
    plen = maxlen()
    for i in range(pheight):
        for j in range(plen):
            if grid[x + i][y + j] != 1:
                grid[x + i][y + j] = pieces[cur_p][i][j]

def maxlen():
    plen = 0
    count = 0
    for i in range(4):
        for j in range(4):
            if pieces[cur_p][i][j] == 1:
                count += 1
        if count > plen:
            plen = count
        count = 0
    return plen

def maxheight():
    pheight = 0
    count = 0
    for i in range(4):
        for j in range(4):
            if pieces[cur_p][j][i] == 1:
                count += 1
        if count > pheight:
            pheight = count
        count = 0
    return pheight

def move_sideways(x, y, direction):
    plen = 0
    count = 0
    for i in range(4):
        for j in range(4):
            if pieces[cur_p][i][j] == 1:
                count += 1
        if count > plen:
            plen = count
        count = 0
    if direction == '>' and y + plen < cols:
        for i in range(4):
            if pieces[cur_p][i][plen - 1] == 1 and grid[x + i][y + plen] == 1:
                return False
        return True
    elif direction == '<' and y > 0:
        if cur_p == 1:
            if grid[x][y] == 1 or grid[x + 2][y] == 1:
                return False
        for i in range(4):
            if pieces[cur_p][i][0] == 1 and grid[x + i][y - 1] == 1:
                return False
        return True
    return False

def move_down(x, y):
    pheight = 0
    count = 0
    for i in range(4):
        for j in range(4):
            if pieces[cur_p][j][i] == 1:
                count += 1
        if count > pheight:
            pheight = count
        count = 0
    if x + 1 == len(grid):
        return False
    else:
        if cur_p == 1:
            if grid[x + 2][y] == 1 or grid[x + 2][y + 2] == 1:
                return False
        for i in range(len(pieces[cur_p])):
            if pieces[cur_p][pheight - 1][i] == 1 and grid[x + pheight][y + i] == 1:
                return False
    return True

def move():
    global cur_j
    x, y = start
    blocked = False
    while not blocked:
        jet = jets[cur_j]
        #print(x, y, jet)
        if cur_j == len(jets) - 1:
            cur_j = 0
        else:
            cur_j += 1
        #check left and right pos
        if jet == '>' and move_sideways(x, y, jet):
            y += 1
        if jet == '<' and move_sideways(x, y, jet):
            y -= 1
        #check bottom pos
        if move_down(x, y):
            x += 1
        else:
            blocked = True
    return x, y

def update_grid():
    pheight = maxheight()
    highest_rock = 0
    cur_height = len(grid)
    for i, row in enumerate(grid):
        if 1 in row:
            highest_rock = i
            break
    #or row in grid:
    #    print(row)
    if highest_rock - pheight > 3:
        for i in range((highest_rock - pheight) - 3):
            del grid[0]
    else:
        for i in range((3 - highest_rock) + pheight):
            grid.insert(0, [0 for i in range(7)])
    return highest_rock, cur_height

h = 0
c = 0
while trocks < 2022:
    print(trocks)
    x, y = move()
    draw(x, y)
    if cur_p == 4:
        cur_p = 0
    else:
        cur_p += 1
    h, c = update_grid()
    trocks += 1

print(c - h)








            









