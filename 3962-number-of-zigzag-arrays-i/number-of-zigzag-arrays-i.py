class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        if n == 1:
            return (r - l + 1) % mod

        m = r - l + 1

        dp0 = [1] * m
        dp1 = [1] * m

        for i in range(2, n+1):
            next_dp0 = [0] * m
            next_dp1 = [0] * m
            
            suff_sum = 0
            for x in range(m - 1, -1, -1):
                next_dp0[x] = suff_sum
                suff_sum = (suff_sum + dp1[x]) % mod
                
            pref_sum = 0
            for x in range(m):
                next_dp1[x] = pref_sum
                pref_sum = (pref_sum + dp0[x]) % mod
                
            dp0 = next_dp0
            dp1 = next_dp1

        return (sum(dp0) + sum(dp1)) % mod