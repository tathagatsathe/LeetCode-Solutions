class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        max_ = nums[-1]
        return sum([(max_ - num) for num in nums])
        