class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])
        def uniqP(a,b,grid,dp):
            nonlocal n,m
            if a==0 and b==0:
                return grid[a][b]
            if dp[a][b]!=-1:
                return dp[a][b]
            if a<0 or b<0:
                return float('inf')
            
            up=grid[a][b]+uniqP(a-1,b,grid,dp)
            left=grid[a][b]+uniqP(a,b-1,grid,dp)
            dp[a][b]=min(up,left)
            return dp[a][b]
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        return uniqP(n-1,m-1,grid,dp)