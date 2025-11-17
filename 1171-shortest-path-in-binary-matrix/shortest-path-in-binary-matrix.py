from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        directions =[(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1),(-1,0)] 
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        if grid[n-1][n-1] != 0 or grid[0][0] != 0:
            return -1
        if n==1:
            return 1

        st = deque([(0,0,1)])

        while st:
            i, j, level = st.popleft()

            if i == n-1 and j == n-1:
                return level

            for (x, y) in directions:
                nx, ny = i+x, j+y
                if 0<=nx<n and 0<=ny<n and grid[nx][ny]==0 and visited[nx][ny]==False:
                    st.append((nx, ny, level+1))
                    visited[nx][ny]=True
                    
        return -1                