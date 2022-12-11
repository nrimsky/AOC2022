def ans(inp):
    all_calories = [0]
    for line in inp.split("\n"):
        if line.strip() == "":
            all_calories.append(0)
        else:
            all_calories[-1] += int(line.strip())
    return max(all_calories)


if __name__ == '__main__':
    test_inp = """1000
    2000
    3000
    
    4000
    
    5000
    6000
    
    7000
    8000
    9000
    
    10000"""
    assert ans(test_inp) == 24000

    with open("inputs/inp1.txt") as f:
        actual_inp = f.read()
        print(ans(actual_inp))
