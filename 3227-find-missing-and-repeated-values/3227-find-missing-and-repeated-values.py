class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hm={}
        n=len(grid)
        for i in grid:
            for j in i:
                if j in hm:
                    hm[j]+=1
                else:
                    hm[j]=1
        r,m=0,0
        for i in range(1,n**2+1):
            if i not in hm:
                m=i
            elif hm[i]==2:
                r=i
        return [r,m]