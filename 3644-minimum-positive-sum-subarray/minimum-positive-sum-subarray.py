class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float("inf")
        
        for i in range(n-l+1):
            sum_ = sum(nums[i:i+l])
            if sum_ > 0:
                ans = min(ans, sum_)
            for j in range(i+l, min(i+r,n)):
                sum_+=nums[j]
                if sum_ > 0:
                    ans = min(ans, sum_)


        return -1 if ans == float("inf") else ans