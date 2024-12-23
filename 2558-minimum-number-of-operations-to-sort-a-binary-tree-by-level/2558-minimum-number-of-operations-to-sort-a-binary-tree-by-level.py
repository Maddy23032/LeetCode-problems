# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def cswaps(li):
            s=0
            sl=sorted(li)
            imap={n:i for i,n in enumerate(li)}
            for i in range(len(li)):
                if li[i]!=sl[i]:
                    s+=1
                    j=imap[sl[i]]
                    li[i],li[j]=li[j],li[i]
                    imap[li[j]]=j
            return s
        r=0
        q=deque([root])
        while q:
            l=[]
            for _ in range(len(q)):
                node=q.popleft()
                l.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            r+=cswaps(l)
        return r