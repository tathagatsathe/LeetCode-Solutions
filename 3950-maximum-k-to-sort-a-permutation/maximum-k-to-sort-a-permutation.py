class Solution:
    def sortPermutation(self, nums: List[int]) -> int:

        if nums[0] != 0: return 0
        k = ~ 0

        for i, num in enumerate(nums):
            if i != num:
                k = k & i

        return k if k > 0 else 0