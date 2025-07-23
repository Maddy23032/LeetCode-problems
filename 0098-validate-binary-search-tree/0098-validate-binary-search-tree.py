# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def isvb(root,minv,maxv):
            if not root:
                return True
            if root.val>=maxv or root.val<=minv:return False
            return isvb(root.left,minv,root.val) and isvb(root.right,root.val,maxv)
        return isvb(root,float('-inf'),float('inf'))