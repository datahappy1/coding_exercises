# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).
# Here's the signature:

# levenshtein distance
def LD(s, t):
    if s == "":
        return len(t)
    if t == "":
        return len(s)
    if s[-1] == t[-1]:
        cost = 0
    else:
        cost = 1

    res = min([LD(s[:-1], t) + 1,
               LD(s, t[:-1]) + 1,
               LD(s[:-1], t[:-1]) + cost])

    return res


print(LD('biting', 'sitting'))
# 2
