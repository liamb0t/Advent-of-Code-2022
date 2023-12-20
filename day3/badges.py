f = open('adventofcode/day3/data.txt', 'r')
data = f.read().splitlines()
total = 0
lower_priority = {chr(i+96):i for i in range(1,27)}
upper_priority = {chr(i+64-26):i for i in range(27,53)}

for i in range(0, len(data), 3):
    rucksack_1 = data[i]
    rucksack_2 = data[i + 1]
    rucksack_3 = data[i + 2]
    for item in rucksack_1:
        if item in rucksack_2 and item in rucksack_3:
            if item.isupper():
                total += upper_priority[item]
                break
            else:
                total += lower_priority[item]
                break
            
print(total)
