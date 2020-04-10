class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [[0] * (n + 1) for _ in range(m + 1)]

        dp[1][1] = grid[0][0]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = grid[i - 1][j - 1] + max(dp[i - 1][j], dp[i][j - 1])

        return dp[m][n]