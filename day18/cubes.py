f = open('adventofcode/day18/test_sdata.txt', 'r')
data = [[int(line.split(',')[i]) for i in range(3)] for line in f.read().splitlines() ]

test = [[1,1,1], [2,1,1]]

hash = {tuple(cube): 0 for cube in data}


def is_nexto(c1, c2):
    x, y, z = c1[0], c1[1], c1[2]
    nx, ny, nz = c2[0], c2[1], c2[2]
    if (abs(nx-x), abs(ny-y), abs(nz-z)) in [(0, 0, 1), (1, 0, 0), (0, 1, 0)]:
        return True
    return False 

def get_sides(cubes):
    s = 0
    for i in range(len(cubes)):
        start = cubes.index(cubes[i])
        for j in range(start, len(cubes) - 1):
            cube1 = cubes[i]
            cube2 = cubes[j + 1]
            if is_nexto(cube1, cube2):
                hash[tuple(cube1)] += 1
                hash[tuple(cube2)] += 1
           

print(get_sides(data))
s = 0 
n = (len(data)) * 6
for thing in hash:
    s += hash[thing]


print(n - s)
data.sort()
print(data)
minx, maxx = 999, 0
miny, maxy = 999, 0
minz, maxz= 999, 0 
for ball in data:
    if ball[0] > maxx:
        maxx = ball[0]
    if ball[0] < minx:
        minx = ball[0]
    if ball[1] > maxy:
        maxy = ball[1]
    if ball[1] < miny:
        miny = ball[1]
    if ball[2] > maxz:
        maxz = ball[2]
    if ball[2] < minz:
        minz = ball[2]

a = 0
print(minx, maxx, miny, maxy, minz, maxz)
for x in range(minx+2, maxx):
    for y in range(miny+2, maxy):
        for z in range(minz+2, maxz):
            air = [x, y, z]
            if air not in data:
                print(air)
                a += 1


print(a)

