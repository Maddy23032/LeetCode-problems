from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows, cols = len(obstacleGrid), len(obstacleGrid[0])

        dp = [[-1 for _ in range(cols)] for _ in range(rows)]

        def dfs(i, j):
            if i >= rows or j >= cols:
                return 0
            if obstacleGrid[i][j] == 1:
                return 0
            if i == rows - 1 and j == cols - 1:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return dp[i][j]

        return dfs(0, 0)
