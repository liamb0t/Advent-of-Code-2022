f = open('adventofcode/day1/data.txt', 'r')
items = f.read().splitlines()
calories = []
total = 0

for item in items:
    if item == '':
        calories.append(total)
        total = 0
    else:
        total += int(item)

calories.sort(reverse=True)
print(sum(calories[0:3]))


