class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        ans = []
        targetCount = 0
        lessThanTargetCount = 0

        for i, val in enumerate(nums):
            if val < target:
                lessThanTargetCount+=1
            if val == target:
                targetCount+=1

        return list(range(lessThanTargetCount, lessThanTargetCount + targetCount))