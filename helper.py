import csv
import pathlib


def get_columns_as_list_of_int_day_1(path: str | pathlib.Path) -> list[list[int]]:
    result = [[], []]

    with open(path, encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            result[0].append(int(row[0]))
            result[1].append(int(row[1]))
    return result


def get_rows_from_file_day_2(path: str | pathlib.Path) -> list[list[int]]:
    result = []

    with open(path, encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            numbers_in_row_as_int = list(map(int, row))
            result.append(numbers_in_row_as_int)

    return result


if __name__ == '__main__':
    test = get_columns_as_list_of_int_day_1("input_data/day_1/input.txt")
    #print(test[:3])
    test_day_2 = get_rows_from_file_day_2("input_data/day_2/input.txt")
    print(test_day_2)