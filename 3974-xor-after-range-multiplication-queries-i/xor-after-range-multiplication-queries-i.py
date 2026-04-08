class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(nums)
        q = len(queries)

        for i in range(q):
            l, r, k, v = queries[i]
            idx = l
            while idx <= r:
                nums[idx] = (nums[idx] * v) % mod
                idx+=k


        ans = 0
        for i in range(n):
            ans = ans^nums[i]

        return ans