class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        if m == 0 or n == 0:
            return max(m, n)
        dp = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = 0 if word1[i] == word2[j] else 1
                elif i == 0:
                    dp[i][j] = j if word1[i] == word2[j] else dp[i][j-1]+1
                elif j == 0:
                    dp[i][j] = i if word1[i] == word2[j] else dp[i-1][j]+1
                else:
                    dp[i][j] = dp[i-1][j-1] if word1[i] == word2[j] else min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1]))+1


        return dp[m-1][n-1]