import heapq

class Solution:
    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return 0
        directions = [(0,-1),(1,0),(-1,0),(0,1)]
        visited = [[False]*n for _ in range(n)]
        dp = [[float("inf")]*n for _ in range(n)]
        h = []

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    heapq.heappush(h, (0, i, j))

        while h:
            dist, i, j = heapq.heappop(h)

            if dist>=dp[i][j]:
                continue
            dp[i][j] = dist
            for x, y in directions:
                if 0<=i+x<n and 0<=j+y<n:
                    heapq.heappush(h, (dist+1, i+x, j+y))

        
        # print('dp: ',dp)


        h = []
        heapq.heappush(h, (-dp[0][0], 0, 0))
        ans = float("-inf")
        while h:
            dist, i, j = heapq.heappop(h)
            # print('i: ',i, ' j: ',j)
            if dist > ans:
                ans = dist
            if visited[i][j]:
                continue
            
            if i == n-1 and j==n-1:
                break

            visited[i][j] = True
            for x, y in directions:
                if 0<=i+x<n and 0<=j+y<n:
                    heapq.heappush(h, (-dp[i+x][j+y], i+x, j+y))


        # print('ans: ',ans)
        if ans == float("-inf"):
            return -1
        return -ans
        

