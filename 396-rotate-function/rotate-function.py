class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        S = sum(nums)

        F = sum([i*num for i, num in enumerate(nums)])
        ans = F

        for i in range(n):
            F = F + S - n*nums[-i-1]
            ans = max(ans, F)

        return ans