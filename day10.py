from math import floor

checkpoints = [20, 60, 100, 140, 180, 220]

def try_draw_pixel(cycle, sprite_pos):
    crt_col = (cycle)%40
    crt_row = (floor(cycle / 40)) % 7
    if crt_col in set(range(sprite_pos - 1, sprite_pos + 2)):
        return (crt_row, crt_col)
    return None

def draw_grid(points):
    for row in range(6):
        r = ""
        for col in range(40):
            if (row, col) in points:
                r += "#"
            else:
                r += "."
        print(r)


def ans(inp):
    cycle = 0
    x = 1
    check_idx = 0
    tot = 0

    drawn_pixels = set()

    
    for line in inp.split("\n"):
        if line[0] == "n":
            n = 0
            n_extra_cycles = 1
        else:
            n = int(line[4:])
            n_extra_cycles = 2

        for c in range(cycle, cycle + n_extra_cycles):
            drawn = try_draw_pixel(c, x)
            if drawn:
                drawn_pixels.add(drawn)

        cycle += n_extra_cycles

        if check_idx < len(checkpoints):
            if cycle >= checkpoints[check_idx]:
                tot += checkpoints[check_idx] * x
                check_idx += 1

        x += n
    draw_grid(drawn_pixels)
    return tot

if __name__ == '__main__':
    with open("inputs/testinp10.txt") as tstinput:
        print(ans(tstinput.read()))
    with open("inputs/inp10.txt") as tstinput:
        print(ans(tstinput.read()))
        # PAPKFKEJ