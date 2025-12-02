class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        nums.sort()
        n = len(nums)
        dp = [None]*(n+2)

        def fn(nums, k):
            if k>=n:
                return 0

            if dp[k]!=None:
                return dp[k]
            i=k
            curr_sum = nums[i]
            while i+1<n and nums[i]==nums[i+1]:
                curr_sum+=nums[i+1]
                i+=1

            j = i
            if i+1<n and nums[i] == nums[i+1] - 1:
                j+=1
                while j+1<n and nums[j]==nums[j+1]:
                    j+=1

            dp[k] = max(curr_sum + fn(nums, j+1), fn(nums, k+1))
            return dp[k]

        return fn(nums, 0)