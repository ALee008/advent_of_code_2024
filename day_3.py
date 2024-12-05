import re
import pathlib


def read_input_as_string(path: str | pathlib.Path) -> str:
    file = pathlib.Path(path)

    return file.read_text()


def find_pattern(input_string: str) -> list[str]:
    # Regex pattern to match 'mul(digits,digits)' with 1-3 digits each
    pattern = r"mul\(\d{1,3},\d{1,3}\)"

    # Find all matches
    matches = re.findall(pattern, input_string)

    return matches


def mul(x: int, y: int) -> int:
    return x * y


def evaluate_expressions(expressions: list[str]) -> int:
    evaluated = map(eval, expressions)

    sum_ = sum(evaluated)

    return sum_


if __name__ == '__main__':
    file_input = read_input_as_string("input_data/day_3/input.txt")

    pattern_founds = find_pattern(file_input)

    s = evaluate_expressions(pattern_founds)
    print(s)
