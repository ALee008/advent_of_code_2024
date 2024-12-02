import itertools
import pathlib
from collections import namedtuple

from helper import get_rows_from_file_day_2

Pairs = namedtuple("Pairs", "x y")


def check_reports_for_safety(path: str | pathlib.Path) -> int:
    reports = get_rows_from_file_day_2(path)
    checks = [pairwise_compare(report) for report in reports]

    return sum(checks)


def monotone_increasing(report: list[int]) -> bool:
    for p in itertools.pairwise(report):
        pair = Pairs(*p)
        if not pair.y > pair.x:
            return False

    return True


def monotone_decreasing(report: list[int]) -> bool:
    for p in itertools.pairwise(report):
        pair = Pairs(*p)
        if not pair.y < pair.x:
            return False

    return True


def pairwise_compare(report: list[int]) -> bool:
    if any([monotone_increasing(report), monotone_decreasing(report)]):
        for pair in itertools.pairwise(report):
            pairs = Pairs(*pair)
            distance = abs(pairs.y - pairs.x)
            if distance > 3:
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    r = check_reports_for_safety("input_data/day_2/input.txt")
    print(r)
    # print(monotone_increasing([35, 37, 38, 41, 43, 43]))
    # print(monotone_decreasing([35, 37, 38, 41, 43, 41]))
    # print(monotone_increasing([35, 37, 38, 41, 43, 45]))
    # print(monotone_decreasing([55, 47, 38, 21, 13, 1]))
