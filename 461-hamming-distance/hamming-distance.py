class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = 0
        x, y = bin(x)[2:], bin(y)[2:]
        m, n = len(x), len(y)
        l = max(m, n)
        x, y = "0"*(l-m) + x, "0"*(l-n) + y

        for i in range(l):
            if x[i] != y[i]:
                ans+=1

        return ans