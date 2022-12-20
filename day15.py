import re
from shapely import MultiPolygon, Polygon

def ans(inp, target_row):
    blocked_idx = set()
    beacons_already_in_row = set()
    for line in inp.split("\n"):
        parts = re.split(r'Sensor at x=|, y=|: closest beacon is at x=', line)
        s_x, s_y, b_x, b_y = [int(p) for p in parts[1:]]
        if b_y == target_row:
            beacons_already_in_row.add(b_x)
        dist = abs(s_x - b_x) + abs(s_y - b_y)
        dist_to_taget_row = abs(s_y - target_row)
        if dist_to_taget_row > dist:
            continue 
        radius = dist - dist_to_taget_row
        for i in range(s_x - radius, s_x + radius + 1):
            blocked_idx.add(i)
    print(len(blocked_idx - beacons_already_in_row))

def ans2(inp, m):
    admissible_area = Polygon([(0, m), (m, 0), (m, m)])
    not_allowed = None
    for line in inp.split("\n"):
        parts = re.split(r'Sensor at x=|, y=|: closest beacon is at x=', line)
        s_x, s_y, b_x, b_y = [int(p) for p in parts[1:]]
        d = abs(s_x - b_x) + abs(s_y - b_y)
        top = (s_x, s_y + d)
        right = (s_x + d, s_y)
        bottom = (s_x, s_y - d)
        left = (s_x - d, s_y)
        shape = Polygon([top, right, bottom, left])
        if not_allowed:
            not_allowed = not_allowed.union(shape)
        else:
            not_allowed = shape
    admissible_area = admissible_area.difference(not_allowed)
    print(admissible_area)

def calc_ans(x, y):
    return x * 4000000 + y 


if __name__ == "__main__":
    with open("inputs/testinp15.txt") as txtfile:
        ans(txtfile.read(), 10)
    with open("inputs/inp15.txt") as txtfile:
        ans(txtfile.read(), 2000000)
    with open("inputs/testinp15.txt") as txtfile:
        ans2(txtfile.read(), 20)  # Centers around 14, 11
    print(calc_ans(14, 11))
    with open("inputs/inp15.txt") as txtfile:
        ans2(txtfile.read(), 4000000)  # Centers around 3299359, 3355220
    print(calc_ans(3299359, 3355220))







