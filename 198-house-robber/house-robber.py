class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [None]*(len(nums)+2)
        def robbed(nums, i):
            if dp[i]!=None:
                return dp[i]
            if nums[i:] == []:
                dp[i] = 0
                return 0

            dp[i] = max(nums[i] + robbed(nums,i+2), robbed(nums, i+1))
            return dp[i]

        return robbed(nums, 0)
        