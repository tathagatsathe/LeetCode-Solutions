import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        def getValidVertices(i,j):
            directions = [(-1,0),(1,0),(0,1),(0,-1)]
            vertices = []
            for (x, y) in directions:
                if x+i>=0 and y+j>=0 and x+i<n and y+j<n and visited[x+i][y+j]==False:
                    vertices.append((x+i,y+j))

            return vertices

        h = []
        ans = grid[0][0]
        heapq.heappush(h, (ans, 0, 0))

        while h:
            min_time, x, y = heapq.heappop(h)

            if visited[x][y] == True:
                continue

            if min_time > ans:
                ans = min_time

            if x == n-1 and y == n-1:
                break
            visited[x][y] = True
            adj = getValidVertices(x,y)

            for i, j in adj:
                if visited[i][j] == False:
                    heapq.heappush(h,(max(grid[i][j],min_time), i, j))



        return ans
        