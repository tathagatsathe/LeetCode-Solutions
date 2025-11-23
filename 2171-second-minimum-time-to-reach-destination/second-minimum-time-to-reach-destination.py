import heapq

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = [[] for _ in range(n)]

        for i, j in edges:
            graph[i-1].append(j-1)
            graph[j-1].append(i-1)

        dp = [[float("inf")]*2 for _ in range(n)]
        dp[0][0] = 0
        h = []
        heapq.heappush(h, (0, 0))
        
        while h:
            t, node = heapq.heappop(h)

            next_t = t

            if (next_t//change)%2 == 1:
                next_t = (next_t//change + 1)*change

            next_t+=time

            for g in graph[node]:
                if next_t<dp[g][0]:
                    dp[g][1] = dp[g][0]
                    dp[g][0] = next_t
                    heapq.heappush(h, (next_t, g))
                elif dp[g][1] > next_t > dp[g][0]:
                    dp[g][1] = next_t
                    heapq.heappush(h, (next_t, g))


        return dp[n-1][1]
        