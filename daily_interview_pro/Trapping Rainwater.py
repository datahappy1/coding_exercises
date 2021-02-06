# You have a landscape, in which puddles can form. You are given an array of non-negative integers
# representing the elevation at each location. Return the amount of water that would accumulate if it rains.
#
# For example: [0,1,0,2,1,0,1,3,2,1,2,1] should return 6 because 6 units of water can get trapped here.
#        X
#     X███XX█X
#   X█XX█XXXXXX
# # [0,1,0,2,1,0,1,3,2,1,2,1]
# Here's your starting pont:

def capacity(arr):
    # Fill this in.
    res = 0
    for idx, item in enumerate(arr):
        if 0 < idx < len(arr) - 1:
            if arr[idx - 1] > item or arr[idx + 1] > item:
                res += 1
    return res


print(capacity([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
# 6
