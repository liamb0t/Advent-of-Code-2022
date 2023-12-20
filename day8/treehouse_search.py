f = open('adventofcode/day8/data.txt', 'r')
data = f.read().splitlines()
trees = [[int(data[row][col]) for col in range(0, len(data))] for row in range(0, len(data))]
scores = {}

def is_visible_right(x, y):
    visible_trees = 0
    tree_height = trees[x][y]
    for i in range(y + 1, len(trees)):
        if trees[x][i] >= tree_height:
            visible_trees += 1
            return visible_trees
        else:
            visible_trees += 1
    return visible_trees
   
def is_visible_left(x, y):
    visible_trees = 0
    tree_height = trees[x][y]
    for i in range(y - 1, -1, -1):
        if trees[x][i] >= tree_height:
            visible_trees += 1
            return visible_trees
        else:
            visible_trees += 1
    return visible_trees
   
def is_visible_top(x, y):
    visible_trees = 0
    tree_height = trees[x][y]
    for i in range(x - 1, -1, -1):
        if trees[i][y] >= tree_height:
            visible_trees += 1
            return visible_trees
        else:
            visible_trees += 1
    return visible_trees
   
def is_visible_below(x, y):
    visible_trees = 0
    tree_height = trees[x][y]
    for i in range(x + 1, len(trees)):
        if trees[i][y] >= tree_height:
            visible_trees += 1
            return visible_trees
        else:
            visible_trees += 1
    return visible_trees
    
def get_scenic_score(x, y):
    a, b, c, d = is_visible_below(x, y), is_visible_left(x, y), is_visible_right(x, y), is_visible_top(x, y)
    score = a * b * c * d
    #print(f'x: {x}, y:{y}, visible_below: {a}, vis_left: {b}, vis_right: {c}, vis_top: {d}, score: {score}')
    return score

for row in range(0, len(trees)):
    for col in range(0, len(trees)):
        scores[row, col] = get_scenic_score(row, col)

print(max(scores.values()))
           


            
