class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums = [abs(num) for num in nums]
        nums.sort(reverse=True)
        n = len(nums)
        ans = 0
        mid = n // 2

        if n % 2 == 0:
            mid-=1

        for i in range(n):
            if i <= mid:
                ans+=nums[i]**2
            else:
                ans-=nums[i]**2

        return ans