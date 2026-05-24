import heapq

class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        n = len(arr)
        dp = [None]*n
        h = []

        # print('n: ',n)

        for i in range(n):
            heapq.heappush(h, (arr[i], i))

        while h:
            val, i = heapq.heappop(h)
            # print(val, i)
            max_ = 0
            for k in range(max(i+1,0), min(i+d+1,n)):
                if arr[k] >= arr[i]:
                    break
                max_ = max(max_, dp[k])
                # print(k)
            # print('_______')

            for k in range(min(i-1,n-1), max(i-d-1,-1),-1):
                if arr[k] >= arr[i]:
                    break
                max_ = max(max_, dp[k])
                # print(k)

            dp[i] = max_ + 1
            # print('____________________________')
            
        # print(dp)
        # return 0
        return max(dp)
