# You are given the preorder and inorder traversals of a binary tree in the form of arrays.
# Write a function that reconstructs the tree represented by these traversals.
#
# Example:
# Preorder: [a, b, d, e, c, f, g]
# Inorder: [d, b, e, a, f, c, g]
#
# The tree that should be constructed from these traversals is:
#     a
#    / \
#   b   c
#  / \ / \
# d  e f  g
from collections import deque


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = deque()
        q.append(self)
        result = ''
        while len(q):
            n = q.popleft()
            result += n.val
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)

        return result


def reconstruct(preorder, inorder):
    if inorder:
        root = Node(preorder.pop(0))
        root_index = inorder.index(root.val)
        root.left = reconstruct(preorder, inorder[:root_index])
        root.right = reconstruct(preorder, inorder[root_index + 1:])
        return root


preorder = ['a', 'b', 'd', 'e', 'c', 'f', 'g']
inorder = ['d', 'b', 'e', 'a', 'f', 'c', 'g']
tree = reconstruct(preorder, inorder)
print(tree)
# abcdefg
