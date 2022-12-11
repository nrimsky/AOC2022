import re


def parse_inp(txt):
    diagram = [[]]
    instructions = []
    for line in txt.split("\n"):
        if len(line) == 0:
            continue
        if line[0] == 'm':
            s = re.split('move | from | to ', line)[1:]
            s = [int(i) for i in s]
            instructions.append(s)
        else:
            for i, item in enumerate(line[1::4]):
                if len(diagram) <= i:
                    diagram.append([])
                if item != ' ':
                    diagram[i].append(item)
    return diagram, instructions


def ans(inp):
    diagram, instructions = parse_inp(inp)
    for ins in instructions:
        move, _from, _to = ins
        from_idx = _from - 1
        to_idx = _to - 1
        diagram[to_idx] = diagram[from_idx][:move][::-1] + diagram[to_idx]
        diagram[from_idx] = diagram[from_idx][move:]
    return "".join([d[0] for d in diagram])


def ans2(inp):
    diagram, instructions = parse_inp(inp)
    for ins in instructions:
        move, _from, _to = ins
        from_idx = _from - 1
        to_idx = _to - 1
        diagram[to_idx] = diagram[from_idx][:move] + diagram[to_idx]
        diagram[from_idx] = diagram[from_idx][move:]
    return "".join([d[0] for d in diagram])


if __name__ == '__main__':
    with open("inputs/testinp5.txt") as txtfile:
        assert ans(txtfile.read()) == "CMZ"

    with open("inputs/inp5.txt") as txtfile:
        print(ans(txtfile.read()))

    with open("inputs/inp5.txt") as txtfile:
        print(ans2(txtfile.read()))
