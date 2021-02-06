# Given a mathematical expression with just single digits, plus signs, negative signs, and brackets,
# evaluate the expression. Assume the expression is properly formed.
# Example:
# Input: - ( 3 + ( 2 - 1 ) )
# Output: -4
# Here's the function signature:4
from itertools import groupby


def eval_expr(expression):
    # Fill this in.
    _items = []
    _precedence = 0
    result = 0

    for item in expression:
        if item == ' ':
            continue
        elif item == '(':
            _precedence += 1
            continue
        elif item == ')':
            _precedence -= 1
            continue
        _dic = {"item": item, "precedence": _precedence}
        _items.append(_dic)

    _items.sort(key=lambda x: x['precedence'], reverse=True)
    for k, v in groupby(_items, key=lambda x: x['precedence']):
        temp_list = [x.get('item') for x in v]
        iterable_temp_list = iter(temp_list)

        for idx, item in enumerate(iterable_temp_list):
            if item.isnumeric():
                result += int(item)
            elif item == "-":
                try:
                    result -= int(temp_list[idx + 1])
                    next(iterable_temp_list)
                except IndexError:
                    result = result * -1
            elif item == "+":
                try:
                    result += int(temp_list[idx + 1])
                    next(iterable_temp_list)
                except IndexError:
                    pass

    return result


print(eval_expr('- (3 + ( 2 - 1 ) )'))
# -4
