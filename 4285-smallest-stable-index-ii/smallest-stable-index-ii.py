class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        instability_score = []

        max_ = float("-inf")
        for val in nums:
            max_ = max(max_, val)
            instability_score.append(max_)

        n = len(nums)
        min_ = float("inf")
        ans = -1

        for i in range(n-1, -1, -1):
            min_ = min(min_, nums[i])
            instability_score[i] = instability_score[i] - min_
            if instability_score[i] <= k:
                ans = i

        return ans