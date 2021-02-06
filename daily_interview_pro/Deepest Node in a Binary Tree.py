# You are given the root of a binary tree. Return the deepest node (the furthest node from the root).
# Example:
#     a
#    / \
#   b   c
#  /
# d
#
# The deepest node in this tree is d at depth 3.
# Here's a starting point:

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        # string representation
        return self.val


class Finder:
    def __init__(self):
        self.cnt_left = 0
        self.cnt_right = 0
        self.last_processed_node = None

    def deepest(self, node):
        # Fill this in.
        if not node.left and not node.right:
            return node

        if node.left:
            self.cnt_left += 1
            if self.cnt_left >= self.cnt_right:
                self.last_processed_node = node.left
            self.deepest(node.left)
        if node.right:
            self.cnt_right += 1
            if self.cnt_right > self.cnt_left:
                self.last_processed_node = node.right
            self.deepest(node.right)

        return self.last_processed_node, max(self.cnt_right, self.cnt_left) + 1


root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

finder = Finder()
print(finder.deepest(root))
# (d, 3)
