import heapq

class Solution:
    def frequencySort(self, s: str) -> str:
        mp = {}
        for i in s:
            if i not in mp:
                mp[i] = 0
            mp[i]+=1

        h = []
        for k in mp:
            heapq.heappush(h, [-mp[k],k])

        ans = ""
        while h:
            freq, ch = heapq.heappop(h)
            ans+=(ch*(-freq))

        return ans

