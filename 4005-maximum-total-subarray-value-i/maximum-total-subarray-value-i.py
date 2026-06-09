class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max_, min_ = max(nums), min(nums)
        return k*(max_ - min_)