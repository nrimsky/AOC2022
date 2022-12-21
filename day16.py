import re
from collections import defaultdict, deque

def parse_inp(inp):
    graph = {}
    flow_rates = {}
    for line in inp.split("\n"):
        parts = re.split(r'Valve | has flow rate=|; tunnel[s]? lead[s]? to valve[s]? |, ', line)
        graph[parts[1]] = parts[3:]
        flow_rates[parts[1]] = int(parts[2])
    return graph, flow_rates

def get_max_pressure(start, graph, flow_rates, max_t):
    max_rate = sum([r for r in flow_rates.values()])
    best = 0
    best_path = None
    to_visit=deque([(start, 0, 0, 0, set())]) # valve, time, rate, released pressure, opened valves
    k = 0
    n = len([k for k in flow_rates.values() if k != 0])
    while len(to_visit) > 0:
        k += 1
        if k % 1000000 == 0:
            print(best)
        valve, time, rate, released, opened = to_visit.pop()
        if released > best:
            best = released
            best_path = [time, rate, released, opened]
        if time >= max_t:
            continue
        if len(opened) == n:
            t = released + (max_t - time) * rate 
            if t > best:
                best = t
                best_path = [max_t, rate, t, opened]
            continue
        
        
        unopened = sorted([k for k in flow_rates.values() if k > 0 and k not in opened])[::-1]
        max_poss_released = released
        _rate = rate 
        _t = time
        for i, u in enumerate(unopened):
            if _t < max_t:
                _t += 2
                max_poss_released += 2*_rate
                _rate += u 
            else:
                break
        max_poss_released += max([max_t - _t, 0]) * max_rate

        if max_poss_released <= best:
            continue
            
        fr = flow_rates[valve]
        # we did open the current valve
        if valve not in opened and fr != 0:
            to_visit.append((valve, time + 1, rate+fr, released+rate, opened.union(set([valve])))) 
        for nxt in graph[valve]:
            # we did not open the current valve
            to_visit.append((nxt, time + 1, rate, released+rate, opened)) 
    return best, best_path

def ans(inp, max_t=30):
    graph, flow_rates = parse_inp(inp)
    print(get_max_pressure('AA', graph, flow_rates, max_t))



if __name__ == "__main__":
    with open("inputs/testinp16.txt") as txtfile:
        ans(txtfile.read(), max_t=30)
    with open("inputs/inp16.txt") as txtfile:
        ans(txtfile.read(), max_t=30)