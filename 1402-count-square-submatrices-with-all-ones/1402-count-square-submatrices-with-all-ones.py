class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ROWS, COLS = len (matrix), len(matrix[0])
        dp = defaultdict(int)
        res = 0
        for r in range (ROWS):
            cur_dp = defaultdict(int)
            for c in range(COLS):
                if matrix[r][c]:
                    cur_dp[c] = 1 + min(
                        dp[c],
                        cur_dp[c - 1],
                        dp[c - 1]
                    )
                    res += cur_dp[c]
            dp = cur_dp
        return res