class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # l=[[0]*n for _ in range(m)]
        # for i in range(m):
        #     l[i][n-1]=1
        # for i in range(n):
        #     l[m-1][i]=1
        # for i in range(m-2,-1,-1):
        #     for j in range(n-2,-1,-1):
        #         l[i][j]=l[i+1][j]+l[i][j+1]
        # return l[0][0]
        def upr(x,y,m,n,l):
            if x==m-1 and y==n-1:
                return 1
            if l[x][y]!=-1:
                return l[x][y]
            rp,dp=0,0
            if x<m-1:
                rp=upr(x+1,y,m,n,l)
            if y<n-1:
                dp=upr(x,y+1,m,n,l)
            l[x][y]=rp+dp
            return l[x][y]
        l=[[-1]*n for _ in range(m)]
        return upr(0,0,m,n,l)