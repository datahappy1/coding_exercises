# You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.
# Example:
# [-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.
# Here's a starting point:
# def printArr(a, n):
#     for i in range(n):
#         print(a[i], end=" ")
#     print()

result = []


def heapPermutation(a, size, n):
    # if size becomes 1 then prints the obtained
    # permutation
    if size == 1:
        _result = []
        for i in range(n):
            _result.append(a[i])
        result.append(_result)
        return a, n

    for i in range(size):
        heapPermutation(a, size - 1, n)

        # if size is odd, swap 0th i.e (first)
        # and (size-1)th i.e (last) element
        # else If size is even, swap ith
        # and (size-1)th i.e (last) element
        if size & 1:
            a[0], a[size - 1] = a[size - 1], a[0]
        else:
            a[i], a[size - 1] = a[size - 1], a[i]


def maximum_product_of_three(lst):
    # Fill this in.
    heapPermutation(lst, len(lst), 3)
    candidates = result
    return max([candidate[0] * candidate[1] * candidate[2] for candidate in candidates])


print(maximum_product_of_three([-4, -4, 2, 8]))
# 128
