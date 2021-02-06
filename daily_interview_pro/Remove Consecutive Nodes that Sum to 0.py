# Given a linked list of integers, remove all consecutive nodes that sum up to 0.
#
# Example:

# Input: 10 -> 5 -> -3 -> -3 -> 1 -> 4 -> -4
# Output: 10
#
# The consecutive nodes 5 -> -3 -> -3 -> 1 sums up to 0 so that sequence should be removed.
# 4 -> -4 also sums up to 0 too so that sequence should also be removed.
# Here's a starting point:


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def removeConsecutiveSumTo0(head: Node) -> Node:
    dummy = curr_node = Node(0)
    dummy.next = head
    prefix_sum = 0
    prefix_sum_map = {}
    while curr_node:
        prefix_sum += curr_node.value
        if prefix_sum in prefix_sum_map:
            curr_node = prefix_sum_map.get(prefix_sum).next
            sum = prefix_sum + curr_node.value
            while sum != prefix_sum and sum in prefix_sum_map:
                del prefix_sum_map[sum]
                curr_node = curr_node.next
                sum += curr_node.value
            prefix_sum_map[prefix_sum].next = curr_node.next
        else:
            prefix_sum_map[prefix_sum] = curr_node
        curr_node = curr_node.next
    return dummy.next


node = Node(10)
node.next = Node(5)
node.next.next = Node(-3)
node.next.next.next = Node(-3)
node.next.next.next.next = Node(1)
node.next.next.next.next.next = Node(4)
node.next.next.next.next.next.next = Node(-4)
node = removeConsecutiveSumTo0(node)
while node:
    print('output', node.value, )
    node = node.next
    # 10
