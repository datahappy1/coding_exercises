"""
distributed factorial attempt
"""
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from typing import Iterator


def calculate_factorial(n_range: range) -> int:
    """
    this function calculates factorial on n range
    :param n_range:
    :return:
    """
    factorial = 1
    for i in n_range:
        factorial *= i
    return factorial


def input_reader(n: int, split_size: int) -> dict:
    """
    this is the function responsible for reading input size n and
    splitting the generated range into splits of size split_size
    :param n:
    :param split_size:
    :return:
    """
    splits_result = defaultdict(list)
    for elem in range(1, n + 1):
        splits_result[elem // split_size].append(elem)
    return splits_result


def map_factorials(splits: dict, workers: int) -> Iterator:
    """
    this function maps the splits to workers to calculate partial factorials
    :param splits:
    :param workers:
    :return:
    """
    with ProcessPoolExecutor(max_workers=workers) as exe:
        mapped_result = exe.map(calculate_factorial, splits.values())
    return mapped_result


def combine_factorials(mapped_result: Iterator) -> int:
    """
    this function calculates the final result factorial
    :param mapped_result:
    :return:
    """
    reduced_result = 1
    for mr in mapped_result:
        reduced_result *= mr
    return reduced_result


def validate_input_size(n: int) -> bool:
    """
    this is a basic input validation function
    :param n:
    :return:
    """
    if n <= 0 or n > 1000:
        return False
    return True


if __name__ == "__main__":
    factorial_size = 100

    SPLITS = 10
    WORKERS = 10

    is_valid = validate_input_size(n=factorial_size)
    if is_valid is False:
        raise ValueError("Invalid input size")

    input_splits = input_reader(n=factorial_size, split_size=SPLITS)
    result = combine_factorials(map_factorials(input_splits, workers=WORKERS))
    print(result)
