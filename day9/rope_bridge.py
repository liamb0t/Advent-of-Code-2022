f = open('adventofcode/day9/data.txt', 'r')
data = f.read().splitlines()
instructions = [line.split() for line in data]

def find_tail(head, tail):
    hx, hy = head[0], head[1]
    tx, ty = tail[0], tail[1]
    if abs(hx -  tx) > 1 or abs(hy -  ty) > 1:
        if hx > tx:
            tx += 1
        if hy > ty:
            ty += 1
        if hx < tx:
            tx -= 1
        if hy < ty:
            ty -= 1
        return tx, ty
    return tx, ty

def move_head(head, dir, moves):
    path = []
    dirs = {'R': 1, 'L': -1, 'U': -1, 'D': 1}
    hx, hy = head[0], head[1]
    for i in range(moves):
        if dir in ['R', 'L']:
            hy += dirs[dir]
        elif dir in ['U', 'D']:
            hx += dirs[dir]
        path.append((hx, hy))
    return path

s = (100, 100)
paths = {i: [s] for i in range(1, 10)}
h_paths = [s]

for instruction in instructions:
    dir, n = instruction[0], int(instruction[1]) 
    current_loc = h_paths[-1]
    h_paths += move_head(current_loc, dir, n)

paths = {0: h_paths}
for i in range(1, 10):
    paths[i] = [s]

for i in range(10):
    for hloc in paths[i]:
        if i + 1 < 10:
            knot = paths[i + 1][-1]
            paths[i + 1].append(find_tail(hloc, knot))

grid = [['.' for j in range(250)] for i in range(250)]
for loc in paths[9]:
    x, y = abs(loc[0]), abs(loc[1])
    grid[x][y] = '#'


for row in grid:
    print(row)

print(len(list(set(paths[9]))))