# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node,path):
            if  node is None:
                return 0
            path=(path<<1)+node.val
            if node.left is None and  node.right is None:
                return path
            return dfs(node.left,path)+dfs(node.right,path)
        return dfs(root,0)