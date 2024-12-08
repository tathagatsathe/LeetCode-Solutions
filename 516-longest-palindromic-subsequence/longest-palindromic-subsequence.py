class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0]*(len(s)) for _ in range(len(s))]
        reverse_s = s[::-1]

        for i in range(len(s)):
            for j in range(len(s)):
                if((i==0 or j==0) and s[i]==reverse_s[j]):
                    dp[i][j] = 1
                    continue
                if(s[i]==reverse_s[j]):
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[len(s)-1][len(s)-1]
        