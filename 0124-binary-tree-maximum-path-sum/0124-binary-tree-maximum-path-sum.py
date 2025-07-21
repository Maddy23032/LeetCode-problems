# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxsum=float('-inf')
        def maxPathDown(node):
            if not node:
                return 0
            l=max(0,maxPathDown(node.left))
            r=max(0,maxPathDown(node.right))
            self.maxsum=max(self.maxsum,l+r+node.val)
            return max(l,r)+node.val

        maxPathDown(root)
        return self.maxsum