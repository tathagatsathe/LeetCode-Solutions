class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        s = (total+target)

        if abs(target)>total or s%2:
            return 0

        s //=2
        dp = [0]*(s+1)
        dp[0] = 1
        for num in nums:
            for i in range(s,num-1,-1):
                dp[i]+=dp[i-num]

        return dp[s]
        