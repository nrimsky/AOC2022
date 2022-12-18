"""
The sand is pouring into the cave from point 500,0.
At some point no more sand can come to rest -> how much sand produced by this point
"""

def crosses_horizontal_boundary(x, y, horizontal_boundaries):
    for _range, _y in horizontal_boundaries:
        if (y == _y) and (x in _range):
            return True 
    return False


def crosses_vertical_boundary(x, y, vertical_boundaries):
    for _x, _range in vertical_boundaries:
        if x == _x and y in _range:
            return True 
    return False


def is_valid_step(x, y, horizontal_boundaries, vertical_boundaries, settled_sand_coords, max_x, min_x):
    if (x, y) in settled_sand_coords:
        return False
    if x < min_x:
        return True 
    if x > max_x:
        return True
    if crosses_horizontal_boundary(x, y, horizontal_boundaries):
        return False
    if crosses_vertical_boundary(x, y, vertical_boundaries):
        return False
    return True

def get_next_step(x, y, horizontal_boundaries, vertical_boundaries, settled_sand_coords, max_y, max_x, min_x, has_floor):
    """
    A unit of sand always falls down one step if possible. 
    If the tile immediately below is blocked (by rock or sand), 
    the unit of sand attempts to instead move diagonally one step down and to the left. 
    If that tile is blocked, 
    the unit of sand attempts to instead move diagonally one step down and to the right.
    """
    if has_floor:
        if y + 1 >= max_y + 2:
            return None
    if is_valid_step(x, y+1, horizontal_boundaries, vertical_boundaries, settled_sand_coords, max_x, min_x):
        return x, y+1
    if is_valid_step(x-1, y+1, horizontal_boundaries, vertical_boundaries, settled_sand_coords, max_x, min_x):
        return x-1, y+1
    if is_valid_step(x+1, y+1, horizontal_boundaries, vertical_boundaries, settled_sand_coords, max_x, min_x):
        return x+1, y+1
    return None



def parse_solid_rock_structure(inp):
    lines = [l.split(" -> ") for l in inp.split("\n")]
    lines = [[tuple([int(x) for x in p.split(",")]) for p in l] for l in lines]
    vertical_boundaries = []
    horizontal_boundaries = []
    max_y = -1
    max_x = -1 
    min_x = 100000
    
    for l in lines:
        x, y = l[0]
        if y > max_y:
            max_y = y
        if x > max_x:
            max_x = x 
        if x < min_x:
            min_x = x
        for new_x, new_y in l[1:]:
            if new_y > max_y:
                max_y = new_y
            if new_x > max_x:
                max_x = new_x
            if new_x < min_x:
                min_x = new_x
            if new_x == x:
                if y < new_y:
                    vertical_boundaries.append([x, range(y, new_y+1)])
                else:
                    vertical_boundaries.append([x, range(new_y, y+1)])
            elif new_y == y:
                if x < new_x:
                    horizontal_boundaries.append([range(x, new_x+1), y])
                else:
                    horizontal_boundaries.append([range(new_x, x+1), y])
            x, y = new_x, new_y
    
    return horizontal_boundaries, vertical_boundaries, max_y, max_x, min_x

def print_structure(horizontal_boundaries, vertical_boundaries,  max_y, max_x, min_x, filled):
    for row in range(0, max_y + 3):
        r = []
        for col in range(min([min_x, 500-max_y-1]), max([max_x + 1,  500+max_y+2])):
            if crosses_horizontal_boundary(col, row, horizontal_boundaries):
                r.append("#")
            elif crosses_vertical_boundary(col, row, vertical_boundaries):
                r.append("#")
            elif (col, row) in filled:
                r.append("o")
            else:
                r.append(".")
        print("".join(r))

def ans(inp, has_floor = False):
    horizontal_boundaries, vertical_boundaries,  max_y, max_x, min_x = parse_solid_rock_structure(inp)
    # print_structure(horizontal_boundaries, vertical_boundaries,  max_y, max_x, min_x, set())
    settled_sand_coords = set()
    x, y = 500, 0

    iters = 0
    while True:
        iters += 1
        if iters >= 5000000:
            print(len(settled_sand_coords))
            print_structure(horizontal_boundaries, vertical_boundaries,  max_y, max_x, min_x, settled_sand_coords)
            return
        next_step = get_next_step(x, y, horizontal_boundaries, vertical_boundaries, settled_sand_coords, max_y, max_x, min_x, has_floor)
        if next_step:
            x, y = next_step[0], next_step[1]
            if (y > max_y + 2):
                break
        else:
            settled_sand_coords.add((x, y))
            if ((x == 500) and (y == 0)):
                break                
            x, y = 500, 0
    # print_structure(horizontal_boundaries, vertical_boundaries,  max_y, max_x, min_x, settled_sand_coords)
    return len(settled_sand_coords)

if __name__ == "__main__":
    with open("inputs/testinp14.txt") as txtfile:
        print(ans(txtfile.read()))
    with open("inputs/inp14.txt") as txtfile:
        print(ans(txtfile.read()))

    with open("inputs/testinp14.txt") as txtfile:
        print(ans(txtfile.read(), has_floor=True))
    with open("inputs/inp14.txt") as txtfile:
        print(ans(txtfile.read(), has_floor=True))
