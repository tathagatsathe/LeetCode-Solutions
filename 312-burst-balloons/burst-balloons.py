class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = [[0]*n for _ in range(n)]
        ans = 0
        for l in range(1, n):
            for s in range(n-l):
                i = s
                j = l + s
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j] + nums[i]*nums[k]*nums[j])

        return dp[0][n-1]