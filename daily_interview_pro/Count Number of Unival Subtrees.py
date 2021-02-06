# A unival tree is a tree where all the nodes have the same value.
# Given a binary tree, return the number of unival subtrees in the tree.
#
# For example, the following tree should return 5:
#
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1
#
# The 5 trees are:
# - The three single '1' leaf nodes. (+3)
# - The single '0' leaf node. (+1)
# - The [1, 1, 1] tree at the bottom. (+1)

# Here's a starting point:

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class solution:
    count = 0

    def count_unival_subtrees(self, root):
        # Fill this in.
        try:
            if root.val == root.left.val == root.right.val:
                solution.count += 1
        except AttributeError:
            pass
        if root.left == root.right or (not root.left and not root.right):
            solution.count += 1

        if root.left:
            self.count_unival_subtrees(root.left)
        if root.right:
            self.count_unival_subtrees(root.right)

        return solution.count


a = Node(0)
a.left = Node(1)
a.right = Node(0)
a.right.left = Node(1)
a.right.right = Node(0)
a.right.left.left = Node(1)
a.right.left.right = Node(1)

print(solution().count_unival_subtrees(a))
# 5
