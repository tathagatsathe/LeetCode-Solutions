class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        dp = [[[0,0]]*n for j in range(m)]

        # print(dp)

        for i in range(m):
            countX, countY = 0, 0
            for j in range(n):
                if grid[i][j] == "X":
                    countX+=1
                elif grid[i][j] == "Y":
                    countY+=1
                if i > 0:
                    dp[i][j] = [countX + dp[i-1][j][0], countY + dp[i-1][j][1]]
                else:
                    dp[i][j] = [countX, countY]

                if dp[i][j][0]!=0 and dp[i][j][0] == dp[i][j][1]:
                    ans+=1

        # print(dp)

        return ans


# [
#     [[0, 0], [0, 0], [0, 0]], 
#     [[0, 0], [0, 0], [0, 0]]
# ]

[
    [[1, 0], [1, 1], [1, 1]], 
    [[1, 1], [1, 2], [1, 2]]
]