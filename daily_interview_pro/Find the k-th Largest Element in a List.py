# Given a list, find the k-th largest element in the list.
# Input: list = [3, 5, 2, 4, 6, 8], k = 3
# Output: 5

def findKthLargest(nums, k):
    # Fill this in.
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k - 1]


print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5
