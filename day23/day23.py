from copy import deepcopy
f = open('adventofcode/2022/day23/test.txt', 'r').read().splitlines()
data = [[s for s in row] for row in f]
# x is rows y is cols
T = 4
rows = len(data)
cols = len(data[0])
grid = {(x, y): (True, -1, -1) if data[x][y] == '#' else (False, -1, -1) for x in range(rows) for y in range(cols)}
grid_update = deepcopy(grid)
props = []
dirs = [

    [(-1, 0), (-1, 1), (-1, -1)],
    [(1, 0), (1, 1), (1, -1)],
    [(0, -1), (1, -1), (-1, -1)],
    [(0, 1), (-1, 1), (1, 1)]
]

def get_neighbours(x, y, dirs):
    neighbours = []
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        if (nx >= 0 and ny >= 0 and nx < rows and ny < cols):
            neighbours.append((nx, ny))
    return neighbours

moore_dirs = list(set([dir for pole in dirs for dir in pole]))

def next_pos(x, y):
    key, empty = 0, True 
    for dir in dirs:
        for nx, ny in get_neighbours(x, y, dir):
            if grid[(nx, ny)][0] == True:
                empty = False
        if empty == True:
            dx, dy = dirs[key][0]
            nx, ny = ex + dx, ey + dy
            if (nx >= 0 and ny >= 0 and nx < rows and ny < cols):
                return (nx, ny)
        else:
            key += 1
            empty = True
    return False

for t in range(T):
    grid = deepcopy(grid_update)
    props = []
    for ex, ey in grid:
        if grid[(ex, ey)][0] == True:
            empty = True
            for nx, ny in get_neighbours(ex, ey, moore_dirs):
                if grid[(nx, ny)][0] == True:
                    empty = False
            if empty == False:
                prop = next_pos(ex, ey)
                if prop:
                    props.append(prop)
                    nx, ny = prop
                    grid_state = grid[(ex, ey)][0]
                    grid[(ex, ey)] = (grid_state, nx, ny)
    
    for ex, ey in grid:
        isElf, px, py = grid[(ex, ey)]
        if px != -1 and py != -1:
            if props.count((px, py)) == 1:
                print(ex, ey, px, py)
                grid_update[(px, py)] = (True, -1, -1)
                grid_update[(ex, ey)] = (False, -1, -1)
        else:
            if grid[(ex, ey)][0] == False:
                grid_update[(ex, ey)] = (False, -1, -1)
            else:
                grid_update[(ex, ey)] = (True, -1, -1)
                          
    dirs = dirs[1:] + [dirs[0]]

arr = [[0 for j in range(cols)] for i in range(rows)]
for x, y in grid:
    if grid[(x, y)][0] == True:
        arr[x][y] = '#'
    else:
        arr[x][y] = '.'


for r in arr:
    print(r)