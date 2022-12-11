def get_item_score(item):
    score_lower = ord(item) - 96
    if score_lower > 0:
        return score_lower
    else:
        return score_lower + 58


def ans(inp):
    tot = 0
    sacks = inp.split("\n")
    for sack in sacks:
        mid = int(len(sack) / 2)
        comp_1_contents = set([i for i in sack[:mid]])
        for i in sack[mid:]:
            if i in comp_1_contents:
                tot += get_item_score(i)
                break
    return tot


def ans2(inp):
    tot = 0
    sacks = inp.split("\n")
    for i in range(0, len(sacks), 3):
        s1, s2, s3 = sacks[i:i + 3]
        int_1 = set([s for s in s1]).intersection(set([s for s in s2]))
        for s in s3:
            if s in int_1:
                tot += get_item_score(s)
                break
    return tot


if __name__ == '__main__':
    assert ans("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg"
               "\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw") == 157

    with open("inputs/inp3.txt") as inp3:
        print(ans(inp3.read()))

    assert ans2("vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg"
                "\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw") == 70

    with open("inputs/inp3.txt") as inp3:
        print(ans2(inp3.read()))
