# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.i = 0  # use self.i as a global index shared across recursive calls

        def helper(limit):
            if self.i >= len(preorder) or preorder[self.i] > limit:
                return None
            root = TreeNode(preorder[self.i])
            self.i += 1
            root.left = helper(root.val)
            root.right = helper(limit)
            return root

        return helper(float('inf'))
