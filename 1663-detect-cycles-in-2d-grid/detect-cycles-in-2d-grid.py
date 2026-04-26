class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        count = [[0]*n for _ in range(m)]
        ans = False

        def fn(i, j, val, c, prev_i, prev_j):
            ans = False
            count[i][j]= c + 1
            directions = [(0,-1),(-1,0),(0,1),(1,0)]

            for x, y in directions:
                if i+x >=0 and j+y >=0 and i+x<m and j+y<n:
                    if grid[i+x][j+y] == val:
                        if count[i+x][j+y] > 0 and (count[i][j] - count[i+x][j+y]) >= 3 and (i+x, j+y) != (prev_i, prev_j):
                            ans = True
                        elif count[i+x][j+y] == 0:
                            ans = fn(i+x, j+y, val, count[i][j], i, j)
                        if ans:
                            break

            count[i][j]-=1

            return ans

        
        for i in range(m):
            for j in range(n):
                if count[i][j] == 0:
                    temp = fn(i, j, grid[i][j], 0, None, None)
                    if temp:
                        return True

        return False