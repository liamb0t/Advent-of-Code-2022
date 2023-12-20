f = open('adventofcode/day10/data.txt', 'r')
data = f.read().splitlines()
X = 1
cycle = 1
instruction = {'noop': 1, 'addx': 2}
dict = {i : X for i in range(0, len(data))}
sprite = [0, 1, 2]
crt = []

#part1
for line in data:
    if line[0:4] == 'addx':
        for i in range(instruction[line[0:4]]):
            if i > 0:
                X += int(line.replace('addx', ''))
            cycle += 1
            dict[cycle] = X
    if line[0:4] == 'noop':
        cycle += 1
        dict[cycle] = X

#part2
for i in range(6):
    row = []
    for j in range(1, 41):
        cycle = j + (40 * i)
        sprite[0], sprite[1], sprite[2] = dict[cycle] - 1, dict[cycle], dict[cycle] + 1
        position = j - 1
        if position in sprite:
            row.append('#')
        else:
            row.append('.')
    crt.append(row)
        
for row in crt:
    print(row)