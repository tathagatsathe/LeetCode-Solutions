class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        ans = []
        n = len(nums)
        parent = list(range(n))
        
        def findParent(u):
            if u != parent[u]:
                return findParent(parent[u])
            return parent[u]

        def union(u, v):
            parent_u = findParent(u)
            parent_v = findParent(v)

            if parent_u != parent_v:
                parent[u] = parent_v


        for i in range(1, n):
            if abs(nums[i] - nums[i-1]) <= maxDiff:
                union(i, i-1)

        for u, v in queries:
            ans.append(parent[u] == parent[v])

        return ans