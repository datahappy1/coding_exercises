# Given an array of n positive integers and a positive integer s,
# find the minimal length of a contiguous subarray of which the sum ≥ s.
# If there isn't one, return 0 instead.
# Example:
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem constraint.
# Here is the method signature:
class Solution:
    n = 0
    lens = []

    def minSubArrayLen(self, nums, s):
        # Fill this in
        while True:
            for idx, num in enumerate(nums):
                item = nums[Solution.n:idx + 1]
                if item:
                    Solution.lens.append(item)
            Solution.n += 1

            if Solution.n == len(nums):
                if not Solution.lens:
                    return 0
                return min([len(x) for x in Solution.lens if sum(x) >= s])


print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
