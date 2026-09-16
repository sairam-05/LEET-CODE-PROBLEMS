# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        s=[]
        def order(node):
            if node and node.left and node.left.left is None and node.left.right is None:

                s.append(node.left.val)
            if node:
                order(node.left)
                order(node.right)
        order(root)
        return sum(s)
