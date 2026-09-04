class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        prefix, suffix = [], []

        max_ = float("-inf")
        for val in nums:
            max_ = max(max_, val)
            prefix.append(max_)

        min_ = float("inf")

        ans = -1
        n = len(nums)

        for i, val in enumerate(nums[::-1]):
            min_ = min(min_, val)
            prefix[n - 1 -i] = prefix[n - 1 -i] - min_

            if prefix[n - 1 -i] <= k:
                ans = n - 1 - i

        return ans

        