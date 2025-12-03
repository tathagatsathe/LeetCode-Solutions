class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        n = len(nums)
        if s%2!=0:
            return False

        s = s//2
        dp = [[None]*(s+1) for _ in range(n+1)]
        def fn(i, s):
            if i>=n:
                return False

            if s == 0:
                return True
            if dp[i][s]!=None:
                return dp[i][s]
            temp = fn(i+1, s-nums[i])
            if temp:
                dp[i][s] = temp
                return True
            temp2 = fn(i+1, s)
            if temp2:
                dp[i][s] = True
                return True
            dp[i][s] = False
            return False

        return fn(0, s)

