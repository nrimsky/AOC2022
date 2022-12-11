def ans(inp, l):
    last = [c for c in inp[0:l]]
    for i, c in enumerate(inp[l:]):
        if len(set(last)) == l:
            return i + l
        last[i % l] = c
    return len(inp)


if __name__ == '__main__':
    assert ans("bvwbjplbgvbhsrlpgdmjqwftvncz", 4) == 5
    assert ans("nppdvjthqldpwncqszvftbrmjlhg", 4) == 6
    assert ans("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 4) == 10
    assert ans("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 4) == 11
    with open("inputs/inp6.txt") as txtfile:
        assert (ans(txtfile.read(), 4)) == 1651
    with open("inputs/inp6.txt") as txtfile:
        assert (ans(txtfile.read(), 14)) == 3837
