class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            
        s_vals = [1 << (ord(c) - ord('a')) for c in s]
        
        timer = 0
        tin = [0] * n
        tout = [0] * n
        up = [[0] * 17 for _ in range(n)]
        initial_mask = [0] * n
        
        stack = [(0, 0, 0)] 
        while stack:
            u, p, state = stack.pop()
            
            if state == 0:
                timer += 1
                tin[u] = timer
                up[u][0] = p
                
                for i in range(1, 17):
                    up[u][i] = up[up[u][i-1]][i-1]
                
                if u == 0:
                    initial_mask[u] = s_vals[0]
                else:
                    initial_mask[u] = initial_mask[p] ^ s_vals[u]
                    
                stack.append((u, p, 1))
                
                for v in adj[u]:
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer
                
        def is_ancestor(u: int, v: int) -> bool:
            return tin[u] <= tin[v] and tout[u] >= tout[v]

        def get_lca(u: int, v: int) -> int:
            if is_ancestor(u, v): return u
            if is_ancestor(v, u): return v
            for i in range(16, -1, -1):
                if not is_ancestor(up[u][i], v):
                    u = up[u][i]
            return up[u][0]
            
        bit = [0] * (n + 2)
        
        def update_bit(idx: int, val: int):
            while idx <= n:
                bit[idx] ^= val
                idx += idx & -idx
                
        def query_bit(idx: int) -> int:
            res = 0
            while idx > 0:
                res ^= bit[idx]
                idx -= idx & -idx
            return res

        ans = []
        for q in queries:
            parts = q.split()
            if parts[0] == "update":
                u = int(parts[1])
                new_char_val = 1 << (ord(parts[2]) - ord('a'))
                
                if s_vals[u] != new_char_val:
                    delta = s_vals[u] ^ new_char_val
                    s_vals[u] = new_char_val
                    
                    update_bit(tin[u], delta)
                    update_bit(tout[u] + 1, delta)
            else:
                u, v = int(parts[1]), int(parts[2])
                lca = get_lca(u, v)
                
                mask_u = initial_mask[u] ^ query_bit(tin[u])
                mask_v = initial_mask[v] ^ query_bit(tin[v])
                
                path_mask = mask_u ^ mask_v ^ s_vals[lca]
                
                ans.append((path_mask & (path_mask - 1)) == 0)
                
        return ans