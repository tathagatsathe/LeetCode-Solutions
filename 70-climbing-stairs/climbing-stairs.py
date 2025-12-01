class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0]*(n+1)
        
        def climb(n):
            if dp[n]!=0:
                return dp[n]
            if n <= 1:
                return 1
            dp[n] = climb(n-1) + climb(n-2)
            return dp[n]

        return climb(n)
        
        