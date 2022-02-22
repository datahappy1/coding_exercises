input = {
    "keyA": "aba",
    "keyB": "aaa",
    "keyC": "dca",
    "keyD": "aa"
}
output = dict()
last_eval_value = None
eval_item_order = []

for k, v in input.items():
    if last_eval_value and v > last_eval_value:
        eval_item_order.append((k, v))
    else:
        eval_item_order.insert(-1, (k, v))
    last_eval_value = v

for elem in eval_item_order:
    output[elem[0]] = elem[1]

print(input)
print(output)
