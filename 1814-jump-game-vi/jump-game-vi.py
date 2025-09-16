from collections import deque
import heapq

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        heap = []
        n = len(nums)
        dp = [0]*n
        i=1
        dp[0] = nums[0]
        heapq.heappush(heap, (-dp[0], 0))
        while(i<n):
            dp[i] = nums[i] - heap[0][0]
            while(heap and heap[0][1]<=i-k):
                heapq.heappop(heap)
            
            heapq.heappush(heap, (-dp[i], i))
            i+=1

        return dp[n-1]