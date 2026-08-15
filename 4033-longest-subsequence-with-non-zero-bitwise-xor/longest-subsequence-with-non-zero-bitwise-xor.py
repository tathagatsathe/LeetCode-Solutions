class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        xor = 0
        n = len(nums)

        if sum(nums) == 0:
            return 0

        for num in nums:
            xor^=num

        if xor:
            return n

        return n - 1