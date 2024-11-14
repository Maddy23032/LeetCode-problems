class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def cd(x):
            stores=0
            for i in quantities:
                stores+=math.ceil(i/x)
            return stores<=n
        l,r=1,max(quantities)
        m=0
        while l<=r:
            x=(l+r)//2
            if cd(x):
                m=x
                r=x-1
            else:l=x+1    
        return m    