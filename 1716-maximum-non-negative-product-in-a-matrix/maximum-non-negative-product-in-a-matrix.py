class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        dp = [[[0,0]]*n for _ in range(m)]
        zero = False
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zero = True
                min_, max_ = 0, 0
                temp = None
                if i==0 and j == 0:
                    if grid[i][j] > 0:
                        max_ = grid[i][j]
                    else:
                        min_ = abs(grid[i][j])
                elif i == 0 and j > 0:
                    if grid[i][j] < 0:
                        max_ = dp[i][j-1][0]*abs(grid[i][j])
                        min_ = dp[i][j-1][1]*abs(grid[i][j])
                    else:
                        min_ = dp[i][j-1][0]*grid[i][j]
                        max_ = dp[i][j-1][1]*grid[i][j]
                elif j == 0 and i > 0:
                    if grid[i][j] < 0:
                        max_ = dp[i-1][j][0]*abs(grid[i][j])
                        min_ = dp[i-1][j][1]*abs(grid[i][j])
                    else:
                        min_ = dp[i-1][j][0]*grid[i][j]
                        max_ = dp[i-1][j][1]*grid[i][j]
                elif i > 0 and j > 0:
                    if grid[i][j] < 0:
                        max_ = max(dp[i-1][j][0], dp[i][j-1][0]) * abs(grid[i][j])
                        min_ = max(dp[i-1][j][1], dp[i][j-1][1]) * abs(grid[i][j])
                    else:
                        max_ = max(dp[i-1][j][1], dp[i][j-1][1]) * abs(grid[i][j])
                        min_ = max(dp[i-1][j][0], dp[i][j-1][0]) * abs(grid[i][j])

                dp[i][j] = [min_, max_]
            


        if zero == False and dp[m-1][n-1][1] == 0:
            return -1

        return dp[m-1][n-1][1] % mod

            
# class Solution:
#     def maxProductPath(self, grid: List[List[int]]) -> int:
#         m, n = len(grid), len(grid[0])
#         mod = 10**9 + 7
#         dp = [[[0,0]]*n for _ in range(m)]
#         zero = False
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j] == 0:
#                     zero = True
#                 min_, max_ = None, None

#                 if i==0 and j == 0:
#                     if grid[i][j] > 0:
#                         max_ = grid[i][j]
#                     else:
#                         min_ = abs(grid[i][j])
#                 elif i == 0 and j > 0:
#                     if grid[i][j] < 0:
#                         if dp[i][j-1][0] != None:
#                             max_ = dp[i][j-1][0]*abs(grid[i][j]) % mod
#                         if dp[i][j-1][1] != None:
#                             min_ = dp[i][j-1][1]*abs(grid[i][j]) % mod
#                     else:
#                         if dp[i][j-1][0] != None:
#                             min_ = dp[i][j-1][0]*grid[i][j] % mod
#                         if dp[i][j-1][1] != None:
#                             max_ = dp[i][j-1][1]*grid[i][j] % mod
#                 elif j == 0 and i > 0:
#                     if grid[i][j] < 0:
#                         if dp[i-1][j][0] != None:
#                             max_ = dp[i-1][j][0]*abs(grid[i][j]) % mod
#                         if dp[i-1][j][1] != None:
#                             min_ = dp[i-1][j][1]*abs(grid[i][j]) % mod
#                     else:
#                         if dp[i-1][j][0] != None:
#                             min_ = dp[i-1][j][0]*grid[i][j] % mod
#                         if dp[i-1][j][1] != None:
#                             max_ = dp[i-1][j][1]*grid[i][j] % mod
#                 elif i > 0 and j > 0:
#                     if grid[i][j] < 0:
#                         if dp[i-1][j][0] != None and dp[i][j-1][0] != None:
#                             max_ = max(dp[i-1][j][0], dp[i][j-1][0]) * abs(grid[i][j]) % mod
#                         elif dp[i-1][j][0] != None:
#                             max_ = dp[i-1][j][0] * abs(grid[i][j]) % mod
#                         elif dp[i][j-1][0] != None:
#                             max_ = dp[i][j-1][0] * abs(grid[i][j]) % mod

#                         if dp[i-1][j][1] !=None and dp[i][j-1][1] != None:
#                             min_ = max(dp[i-1][j][1], dp[i][j-1][1]) * abs(grid[i][j]) % mod
#                         elif dp[i][j-1][1] != None:
#                             min_ = dp[i][j-1][1] * abs(grid[i][j]) % mod
#                         elif dp[i-1][j][1] != None:
#                             min_ = dp[i-1][j][1] * abs(grid[i][j]) % mod
#                     else:
#                         if dp[i-1][j][1] !=None and dp[i][j-1][1] != None:
#                             max_ = max(dp[i-1][j][1], dp[i][j-1][1]) * abs(grid[i][j]) % mod
#                         elif dp[i][j-1][1] != None:
#                             max_ = dp[i][j-1][1] * abs(grid[i][j]) % mod
#                         elif dp[i-1][j][1] != None:
#                             max_ = dp[i-1][j][1] * abs(grid[i][j]) % mod

#                         if dp[i-1][j][0] !=None and dp[i][j-1][0] != None:
#                             min_ = max(dp[i-1][j][0], dp[i][j-1][0]) * abs(grid[i][j]) % mod
#                         elif dp[i][j-1][0] != None:
#                             min_ = dp[i][j-1][0] * abs(grid[i][j]) % mod
#                         elif dp[i-1][j][0] != None:
#                             min_ = dp[i-1][j][0] * abs(grid[i][j]) % mod

#                 dp[i][j] = [min_, max_]
            
#         print(dp)

#         if dp[m-1][n-1][1] == None:
#             return -1

#         return dp[m-1][n-1][1] % mod

            