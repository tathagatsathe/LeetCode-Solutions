class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ans = 0
        n = len(s)
        m = len(t)
        dp = [[0]*(m) for _ in range(n)]


        dp[0][0] = 1 if s[0] == t[0] else 0

        for i in range(1, n):
            dp[i][0] = dp[i-1][0]
            if s[i] == t[0]:
                dp[i][0]+=1

        for i in range(1, n):
            for j in range(1, m):
                if j > i:
                    continue
                if s[i] == t[j]:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

        
        return dp[-1][-1]