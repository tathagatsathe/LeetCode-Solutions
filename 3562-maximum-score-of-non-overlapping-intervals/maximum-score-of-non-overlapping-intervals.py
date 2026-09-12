from typing import List
import bisect

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        arr = sorted((l, r, w, i) for i, (l, r, w) in enumerate(intervals))
        
        start_times = [x[0] for x in arr]
        
        next_valid = [bisect.bisect_right(start_times, x[1]) for x in arr]
        
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            w = arr[i][2]
            idx = arr[i][3]
            nxt_j = next_valid[i]
            
            dp_i = dp[i]
            dp_next = dp[i + 1]
            dp_jump = dp[nxt_j]
            
            for k in range(1, 5):
                skip_w, skip_idx = dp_next[k]
                
                jump_w, jump_idx = dp_jump[k - 1]
                pick_w = w + jump_w
                
                if pick_w > skip_w:
                    dp_i[k] = (pick_w, sorted(jump_idx + [idx]))
                elif pick_w < skip_w:
                    dp_i[k] = (skip_w, skip_idx)
                else:
                    pick_idx = sorted(jump_idx + [idx])
                    if pick_idx < skip_idx:
                        dp_i[k] = (pick_w, pick_idx)
                    else:
                        dp_i[k] = (skip_w, skip_idx)
                        
        return dp[0][4][1]

