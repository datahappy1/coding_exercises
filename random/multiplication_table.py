def get_row(row_size, multiplier):
    return ' '.join(
        [str(i * multiplier) for i in range(1, row_size + 1)]
    ) + "\n"


def multi_table(input_size):
    return ''.join(
        [get_row(row_size=input_size, multiplier=i + 1) for i in range(0, input_size)]
    )


print(multi_table(5))
