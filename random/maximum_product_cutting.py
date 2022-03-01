# /*
# Given a rope of length n meters, cut the rope in different parts of integer lengths in a way that
# maximizes product of lengths of all parts. You must make at least one cut.
# Assume that the length of rope is more than 2 meters.
#
# let target_value = 5
# returns [2, 3] -> 6
# */

target_value = 10
results = dict()


def generate_root_values_split(target_value_param: int):
    for item in range(1, target_value_param):
        y = target_value_param - item
        if item <= y:
            results[item] = [[item, y]]


def split_value_recursive(input_value1: int, input_value2: int):
    if input_value2 > 1:
        last_item = results[input_value1][-1].copy()
        last_item_max_value = max(last_item)
        last_item.remove(last_item_max_value)
        last_item.extend([last_item_max_value - 1, 1])
        results[input_value1].append(last_item)
        split_value_recursive(input_value1, input_value2 - 1)


def split_values():
    for k, v in results.items():
        split_value_recursive(v[0][0], v[0][1])

    for k, v in results.items():
        for i in v:
            count_of_ones = len([u for u in i if u == 1])
            if count_of_ones > 1:
                while 1 in i:
                    i.remove(1)
                i.append(count_of_ones)


def filter_results():
    for v in results.values():
        for iv in v:
            if len(iv) == 1:
                v.remove(iv)


def deduplicate_results_by_multiplied_value():
    def _multiply(numbers):
        a = 1
        for num in numbers:
            a *= num
        return a

    deduped_results, multiplied_seen_results = [], set()
    for key, val in results.items():
        for i in val:
            multiplied_item = _multiply(i)
            if multiplied_item in multiplied_seen_results:
                continue
            multiplied_seen_results.add(multiplied_item)
            deduped_results.append({'key': i, 'value': multiplied_item})
    return deduped_results


def format_results(deduplicated_results):
    deduplicated_results.sort(key=lambda e: e['value'], reverse=True)
    for sorted_item in deduplicated_results:
        print(f"{sorted_item['key']} -> {sorted_item['value']}")


generate_root_values_split(target_value)
split_values()
filter_results()
format_results(deduplicate_results_by_multiplied_value())
