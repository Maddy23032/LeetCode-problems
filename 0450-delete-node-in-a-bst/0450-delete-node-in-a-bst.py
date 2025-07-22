# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def flr(root):
            if not root.right:return root
            return flr(root.right)
        def helper(root):
            if not root.left:return root.right
            elif not root.right:return root.left
            else:
                rightChild=root.right
                lastright=flr(root.left)
                lastright.right=rightChild
                return root.left
        if not root:
            return root
        if root.val==key:
            return helper(root)
        dummy=root
        while root:
            if root.val>key:
                if root.left and root.left.val==key:
                    root.left=helper(root.left)
                    break
                else:
                    root=root.left
            else:
                if root.right and root.right.val==key:
                    root.right=helper(root.right)
                    break
                else:
                    root=root.right
        return dummy