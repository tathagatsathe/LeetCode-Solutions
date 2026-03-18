class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0

        for i in range(m):
            if i > 0:
                grid[i][0]+=grid[i-1][0]
            if grid[i][0] > k:
                break
            ans+=1
            for j in range(1, n):
                grid[i][j]+=grid[i][j-1]
                if i > 0:
                    grid[i][j]+=(grid[i-1][j]-grid[i-1][j-1])
                if grid[i][j] <= k:
                    ans+=1
                else:
                    break

        return ans
