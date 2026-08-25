class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums = set(nums)

        for i in range(1, 101):
            if k*i not in nums:
                return k*i

        return k*101