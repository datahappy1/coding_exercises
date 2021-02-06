# Given a list of numbers, where every number shows up twice except for one number, find that one number.
#
# Example:
# Input: [4, 3, 2, 4, 1, 3, 2]
# Output: 1
# Here's the function signature:
from datetime import datetime
from pympler import tracker


# https://pympler.readthedocs.io/…st/
def singleNumber(nums):
    # Fill this in.
    tr = tracker.SummaryTracker()

    numbers = (num for num in nums)
    hashTable = {}
    for number in numbers:
        if hashTable.get(number):
            del hashTable[number]
        else:
            hashTable[number] = number

    tr.print_diff()
    return [x for x in hashTable.values()]


large_list = list(range(1, 1000000)) * 2
large_list.pop(5000)

print(datetime.now())
print(singleNumber(large_list))
print(datetime.now())

# print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1

# Challenge: Find a way to do this using O(1) memory.
