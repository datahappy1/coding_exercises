# Given a list of numbers with only 3 unique numbers (1, 2, 3), sort the list in O(n) time.
#
# Example 1:
# Input: [3, 3, 2, 1, 3, 2, 1]
# Output: [1, 1, 2, 2, 3, 3, 3]
#

# Python Quicksort algorithm
from random import randint

def sortNums(nums):
    # Fill this in.
    if len(nums) < 2:
        return nums

    pivot = nums[randint(0, len(nums) - 1)]
    rights, lefts, sames = [], [], []
    for item in nums:
        if item < pivot:
            lefts.append(item)
        elif item > pivot:
            rights.append(item)
        elif item == pivot:
            sames.append(item)

    return sortNums(lefts) + sames + sortNums(rights)

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]