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


def split_input(input_string: str, pattern=r"(don't\(\)|do\(\))"):
    """Split the input string at words "don't()" and "do()". Example:

    some_characters_etc_mul(2,3)...
    do()
    +/0mul(3,2)...
    don't()
    810/&"=mul(1,2)...
    """
    return re.split(pattern, input_string)


def get_valid_rows_from_split_input(input_string: str) -> str:
    split = split_input(input_string)
    valid_rows = []
    for index, row in enumerate(split):
        if index == 0:
            valid_rows.append(split[index])
        if row.strip() == "do()":
            valid_rows.append(split[index + 1])

    return "".join(valid_rows)


if __name__ == '__main__':
    file_input = read_input_as_string("input_data/day_3/input.txt")
    pattern_founds = find_pattern(file_input)
    s = evaluate_expressions(pattern_founds)
    print(s)
    valid_inputs = get_valid_rows_from_split_input(file_input)
    pattern_founds = find_pattern(valid_inputs)
    s = evaluate_expressions(pattern_founds)
    print(s)
