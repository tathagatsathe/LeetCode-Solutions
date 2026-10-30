import heapq

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        best_run = [float("inf")]*n
        h = [(0, 1, 0)]
        
        while h:
            weight, run, node  = heapq.heappop(h)

            if run >= best_run[node]:
                continue

            best_run[node] = run

            if node == n - 1:
                return weight
            
            for nei, wt in adj[node]:
                new_cost = weight + wt

                if labels[node] == labels[nei]:
                    new_run = run + 1
                else:
                    new_run = 1

                if new_run <= k:
                    heapq.heappush(h, (new_cost, new_run, nei))

        return -1  