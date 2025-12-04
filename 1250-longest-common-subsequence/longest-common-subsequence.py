class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 1 if text1[i]==text2[j] else 0
                elif i == 0:
                    dp[i][j] = 1 if text1[i]==text2[j] else dp[i][j-1]
                elif j == 0:
                    dp[i][j] = 1 if text1[i]==text2[j] else dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] + 1 if text1[i]==text2[j] else max(dp[i][j-1],dp[i-1][j])

        return dp[m-1][n-1]