class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = 0
        min_ = float("inf")
        for i, num in enumerate(nums):
            if nums[i] == target and abs(i - start) < min_:
                min_ = abs(i - start)
                ans = i

        return abs(ans-start)