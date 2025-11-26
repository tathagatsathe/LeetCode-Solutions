from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for flight in flights:
            graph[flight[0]].append((flight[1],flight[2]))

        queue = deque([(src, 0)])
        dp = [float("inf")]*n
        dp[src] = 0
        for i in range(k+1):
            for _ in range(len(queue)):
                node, curr_cost = queue.popleft()
                for j, nxt_cost in graph[node]:
                    if dp[j] > nxt_cost + curr_cost:
                        dp[j] = nxt_cost + curr_cost
                        queue.append((j, nxt_cost + curr_cost))


        return dp[dst] if dp[dst]!=float("inf") else -1