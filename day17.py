ROCKS = [[[0, 0, 1, 1, 1, 1, 0]], [[0, 0, 0, 1, 0, 0, 0],
                                   [0, 0, 1, 1, 1, 0, 0],
                                   [0, 0, 0, 1, 0, 0, 0]], [[0, 0, 0, 0, 1, 0, 0],
                                                            [0, 0, 0, 0, 1, 0, 0],
                                                            [0, 0, 1, 1, 1, 0, 0]], [[0, 0, 1, 0, 0, 0, 0],
                                                                                     [0, 0, 1, 0, 0, 0, 0],
                                                                                     [0, 0, 1, 0, 0, 0, 0],
                                                                                     [0, 0, 1, 0, 0, 0, 0]], [[0, 0, 1, 1, 0, 0, 0,],
                                                                                                              [0, 0, 1, 1, 0, 0, 0,]]]


def rock_fall(structure, rock_bottom_idx, offset):
    new_structure = [[s for s in r] for r in structure]
    for i in reversed(list(range(offset, rock_bottom_idx+1+offset))):
        for j in range(len(new_structure[0])):
            if new_structure[i][j] == 1:
                if new_structure[i + 1][j] == 0:
                    new_structure[i + 1][j] = 1
                    new_structure[i][j] = 0
                else:
                    return None 
    if 2 not in new_structure[0]:
        return new_structure[1:], offset
    return new_structure, offset + 1


def rock_left(structure, rock_bottom_idx, offset):
    new_structure = [[s for s in r] for r in structure]
    for i in range(offset, rock_bottom_idx + 1 + offset):
        for j in range(len(new_structure[0])):
            if new_structure[i][j] == 1:
                if j == 0:
                    return None 
                if new_structure[i][j-1] != 0:
                    return None 
                new_structure[i][j-1] = 1
                new_structure[i][j] = 0
    return new_structure        

def rock_right(structure, rock_bottom_idx, width, offset):
    new_structure = [[s for s in r] for r in structure]
    for i in range(offset, offset + rock_bottom_idx + 1):
        for j in reversed(list(range(len(new_structure[0])))):
            if new_structure[i][j] == 1:
                if j == width - 1:
                    return None 
                if new_structure[i][j+1] != 0:
                    return None 
                new_structure[i][j+1] = 1
                new_structure[i][j] = 0
    return new_structure     

def get_new_floor(old_structure, rock, step, directions, width):
    """
    Each rock appears so that its left edge is two units away from the left wall 
    and its bottom edge is three units above the highest rock in the room 
    (or the floor, if there isn't one).
    """
    offset = 0
    structure = rock + [[0 for _ in range(width)] for _ in range(3)] + old_structure
    rock_bottom_idx = len(rock) - 1
    instruction_idx = step
    n_directions = len(directions)
    while True:
        # try to shift rock
        shift_dir = directions[instruction_idx % n_directions]
        if shift_dir == '>':
            res = rock_right(structure, rock_bottom_idx, width, offset)
            if res:
                structure = res  
                # print("RIGHT")
                # vis(structure)             
        elif shift_dir == '<':
            res = rock_left(structure, rock_bottom_idx, offset)
            if res:
                structure = res
                # print("LEFT")
                # vis(structure)      
        instruction_idx += 1
        # check if rock can fall one unit down
        res = rock_fall(structure, rock_bottom_idx, offset)
        if not res:
            break 
        else:
            structure, offset = res
            # print("FALL")
            # vis(structure)
    return structure, instruction_idx

def vis(structure):
    m = {1: '@', 2: '#', 0: '.'}
    for f in structure[:-1]:
        print("".join([m[x] for x in f]))
    print("___________")

def ans(inp, width=7, n_rocks=2022):
    structure = [[2 for _ in range(width)]]
    n_rock_types = len(ROCKS)
    instruction_idx = 0
    for falling_rock_idx in range(n_rocks):
        rock_list_idx = falling_rock_idx % n_rock_types
        curr_rock = [[k for k in r] for r in ROCKS[rock_list_idx]]
        structure, instruction_idx = get_new_floor(structure, curr_rock, instruction_idx, inp, width)
        # "Solidify" floor by changing 1s to 2s
        for r in range(len(structure)):
            for c in range(len(structure[0])):
                if structure[r][c] == 1:
                    structure[r][c] = 2
    # print("DONE")
    # vis(structure)
    return len(structure) - 1


if __name__ == "__main__":
    with open('inputs/testinp17.txt') as tstfile:
        print(ans(tstfile.read().strip(), 7, 2022))
    with open('inputs/inp17.txt') as tstfile:
        print(ans(tstfile.read().strip(), 7, 2022))