def ans(inp):
    tot = 0
    for line in inp.split("\n"):
        p1, p2 = line.split(",")
        s1, e1 = p1.split("-")
        s2, e2 = p2.split("-")
        s1, e1 = int(s1), int(e1)
        s2, e2 = int(s2), int(e2)
        if s2 >= s1 and e2 <= e1:
            tot += 1
        elif s1 >= s2 and e1 <= e2:
            tot += 1
    return tot


def ans2(inp):
    tot = 0
    for line in inp.split("\n"):
        p1, p2 = line.split(",")
        s1, e1 = p1.split("-")
        s2, e2 = p2.split("-")
        s1, e1 = int(s1), int(e1)
        s2, e2 = int(s2), int(e2)
        if s2 > e1:
            continue
        if s1 > e2:
            continue
        tot += 1
    return tot


if __name__ == '__main__':
    assert ans("2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8") == 2
    with open("inputs/inp4.txt") as inp4:
        print(ans(inp4.read()))

    assert ans2("2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8") == 4
    with open("inputs/inp4.txt") as inp4:
        print(ans2(inp4.read()))
