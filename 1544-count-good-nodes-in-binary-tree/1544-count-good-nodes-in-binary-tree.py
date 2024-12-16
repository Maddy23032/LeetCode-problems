# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,mv):
            if not node:
                return 0
            r=1 if mv<=node.val else 0
            mv=max(mv,node.val)
            r+=dfs(node.left,mv)  
            r+=dfs(node.right,mv)
            return r
        return dfs(root,root.val)      