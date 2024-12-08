class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*(len(s)+1) for _ in range(len(s)+1)]
        revese_s = s[::-1]

        for i in range(len(s)):
            for j in range(len(s)):
                if(s[i]==revese_s[j]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(s)-1][len(s)-1]
        