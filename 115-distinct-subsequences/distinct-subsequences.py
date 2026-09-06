class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ans = 0
        n = len(s)
        m = len(t)
        dp = [[None]*(m+1) for _ in range(n+1)]

        def fn(i, j):
            nonlocal ans

            if j >= m:
                return 1
            
            if i >= n:
                return 0

            if dp[i][j] != None:
                return dp[i][j]

            a = 0
            if s[i] == t[j]:
                a = fn(i+1, j+1)
            b = fn(i+1, j)

            dp[i][j] = a + b

            return a + b

        ans = fn(0, 0)

        return ans