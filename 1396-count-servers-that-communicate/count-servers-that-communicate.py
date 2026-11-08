class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        row_sum = [0]*m
        col_sum = [0]*n
        for i in range(m):
            for j in range(n):
                col_sum[j]+=grid[i][j]
                row_sum[i]+=grid[i][j]

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (col_sum[j] > 1 or row_sum[i] > 1):
                    ans+=1

        return ans