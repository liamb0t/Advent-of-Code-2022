from itertools import permutations
f = open('adventofcode/day16/data.txt', 'r')
data = f.read().splitlines()
t = 30
pressure = 0
total_moves = 0
tunnels = {}
flow_rates = {}
T = 30
distances = {}

def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    visited = set()
    # push the first path into the queue
    queue.append([start])
    
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a 
        # new path and push it into the queue
        elif node not in visited:
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
        visited.add(node)

def calc_expected_payoff(t, moves_to_valve, f_rate):
    return (f_rate * (T - t - moves_to_valve - 1))

for line in data:
    v = line.split(';')[0].split()[1]
    f = int(line.split(';')[0].split('=')[-1])
    n = [n.strip() for n in line.split(';')[1].split('s ')[-1].split(',')]
    tunnels[v] = n
    flow_rates[v] = f

for tunnel in tunnels:
    distances[tunnel] = {n: bfs(tunnels, tunnel, n) for n in tunnels if n != tunnel}

valves = [valve for valve in tunnels if flow_rates[valve] != 0]
payoffs = {valve: [i * flow_rates[valve] for i in range(T)] for valve in valves}
valves.insert(0, 'AA')

paths = []
for i in range(len(valves)):
    for j in range(len(valves) - 1):
        x = bfs(tunnels, valves[i], valves[j + 1])
        if len(x) > 1:
            paths.append(x)

sgraph = {valve: [] for valve in valves}

for item in paths:
    sgraph[item[0]].append(item[1:])

def get_state(t, valves_on, score, curr):
    curr_loc = curr
    if len(sgraph[curr_loc]) == 0:
        return score, valves_on
    valve_to_turn = sgraph[curr_loc].pop(0)[-1]
    if valve_to_turn in valves_on:
        return get_state(t, valves_on, score, curr)
    d = len(distances[curr_loc][valve_to_turn]) - 1
    t = t - d - 1
    pressure = score + payoffs[valve_to_turn][t]
    if t <= 0:
        return pressure, valves_on
    valves_on.append(valve_to_turn)
    return get_state(t, valves_on, pressure, valve_to_turn)

print(get_state(30, [], 0, 'AA'))

