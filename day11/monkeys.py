f = open('adventofcode/day11/data.txt', 'r')
data = f.read().splitlines()
monkeys = {}
w = 0

balh = []
arr = []
for line in data:
    if line != '':
        arr.append(line.split(' '))
    else:
        balh.append(arr)
        arr = []
        
for i in range(8):
    s = ''
    if balh[i][2][-1] == 'old':
        s = ''
    else:
        s = int(balh[i][2][-1])
    monkeys[i] = {
        'items': [int(item.replace(',', '')) for item in balh[i][1][2:]],
        'operations': [balh[i][2][-2], s,],
        'test': int(balh[i][3][-1]),
        True: int(balh[i][4][-1]),
        False: int(balh[i][5][-1]),
        'inspected_items': 0
    }

p = 3 * 17 * 2 * 19 * 11 * 5 * 13 * 7
print(p)

for i in range(10000):
    for monkey in monkeys:
        if monkeys[monkey]['items']:
            for item in monkeys[monkey]['items']:
                monkeys[monkey]['inspected_items'] += 1
                if monkeys[monkey]['operations'][0] == '*' and monkeys[monkey]['operations'][1] != '':
                    w = item * monkeys[monkey]['operations'][1]
                if monkeys[monkey]['operations'][0] == '+' and monkeys[monkey]['operations'][1] != '':
                    w = item + monkeys[monkey]['operations'][1]
                if monkeys[monkey]['operations'][1] == '':
                    w = item * item
                w = int(w % p)
                if w % monkeys[monkey]['test'] == 0:
                    monkey_to_receive = monkeys[monkey][True]
                else:
                    monkey_to_receive = monkeys[monkey][False]
                monkeys[monkey_to_receive]['items'].append(w)
            monkeys[monkey]['items'] = []
                
for monkey in monkeys:
    print(monkey, monkeys[monkey]) 

print(120005 * 125972)


