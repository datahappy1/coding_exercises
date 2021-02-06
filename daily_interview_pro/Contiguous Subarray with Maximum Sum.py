# You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.
# Example:
# [34, -50, 42, 14, -5, 86]
# Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].
# Your solution should run in linear time.
# Here's a starting point:

def max_subarray_sum(arr):
    max_so_far = 0
    max_ending_here = 0
    size = len(arr)

    for i in range(0, size):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0

        # Do not compare for all elements. Compare only
        # when  max_ending_here > 0
        elif (max_so_far < max_ending_here):
            max_so_far = max_ending_here

    return max_so_far


print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137
