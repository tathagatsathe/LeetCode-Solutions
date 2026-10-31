class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m, n = len(grid), len(grid[0])

        dp = [[[0,0] for _ in range(n)] for _ in range(m)]

        for i in range(n):
            dp[0][i][0] = 1
            if grid[0][i] == 1:
                break

        for j in range(m):
            dp[j][0][1] = 1
            if grid[j][0] == 1:
                break

        for i in range(1, m):
            for j in range(1, n):
                if grid[i-1][j] == 1:
                    dp[i][j][1]= (dp[i][j][1] + dp[i-1][j][0]) % MOD
                else:
                    dp[i][j][1] = (dp[i][j][1] + dp[i-1][j][0] + dp[i-1][j][1]) % MOD
                if grid[i][j-1] == 1:
                    dp[i][j][0] = (dp[i][j][0] + dp[i][j-1][1]) % MOD
                else:
                    dp[i][j][0] = (dp[i][j][0] + dp[i][j-1][0] + dp[i][j-1][1]) % MOD

        return (dp[m-1][n-1][0] + dp[m-1][n-1][1]) % MOD