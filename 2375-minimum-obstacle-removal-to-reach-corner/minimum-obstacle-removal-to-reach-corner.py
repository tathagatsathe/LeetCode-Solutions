import heapq
from collections import deque
class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        def getValidVertices(i, j):
            directions = [(-1,0),(0, -1),(1,0),(0,1)]
            vertices = []
            for x, y in directions:
                if x+i>=0 and y+j>=0 and x+i<m and y+j<n and visited[x+i][y+j]==False:
                    vertices.append((x+i, y+j))

            return vertices

        visited = [[False]*n for _ in range(m)]
        cost = grid[0][0]
        h = deque()
        h.append((0, 0,0))
        visited[0][0] = True
        while h:
            obstacles, x, y = h.popleft()

            if x==m-1 and y==n-1:
                return obstacles

            vertices = getValidVertices(x, y)

            # print('x: ',x, ' y: ',y)
            for i, j in vertices:
                if grid[i][j] == 0:
                    h.appendleft((obstacles, i, j))
                else:
                    h.append((obstacles+1, i, j))
                visited[i][j] = True

        # print('dp: ',dp)
        return -2
        