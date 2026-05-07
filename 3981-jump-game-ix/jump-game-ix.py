import heapq
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)
        max_ = nums.copy()
        min_ = nums.copy()

        mx = nums[0]
        for i in range(1,n):
            mx = max(mx,max_[i])
            max_[i] = mx

        mn = nums[-1]

        for i in range(n-2, -1, -1):
            mn = min(mn, min_[i])
            min_[i] = mn

        # print(max_)
        # print(min_)

        mx = max_[n-1]
        mn = min_[n-1]
        dp = [0]*n
        dp[n-1] = mx

        for i in range(n-2, -1, -1):
            if max_[i] <= min_[i+1]:
                # mn = min_[i]
                mx = max_[i]
            dp[i] = mx

        # print(dp)


        return dp

