from collections import deque

class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = [0]*(n+1)
        prefix[0] = 0
        ans = n+1

        for i in range(n):
            prefix[i+1] = prefix[i]+nums[i]

        dq = deque()

        for j in range(n+1):
            while dq and prefix[j] - prefix[dq[0]] >=k:
                ans = min(ans, j - dq[0])
                dq.popleft()

            while dq and prefix[j] <= prefix[dq[-1]]:
                dq.pop()
        
            dq.append(j)

        return ans if ans <= n else -1
            
