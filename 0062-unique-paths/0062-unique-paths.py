class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def uniqP(a,b,dp):
            nonlocal m,n
            if a==m-1 and b==n-1:
                dp[a][b]=1
                return dp[a][b]
            if a >= m or b >= n:
                return 0
            if dp[a][b]!=-1:
                return dp[a][b]
            dp[a][b]=uniqP(a+1,b,dp)+uniqP(a,b+1,dp)
            return dp[a][b]

        
        dp=[[-1 for _ in range(n)] for _ in range(m)]
        return uniqP(0,0,dp)