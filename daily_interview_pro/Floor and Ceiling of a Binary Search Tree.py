# Given an integer k and a binary search tree,
# find the floor(less than or equal to) of k, and the ceiling(larger than or equal to) of k.
# If either does not exist, then print them as None.
# Here is the definition of a node for the tree.
#
#
# class Node:
#     def __init__(self, value):
#         self.left = None
#         self.right = None
#         self.value = value
#
#
# def findCeilingFloor(root_node, k, floor=None, ceil=None):
#
#
# # Fill this in.
#
# root = Node(8)
# root.left = Node(4)
# root.right = Node(12)
#
# root.left.left = Node(2)
# root.left.right = Node(6)
#
# root.right.left = Node(10)
# root.right.right = Node(14)
#
# print(findCeilingFloor(root, 5))
# # (4, 6)

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


def findCeilingFloor(root_node, k, floors=None, ceils=None):
    # Fill this in.
    if not floors and not ceils:
        floors, ceils = [], []

    if root_node:
        if root_node.value <= k:
            floors.append(root_node.value)

        elif root_node.value >= k:
            ceils.append(root_node.value)

        findCeilingFloor(root_node.right, k, floors, ceils)
        findCeilingFloor(root_node.left, k, floors, ceils)

    return max(floors) if floors else None, min(ceils) if ceils else None


root = Node(8)
root.left = Node(4)
root.right = Node(12)

root.left.left = Node(2)
root.left.right = Node(6)

root.right.left = Node(10)
root.right.right = Node(14)

print(findCeilingFloor(root, 5))
# (4, 6)
