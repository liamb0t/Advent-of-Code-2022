f = open('adventofcode/day15/test_data.txt', 'r')
data = f.read().split('\n')
i = 0
sensor_data = []
not_bs_locs = {(i, j): False for i in range(21) for j in range(21)}

for line in data:
    arr = []
    for x in line.split('='):
        if x[0] != 'x':
            arr.append(int(x.split(',')[0]))
    sensor_data.append(arr)

def manhatten(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

for d in sensor_data:
    sx, sy, bx, by = d[0], d[1], d[2], d[3]
    man = manhatten(sx, bx, sy, by)
    for r in range(sy - man - 1, sy + man + 1):
        for c in range(sx-man - 1, sx+man+ 1):
            if manhatten(sx, c, sy, r) <= man:
                if (c, r) in not_bs_locs:
                    not_bs_locs[(c, r)] = True
                    
print(list(not_bs_locs.keys())[list(not_bs_locs.values()).index(False)])  
print(not_bs_locs)
g = [[0 for j in range(21)] for i in range(21)]
for x, y in not_bs_locs:
    if not_bs_locs[(x, y)] == True:
        g[x][y] = '#'


for row in g:
    print(row)