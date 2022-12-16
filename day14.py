"""
The sand is pouring into the cave from point 500,0.
At some point no more sand can come to rest -> how much sand produced by this point
"""

def crosses_horizontal_boundary(x, y, horizontal_boundaries):
    for _range, _y in horizontal_boundaries:
        if y == _y and x in _range:
            return True 
    return False


def crosses_vertical_boundary(x, y, vertical_boundaries):
    for _x, _range in vertical_boundaries:
        if x == _x and y in _range:
            return True 
    return False


def is_valid_step(x, y, horizontal_boundaries, vertical_boundaries, settled_sand_coords):
    if (x, y) in settled_sand_coords:
        return False
    if crosses_horizontal_boundary(x, y, horizontal_boundaries):
        return False
    if crosses_vertical_boundary(x, y, vertical_boundaries):
        return False
    return True

def get_next_step(x, y, horizontal_boundaries, vertical_boundaries, settled_sand_coords):
    """
    A unit of sand always falls down one step if possible. 
    If the tile immediately below is blocked (by rock or sand), 
    the unit of sand attempts to instead move diagonally one step down and to the left. 
    If that tile is blocked, 
    the unit of sand attempts to instead move diagonally one step down and to the right.
    """
    if is_valid_step(x, y+1, horizontal_boundaries, vertical_boundaries, settled_sand_coords):
        return x, y+1
    if is_valid_step(x-1, y+1, horizontal_boundaries, vertical_boundaries, settled_sand_coords):
        return x-1, y+1
    if is_valid_step(x+1, y+1, horizontal_boundaries, vertical_boundaries, settled_sand_coords):
        return x+1, y+1
    return None



def parse_solid_rock_structure(inp):
    lines = [l.split(" -> ") for l in inp.split("\n")]
    lines = [[tuple([int(x) for x in p.split(",")]) for p in l] for l in lines]
    vertical_boundaries = []
    horizontal_boundaries = []
    max_y = -1
    
    for l in lines:
        x, y = l[0]
        for new_x, new_y in l[1:]:
            if new_y > max_y:
                max_y = new_y
            if new_x == x:
                if y <= new_y + 1:
                    vertical_boundaries.append([x, range(y, new_y+1)])
                else:
                    vertical_boundaries.append([x, range(new_y, y+1)])
            elif new_y == y:
                if x <= new_x + 1:
                    horizontal_boundaries.append([range(x, new_x+1), y])
                else:
                    horizontal_boundaries.append([range(new_x, x+1), y])
            x, y = new_x, new_y
    
    return horizontal_boundaries, vertical_boundaries, max_y

def ans(inp):
    horizontal_boundaries, vertical_boundaries, max_y = parse_solid_rock_structure(inp)
    settled_sand_coords = set()
    settled_sand_coords_ = []
    x, y = 500, 0
    while True:
        next_step = get_next_step(x, y, horizontal_boundaries, vertical_boundaries, settled_sand_coords)
        if next_step:
            x, y = next_step[0], next_step[1]
            if (y > max_y + 1):
                break
        else:
            if ((x == 500) and (y == 0)):
                break                
            settled_sand_coords.add((x, y))
            x, y = 500, 0
    return len(settled_sand_coords)

if __name__ == "__main__":
    with open("inputs/testinp14.txt") as txtfile:
        print(ans(txtfile.read()))
    with open("inputs/inp14.txt") as txtfile:
        print(ans(txtfile.read()))  # 995 - 1 [Off by one, not sure why, subtracted one on second submission and passed...]
