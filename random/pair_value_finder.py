# /*
# In a technical interview, you've been given an array of numbers and you need to find a pair of numbers that are equal
# to the given target value. Numbers can be either positive, negative, or both.
# Can you design an algorithm that works in O(n)—linear time or greater?
#
# let sequence = [8, 10, 2, 9, 7, 5]
# let results = pairValues(sum: 11) = //returns (9, 2)
# */
from typing import Optional, Set

sequence = [8, 10, 2, 9, 7, 5]
target = 12


def pair_value_finder(input_list: [], target_value: int) -> Set[Optional[tuple]]:
    diffs = set()
    input_dict = dict()
    for item in input_list:
        input_dict[item] = None

    for key in input_dict.keys():
        try:
            input_dict[target_value-key]
        except KeyError:
            continue
        diffs.add((key, target_value-key))

    return diffs


print(pair_value_finder(sequence, target))
