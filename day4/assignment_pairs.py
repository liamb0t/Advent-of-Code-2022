import re 
f = open('adventofcode/day4/data.txt', 'r')
data = f.read().splitlines()
pairs = []
overlaps_p1 = 0
overlaps_p2 = 0

for line in data:
    x = [int(digit) for digit in re.split('-|,', line)]
    pairs.append(x)

for pair in pairs:
    print(pair)
    a, b, c, d = pair[0], pair[1], pair[2], pair[3]
    if a <= c and b >= d or a >= c and b <= d:
        overlaps_p1 += 1

print(overlaps_p1)

for pair in pairs:
    arr_1 = [i for i in range(pair[0], pair[1] + 1)]
    arr_2 = [i for i in range(pair[2], pair[3] + 1)]
    for digit in arr_1:
        if digit in arr_2:
            overlaps_p2 += 1
            break

print(overlaps_p2)