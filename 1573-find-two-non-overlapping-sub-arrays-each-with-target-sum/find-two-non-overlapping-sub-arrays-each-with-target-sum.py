class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        prefix_sums = {0: -1}
        current_sum = 0
        n = len(arr)
        min_len_at = [float('inf')] * n
        min_so_far = float('inf')
        ans = float('inf')
        
        for i, val in enumerate(arr):
            current_sum += val
            if current_sum - target in prefix_sums:
                start = prefix_sums[current_sum - target]
                curr_len = i - start
                if start >= 0:
                    ans = min(ans, curr_len + min_len_at[start])
                min_so_far = min(min_so_far, curr_len)
            min_len_at[i] = min_so_far
            prefix_sums[current_sum] = i
            
        return ans if ans != float('inf') else -1