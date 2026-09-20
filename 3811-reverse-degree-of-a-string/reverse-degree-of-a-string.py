class Solution:
    def reverseDegree(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans+=(i+1)*(26 - (ord(s[i]) - ord('a')))

        return ans