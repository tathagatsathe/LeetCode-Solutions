class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_ = max(nums)
        return sum([(max_ - num) for num in nums])
        