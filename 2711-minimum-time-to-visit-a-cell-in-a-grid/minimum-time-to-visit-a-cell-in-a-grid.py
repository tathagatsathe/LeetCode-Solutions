from collections import deque
import heapq
class Solution:
    def minimumTime(self, grid: List[List[int]]) -> int:        
        m = len(grid)
        n = len(grid[0])
        directions = [(-1,0),(0,-1),(1,0),(0,1)]
        visited = [[False]*n for _ in range(m)]
        h = []
        heapq.heappush(h,(0,0,0))

        if grid[0][0]!=0 or (grid[0][1]>1 and grid[1][0]>1):
            return -1

        while h:
            time, i, j = heapq.heappop(h)

            if visited[i][j]:
                continue

            grid[i][j] = time
            if i == m-1 and j==n-1:
                return grid[i][j]
            visited[i][j] = True
            for x, y in directions:
                if 0<=x+i<m and 0<=y+j<n and visited[x+i][y+j]==False:
                    if grid[x+i][y+j]<=time+1:
                        heapq.heappush(h, (time+1,x+i,y+j))
                    else:
                        temp = 0 if (grid[x+i][y+j]-grid[i][j])%2  else 1
                        heapq.heappush(h, (grid[x+i][y+j]+temp, x+i,y+j))

        return -1
