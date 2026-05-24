import heapq

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [None]*n
        h = []

        for i in range(n):
            heapq.heappush(h, (arr[i], i))

        while h:
            val, i = heapq.heappop(h)
            max_ = 0
            for k in range(max(i+1,0), min(i+d+1,n)):
                if arr[k] >= arr[i]:
                    break
                max_ = max(max_, dp[k])

            for k in range(min(i-1,n-1), max(i-d-1,-1),-1):
                if arr[k] >= arr[i]:
                    break
                max_ = max(max_, dp[k])

            dp[i] = max_ + 1

        return max(dp)
