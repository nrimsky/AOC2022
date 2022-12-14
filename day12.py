from collections import deque, defaultdict

def get_elevation(letter):
    if letter == 'S':
        return ord('a')
    elif letter == 'E':
        return ord('z')
    return ord(letter)


def get_connected_squares(row, col, n_rows, n_cols):
    connected = []
    if row > 0:
        connected.append((row - 1, col))
    if row < n_rows - 1:
        connected.append((row + 1, col))
    if col > 0:
        connected.append((row, col - 1))
    if col < n_cols - 1:
        connected.append((row, col + 1))
    return connected


def get_valid_next_steps(row, col, elevations):
    n_rows, n_cols = len(elevations), len(elevations[0])
    connected = get_connected_squares(row, col, n_rows, n_cols)
    curr_elevation = elevations[row][col]
    valid = [c for c in connected if elevations[c[0]][c[1]] <= curr_elevation + 1]
    return valid


def find_start_end(parsed):
    start = (0, 0)
    end = (0, 0)
    for row_idx, row in enumerate(parsed):
        for col_idx, item in enumerate(row):
            if item == 'S':
                start = (row_idx, col_idx)
            elif item == 'E':
                end = (row_idx, col_idx)
    return start, end

def ans(inp):
    parsed = [[a for a in s] for s in inp.split("\n")]
    elevations = [[get_elevation(l) for l in s] for s in parsed]
    start, end = find_start_end(parsed)
    visited = set()
    to_visit = deque([(start, 0)])
    while len(to_visit) > 0:
        curr, dist = to_visit.pop()
        if curr in visited:
            continue
        if curr == end:
            return dist
        visited.add(curr)
        valid_next = get_valid_next_steps(curr[0], curr[1], elevations)
        for place in valid_next:
            if place not in visited:
                to_visit.appendleft((place, dist + 1))
    return dist

if __name__ == "__main__":
    with open("inputs/testinp12.txt") as tstfile:
        print(ans(tstfile.read()))
    with open("inputs/inp12.txt") as textfile:
        print(ans(textfile.read()))