# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.counter=0
        self.kthsmall=float('inf')
        def inorder(root):
            if not root:
                return root
            inorder(root.left)
            self.counter+=1
            if(self.counter==k):
                self.kthsmall=root.val
            inorder(root.right)
        inorder(root)
        return self.kthsmall