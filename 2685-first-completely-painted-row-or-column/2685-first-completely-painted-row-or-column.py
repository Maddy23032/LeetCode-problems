class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        r,c=len(mat),len(mat[0])
        hm={}
        for i in range(r):
            for j in range(c):
                hm[mat[i][j]]=(i,j)
        rc,cc=[0]*r,[0]*c
        for i in range(len(arr)):
            a,b=hm[arr[i]]
            rc[a]+=1
            cc[b]+=1
            if rc[a]==c or cc[b]==r:
                return i
        