import heapq

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

        dp = [[float("inf")]*n for _ in range(m)]
        visited = [[False]*n for _ in range(m)]
        h = []
        heapq.heappush(h, (grid[0][0], 0, 0))
        # print('h: ',h)
        while h:
            obstacles, x, y = heapq.heappop(h)

            if obstacles >= dp[x][y]:
                continue

            vertices = getValidVertices(x, y)

            dp[x][y] = obstacles
            visited[x][y] = True

            # print('x: ',x, ' y: ',y)
            for i, j in vertices:
                heapq.heappush(h, (obstacles + grid[i][j], i, j))


        # print('dp: ',dp)
        return dp[m-1][n-1]
        