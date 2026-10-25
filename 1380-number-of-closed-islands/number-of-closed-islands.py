class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(i, j):
            directions = [(-1,0), (0, -1), (1, 0), (0, 1)]
            for x, y in directions:
                if 0 <= x + i < m and 0 <= y + j < n and grid[x+i][y+j] == 0 and not visited[x+i][y+j]:
                    visited[x+i][y+j] = True
                    dfs(x+i, y+j)


        for i in range(m):
            if grid[i][0] == 0 and not visited[i][0]:
                visited[i][0] = True
                dfs(i, 0)
            if grid[i][n-1] == 0 and not visited[i][n-1]:
                visited[i][n-1] = True
                dfs(i, n-1)

        for i in range(n):
            if grid[0][i] == 0 and not visited[0][i]:
                visited[0][i] = True
                dfs(0, i)
            if grid[m-1][i] == 0 and not visited[m-1][i]:
                visited[m-1][i] = True
                dfs(m-1, i)

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j)
                    ans+=1

        return ans
