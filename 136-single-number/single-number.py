class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        ans = nums[0]

        for num in nums[1:]:
            ans = ans ^ num

        return ans