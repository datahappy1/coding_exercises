from math import ceil


class limlist:
    def __init__(self, lim):
        self.obj = []
        self.lim = lim

    def lim_extend(self, item):
        if len(self.obj) < self.lim:
            self.obj.extend(item)

    def __repr__(self):
        return str(self.obj)


def matrix_spiral_print(M):
    # Fill this in.
    rows, cols = [], []

    for row in M:
        rows.append([x for x in row])
    _row_member_count = len(rows[0])

    for i in range(0, _row_member_count):
        cols.append([x[i] for x in rows])

    rows_len = len(rows)
    cols_len = len(cols)
    matrix_member_count = rows_len * cols_len
    result = limlist(matrix_member_count)

    iters_count = int(ceil(rows_len / 2))

    for i in range(0, iters_count):
        result.lim_extend(rows[i][i:cols_len - i])
        result.lim_extend(cols[cols_len - i - 1][i + 1:rows_len - i - 1])
        result.lim_extend(list(reversed(rows[rows_len - i - 1][i:cols_len - i])))
        result.lim_extend(list(reversed(cols[i][i + 1:rows_len - i - 1])))

    return result


grid = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        # [16, 17, 18, 19, 20],
        #  [21, 22, 23, 24, 25]
        ]

print(matrix_spiral_print(grid))
