f = open('adventofcode/day21/data.txt', 'r')
data = f.read().splitlines()
monkeys = {}
queue = []

for line in data:
    name = line.split(': ')[0]
    if line.split(': ')[1].isdigit():
        monkeys[name] = int(line.split(': ')[1])
    else:
        queue.append(line)

while queue:
    line = queue.pop(0)
    name = line.split(': ')[0]
    left, op, right = line.split(': ')[1].split()[0], line.split(': ')[1].split()[1], line.split(': ')[1].split()[2]
    if left in monkeys and right in monkeys:
        monkeys[name] = eval(f'{monkeys[left]} {op} {monkeys[right]}')
    else:
        queue.append(line)

print(monkeys['root'])