# You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise.
# Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root,
# and all values in the right subtree are greater than or equal to the root.
#
# Here's a starting point:

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


class Bst:
    def __init__(self):
        self.isValid = None

    def is_bst(self, root):
        # Fill this in.
        print(root.key, root.left, root.right)
        if not root.left and not root.right:
            # leaf node
            pass
        elif not all([root.left, root.right]):
            # node without left or right
            self.isValid = False
            return self.isValid

        if root.left:
            if root.left.key <= root.key:
                self.isValid = True
                self.is_bst(root.left)
            else:
                self.isValid = False
                return self.isValid
        if root.right:
            if root.right.key >= root.key:
                self.isValid = True
                self.is_bst(root.right)
            else:
                self.isValid = False
                return self.isValid

        return self.isValid


a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
a.right.right = TreeNode(9)
bst = Bst()
print(bst.is_bst(a))

#    5
#   / \
#  3   7
# / \ /
# 1  4 6
