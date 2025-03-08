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
import timeit


# # less performant set based version:
# def get_smallest_pos_int(input_arr: List[int]) -> int:
#     input_uniq = set(input_arr)
#     input_uniq_max = max(input_uniq)
#     if input_uniq_max < 0:
#         return 1
#     gen_set = {i for i in range(1, input_uniq_max)}
#     gen_set_diff = gen_set.difference(input_uniq)
#     return min(gen_set_diff) if gen_set_diff else input_uniq_max + 1


def get_smallest_pos_int(input_arr: List[int]) -> int:
    # unique
    # get min value
    # add to unique set value min value +1
    # eval len until changed
    # return found value
    unique_input = set(input_arr)
    unique_input_initial_len = len(unique_input)
    next_value = 0
    while unique_input_initial_len == len(unique_input):
        next_value += 1
        unique_input.add(next_value)
    return next_value


# print(get_smallest_pos_int(input_arr=[1, 3, 6, 4, 1, 2]))
# print(get_smallest_pos_int(input_arr=[1, 2, 3]))
# print(get_smallest_pos_int(input_arr=[-1, -3]))
large_arr = [x for x in range(-100000000, 100000000)]
start = timeit.default_timer()
print("The start time is :", start)

print(get_smallest_pos_int(input_arr=large_arr))
print("The difference of time is :", timeit.default_timer() - start)
