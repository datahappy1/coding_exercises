# Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A
# so that the result equals B.
# Example 1:
# Input: A = "ab", B = "ba"
# Output: true

# Example 2:
# Input: A = "ab", B = "ab"
# Output: false

# Example 3:
# Input: A = "aa", B = "aa"
# Output: true

# Example 4:
# Input: A = "aaaaaaabc", B = "aaaaaaacb"
# Output: true

# Example 5:
# Input: A = "", B = "aa"
# Output: false

# Here's a starting point:
class Solution:
    def buddyStrings(self, A, B):
        # Fill this in.
        if len(A) != len(B):
            return False
        elif any(x for x in A if x not in B):  # otherwise when A and B has any element that are not common, then
            return False
        elif A == B and len(set(A)) == len(
                A):  # otherwise when A is same as B and all characters are distinct in A, then
            return False
        else:  # otherwise,
            count = 0
        for i in range(0, len(A)):
            if A[i] != B[i]:
                count += 1
                if count == 3:
                    return False
        return True


print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False
