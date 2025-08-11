class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # def uniqP(a,b,dp):
        #     nonlocal m,n
        #     if a==m-1 and b==n-1:
        #         dp[a][b]=1
        #         return dp[a][b]
        #     if a >= m or b >= n:
        #         return 0
        #     if dp[a][b]!=-1:
        #         return dp[a][b]
        #     dp[a][b]=uniqP(a+1,b,dp)+uniqP(a,b+1,dp)
        #     return dp[a][b]

        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = 1  # base case
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                down = dp[i+1][j] if i+1 < m else 0
                right = dp[i][j+1] if j+1 < n else 0
                dp[i][j] = down + right
        
        return dp[0][0]
