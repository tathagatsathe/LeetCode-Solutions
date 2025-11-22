import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        no_of_rows = len(heights)
        no_of_cols = len(heights[0])
        # visited = [[False]*no_of_cols for _ in range(no_of_rows)]
        dp = [[float("inf")]*no_of_cols for _ in range(no_of_rows)]
        dp[0][0] = 0
        
        def getValidVertices(i,j):
            directions = [(-1,0),(0,-1),(1,0),(0,1)]
            vertices = []
            for x, y in directions:
                if x+i>=0 and y+j>=0 and x+i<no_of_rows and y+j<no_of_cols:
                    vertices.append((x+i, y+j))

            return vertices

        
        h = []
        heapq.heappush(h, (0, 0, 0))

        while h:
            effort, x, y = heapq.heappop(h)
            if effort > dp[x][y]:
                continue
            
            if x == no_of_rows - 1 and y == no_of_cols - 1:
                return effort

            vertices = getValidVertices(x,y)

            for i, j in vertices:
                temp = max(effort, abs(heights[i][j] - heights[x][y]))
                if temp < dp[i][j]:
                    dp[i][j] = temp
                    heapq.heappush(h, (temp, i, j))

        return -1