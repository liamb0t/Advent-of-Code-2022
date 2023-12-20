### A = rock, B = paper, C = scissors
### X = lose, Y = draw, Z = win
f = open('adventofcode/day2/data.txt', 'r')
data = f.read()
games = data.replace('A', 'R').replace('B', 'P').replace('C', 'S').splitlines()
total = 0

payoffs_shapes = {
    'R': 1,
    'P': 2,
    'S': 3,
}

payoffs_game = {
    'X': 0,
    'Y': 3,
    'Z': 6,
}

scenarios = {
    'R': {
        'X': 'S',
        'Y': 'R',
        'Z': 'P',
    },
    'P': {
        'X': 'R',
        'Y': 'P',
        'Z': 'S',
    },
    'S': {
        'X': 'P',
        'Y': 'S',
        'Z': 'R',
    },
}

def get_response(move, result):
    return scenarios[move][result]

for game in games:
    opponent_move = game[0]
    game_result = game[2]
    shape = get_response(opponent_move, game_result)
    total += payoffs_game[game_result]
    total += payoffs_shapes[shape]

print(total)
    





