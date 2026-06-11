from collections import deque

class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = 10**9 + 7
        n = len(edges) + 1
        visited = [False]*(n+1)
        adj = [[] for _ in range(n+1)]

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        d = 2**-2

        dq = deque([1])

        while dq:
            d = (d*2)%mod
            for _ in range(len(dq)):
                nd = dq.popleft()
                if visited[nd] == False:
                    visited[nd] = True
                    for ad in adj[nd]:
                        if visited[ad]==False:
                            dq.append(ad)
            

        return int(d)