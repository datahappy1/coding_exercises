# Given a binary tree, return all values given a certain height h.
# Here's a starting point:

class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = []

    def valuesAtHeight(self, root, desired_height, current_height=1):
        # Fill this in.
        if desired_height == current_height:
            self.result.append(root.value)
        else:
            if root.left:
                self.valuesAtHeight(root.left, desired_height, current_height + 1)
            if root.right:
                self.valuesAtHeight(root.right, desired_height, current_height + 1)
        return self.result


#     1
#    / \
#   2   3
#  / \   \
# 4   5   7

a = Node(1)
a.left = Node(2)
a.right = Node(3)
a.left.left = Node(4)
a.left.right = Node(5)
a.right.right = Node(7)
print(Solution().valuesAtHeight(a, 3))
# [4, 5, 7]
