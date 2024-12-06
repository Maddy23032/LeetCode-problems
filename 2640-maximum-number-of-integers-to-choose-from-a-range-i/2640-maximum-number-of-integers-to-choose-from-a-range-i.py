class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        s=set(banned)
        c=0
        for i in range(1,n+1):
            if i in s:
                continue
            if maxSum-i<0:
                return c    
            maxSum-=i
            c+=1    
        return c        