from collections import Counter
class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 2
        freq = {}
        for c in s:
            freq[c] = 0

        n = len(s)
        left = 0
        for i in range(n):
            freq[s[i]]+=1
            ans = max(i-left, ans)
            while i<n and freq[s[i]]>2:
                freq[s[left]]-=1
                left+=1
            

        ans = max(n-left,ans)

        return ans
