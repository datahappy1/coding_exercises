def function_a(input_list):
    if not isinstance(input_list, list) or len(input_list) <= 1:
        return None
    input_list.append(0)
    sorted_input_list = (sorted(input_list))
    sorted_input_list_iterator = iter(sorted_input_list)
    next(sorted_input_list_iterator)

    for item in sorted_input_list:
        item_plus_1 = item + 1
        try:
            next_item = next(sorted_input_list_iterator)
            if item <= 0 and next_item > 1:
                return 1
            if next_item not in (item, item_plus_1) and next_item > 0:
                return item_plus_1
        except StopIteration:
            return item_plus_1


#
A = [3, 4, -1, 1]  # sample input list
print(function_a(A))
B = [1, 3, 6, 4, 1, 2]
print(function_a(B))
C = [-1, 0, 3]
print(function_a(C))
D = [-1, -3, 2]
print(function_a(D))
E = [-1, 0, 1, 2, 3]
print(function_a(E))
