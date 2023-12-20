f = open('adventofcode/day19/test_data.txt', 'r')
data = f.read().splitlines()
blueprints = {}
t = 24
ore = 0
obs = 0
clay = 0
ore_bots = 1
clay_bot = 0
obs_bot = 0
geode_bot = 0

for line in data:
    i = int(line.split()[1].split(':')[0])
    ore_ore = int(line.split()[6])
    clay_ore = int(line.split()[12])
    obsidian_ore = int(line.split()[18])
    obsidian_clay = int(line.split()[21])
    geode_ore = int(line.split()[27])
    geode_obsidian = int(line.split()[30])
    blueprints[i] = {'ore_bot': 
                        {'ore': ore_ore},
                    'clay_bot': 
                        {'ore': clay_ore},
                    'obsidian_bot': 
                        {'ore': obsidian_ore, 
                        'obsidian_clay': obsidian_clay},
                    'geode_bot': {
                        'ore': geode_ore,
                        'obdidian': geode_obsidian
                    }}

for b in blueprints.values():
    print(b)


def produce(t, obs, clay, ore, i):
    ore += 1
    if ore >= blueprints[i]['clay_bot']['ore']:
        clay_bot += 1
        ore -= blueprints[i]['clay_bot']['ore']
    return 