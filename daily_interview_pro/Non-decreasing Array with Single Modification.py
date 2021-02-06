# You are given an array of integers in an arbitrary order.
# Return whether or not it is possible to make the array non-decreasing by modifying at most 1 element to any value.
# We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).
# Example:
# [13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.
# [13, 4, 1] however, should return false, since there is no way to modify just one element to make the array non-decreasing.
#
# Can you find a solution in O(n) time?
# Here is the function signature:

def check(lst):
    # Fill this in.
    lst_iter = (x for x in lst)
    next(lst_iter)
    found = None
    for item in lst:
        try:
            next_item = next(lst_iter)
            if item <= next_item:
                pass
            elif not found:
                found = True
            elif found:
                return False
        except StopIteration:
            return True


print(check([13, 4, 7]))
# True
print(check([13, 4, 1]))
# False
print(check([5, 1, 3, 2, 5]))
# False
