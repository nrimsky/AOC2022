ROCKS = [[(0, 2), (0, 3), (0, 4), (0, 5)],
         [(0, 3), (1, 2), (1, 3), (1, 4), (2, 3)],
         [(2, 4), (1, 4), (0, 2), (0, 3), (0, 4)],
         [(0, 2), (1, 2), (2, 2), (3, 2)],
         [(0, 2), (0, 3), (1, 2), (1, 3)]]

def print_settled(top, settled):
    for row in range(top+1, -1, -1):
        r = ""
        for col in range(7):
            if (row, col) in settled:
                r += '#'
            else:
                r += '.'
        print(r)

def shift_right(rock):
    return [(r[0], r[1] + 1) for r in rock]

def shift_left(rock):
    return [(r[0], r[1] - 1) for r in rock]

def shift_up(rock, amount):
    return [(r[0] + amount, r[1]) for r in rock]

def shift_down(rock):
    return [(r[0] - 1, r[1]) for r in rock]

def rock_valid(rock, settled):
    for point in rock:
        if point in settled:
            return False
        if point[1] < 0 or point[1] > 6:
            return False
        if point[0] < 0:
            return False
    return True

def ans(inp, n):
    instruction_idx = 0
    top = 0
    settled = set()
    for i in range(n):
        rock = ROCKS[i % len(ROCKS)]
        rock = shift_up(rock, top + 3)
        while True:
            if inp[instruction_idx % len(inp)] == '>':
                new_rock = shift_right(rock)
            else:
                new_rock = shift_left(rock)
            instruction_idx += 1
            if rock_valid(new_rock, settled):
                rock = new_rock
            new_rock = shift_down(rock)
            if rock_valid(new_rock, settled):
                rock = new_rock
            else:
                break 
        for point in rock:
            if point[0] + 1 > top:
                top = point[0] + 1
            settled.add(point)
    return top

if __name__ == "__main__":
    with open('inputs/testinp17.txt') as tstfile:
        print(ans(tstfile.read().strip(), 2022))
    with open('inputs/inp17.txt') as tstfile:
        print(ans(tstfile.read().strip(), 2022))