# You are given a positive integer N which represents the number of steps in a staircase.\
# You can either climb 1 or 2 steps at a time.Write a function that returns the number of
# unique ways to climb the stairs.

# Can you find a solution in O(n) time?


def staircase(n, m=2):
    temp = 0
    res = [1]

    for i in range(1, n + 1):
        s = i - m - 1
        e = i - 1

        if s >= 0:
            temp -= res[s]
        temp += res[e]
        res.append(temp)

    return res[n]


print(staircase(4))
# 5
print(staircase(5))
# 8
