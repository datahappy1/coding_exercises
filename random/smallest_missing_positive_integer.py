# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# Examples
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
# Input ranges
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].
from typing import List


def get_smallest_pos_int(input_arr: List[int]) -> int:
    # unique
    # get min value
    # add to unique set value min value +1
    # eval len until changed
    # return found value
    unique_input = set(input_arr)
    unique_input_initial_len, unique_input_min_val = len(unique_input), min(unique_input)
    next_value = 0
    while unique_input_initial_len == len(unique_input):
        next_value += 1
        unique_input.add(next_value)
    return next_value


print(get_smallest_pos_int(input_arr=[1, 3, 6, 4, 1, 2]))
print(get_smallest_pos_int(input_arr=[1, 2, 3]))
print(get_smallest_pos_int(input_arr=[-1, -3]))
large_arr = [x for x in range(-100000, 100000)]
print(get_smallest_pos_int(input_arr=large_arr))
