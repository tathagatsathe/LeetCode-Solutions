import bisect
from typing import List

class SegmentTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (4 * size)

    def update(self, idx, val):
        self._update(1, 0, self.n - 1, idx, val)

    def _update(self, node, start, end, idx, val):
        if start == end:
            self.tree[node] = val
            return
        mid = (start + end) // 2
        if start <= idx <= mid:
            self._update(2 * node, start, mid, idx, val)
        else:
            self._update(2 * node + 1, mid + 1, end, idx, val)
        self.tree[node] = max(self.tree[2 * node], self.tree[2 * node + 1])

    def query(self, l, r):
        if l > r:
            return 0
        return self._query(1, 0, self.n - 1, l, r)

    def _query(self, node, start, end, l, r):
        if r < start or end < l:
            return 0
        if start >= l and end <= r:
            return self.tree[node]
        
        mid = (start + end) // 2
        p1 = self._query(2 * node, start, mid, l, r)
        p2 = self._query(2 * node + 1, mid + 1, end, l, r)
        return max(p1, p2)


class Solution:
    def getResults(self, queries: List[List[int]]) -> List[bool]:
        max_x = min(50000, 3 * len(queries)) + 1
        sgtree = SegmentTree(max_x)

        obstacles = [0, max_x] 
        ans = []
        
        for query in queries:
            if query[0] == 1:
                x = query[1]
                idx = bisect.bisect_left(obstacles, x)

                prev_obs = obstacles[idx - 1]
                next_obs = obstacles[idx]
                
                sgtree.update(x, x - prev_obs)

                if next_obs != max_x:
                    sgtree.update(next_obs, next_obs - x)
                    
                bisect.insort(obstacles, x)
                
            elif query[0] == 2:
                x, sz = query[1], query[2]
                
                idx = bisect.bisect_left(obstacles, x)
                prev_obs = obstacles[idx - 1]

                max_gap_before = sgtree.query(0, prev_obs)

                tail_gap = x - prev_obs
                
                actual_max_sz = max(max_gap_before, tail_gap)
                
                ans.append(actual_max_sz >= sz)

        return ans