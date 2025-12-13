import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        h = []
        dp = [0]*(ord('z') - ord('0') + 1)
        for i in s:
            dp[ord(i)-ord('0')]+=1

        for i in range(len(dp)):
            if dp[i]!=0:
                heapq.heappush(h, [-dp[i], chr(i+ord('0'))])

        ans = ""
        while h:
            freq, ch = heapq.heappop(h)
            ans+=(ch*(-freq))

        return ans

