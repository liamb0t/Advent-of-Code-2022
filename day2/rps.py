###A = rock, B = paper, C = scissors
###x = rock, Y = paper, Z = scissors
f = open('adventofcode/day2/data.txt', 'r')
data = f.read()
games = data.replace('A', 'R').replace('B', 'P').replace('C', 'S').replace('X', 'R').replace('Y', 'P').replace('Z', 'S').splitlines()
total_score = 0

payoffs = {
    'R': 1,
    'P': 2,
    'S': 3,
}

def get_score(move, response):
    score = 0
    score += payoffs[response]
    if (move == response):
        score += 3
    elif (move == 'R' and response == 'P' or move == 'P' and response == 'S' or move == 'S' and response == 'R'):
        score += 6
    return score

for game in games:
    opponent_move = game[0]
    my_move = game[2]
    total_score += get_score(opponent_move, my_move)

print(total_score)

