import heapq
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)
        cost = [0] * (n - x + 1)
        
        low, high = [], []
        sum_low, sum_high = 0, 0
        size_low, size_high = 0, 0
        
        removed = [False] * n
        in_low = [False] * n 
        
        def prune_low():
            while low and removed[low[0][1]]:
                heapq.heappop(low)
                
        def prune_high():
            while high and removed[high[0][1]]:
                heapq.heappop(high)
                
        def balance():
            nonlocal sum_low, sum_high, size_low, size_high
            while size_low > size_high + 1:
                prune_low()
                val, idx = heapq.heappop(low)
                val = -val 
                
                sum_low -= val
                sum_high += val
                size_low -= 1
                size_high += 1
                
                in_low[idx] = False
                heapq.heappush(high, (val, idx))
                
            while size_low < size_high:
                prune_high()
                val, idx = heapq.heappop(high)
                
                sum_high -= val
                sum_low += val
                size_high -= 1
                size_low += 1
                
                in_low[idx] = True
                heapq.heappush(low, (-val, idx))

        def insert(in_val: int, in_idx: int):
            nonlocal sum_low, sum_high, size_low, size_high
            prune_low()
            prune_high()
            
            if low and in_val <= -low[0][0]:
                heapq.heappush(low, (-in_val, in_idx))
                sum_low += in_val
                size_low += 1
                in_low[in_idx] = True
            elif high and in_val >= high[0][0]:
                heapq.heappush(high, (in_val, in_idx))
                sum_high += in_val
                size_high += 1
                in_low[in_idx] = False
            else:
                heapq.heappush(low, (-in_val, in_idx))
                sum_low += in_val
                size_low += 1
                in_low[in_idx] = True

        for i in range(x):
            insert(nums[i], i)
            balance()
            
        prune_low()
        median = -low[0][0]
        cost[0] = (sum_high - sum_low) + median * (size_low - size_high)
        
        for i in range(x, n):
            out_idx = i - x
            out_val = nums[out_idx]
            removed[out_idx] = True
            
            if in_low[out_idx]:
                sum_low -= out_val
                size_low -= 1
            else:
                sum_high -= out_val
                size_high -= 1
                
            insert(nums[i], i)
            balance()
            
            prune_low()
            median = -low[0][0]
            cost[i - x + 1] = (sum_high - sum_low) + median * (size_low - size_high)

        dp_states = [[float('inf')] * (k + 1) for _ in range(n + 1)]
        for i in range(n + 1):
            dp_states[i][0] = 0
            
        for i in range(n):
            for j in range(k + 1):
                if dp_states[i][j] < dp_states[i + 1][j]:
                    dp_states[i + 1][j] = dp_states[i][j]
                    
            if i + x <= n:
                for j in range(1, k + 1):
                    if dp_states[i][j - 1] != float('inf'):
                        if dp_states[i][j - 1] + cost[i] < dp_states[i + x][j]:
                            dp_states[i + x][j] = dp_states[i][j - 1] + cost[i]
                        
        return dp_states[n][k]