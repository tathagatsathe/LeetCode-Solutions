class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0,0]]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                temp = []
                if i > 0:
                    temp.extend([grid[i][j] * dp[i-1][j][0], grid[i][j] * dp[i-1][j][1]])
                if j > 0:
                    temp.extend([grid[i][j] * dp[i][j-1][0], grid[i][j] * dp[i][j-1][1]])
                if i == 0 and j == 0:
                    temp.append(grid[i][j])

                dp[i][j] = [min(temp), max(temp)]

        res = dp[m-1][n-1][1]

        return res % (10**9 + 7) if res >= 0 else -1

            