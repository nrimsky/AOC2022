from functools import cmp_to_key

def ordered(p1, p2):
    if type(p1) is int and type(p2) is int:
        if p1 < p2:
            return 1 
        elif p1 == p2:
            return 0 
        else:
            return -1
    if type(p1) is int:
        p1 = [p1]
    if type(p2) is int:
        p2 = [p2]
    l = min([len(p1), len(p2)])
    for i in range(l):
        res = ordered(p1[i], p2[i])
        if res != 0:
            return res 
    if len(p1) < len(p2):
        return 1 
    elif len(p1) == len(p2):
        return 0 
    else:
        return -1

def ans(inp):
    tot = 0
    pairs = inp.split("\n\n")
    pairs = [[eval(x) for x in p.split("\n")] for p in pairs]
    for i, p in enumerate(pairs):
        if ordered(p[0], p[1]) >= 0:
            tot += (i + 1)
    return tot

def ans2(inp):
    parsed = [eval(l) for l in inp.split("\n") if len(l) != 0]
    parsed += [[[2]],[[6]]]
    s = sorted(parsed, key = cmp_to_key(ordered))[::-1]
    tot = 1
    for i, p in enumerate(s):
        if p == [[2]] or p == [[6]]:
            tot *= (i + 1)
    return tot

if __name__ == "__main__":
    with open("inputs/testinp13.txt") as txtfile:
        print(ans(txtfile.read()))
    with open("inputs/inp13.txt") as txtfile:
        print(ans(txtfile.read()))
    with open("inputs/testinp13.txt") as txtfile:
        print(ans2(txtfile.read()))
    with open("inputs/inp13.txt") as txtfile:
        print(ans2(txtfile.read()))