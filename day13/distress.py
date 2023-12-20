import ast
from copy import deepcopy

f = open('adventofcode/day13/data.txt', 'r')
data = f.read().split('\n\n')
pairs = []
for line in data:
    a, b = map(eval, line.split('\n'))
    pairs.append([a, b])


p1 = [1,[2,[3,[4,[5,6,7]]]],8,9]
p2 = [1,[2,[3,[4,[5,6,0]]]],8,9]

def is_right_order(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 0 if a == b else (-1 if a < b else 1)
    elif isinstance(a, int):
        return is_right_order([a], b)
    elif isinstance(b, int):
        return is_right_order(a, [b])
    elif a and b:
        q = is_right_order(a[0], b[0])
        return q if q else is_right_order(a[1:], b[1:])
    return 1 if a else (-1 if b else 0)

print(is_right_order(p1, p2)) 

#answers = []
#for index, pair in enumerate(pairs):
#    packet1, packet2 = pair[0], pair[1]
#    if is_right_order(packet1, packet2):
#        answers.append(index + 1)

#print(sum(answers))

[1, 3, 4, 5, 6, 7, 8, 13, 14, 17, 19, 23, 24, 25, 26, 27, 29, 31, 33, 34, 35, 38, 39, 41, 43, 44, 45, 47, 48, 49, 50, 51, 52, 53, 55, 56, 57, 63, 64, 
65, 68, 70, 71, 72, 73, 74, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 92, 93, 95, 96, 97, 98, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 
112, 113, 114, 115, 116, 117, 118, 119, 120, 123, 124, 126, 127, 129, 131, 132, 133, 134, 136, 137, 138, 139, 141, 146, 147, 148, 149, 150]