class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0,-1),(0,1),(-1,0),(1,0)]

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]!=1:
                return

            grid[i][j]=2
            for (x, y) in directions:
                dfs(i+x, j+y)

            
        
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)

        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans+=1

        return ans


        