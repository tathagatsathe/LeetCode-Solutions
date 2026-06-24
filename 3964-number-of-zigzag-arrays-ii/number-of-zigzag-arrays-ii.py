import numpy as np
import math
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        mod = 10**9 + 7
        width = r - l 
        dp = np.ones(width, dtype=object)
        I = np.array([[1 if i<= j else 0 for i in range(width)] for j in range(width)], dtype=object)
        I2 = I @ (I.T)

        def fn(n):
            # print('n: ',n)
            if n <=0:
                return np.eye(width, dtype=object)
            if n == 1:
                return I2.copy()
            
            res = I2.copy()
            l = int(math.log2(n))
            # print('l: ',l)
            for _ in range(l):
                res = (res@res) % mod
            
            temp = fn(n - 2**l)
            return (res @ temp)%mod


        In = fn(n//2)%mod
        # print('fn: ', In)


        # print('dp: ', dp)
        # print('In: ',In)
        
        if n % 2 == 1:
            In = (In @ I )%mod

        # print('In final: ',In)
        ans = (dp @ In)%mod
        
        # print('ans: ',ans)
        idx = 0
        if n % 2 == 0:
            idx = -1
        return (int(ans[idx])*2)%mod