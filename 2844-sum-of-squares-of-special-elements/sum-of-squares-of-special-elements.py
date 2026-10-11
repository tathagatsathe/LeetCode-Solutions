class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        ans = 0
        
        for i, val in enumerate(nums):
            if len(nums) % (i+1) == 0:
                ans+=val**2

        return ans