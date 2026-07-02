import heapq

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def getValidMoves(i, j):
            res = []
            directions = [(-1,0), (0,1), (1,0), (0,-1)]
            for x, y in directions:
                if i+x>=0 and j+y>=0 and i+x<m and j+y<n and visited[i+x][j+y] == False:
                    res.append((i+x, j+y))

            return res

        h = []

        heapq.heappush(h, (grid[0][0], 0,0))
        visited[0][0] = True

        while h:
            cost, x, y = heapq.heappop(h)
            if x == m-1 and y == n-1:
                return True
            
            moves = getValidMoves(x, y)

            for i, j in moves:
                if cost + grid[i][j] < health and visited[i][j] == False:
                    heapq.heappush(h, (cost + grid[i][j], i, j))
                    visited[i][j] = True


        return False