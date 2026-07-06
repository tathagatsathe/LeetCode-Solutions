class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n < 2:
            return max(nums)

        prev2, prev1 = nums[0], nums[1]

        for i in range(2, n):
            curr = max(prev2 + nums[i], prev1)
            prev2, prev1 = max(prev1, prev2), curr

        return max(prev1, prev2)
        