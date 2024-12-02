import functools
import operator

import helper


def distance() -> int:
    left, right = helper.get_columns_as_list_of_int_day_1("input_data/day_1/input.txt")
    sorted_left = sorted(left)
    sorted_right = sorted(right)
    zipped = zip(sorted_left, sorted_right)
    difference = [abs(functools.reduce(operator.sub, z)) for z in zipped]
    return sum(difference)


def similarity_score() -> int:
    left, right = helper.get_columns_as_list_of_int_day_1("input_data/day_1/input.txt")
    left_as_set = set(left)
    scores = []
    for l in left_as_set:
        if l in right:
            score = l * len([el for el in right if el == l])
            scores.append(score)

    return sum(scores)


if __name__ == '__main__':
    #diff = distance()
    sim = similarity_score()
    print(similarity_score())
