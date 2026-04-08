class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        q = len(queries)

        for l, r, k, v in queries:
            idx = l
            for idx in range(l, r+1, k):
                nums[idx] = (nums[idx] * v) % mod

        ans = 0
        for i in range(n):
            ans = ans^nums[i]

        return ans