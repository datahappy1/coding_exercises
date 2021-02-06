# You are given the root of a binary tree. Invert the binary tree in place.
# That is, all left children should become right children, and all right children
# should become left children.
#
# Example:
#
#     a
#    / \
#   b   c
#  / \  /
# d   e f
#
# The inverted version of this tree is as follows:
#
#   a
#  / \
#  c  b
#  \  / \
#   f e  d
#
# Here is the function signature:
#
# class Node:
#   def __init__(self, value):
#     self.left = None
#     self.right = None
#     self.value = value
#   def preorder(self):
#     print self.value,
#     if self.left: self.left.preorder()
#     if self.right: self.right.preorder()


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def preorder(self):
        print(self.value)
        if self.left: self.left.preorder()
        if self.right: self.right.preorder()


def invert(root_node):
    # Fill this in.

    if root_node:
        _tmp = (root_node.left, root_node.right)
        root_node.left = _tmp[1]
        root_node.right = _tmp[0]
        invert(root_node.right)
        invert(root_node.left)

    return


root = Node('a')
root.left = Node('b')
root.right = Node('c')
root.left.left = Node('d')
root.left.right = Node('e')
root.right.left = Node('f')

root.preorder()
# a b d e c f
print("\n")
invert(root)
root.preorder()
# a c f b e d
