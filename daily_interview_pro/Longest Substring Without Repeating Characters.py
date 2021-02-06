#Given a string, find the length of the longest substring without repeating characters.

class Solution:
    def length_of_longest_substring(self, input_string):
        # Fill this in.
        candidates = []
        seen = []
        candidate = str()
        for item in input_string:
            candidate += item
            if item in seen:
                seen = []
                candidate = str()
            else:
                seen += item
                candidates.append(candidate)

        return max([len(x) for x in candidates])


print(Solution().length_of_longest_substring('abrkaabcdefghijjxxx'))
# 10 abcdefghij
