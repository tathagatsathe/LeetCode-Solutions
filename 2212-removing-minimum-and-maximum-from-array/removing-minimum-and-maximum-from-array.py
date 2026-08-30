class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_idx = max_idx = 0
        n = len(nums)

        for i, val in enumerate(nums):
            if val < nums[min_idx]:
                min_idx = i
            if val > nums[max_idx]:
                max_idx = i


        rem_max = min(n - max_idx, max_idx + 1)
        rem_min = min(n - min_idx, min_idx + 1)
        dist_betn_max_min = abs(max_idx - min_idx)

        return min(rem_max + dist_betn_max_min, rem_min + dist_betn_max_min, rem_max + rem_min)