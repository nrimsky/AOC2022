def is_greatest(x, l):
    for n in l:
        if x <= n:
            return False
    return True


def view_dist(x, l):
    d = 0
    for n in l:
        d += 1
        if n >= x:
            return d
    return d


def ans(inp):
    rows = len(inp)
    cols = len(inp[0])
    tot = 2 * cols + 2 * (rows - 2)  # outer rectangle
    max_score = 0
    for i, l in enumerate(inp):
        if i == 0 or i == rows - 1:
            continue
        for j, height in enumerate(l):
            if j == 0 or j == cols - 1:
                continue
            if is_greatest(height, l[0:j]):
                tot += 1
            elif is_greatest(height, l[j + 1:]):
                tot += 1
            elif is_greatest(height, [inp[r][j] for r in range(i)]):
                tot += 1
            elif is_greatest(height, [inp[r][j] for r in range(i + 1, rows)]):
                tot += 1
            s1 = view_dist(height, l[0:j][::-1])
            s2 = view_dist(height, l[j + 1:])
            s3 = view_dist(height, [inp[r][j] for r in list(range(i))[::-1]])
            s4 = view_dist(height, [inp[r][j] for r in range(i + 1, rows)])
            score = s1 * s2 * s3 * s4
            if score > max_score:
                max_score = score

    return tot, max_score


def parse_txt(txt):
    return [[int(x) for x in l] for l in txt.split("\n")]


if __name__ == '__main__':
    with open("inputs/testinp8.txt") as tstfile:
        parsed = parse_txt(tstfile.read())
        print(ans(parsed))

    with open("inputs/inp8.txt") as txtfile:
        parsed = parse_txt(txtfile.read())
        print(ans(parsed))
