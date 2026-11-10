class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float("inf")]*(n+1)
        dp[0] = 0
        
        for i in range(1, n+1):
            c_i1 = c_i2 = c_i3 = float("inf")
            if i-1>=0:
                c_i1 = dp[i-1]
            if i-2>=0:
                c_i2 = dp[i-2]
            if i-3>=0:
                c_i3 = dp[i-3]
            dp[i] = costs[i-1] + min(c_i1+1, c_i2+ 4, c_i3+9)

        return dp[n]