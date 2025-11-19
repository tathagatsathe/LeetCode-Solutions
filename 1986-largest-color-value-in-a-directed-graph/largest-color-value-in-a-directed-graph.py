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

        # print(color_dict)

        n = len(colors)
        dp = [[0]*no_of_colors for _ in range(n)]
        adj = [[] for _ in range(n)]
        indegree = [0]*n
        visited = [0]*n

        for v in edges:
            adj[v[0]].append(v[1])
            indegree[v[1]]+=1

        # print('indegree: ',indegree)
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i][color_dict[colors[i]]]+=1

        # print('dp: ',dp)
        if len(queue) == 0:
            return -1

        # print('queue: ',queue)
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited[node] = 2
                # print('inside loop: ',adj[node], node)
                for ad in adj[node]:
                    if visited[ad] == 2:
                        return -1
                    # if visited[ad] != 1:
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

            # print(queue,'__________')
            # print('DP: ',node, dp)
        
        # print('indegree: ',indegree)
        # print('dp: ',dp)
        # print('adj: ',adj)
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

# [1, 0, 0, 0] 0
# [2, 0, 0, 0] 1
# [1, 1, 0, 0] 2
# [2, 1, 0, 0] 3
# [2, 1, 1, 0] 4
# [2, 2, 0, 0] 5
# [3, 2, 0, 0] 6
# [3, 3, 0, 0] 7
# [3, 3, 0, 3] 8
# [3, 3, 0, 4] 9

# [1, 0, 0, 0] 0
# [2, 0, 0, 0] 1
# [1, 1, 0, 0] 2
# [2, 1, 0, 0] 3
# [2, 1, 1, 0] 4
# [2, 2, 0, 0] 5
# [0, 0, 0, 0] 6
# [1, 2, 0, 0] 7
# [2, 1, 0, 1] 8
# [2, 1, 0, 1] 9