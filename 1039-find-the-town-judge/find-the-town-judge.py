class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = [0]*(n+1)
        adj = [[] for _ in range(n+1)]
        for a, b in trust:
            indegrees[b]+=1
            adj[a].append(b)

        # print(indegrees)
        for i in range(1,n+1):
            if indegrees[i] == n-1 and adj[i]==[]:
                return i

        return -1
