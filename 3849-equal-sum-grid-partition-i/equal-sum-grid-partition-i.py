class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        c, r = [0]*n, [0]*m
        row_sum, col_sum = 0, 0

        for i in range(m):
            for j in range(n):
                c[j]+=grid[i][j]
                r[i]+=grid[i][j]

        row_sum, col_sum = sum(r), sum(c)

        if row_sum % 2 and col_sum % 2:
            return False

        half_row_sum = row_sum//2
        half_col_sum = col_sum//2

        if row_sum % 2 == 0:
            temp = 0
            for i in range(m-1):
                temp+=r[i]
                if temp == half_row_sum:
                    return True

        if col_sum % 2 == 0:
            temp = 0
            for i in range(n-1):
                temp+=c[i]
                if temp == half_col_sum:
                    return True


        return False