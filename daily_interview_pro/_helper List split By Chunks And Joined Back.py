def get_list_in_chunks(l, n):
    n = max(1, n)
    return list(l[i:i + n] for i in range(0, len(l), n))


def join_list_from_chunks(l):
    result = []
    for i in l:
        result.extend(i)
    return result


lx = [1, 2, 3, 4]
lxc = get_list_in_chunks(lx, 2)
print(lxc)

print(join_list_from_chunks(lxc))
