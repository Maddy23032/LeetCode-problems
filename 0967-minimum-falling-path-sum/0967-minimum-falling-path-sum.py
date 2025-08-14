class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # def uniqP(i,j,matrix):
        #     nonlocal n,dp
        #     if i==n-1:
        #         return matrix[i][j]
            
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     firstpath = float('inf')
        #     if j > 0:
        #         firstpath = matrix[i][j] + uniqP(i + 1, j - 1, matrix)
            
        #     secondpath = matrix[i][j] + uniqP(i + 1, j, matrix)
            
        #     thirdpath = float('inf')
        #     if j < n - 1:
        #         thirdpath = matrix[i][j] + uniqP(i + 1, j + 1, matrix)
            
        #     dp[i][j]=min(firstpath,secondpath,thirdpath)
        #     return dp[i][j]

        # minpath=float('inf')
        n, m = len(matrix), len(matrix[0])
        prev = [0 for _ in range(m)]

        for j in range(m):
            prev[j] = matrix[n-1][j]

        for i in range(n-2, -1, -1):
            cur=[0 for _ in range(m)]
            for j in range(m):
                curr = matrix[i][j]
                fp = prev[j-1] if j > 0 else float('inf')
                sp = prev[j]
                tp = prev[j+1] if j < m-1 else float('inf')
                cur[j] = curr + min(fp, sp, tp)
            prev=cur
        return min(prev)
        # for i in range(len(matrix[0])):
        #     minpath=min(minpath,uniqP(0,i,matrix))

        # return minpath