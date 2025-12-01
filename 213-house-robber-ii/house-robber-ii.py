class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        dp = [[None]*(n+2) for _ in range(2)]

        # print(dp)
        def fn(nums, i, k):
            if dp[k][i]!=None:
                return dp[k][i]
            if nums[i:]==[]:
                return 0
            dp[k][i] = max(nums[i] + fn(nums, i+2, k), fn(nums, i+1, k))
            return dp[k][i]

        return max(fn(nums[:-1], 0, 0), fn(nums[1:], 0, 1))