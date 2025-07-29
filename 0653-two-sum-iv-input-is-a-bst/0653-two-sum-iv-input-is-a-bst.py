# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def inorder_dfs(node):
            if node is None:
                return []
            return inorder_dfs(node.left) + [node.val] + inorder_dfs(node.right)
        
        sorted_vals = inorder_dfs(root)
        L, R = 0, len(sorted_vals) - 1

        while L < R:
            curr_sum = sorted_vals[L] + sorted_vals[R]
            if curr_sum == k:
                return True
            elif curr_sum < k:
                L += 1
            else:
                R -= 1
        return False 