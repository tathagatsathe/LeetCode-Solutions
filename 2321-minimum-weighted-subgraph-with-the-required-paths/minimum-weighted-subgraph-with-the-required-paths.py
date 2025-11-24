import heapq

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]
        for edge in edges:
            graph[edge[0]].append((edge[1], edge[2]))
            reverse_graph[edge[1]].append((edge[0], edge[2]))

        def dijkstra(src, graph):
            h = []
            heapq.heappush(h, (0, src))
            dp = [float("inf") for _ in range(n)]
            dp[src] = 0
            while h:
                dist, node = heapq.heappop(h)
                
                if dist>dp[node]:
                    continue

                dp[node] = dist
                for nei, d in graph[node]:
                    heapq.heappush(h, (dist+d, nei))

            return dp

        dp1 = dijkstra(src1, graph)
        dp2 = dijkstra(src2, graph)
        dp3 = dijkstra(dest, reverse_graph)
            
        ans = float("inf")
        for i in range(n):
            temp = dp1[i]+dp2[i]+dp3[i]
            if temp<ans:
                ans = temp

        if ans == float("inf"):
            return -1

        return ans