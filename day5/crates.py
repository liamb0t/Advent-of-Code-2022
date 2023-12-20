f = open('adventofcode/day5/data.txt', 'r')
data = f.read().splitlines()
unwanted_chars = [char for char in 'movefromt']
answer = ''

crates = {
    1: ['F', 'T', 'C', 'L', 'R', 'P', 'G', 'Q'],
    2: ['N', 'Q', 'H', 'W', 'R', 'F', 'S', 'J'],
    3: ['F', 'B', 'H', 'W', 'P', 'M', 'Q', ],
    4: ['V', 'S', 'T', 'D', 'F'], 
    5: ['Q', 'L', 'D', 'W', 'V', 'F', 'Z'], 
    6: ['Z', 'C', 'L', 'S', ],
    7: ['Z', 'B', 'M', 'V', 'D', 'F'],
    8: ['T', 'J', 'B'],
    9: ['Q', 'N', 'B', 'G', 'L', 'S', 'P', 'H'],
}

def parse_data(line):
    a = line
    for char in unwanted_chars:
        a = a.replace(char, '')
    return a.split()

def move_crate_9000(num_of_crates, stack_from, stack_to):
    for i in range(0, int(num_of_crates)):
        crate = crates[int(stack_from)].pop()
        crates[int(stack_to)].append(crate)

def move_crate_9001(num_of_crates, stack_from, stack_to):
        crates_to_move = crates[int(stack_from)][-int(num_of_crates):]
        crates[int(stack_to)] += crates_to_move
        crates[int(stack_from)] = crates[int(stack_from)][:-int(num_of_crates)]

instructions = [parse_data(instruction) for instruction in data]

for instruction in instructions:
    move_crate_9001(instruction[0], instruction[1], instruction[2])

for stack in crates:
    answer += crates[stack][-1]

print(answer)





