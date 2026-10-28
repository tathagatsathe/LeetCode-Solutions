class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n, k = len(grid), len(grid[0]), 0

        max_ = max(max(row) for row in grid)

        while max_:
            k<<=1
            k+=1
            max_>>=1


        dp = [[[None]*(k+1) for _ in range(n)] for _ in range(m)]

        dp[0][0][grid[0][0]] = True

        for i in range(1, m):
            for x in range(k+1):
                if dp[i-1][0][x]:
                    temp = x ^ grid[i][0]
                    dp[i][0][temp] = True

        for i in range(1, n):
            for x in range(k+1):
                if dp[0][i-1][x]:
                    temp = x ^ grid[0][i]
                    dp[0][i][temp] = True

        for i in range(1, m):
            for j in range(1, n):
                for x in range(k+1):
                    if dp[i-1][j][x]:
                        temp = x ^ grid[i][j]
                        dp[i][j][temp] = True
                    if dp[i][j-1][x]:
                        temp = x ^ grid[i][j]
                        dp[i][j][temp] = True


        for x in range(k+1):
            if dp[m-1][n-1][x]:
                return x

        return -1