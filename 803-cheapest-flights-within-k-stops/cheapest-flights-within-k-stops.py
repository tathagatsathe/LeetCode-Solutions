import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]

        for flight in flights:
            graph[flight[0]].append((flight[1],flight[2]))

        # print('graph: ',graph)
        dp = [[float("inf")]*(k+2) for _ in range(n+1)]
        h = []
        heapq.heappush(h, (0, k+1, src))
        while h:
            cost, stops, node = heapq.heappop(h)

            if dp[node][stops]!=float("inf"):
                continue
            if node == dst:
                return cost
            dp[node][stops] = cost
            if stops <= 0:
                continue

            for nei, c in graph[node]:
                heapq.heappush(h, (c+cost, stops-1, nei))


        return -1