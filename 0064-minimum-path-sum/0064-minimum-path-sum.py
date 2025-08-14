class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n,m=len(grid),len(grid[0])

        prev=[0 for _ in range(m)]
        for i in range(n):
            cur=[0 for _ in range(m)]
            for j in range(m):
                if i==0 and j==0:
                    cur[j]=grid[i][j]
                else:
                    up = grid[i][j] + (prev[j] if i > 0 else float('inf'))
                    left = grid[i][j] + (cur[j-1] if j > 0 else float('inf'))
                    cur[j] = min(up, left)
            prev=cur
        return prev[m-1]
        # def uniqP(a,b,grid,dp):
        #     nonlocal n,m
        #     if a==0 and b==0:
        #         return grid[a][b]
        #     if dp[a][b]!=-1:
        #         return dp[a][b]
        #     if a<0 or b<0:
        #         return float('inf')
            
        #     up=grid[a][b]+uniqP(a-1,b,grid,dp)
        #     left=grid[a][b]+uniqP(a,b-1,grid,dp)
        #     dp[a][b]=min(up,left)
        #     return dp[a][b]
        # dp=[[-1 for _ in range(m)] for _ in range(n)]
        # return uniqP(n-1,m-1,grid,dp)