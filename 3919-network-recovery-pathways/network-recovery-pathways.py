import heapq
from typing import List

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        adj = [[] for _ in range(n)]
        
        max_cost = -1
        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                if cost > max_cost:
                    max_cost = cost
                    
        if max_cost == -1:
            return -1

        def check(mid: int) -> bool:
            dist = [float('inf')] * n
            dist[0] = 0
            
            pq = [(0, 0)] 
            
            while pq:
                d, u = heapq.heappop(pq)
                
                if d > k:
                    return False
                    
                if u == n - 1:
                    return True
                    
                if dist[u] < d:
                    continue
                    
                for v, w in adj[u]:
                    if w < mid:
                        continue
                        
                    if d + w < dist[v] and d + w <= k:
                        dist[v] = d + w
                        heapq.heappush(pq, (dist[v], v))
                        
            return False

        left, right = 0, max_cost
        ans = -1
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(mid):
                ans = mid      
                left = mid + 1  
            else:
                right = mid - 1
                
        return ans