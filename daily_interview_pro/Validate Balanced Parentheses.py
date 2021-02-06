# Imagine you are building a compiler. Before running any code, the compiler must check that the parentheses
# in the program are balanced. Every opening bracket must have a corresponding closing bracket.
# We can approximate this using strings.
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:
# - Open brackets are closed by the same type of brackets.
# - Open brackets are closed in the correct order.
# - Note that an empty string is also considered valid.
#
# Example:
# Input: "((()))"
# Output: True
#
# Input: "[()]{}"
# Output: True
#
# Input: "({[)]"
# Output: False
# class Solution:
#     def isValid(self, s):
#         # Fill this in.
#
# # Test Program
# s = "()(){(())"
# # should return False
# print(Solution().isValid(s))
#
# s = ""
# # should return True
# print(Solution().isValid(s))
#
# s = "([{}])()"
# # should return True
# print(Solution().isValid(s))


class Solution:
    _open_brackets = ["(", "{", "["]
    _closed_brackets = [")", "}", "]"]

    def get_opposite(self, item):
        try:
            idx = Solution._open_brackets.index(item)
            opposite = Solution._closed_brackets[idx]
        except ValueError:
            idx = Solution._closed_brackets.index(item)
            opposite = Solution._open_brackets[idx]
        return opposite

    def isValid(self, input_list):
        # Fill this in.
        if input_list == "":
            return True

        _bracket_list = [x for x in input_list]
        _open_brackets_tmp = []
        _closed_brackets_tmp = []
        for item in _bracket_list:
            opposite_item = self.get_opposite(item)
            if item in Solution._open_brackets:
                _open_brackets_tmp.append(item)
            elif item in Solution._closed_brackets:
                _closed_brackets_tmp.append(item)
                try:
                    if opposite_item == _open_brackets_tmp[-1]:
                        _open_brackets_tmp.pop()
                        _closed_brackets_tmp.pop()
                except IndexError:
                    return False

        return True if not _closed_brackets_tmp and not _open_brackets_tmp else False


# # Test Program
s = "(){()(()})"
# # should return False
print(Solution().isValid(s))
# #
s = ""
# # should return True
print(Solution().isValid(s))
#
s = "([{}]){}([]){}"
# # should return True
print(Solution().isValid(s))

s = "(({}))[]}"
# should return False
print(Solution().isValid(s))

s = "((){}]"
# # should return False
print(Solution().isValid(s))
