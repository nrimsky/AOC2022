"""
Assume the head and the tail both start at the same position, overlapping.
count up all of the positions the tail visited at least once
"""


def update_pos(head_pos, direction):
    new_pos = head_pos
    if direction == "R":
        new_pos[0] += 1
    elif direction == "L":
        new_pos[0] -= 1
    elif direction == "U":
        new_pos[1] += 1
    else:
        new_pos[1] -= 1
    return new_pos


def move_tail(head_pos, tail_pos):
    diff_x = head_pos[0] - tail_pos[0]
    diff_y = head_pos[1] - tail_pos[1]
    abs_diff_x = abs(diff_x)
    abs_diff_y = abs(diff_y)
    if abs_diff_x <= 1 and abs_diff_y <= 1:
        return tail_pos
    return [tail_pos[0] + (diff_x / max([abs_diff_x, 1])), tail_pos[1] + (diff_y / max([abs_diff_y, 1]))]


def ans(inp, n_knots):
    curr = [[0, 0] for _ in range(n_knots)]  # Head X Head Y, ..., Tail X Tail Y
    visited = set()
    for line in inp.split("\n"):
        direction, amount = line.split(" ")
        amount = int(amount)
        for _ in range(amount):
            new_head = update_pos(curr[0], direction)
            for i in range(1, n_knots):
                curr[i] = move_tail(curr[i - 1], curr[i])
            visited.add(tuple(curr[-1]))
    return len(visited)


if __name__ == '__main__':
    with open("inputs/testinp9.txt") as txtfile:
        print(ans(txtfile.read(), 2))
    with open("inputs/inp9.txt") as txtfile:
        print(ans(txtfile.read(), 2))
    with open("inputs/testinp9.txt") as txtfile:
        print(ans(txtfile.read(), 10))
    with open("inputs/inp9.txt") as txtfile:
        print(ans(txtfile.read(), 10))