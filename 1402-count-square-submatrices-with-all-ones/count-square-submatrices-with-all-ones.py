class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[matrix[i][j] for j in range(n)] for i in range(m)]
        ans = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if (i == 0 or j == 0):
                        ans+=1
                    else:
                        dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                        ans+=dp[i][j]
        
        return ans