# You are given an array of intervals - that is, an array of tuples(start, end).The array
# may not be sorted, and could contain overlapping intervals.Return another array where
# the overlapping intervals are merged.
# For example: [(1, 3), (5, 8), (4, 10), (20, 25)]
# This input should return [(1, 3), (4, 10), (20, 25)] since(5, 8) and (4, 10)
# can be merged into(4, 10).
# Here's a starting point:
def merge(intervals):
    # Fill this in.
    stack = []

    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    for idx, sorted_interval in enumerate(sorted_intervals):
        if idx == 0:
            stack.append(sorted_interval)
            continue
        if sorted_interval[0] >= max([interval[1] for interval in stack]):
            stack.append(sorted_interval)
        if sorted_interval[1] >= max([interval[1] for interval in stack]):
            _max_stack_item = stack[-1]
            _max_stack_item = (_max_stack_item[0], sorted_interval[1])
            stack[-1] = _max_stack_item

    return stack


print(merge([(1, 3), (5, 8), (4, 10), (20, 25)]))
# [(1, 3), (4, 10), (20, 25)]
print(merge([(1, 3), (5, 8), (7, 10), (20, 25)]))
