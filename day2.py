SHAPE_SCORES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

GAME_SCORES = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3,
}

SHAPES_TO_WIN_DRAW_LOSE = {
    "A": {"X": 3, "Y": 1, "Z": 2},
    "B": {"X": 1, "Y": 2, "Z": 3},
    "C": {"X": 2, "Y": 3, "Z": 1}
}

OUTCOME_SCORES = {
    "X": 0,
    "Y": 3,
    "Z": 6
}


def get_round_score(p1, p2):
    shape_score = SHAPE_SCORES[p2]
    game_score = GAME_SCORES[p1 + p2]
    return shape_score + game_score


def get_round_score_2(p1, p2):
    game_score = OUTCOME_SCORES[p2]
    shape_score = SHAPES_TO_WIN_DRAW_LOSE[p1][p2]
    return shape_score + game_score


def get_score(strategy):
    tot_score = 0
    for line in strategy.split("\n"):
        p1, p2 = line.split(" ")
        tot_score += get_round_score(p1, p2)
    return tot_score


def get_score_2(strategy):
    tot_score = 0
    for line in strategy.split("\n"):
        p1, p2 = line.split(" ")
        tot_score += get_round_score_2(p1, p2)
    return tot_score


if __name__ == '__main__':
    assert get_score("A Y\nB X\nC Z") == 15
    with(open("inputs/inp2.txt")) as txtfile:
        print(get_score(txtfile.read()))

    assert get_score_2("A Y\nB X\nC Z") == 12
    with(open("inputs/inp2.txt")) as txtfile:
        print(get_score_2(txtfile.read()))
