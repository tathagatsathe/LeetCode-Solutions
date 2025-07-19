class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        nums.sort()
        s = sum(nums)
        if(s%2==1):
            return False

        s = int(s/2)
        dp = [[None]*(s+1) for _ in range(len(nums)+1)]
        i = 0
        
        def fn(nums, s, i):
            if(dp[i][s]!=None):
                return dp[i][s]
            if(s==0):
                dp[i][s] = True
                return True
            if(len(nums)==i or s<0):
                dp[i][s] = False
                return False
            s1 = fn(nums, s-nums[i], i+1)
            s2 = fn(nums, s, i+1)
            if(s1==True or s2==True):
                dp[i][s] = True
                return True
            dp[i][s] = False
            return False

        return fn(nums, s, 0)

        