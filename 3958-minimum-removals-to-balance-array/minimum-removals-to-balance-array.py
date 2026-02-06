import bisect

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        remaining = set(nums)
        ans = float("inf")

        for i in range(n):
            idx = bisect.bisect_right(nums, nums[i]*k)
            ans = min(n - (idx - i), ans)

        return 0 if ans == float("inf") else ans
        