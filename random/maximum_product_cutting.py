# /*
# Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that
# maximizes product of lengths of all parts. You must make at least one cut.
# Assume that the length of rope is more than 2 meters.
#
# let target_value = 5
# returns [2, 3] -> 6
# */
from typing import List

ROPE_LENGTH_VALUE = 30
TEMP_RESULTS = dict()

SETTINGS_MAX_RECURSION_COUNT = 5


def generate_root_values_split(target_value_param: int) -> None:
    for key in range(1, target_value_param):
        value = target_value_param - key
        if key <= value:
            TEMP_RESULTS[key] = [[key, value]]


def split_values(input_value1: int, input_value2: int) -> None:
    def _split_value_recursive(_input_value1: int, _input_value2: int) -> None:
        if _input_value2 > 1:
            last_item = TEMP_RESULTS[input_value1][-1].copy()
            last_item_max_value = max(last_item)
            last_item.remove(last_item_max_value)
            last_item.extend([last_item_max_value - 1, 1])
            TEMP_RESULTS[input_value1].append(last_item)
            _split_value_recursive(_input_value1, _input_value2 - 1)

    _split_value_recursive(input_value1, input_value2)

    for key, value in TEMP_RESULTS.items():
        for result_item in value:
            count_of_ones = len([u for u in result_item if u == 1])
            if count_of_ones > 1:
                while 1 in result_item:
                    result_item.remove(1)
                result_item.append(count_of_ones)


def generate_values_split() -> None:
    i = 0
    while True:
        for key, value in TEMP_RESULTS.items():
            split_values(value[0][0], value[0][1])
        i += 1
        if i == SETTINGS_MAX_RECURSION_COUNT:
            break


def filter_results() -> None:
    for value in TEMP_RESULTS.values():
        for result_item in value:
            # You must make at least one cut.
            if len(result_item) == 1:
                value.remove(result_item)


def deduplicate_results_by_multiplied_value() -> List[dict]:
    def _multiply(numbers: List[int]) -> int:
        a = 1
        for num in numbers:
            a *= num
        return a

    deduplicated_results, multiplied_seen_results = [], set()
    for key, value in TEMP_RESULTS.items():
        for result_item in value:
            multiplied_list_items = _multiply(result_item)
            if multiplied_list_items in multiplied_seen_results:
                continue
            multiplied_seen_results.add(multiplied_list_items)
            deduplicated_results.append({"key": result_item, "value": multiplied_list_items})

    return deduplicated_results


def print_sorted_results(deduplicated_results) -> None:
    deduplicated_results.sort(key=lambda e: e["value"], reverse=True)
    for sorted_item in deduplicated_results:
        print(f"{sorted_item['key']} -> {sorted_item['value']}")


generate_root_values_split(ROPE_LENGTH_VALUE)
generate_values_split()
filter_results()
print_sorted_results(deduplicate_results_by_multiplied_value())
