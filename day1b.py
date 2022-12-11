def ans(inp):
    top_calories = [0, 0, 0]
    latest = 0
    for line in inp.split("\n")+[""]:
        if line.strip() == "":
            if latest > top_calories[0]:
                top_calories = [latest, top_calories[0], top_calories[1]]
            elif latest > top_calories[1]:
                top_calories = [top_calories[0], latest, top_calories[1]]
            elif latest > top_calories[2]:
                top_calories = [top_calories[0], top_calories[1], latest]
            latest = 0
        else:
            latest += int(line.strip())
    return sum(top_calories)


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
    assert ans(test_inp) == 45000

    with open("inputs/inp1.txt") as f:
        actual_inp = f.read()
        print(ans(actual_inp))