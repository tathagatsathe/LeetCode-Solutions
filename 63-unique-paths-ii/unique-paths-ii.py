import copy
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        visited = [[0]*n for _ in range(m)]

        if (obstacleGrid[m-1][n-1] or obstacleGrid[0][0]):
            return 0

        visited[m-1][n-1] = 1
        
        def adjCells(obstacleGrid, i, j, visited):
            v = [(1,0),(0,1)]
            cells = []
            for (x, y) in v:
                if((i+x>=0 and j+y>=0 and i+x<len(obstacleGrid) and j+y<len(obstacleGrid[0]) and obstacleGrid[i+x][j+y]==0)):
                    cells.append((i+x, j+y))

            return cells

        def uniquePath(obstacleGrid, i, j, visited, m, n):
            if(visited[i][j]):
                return visited[i][j]

            cells = adjCells(obstacleGrid, i, j, visited)

            ans = 0
            for (x,y) in cells:
                ans+=uniquePath(obstacleGrid, x, y, visited, m, n)

            visited[i][j] = ans

            return visited[i][j]

        return uniquePath(obstacleGrid, 0, 0, visited, m, n)

            