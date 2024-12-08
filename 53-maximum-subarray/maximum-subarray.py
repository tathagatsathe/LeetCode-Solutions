class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float("-inf")
        m = 0

        for i in nums:
            m = max(i+m, i)
            ans = max(m, ans)

        return ans
        