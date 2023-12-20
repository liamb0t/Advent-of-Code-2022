from collections import deque

f = open('adventofcode/day12/data.txt', 'r')
data = f.read().strip()
grid = [list(x) for x in data.split("\n")]
rows = len(grid)
cols = len(grid[0])
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
S = None
E = None

for i in range(rows):
    for j in range(cols):
        if grid[i][j] == 'S':
            S = (i, j)
            grid[i][j] = 'a'
        if grid[i][j] == 'E':
            E = (i, j)
            grid[i][j] = 'z'

def get_neighbours(cell):
    neighbours = []
    x, y = cell[0], cell[1]
    for i in range(4):
        nx = x + dirs[i][0]
        ny = y + dirs[i][1]
        # change conditions for part 1 ------> <= 1
        if (nx >= 0 and ny >= 0 and nx < rows and ny < cols) and (ord(grid[nx][ny]) - ord(grid[x][y]) >= -1):
            neighbours.append((x + dirs[i][0], y + dirs[i][1]))
    return neighbours 

def bfs(start, end):   
    queue = deque()
    visited = set()
    queue.append([start])
    while queue:
        path = queue.popleft()
        node = path[-1]
        if grid[node[0]][node[1]] == end:
            return len(path) - 1
        if node not in visited:
            for neighbour in get_neighbours(node):
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
            visited.add(node)
    return False

#print('part1:', bfs(S, E))
print('part2:', bfs(E, 'a'))





