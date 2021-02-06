# You are given a string s, and an integer k. Return the length of the longest substring in s that
# contains at most k distinct characters.
#
# For instance, given the string:
# aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.
#
# Here's a starting point:
def longest_substring_with_k_distinct_characters(input_string, k):
    # Fill this in.
    string_list = [x for x in input_string]
    for idx, item in enumerate(string_list):
        try:
            if item in string_list[idx + 1]:
                string_list.pop(idx)
                string_list[idx] += item
        except IndexError:
            if item in string_list[idx - 1]:
                string_list.pop(idx)
                string_list[idx - 1] += item
    print(string_list)

    x = 0
    result = 0
    while k <= len(string_list):
        _len = sum([len(x) for x in string_list[x:k]])
        if _len > result:
            result = _len
        print([x for x in string_list[x:k]])
        x += 1
        k += 1

    return result


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
