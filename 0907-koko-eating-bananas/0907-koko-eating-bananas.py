class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def caneat(x):
            be=0
            for i in piles:
                be+=math.ceil(i/x)
            return be<=h    
        res=0
        l,r=1,max(piles)
        while l<=r:
            x=(l+r)//2
            if caneat(x):
                res=x
                r=x-1
            else:
                l=x+1
        return res            