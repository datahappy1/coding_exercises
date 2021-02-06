# You are given an array of k sorted singly linked lists.
# Merge the linked lists into a single sorted linked list and return it.
# Here's your starting point:
class Node(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        c = self
        answer = ""
        while c:
            answer += str(c.val) if c.val else ""
            c = c.next
        return answer


def merge(input_lists):
    # Fill this in.
    _temp_res, res = [], []
    _lists_merged = [Node(input_list).__str__() for input_list in input_lists]
    for _list in [list(x) for x in _lists_merged]:
        _temp_res.append(_list)

    for y in range(len(_temp_res[0])):
        for z in range(len(_temp_res)):
            res.append(_temp_res[z][y])
    return ''.join(res)


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
print(merge([a, b]))
# 123456
