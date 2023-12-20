f = open('adventofcode/day8/data.txt', 'r')
data = f.read().splitlines()
trees = [[int(data[row][col]) for col in range(0, len(data))] for row in range(0, len(data))]
visible_trees = 0

def is_visible_right(x, y):
    tree_height = trees[x][y]
    for i in range(y + 1, len(trees)):
        if trees[x][i] >= tree_height:
            return False
    return True
   
def is_visible_left(x, y):
    tree_height = trees[x][y]
    for i in range(0, y):
        if trees[x][i] >= tree_height:
            return False
    return True
   
def is_visible_top(x, y):
    tree_height = trees[x][y]
    for i in range(0, x):
        if trees[i][y] >= tree_height:
            return False
    return True
   
def is_visible_below(x, y):
    tree_height = trees[x][y]
    for i in range(x + 1, len(trees)):
        if trees[i][y] >= tree_height:
            return False
    return True
   
def is_visible(x, y):
    if (is_visible_right(x, y) or is_visible_left(x, y) 
        or is_visible_top(x, y) or is_visible_below(x, y)):
        return True
    else:
        return False

for row in range(0, len(trees)):
    for col in range(0, len(trees)):
        if row == 0 or col == 0 or col == len(trees) - 1 or row == len(trees) - 1:
            visible_trees += 1
        else:
            if is_visible(row, col):
                visible_trees += 1
           
for row in trees:
    print(row)
print(visible_trees)


            
