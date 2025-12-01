class Solution:
    def fib(self, n: int) -> int:
        dp = [None]*(n+1)
        
        def fn(n):
            if n<=0:
                return 0
            if n == 1:
                return 1
            if dp[n]!=None:
                return dp[n]

            dp[n] = fn(n-1) + fn(n-2)

            return dp[n]

        return fn(n)
        