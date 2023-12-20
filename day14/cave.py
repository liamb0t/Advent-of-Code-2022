f = open('adventofcode/day14/data.txt', 'r')
data = f.read().split('\n')
paths = []
S = (500,0)
rows = 1000
cols = 1000
cave = [[False for col in range(2000)] for row in range(2000)]
#part2
for i in range(1000):
    cave[162+2][i] = True

for line in data:
    arr = []
    for item in line.split('->'):
        x, y = int(item.strip().split(',')[0]), int(item.strip().split(',')[1])
        arr.append((x, y))
    paths.append(arr)

def draw_line(coord1, coord2):
    x1, x2 = min(coord1[0], coord2[0]), max(coord1[0], coord2[0])
    y1, y2 = min(coord1[1], coord2[1]), max(coord1[1], coord2[1])
    for i in range(y1, y2 + 1):
        for j in range(x1, x2 + 1):
           cave[i][j] = True
           
def sandfall(s):
    sx, sy = s[0], s[1]
    is_rock = False
    while is_rock is False:
        if sy + 1 >= rows or sx - 1 < 0 or sx + 1 > cols:
            return None
        else:
            if cave[sy + 1][sx] is False:
                sy += 1
            elif cave[sy + 1][sx] is True and cave[sy + 1][sx - 1] is False:
                sx, sy = sx -1, sy + 1
            elif cave[sy + 1][sx] is True and cave[sy + 1][sx + 1] is False:
                sx, sy = sx + 1, sy + 1
            else:
                is_rock = True
    return (sx, sy)

for path in paths:
    for i in range(len(path) - 1):
        draw_line(path[i], path[i + 1])

sand_paths = []
abyss = False
while not abyss:
    s = sandfall(S)
    if s:
        if s == S:
            abyss = True
        x, y = s[0], s[1]
        cave[y][x] = True
        sand_paths.append(s)
    else:
        abyss = True

print(len(sand_paths))










