def combinations_3(ary):
    l = len(ary)
    for i in range(l - 2):
        for j in range(i + 1, l - 1):
            for k in range(j + 1, l):
                yield (ary[i], ary[j], ary[k])


for combination in combinations_3([1, 2, 3, 4]):
    print(combination)


def combinations_2(ary):
    l = len(ary)
    for i in range(l - 2):
        for j in range(i + 1, l):
            yield (ary[i], ary[j])


for combination in combinations_2([1, 2, 3, 4, 6]):
    print(combination)
