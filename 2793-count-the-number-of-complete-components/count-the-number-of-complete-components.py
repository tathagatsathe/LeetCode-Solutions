class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = [False]*n

        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            visited[node] = True
            edges_count = len(adj[node])
            nodes_count = 1
            for ad in adj[node]:
                if visited[ad] == False:
                    nd_count, edg_count = dfs(ad)
                    edges_count+=edg_count
                    nodes_count+=nd_count

            return nodes_count, edges_count

        ans = 0

        for i in range(n):
            if visited[i] == False:
                nodes_count, edges_count = dfs(i)
                if nodes_count * (nodes_count - 1) == edges_count:
                    ans+=1

        return ans

        
