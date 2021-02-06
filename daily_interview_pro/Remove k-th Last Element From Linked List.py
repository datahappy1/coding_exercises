# You are given a singly linked list and an integer k. Return the linked list,
# removing the k-th last element from the list.
# Try to do it in a single pass and using constant space.
# Here's a starting point:


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        current_node = self
        result = []
        while current_node:
            result.append(current_node.val)
            current_node = current_node.next
        return str(result)


def remove_kth_from_linked_list(head, n):
    # Fill this in
    if not head.next:
        return
    front = head
    back = head
    counter = 0
    flag = False

    while counter <= n:
        if not front:
            flag = True
            break
        front = front.next
        counter += 1
    while front:
        front = front.next
        back = back.next
    if not flag:
        temp = back.next
        back.next = temp.next
        temp.next = None
    else:
        head = head.next
    return head


head = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(head)
# [1, 2, 3, 4, 5]
head = remove_kth_from_linked_list(head, 4)
print('output', head)
# [1, 2, 4, 5]
