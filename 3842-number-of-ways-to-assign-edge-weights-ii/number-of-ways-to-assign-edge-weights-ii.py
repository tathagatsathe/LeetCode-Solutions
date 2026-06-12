class Solution:
    def assignEdgeWeights(self, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        mod = 10**9 + 7
        n = len(edges) + 1
        q = len(queries)
        depth = [0]*(n+1)
        ans = []

        visited = [False]*(n+1)
        adj = [[] for _ in range(n+1)]

        for x, y in edges:
            adj[x].append(y)
            adj[y].append(x)

        LOG = 18
        up = [[0]*LOG for _ in range(n+1)]

        dq = deque([1])
        visited[1] = True
        while dq:
            curr = dq.popleft()
            for neighbor in adj[curr]:
                if visited[neighbor] == False:
                    visited[neighbor] = True
                    depth[neighbor] = depth[curr] + 1
                    up[neighbor][0] = curr

                    for i in range(1, LOG):
                        parent = up[neighbor][i-1]
                        up[neighbor][i] = up[parent][i-1]

                    dq.append(neighbor)

        def get_distance(u, v):

            orig_u, orig_v = u, v

            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for i in range(LOG):
                if (diff >> i) & 1:
                    u = up[u][i]

            if u == v:
                return depth[orig_u] + depth[orig_v] - 2 * depth[u]

            for j in range(LOG - 1, -1, -1):
                if up[u][j] != up[v][j]:
                    u = up[u][j]
                    v = up[v][j]
                    
            lca = up[u][0]
            return depth[orig_u] + depth[orig_v] - 2 * depth[lca]

        no_of_edges = len(edges)

        for i in range(q):
            u, v = queries[i]

            d = get_distance(u, v)
            if d > 0:
                ans.append(pow(2, d-1, mod))
            else:
                ans.append(0)
  
        return ans