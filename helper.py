import csv
import pathlib


def get_columns_as_list_of_int(path: str | pathlib.Path) -> list[list[int]]:
    result = [[], []]

    with open(path, encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            result[0].append(int(row[0]))
            result[1].append(int(row[1]))
    return result


if __name__ == '__main__':
    test = get_columns_as_list_of_int("input_data/day_1/input.txt")
    print(test[:3])
