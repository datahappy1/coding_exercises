# A palindrome is a sequence of characters that reads the same backwards and forwards.
# Given a string, s, find the longest palindromic substring in s.
#
# Example:
# Input: "banana"
# Output: "anana"
#
# Input: "million"
# Output: "illi"

class Solution:
    def get_list_forward_combinations(self, input_list):
        results = []
        i, l = 0, len(input_list)
        while i < l:
            j, k = i, i + 1
            while k <= l:
                results.append(input_list[j:k])
                k += 1
            i += 1
        return results

    def longest_palindrome(self, input_list):
        # Fill this in.
        candidates = []
        candidate = str()
        for _list in self.get_list_forward_combinations([x for x in input_list]):
            _list_reversed = list(reversed(_list))
            for item in list(zip(_list, _list_reversed)):
                if item[0] == item[1]:
                    candidate += item[0]
                    candidates.append(candidate)
                else:
                    break
            candidate = str()
        return max(candidates, key=len)


# Test program
s = "tracecars"
# s = "banana"
# s = "million"
print(str(Solution().longest_palindrome(s)))
# racecar
