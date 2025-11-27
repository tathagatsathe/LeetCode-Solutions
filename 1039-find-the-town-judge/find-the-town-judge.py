class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees = [[0]*2 for _ in range(n+1)]
        adj = [[] for _ in range(n+1)]
        for a, b in trust:
            indegrees[b][0]+=1
            indegrees[a][1]+=1

        for i in range(1,n+1):
            if indegrees[i][0] == n-1 and indegrees[i][1]==0:
                return i

        return -1
