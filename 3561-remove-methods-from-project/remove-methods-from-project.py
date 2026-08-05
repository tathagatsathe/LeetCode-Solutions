class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in invocations:
            adj[u].append(v)

        suspicious = set()

        def dfs(node):
            suspicious.add(node)
            for nei in adj[node]:
                if nei not in suspicious:
                    suspicious.add(nei)
                    dfs(nei)

        dfs(k)

        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        ans = []
        for i in range(n):
            if i not in suspicious:
                ans.append(i)

        return ans