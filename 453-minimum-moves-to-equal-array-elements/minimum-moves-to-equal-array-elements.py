class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)
        max_ = nums[0]
        ans = 0
        
        for i in range(n):
            temp = max_ - nums[i]
            max_ = nums[i]
            ans+=(temp*i)

        return ans