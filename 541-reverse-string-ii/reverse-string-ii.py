class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        i=0
        while(i*k<len(s)):
            s = s[:i*k] + s[i*k:i*k + k][::-1] + s[i*k+k:]
            i+=2

        return s
        