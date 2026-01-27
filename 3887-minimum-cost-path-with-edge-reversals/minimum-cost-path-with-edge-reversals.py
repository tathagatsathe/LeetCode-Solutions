from collections import deque

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        dist = [float("inf")]*n
        adj = [[] for _ in range(n)]

        for i, j, cost in edges:
            adj[i].append((j, cost))
            adj[j].append((i, 2*cost))

        node = 0
        cost = 0
        dist[node] = 0

        queue = []
        heapq.heappush(queue, [cost, node])

        while queue:
            cost, node = heapq.heappop(queue)
            if cost > dist[node]:
                continue

            if node == n - 1:
                return cost

            for next_node, cost_to_node in adj[node]:
                if cost_to_node + cost < dist[next_node]:
                    dist[next_node] = cost_to_node + cost
                    heapq.heappush(queue, [cost + cost_to_node, next_node])
            

        return -1