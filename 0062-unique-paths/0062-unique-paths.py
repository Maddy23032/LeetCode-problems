class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l=[[0]*n for _ in range(m)]
        for i in range(m):
            l[i][n-1]=1
        for i in range(n):
            l[m-1][i]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                l[i][j]=l[i+1][j]+l[i][j+1]
        return l[0][0]