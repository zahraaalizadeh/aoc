import aocd

import utils

SHAPE_MATRIX_Q1 = {
    "X": 1,
    "Y": 2,
    "Z": 3,
    "A": 1,
    "B": 2,
    "C": 3,
}

SCORE_MATRIX_Q1 = {
    "A X": 3,
    "A Y": 6,
    "A Z": 0,
    "B X": 0,
    "B Y": 3,
    "B Z": 6,
    "C X": 6,
    "C Y": 0,
    "C Z": 3,
}

SCORE_MATRIX_Q2 = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

SHAPE_MATRIX_Q2 = {
    "A X": 3,
    "A Y": 1,
    "A Z": 2,
    "B X": 1,
    "B Y": 2,
    "B Z": 3,
    "C X": 2,
    "C Y": 3,
    "C Z": 1,
}



def question_1(data: utils.Data) -> int:
    """
    Calculate total score be if everything goes exactly according to the strategy guide
    """
    score = 0
    for row in data.groups:
        # total score + shape score
        score += SCORE_MATRIX_Q1[row.raw_data] + SHAPE_MATRIX_Q1[row.last().raw_data]
    return score

def question_2(data: utils.Data) -> int:
    score = 0
    for row in data.groups:
        score += SCORE_MATRIX_Q2[row.last().raw_data] + SHAPE_MATRIX_Q2[row.raw_data]
    return score

def test(sample):
    data = utils.Data(sample)
    assert question_1(data) == 15
    assert question_2(data) == 12


# ------------
# MAIN
# ------------
sample = """A Y
B X
C Z"""
test(sample)

input = aocd.get_data(day=2, year=2022)
data = utils.Data(input)
print(question_1(data))
print(question_2(data))
