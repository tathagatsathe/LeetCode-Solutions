class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0
        t = 0
        while n >= 1000:
            ans+=max(0, n - 10**(15- 3*t) + 1) * (5 - t)
            if n >= 10**(15 - 3*t):
                n = 10**(15 - 3*t) - 1
            t+=1

        return ans