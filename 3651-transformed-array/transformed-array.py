class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = nums.copy()
        
        for i in range(n):
            if nums[i] != 0:
                idx = (i + nums[i]) % n
                result[i] = nums[idx]

        return result