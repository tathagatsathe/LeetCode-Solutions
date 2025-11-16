class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(i,j):
            if i<0 or j<0 or i>m-1 or j>n-1 or grid[i][j]=="0":
                return 

            grid[i][j] = "0"
            for d in directions:
                dfs(i+d[0],j+d[1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    ans+=1

        return ans


