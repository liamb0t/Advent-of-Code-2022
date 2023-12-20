 
for perm in permutations(valves, r):
    #print("Processing file {} ({}%)".format(j, 100*j//n))
    for valve in perm:
        next_loc = valve
        if current_loc != next_loc:
            m = distances[current_loc][next_loc]
        if m > T - t:
            break
        x = calc_expected_payoff(t, m, flow_rates[next_loc])
        if x > 0:
            pressure += x
        current_loc = next_loc
        if current_loc in valves:
            valves.remove(current_loc)
        t += m + 1
    if pressure > best_score:
        best_score = pressure
        path = perm
    t = 0
    pressure = 0