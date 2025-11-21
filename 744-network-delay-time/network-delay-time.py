import heapq
from collections import deque
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = [False]*(n+1)
        adj = [[None]*(n+1) for _ in range(n+1)]
        for time in times:
            adj[time[0]][time[1]] = time[2]

        h = []
        heapq.heappush(h, (0, k))

        ans = 0
        count = 0
        while h:
            dist, node = heapq.heappop(h)
            print('node: ', node, ' dist: ',dist)
            if visited[node] == True:
                continue
            visited[node] = True
            count+=1
            if dist>ans:
                ans = dist

            # if count >=n:
            #     break
            for i in range(1,n+1):
                if adj[node][i]!=None and visited[i]==False:
                    heapq.heappush(h, (dist+adj[node][i], i))

        print(adj)
        print(h)
        print(count)
        print(visited)
        print(ans)
        if visited[1:].count(False)>0:
            return -1

        return ans

#     1
# 1 ----- 2
#  \      |
#   \     |  2
# 1  \    |
#     \   |
#      \  |
#       \ |
#        \|
#         3


# [None, None, 1, 2]
# [None, None, None, 2]
# [None, None, None, None]