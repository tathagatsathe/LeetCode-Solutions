from collections import deque
class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        adj = [[] for _ in range(n)]
        indegree = [0]*n
        dp = [0]*n
        queue = deque()
        for rel in relations:
            adj[rel[0]-1].append(rel[1]-1)
            indegree[rel[1]-1]+=1

        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                dp[i] = time[i]

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                for ad in adj[node]:
                    if dp[ad] < dp[node]+ time[ad]:
                        dp[ad] = dp[node] + time[ad]
                    indegree[ad]-=1
                    if indegree[ad] == 0:
                        queue.append(ad)

        return max(dp)