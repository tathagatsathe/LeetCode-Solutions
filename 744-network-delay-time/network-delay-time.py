import heapq
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [False]*(n+1)
        graph = [[] for _ in range(n+1)]
        for time in times:
            graph[time[0]].append((time[2], time[1]))

        h = []
        heapq.heappush(h, (0, k))
        ans = 0
        count = 0
        while h:
            dist, node = heapq.heappop(h)
            if visited[node] == True:
                continue
            visited[node] = True
            count+=1
            if dist>ans:
                ans = dist

            if count>=n:
                break

            for (ad_dist, ad) in graph[node]:
                heapq.heappush(h, (dist+ad_dist, ad))

        if count!=n:
            return -1

        return ans
