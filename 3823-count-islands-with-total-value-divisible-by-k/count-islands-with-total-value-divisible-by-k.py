class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(i, j):
            directions = [(-1,0), (1, 0), (0, -1), (0, 1)]
            sum_ = 0
            for x, y in directions:
                if 0 <= i+x < m and 0 <= j+y < n and not visited[i+x][j+y] and grid[i+x][j+y] > 0:
                    visited[i+x][j+y] = True
                    sum_+=grid[i+x][j+y]
                    sum_+=dfs(i+x, j+y)

            return sum_

        ans = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0 and not visited[i][j]:
                    visited[i][j] = True
                    sum_ = dfs(i, j) + grid[i][j]
                    if sum_ % k == 0:
                        ans+=1

        return ans
