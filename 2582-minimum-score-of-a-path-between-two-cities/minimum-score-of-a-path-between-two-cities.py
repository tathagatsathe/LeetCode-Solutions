from collections import deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = float("inf")
        adj = [[] for _ in range(n+1)]

        for x, y, dist in roads:
            adj[x].append((y, dist))
            adj[y].append((x, dist))

        visited = [False]*(n+1)

        dq = deque([1])
        visited[1] = True

        while dq:
            node = dq.popleft()
            for i, ad in adj[node]:
                if not visited[i]:
                    dq.append(i)
                    visited[i] = True
                ans = min(ans, ad)

        return ans

