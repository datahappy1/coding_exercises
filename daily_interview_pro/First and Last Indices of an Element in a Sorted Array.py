# Given a sorted array, A, with possibly duplicated elements, find the indices of the first
# and last occurrences of a target element, x.Return -1 if the target is not found.
#
# Example:
# Input: A = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15], target = 9
# Output: [6, 8]
#
# Input: A = [100, 150, 150, 153], target = 150
# Output: [1, 2]
#
# Input: A = [1, 2, 3, 4, 5, 6, 10], target = 9
# Output: [-1, -1]
#
# Here is a function signature example:
#
# class Solution:
#     def getRange(self, arr, target):
#         Fill this in.
#
# # Test program
# arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
# x = 2
# print(Solution().getRange(arr, x))


# [1, 4]

# Input: A = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15], target = 9
# Output: [6, 8]
#
# Input: A = [100, 150, 150, 153], target = 150
# Output: [1, 2]
#
# Input: A = [1, 2, 3, 4, 5, 6, 10], target = 9
# Output: [-1, -1]

class Solution:
    def getRange(self, arr, target):
        result_list = [0, 0]
        _idx = None
        for idx, item in enumerate(arr):
            if item == target:
                result_list = [idx, idx]
                _idx = idx
                break

        if result_list[0] == 0:
            return [-1, -1]

        for idx, item in enumerate(arr[_idx + 1:]):
            if item != target:
                result_list[1] = result_list[0] + idx
                break
        return result_list


# Test program
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
target = 2
# Output: [1, 4]
print(Solution().getRange(arr, target))

arr = [1, 3, 3, 5, 7, 8, 9, 9, 9, 15]
target = 9
# Output: [6, 8]
print(Solution().getRange(arr, target))

arr = [100, 150, 150, 153]
target = 150
# Output: [1, 2]
print(Solution().getRange(arr, target))

arr = [1, 2, 3, 4, 5, 6, 10]
target = 9
# Output: [-1, -1]
print(Solution().getRange(arr, target))
