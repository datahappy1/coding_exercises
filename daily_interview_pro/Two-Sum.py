# You are given a list of numbers, and a target number k.
# Return whether or not there are two numbers in the list that add up to k.

# Example:

# Given [4, 7, 1 , -3, 2] and k = 5,
# return true since 4 + 1 = 5.


def two_sum(input_list, k):
    # Fill this in.
    hashTable = {}

    for i in range(len(input_list)):
        complement = k - input_list[i]
        if complement in hashTable:
            # print("Pair with sum", k,"is: (", input_list[i],",",complement,")")
            return True
        hashTable[input_list[i]] = input_list[i]
    return False


print(two_sum([4, 7, 0, -3, 2, 1], 5))
# True
