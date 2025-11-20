from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n)]
        indegree = [0]*n
        dp = [float("inf")]*n
        visited = [0]*n
        for rel in relations:
            adj[rel[0]-1].append(rel[1]-1)
            indegree[rel[1]-1]+=1


        queue = deque()

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = time[i]

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                visited[node] = 2
                for ad in adj[node]:
                    if visited[ad] == 0:
                        dp[ad] = time[ad] + time[node]
                    dp[ad] = max(dp[ad], dp[node] + time[ad])
                    indegree[ad]-=1
                    if indegree[ad] == 0:
                        queue.append(ad)
                    visited[ad] = 1

        return max(dp)