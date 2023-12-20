f = open('adventofcode/day3/data.txt', 'r')
data = f.read().splitlines()
total = 0
lower_priority = {chr(i+96): i for i in range(1,27)}
upper_priority = {chr(i+64-26): i for i in range(27,53)}

def get_compartments(rucksack):
    length = int(len(rucksack)/2)
    return rucksack[:length], rucksack[length:] 

for rucksack in data:
    first_compartment, second_compartment = get_compartments(rucksack)
    for item in first_compartment:
        if item in second_compartment:
            if item.isupper():
                total += upper_priority[item]
                break
            else:
                total += lower_priority[item]
                break

print(total)