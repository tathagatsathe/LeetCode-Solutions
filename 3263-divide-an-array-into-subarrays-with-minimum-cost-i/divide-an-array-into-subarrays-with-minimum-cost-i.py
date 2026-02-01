class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        ans = nums[0]
        nums = nums[1:]
        nums.sort()
        ans+=sum(nums[:2])
        
        return ans
