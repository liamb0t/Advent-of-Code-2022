f = open('adventofcode/day25/data.txt', 'r')
data = f.read().splitlines()

key = {'-': -1, '=': -2}

def SNAFU(string):
    num = 0
    snaf = list(string)
    for i in range(len(snaf), 1, -1):
        if snaf[-i].isdigit():
            num += int(snaf[-i]) * 5** (i - 1)
        else:
            num += key[snaf[-i]] * 5** (i - 1)
    if snaf[-1].isdigit():
        num += 1 * int(snaf[-1])
    else:
         num += 1 * key[snaf[-1]]
    return num

total = 0

for line in data:
    total += SNAFU(line.strip())

print(total)





