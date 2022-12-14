import re
from math import floor
from collections import deque

def ans(inp, n_rounds):
    parsed = [[x.strip() for x in l.split("\n") if len(x.strip()) > 0] for l in re.split('Monkey .*:\n', inp)]
    parsed = [l for l in parsed if len(l) > 0]
    n_inspections = [0 for _ in range(len(parsed))]
    for x in parsed:
        x[0] = deque([int(y) for y in x[0].replace("Starting items: ", "").split(",")])  # Worry levels of starting items
        x[1] = x[1].replace("Operation: new = ", "")  # Operation
        x[2] = int(x[2].replace("Test: divisible by ", ""))  # Divisibility test
        x[3] = int(x[3].split(" ")[-1])  # Monkey to throw to if true
        x[4] = int(x[4].split(" ")[-1])  # Monkey to throw to if false
    
    for round in range(n_rounds):
        for monkey in range(len(parsed)):
            _, op, test, if_true, if_false = parsed[monkey]
            while len(parsed[monkey][0]) > 0:
                n_inspections[monkey] += 1
                item = parsed[monkey][0].popleft()
                new_val = eval(op.replace("old", str(item)))
                new_val = floor(new_val / 3)
                if new_val % test == 0:
                    parsed[if_true][0].append(new_val)
                else:
                    parsed[if_false][0].append(new_val)
                
    n_inspections = sorted(n_inspections)
    return n_inspections[-1] * n_inspections[-2]

def ans2(inp, n_rounds):
    parsed = [[x.strip() for x in l.split("\n") if len(x.strip()) > 0] for l in re.split('Monkey .*:\n', inp)]
    parsed = [l for l in parsed if len(l) > 0]
    n_inspections = [0 for _ in range(len(parsed))]
    for x in parsed:
        x[0] = [int(y) for y in x[0].replace("Starting items: ", "").split(",")]  # Worry levels of starting items
        x[1] = x[1].replace("Operation: new = ", "")  # Operation
        x[2] = int(x[2].replace("Test: divisible by ", ""))  # Divisibility test
        x[3] = int(x[3].split(" ")[-1])  # Monkey to throw to if true
        x[4] = int(x[4].split(" ")[-1])  # Monkey to throw to if false
    
    tests = [x[2] for x in parsed]
    for m in parsed:
        m[0] = deque([[_m%t for t in tests] for _m in m[0]])


    for round in range(n_rounds):
        for monkey in range(len(parsed)):
            _, op, test, if_true, if_false = parsed[monkey]
            while len(parsed[monkey][0]) > 0:
                n_inspections[monkey] += 1
                item = parsed[monkey][0].popleft()
                new_val = [eval(op.replace("old", str(i))) for i in item]
                new_val = [new_val[i] % t for i, t in enumerate(tests)]
                if new_val[monkey] == 0:
                    parsed[if_true][0].append(new_val)
                else:
                    parsed[if_false][0].append(new_val)
                
    n_inspections = sorted(n_inspections)
    return n_inspections[-1] * n_inspections[-2]

if __name__ == "__main__":
    with open("inputs/testinp11.txt") as tstinp:
        print(ans(tstinp.read(), 20))
    with open("inputs/inp11.txt") as txtfile:
        print(ans(txtfile.read(), 20))
    with open("inputs/testinp11.txt") as tstinp:
        print(ans2(tstinp.read(), 10000))
    with open("inputs/inp11.txt") as txtfile:
        print(ans2(txtfile.read(), 10000))