class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ans = []
        n = len(nums)
        parent = [0]*n

        for i in range(1, n):
            if abs(nums[i] - nums[i-1]) <= maxDiff:
                parent[i] = parent[i-1]
            else:
                parent[i] = parent[i-1] + 1

        for u, v in queries:
            ans.append(parent[u] == parent[v])

        return ans