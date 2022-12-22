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

def get_max_pressure(start, graph, flow_rates, best_init=0):
    max_rate = sum([r for r in flow_rates.values()])
    best = best_init
    best_node = None
    to_visit=deque([(start, start, 0, 0, 0, set())]) # valve_human, valve_elephant, time, rate, released pressure, opened valves
    k = 0
    max_open = len([n for n in flow_rates.keys() if flow_rates[n] > 0])

    while len(to_visit) > 0:
        k += 1
        if k % 1000000 == 0:
            print(best, best_node)
        valve_human, valve_elephant, time, rate, released, opened = to_visit.pop()
        if released > best:
            best = released
            best_node = (valve_human, valve_elephant, time, rate, released, opened)
        if time >= 26:
            continue
        if len(opened) == max_open:
            t = released + (26 - time) * rate 
            if t > best:
                best = t
                best_node = (valve_human, valve_elephant, 26, rate, t, opened)
            continue


        # Pruning
        if released + (26 - time - 1) * max_rate + rate <= best:
            continue

        # MOAR Pruning
        # Calculate best case max pressure released for this branch
        _re = released 
        _ra = rate
        _t = time 
        _to_open = sorted([flow_rates[o] for o in flow_rates.keys() if o not in opened and flow_rates[o] > 0])[::-1]
        for i in range(0, len(_to_open), 2):
            if _t >= 26:
                break 
            _re += 2 * _ra
            _ra += _to_open[i]
            if i + 1 < len(_to_open):
                _ra += _to_open[i + 1]
            _t += 2
        _re += max([26 - _t, 0]) * _ra
            
        if _re < best:
            continue

        fl_human = flow_rates[valve_human]
        fl_elephant = flow_rates[valve_elephant]
        open_human = (valve_human not in opened) and (fl_human > 0)
        open_elephant = (valve_elephant not in opened) and (fl_elephant > 0)
        done = set()
        # human open, elephant open
        if open_human and open_elephant and (valve_human != valve_elephant):
            done.add((valve_human, valve_elephant))
            done.add((valve_elephant, valve_human))
            to_visit.append((valve_human, valve_elephant, time+1, rate+fl_elephant+fl_human, released+rate, opened.union(set([valve_human, valve_elephant]))))
        if open_elephant:
            for nxt_human in graph[valve_human]:
                # human go to next, elephant open
                if ((nxt_human, valve_elephant) not in done) and ((valve_elephant, nxt_human) not in done):
                    done.add((nxt_human, valve_elephant))
                    done.add((valve_elephant, nxt_human))
                    to_visit.append((nxt_human, valve_elephant, time+1, rate+fl_elephant, released+rate, opened.union(set([valve_elephant]))))
        if open_human:
            for nxt_elephant in graph[valve_elephant]:
                # human open, elephant go to next
                if ((valve_human, nxt_elephant) not in done) and ((nxt_elephant, valve_human) not in done):
                    done.add((valve_human, nxt_elephant))
                    done.add((nxt_elephant, valve_human))
                    to_visit.append((valve_human, nxt_elephant, time+1, rate+fl_human, released+rate, opened.union(set([valve_human]))))
        for nxt_human in graph[valve_human]:
            for nxt_elephant in graph[valve_elephant]:
                # human go to next, elephant go to next
                if ((nxt_human, nxt_elephant) not in done) and ((nxt_elephant, nxt_human) not in done):
                    done.add((nxt_human, nxt_elephant))
                    done.add((nxt_elephant, nxt_human))
                    to_visit.append((nxt_human, nxt_elephant, time+1, rate, released+rate, opened))
    return best, best_node

def ans(inp, best_init=0):
    graph, flow_rates = parse_inp(inp)
    print(get_max_pressure('AA', graph, flow_rates, best_init=best_init))

if __name__ == "__main__":
    # with open("inputs/testinp16.txt") as txtfile:
    #     ans(txtfile.read()) 
    with open("inputs/inp16.txt") as txtfile:
        ans(txtfile.read())