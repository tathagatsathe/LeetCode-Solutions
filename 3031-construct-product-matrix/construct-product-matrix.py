class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])

        pref = [[1 for j in range(m)] for i in range(n)]
        suff =  [[1 for j in range(m)] for i in range(n)]

        mod = 12345

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    continue
                if i > 0 and j == 0:
                    pref[i][j] = (grid[i-1][m-1] * pref[i-1][m-1])%mod
                else:
                    pref[i][j] = (grid[i][j-1] * pref[i][j-1])%mod

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                if i == n-1 and j == m-1:
                    continue
                if i < n-1 and j == m-1:
                    suff[i][j] = (grid[i+1][0] * suff[i+1][0])%mod
                else:
                    suff[i][j] = (grid[i][j+1] * suff[i][j+1])%mod

        for i in range(n):
            for j in range(m):
                if i == 0 and j == 0:
                    grid[i][j] = suff[i][j] % mod
                elif i == n-1 and j == m-1:
                    grid[i][j] = pref[i][j] % mod
                else:
                    grid[i][j] = (pref[i][j] * suff[i][j])%mod


        return grid