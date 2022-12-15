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

if __name__ == "__main__":
    with open("inputs/testinp13.txt") as txtfile:
        print(ans(txtfile.read()))
    with open("inputs/inp13.txt") as txtfile:
        print(ans(txtfile.read()))