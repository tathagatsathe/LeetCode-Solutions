from collections import deque, Counter
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        no_of_colors = len(set(colors))
        color_dict = {}
        idx = 0
        for color in colors:
            if color not in color_dict:
                color_dict[color] = idx
                idx+=1

        n = len(colors)
        dp = [[0]*no_of_colors for _ in range(n)]
        adj = [[] for _ in range(n)]
        indegree = [0]*n
        visited = [0]*n

        for v in edges:
            adj[v[0]].append(v[1])
            indegree[v[1]]+=1

        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][color_dict[colors[i]]]+=1

        if len(queue) == 0:
            return -1

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited[node] = 2
                for ad in adj[node]:
                    if visited[ad] == 2:
                        return -1
                    for j in range(no_of_colors):
                        if j == color_dict[colors[ad]]:
                            if dp[ad][j]>dp[node][j]:
                                continue
                            else:
                                dp[ad][j] = dp[node][j] + 1
                        else:                          
                            dp[ad][j] = max(dp[node][j], dp[ad][j])

                    indegree[ad]-=1
                    visited[ad] = 1
                    if indegree[ad] == 0:
                        queue.append(ad)

        if sum(indegree)>0:
            return -1
        mx = 0
        idx = 0

        for i in range(n):
            for j in range(no_of_colors):
                if dp[i][j]>mx:
                    mx = dp[i][j]
                    idx = j


        return mx