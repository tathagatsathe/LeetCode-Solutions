class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        graph = [[] for _ in range(n)]

        for i in range(n):
            for j in range(i+1, n):
                if i!=j and (stones[i][0]==stones[j][0] or stones[i][1]==stones[j][1]):
                    graph[i].append(j)
                    graph[j].append(i)

        visited = [False]*n
        def dfs(node):
            if visited[node]:
                return False
            visited[node] = True
            for nei in graph[node]:
                dfs(nei)

            return True

        ans = n
        for i in range(n):
            if dfs(i):
                ans-=1

        return ans