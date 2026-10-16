from typing import List

class SegmentTree:
    def __init__(self, n: int):
        self.n = n
        self.tree_sq = [0] * (4 * n)
        self.tree_sum = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        self.MOD = 10**9 + 7

    def _apply(self, node: int, length: int, val: int):
        self.tree_sq[node] = (self.tree_sq[node] + 2 * val * self.tree_sum[node] + val * val * length) % self.MOD
        self.tree_sum[node] = (self.tree_sum[node] + val * length) % self.MOD
        self.lazy[node] = (self.lazy[node] + val) % self.MOD

    def _push_down(self, node: int, left: int, right: int):
        if self.lazy[node] != 0:
            mid = (left + right) // 2
            self._apply(node * 2, mid - left + 1, self.lazy[node])
            self._apply(node * 2 + 1, right - mid, self.lazy[node])
            self.lazy[node] = 0

    def update(self, node: int, left: int, right: int, q_left: int, q_right: int, val: int):
        if q_left > right or q_right < left:
            return
            
        if q_left <= left and right <= q_right:
            self._apply(node, right - left + 1, val)
            return

        self._push_down(node, left, right)
        mid = (left + right) // 2
        
        self.update(node * 2, left, mid, q_left, q_right, val)
        self.update(node * 2 + 1, mid + 1, right, q_left, q_right, val)
        
        self.tree_sq[node] = (self.tree_sq[node * 2] + self.tree_sq[node * 2 + 1]) % self.MOD
        self.tree_sum[node] = (self.tree_sum[node * 2] + self.tree_sum[node * 2 + 1]) % self.MOD

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        
        seg_tree = SegmentTree(n)
        last_seen = {}
        
        total_ans = 0
        
        for i in range(n):
            start_idx = last_seen.get(nums[i], -1) + 1
            
            seg_tree.update(1, 0, n - 1, start_idx, i, 1)
            
            total_ans = (total_ans + seg_tree.tree_sq[1]) % MOD
            
            last_seen[nums[i]] = i
            
        return total_ans