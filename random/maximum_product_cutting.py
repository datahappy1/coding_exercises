# /*
# Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that
# maximizes product of lengths of all parts. You must make at least one cut.
# Assume that the length of rope is more than 2 meters.
#
# let target_value = 5
# returns [2, 3] -> 6
# */

from typing import List

TARGET_ROPE_LENGTH_VALUE = 15


def generate_base_dataset(value_param: int):
    def _generate_root_values_split(target_value_param: int) -> List:
        _results = []
        for val in range(1, target_value_param):
            diff_val = target_value_param - val
            if val <= diff_val:
                _results.append([val, diff_val])
        yield _results

    if value_param <= 1:
        raise ValueError("TARGET_ROPE_LENGTH_VALUE value has to be > 1")

    results = [[]]
    iteration = 0
    while iteration < value_param:
        try:
            _value_param = max(results[iteration][0])
        except IndexError:
            _value_param = value_param
        results.extend([val for val in _generate_root_values_split(target_value_param=_value_param)])
        iteration += 1

    return results


def transform_base_dataset(base_dataset_param: List[List]) -> dict:
    results = dict()
    for item in enumerate(base_dataset_param):
        if item[1]:
            s = sum([val for val in item[1][0]])
            results[s] = item[1]

    return results


def generate_results(base_dataset_transformed_param: dict) -> List[List]:
    data = base_dataset_transformed_param[TARGET_ROPE_LENGTH_VALUE].copy()

    iter_counter = 0
    for key, value in base_dataset_transformed_param.items():
        for data_item in [item for item in data if item[0] < key]:
            data_item_max_value = max(data_item)
            if key == data_item_max_value:
                for value_item in value:
                    iter_counter += 1
                    new_item = data_item.copy()
                    new_item.remove(data_item_max_value)
                    for leaf_value_item in value_item:
                        new_item.append(leaf_value_item)
                    data.append(new_item)

    print(f"{iter_counter} iterations")

    return data


def deduplicate_results(generated_results_param: List[List]) -> List[dict]:
    def _multiply(numbers: List[int]) -> int:
        a = 1
        for num in numbers:
            a *= num
        return a

    deduplicated_results, multiplied_seen_results = [], set()
    for result_item in generated_results_param:
        multiplied_list_items = _multiply(result_item)
        if multiplied_list_items in multiplied_seen_results:
            continue
        multiplied_seen_results.add(multiplied_list_items)
        deduplicated_results.append({"key": result_item, "value": multiplied_list_items})

    return deduplicated_results


def print_sorted_results(deduplicated_results: List[dict]) -> None:
    deduplicated_results.sort(key=lambda e: e["value"], reverse=True)
    for sorted_item in deduplicated_results:
        print(f"{sorted_item['key']} -> {sorted_item['value']}")


base_dataset = generate_base_dataset(TARGET_ROPE_LENGTH_VALUE)
base_dataset_transformed = transform_base_dataset(base_dataset)
generated_results_data = generate_results(base_dataset_transformed)
deduplicated_results_data = deduplicate_results(generated_results_data)
print_sorted_results(deduplicated_results_data)
