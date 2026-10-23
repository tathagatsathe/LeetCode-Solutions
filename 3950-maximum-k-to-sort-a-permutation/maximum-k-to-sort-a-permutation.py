class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = 0

        while k < max(nums):
            k<<=1
            k+=1
        
        sorted_nums = sorted(nums)

        if sorted_nums == nums:
            return 0

        for i, num in enumerate(nums):
            if sorted_nums[i] != num:
                k = k & sorted_nums[i]

        return k