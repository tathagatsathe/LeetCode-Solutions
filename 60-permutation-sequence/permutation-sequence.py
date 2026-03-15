
dp = [1]*10

for i in range(1, 10):
    dp[i] = dp[i-1]*i

import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # print(dp)
        l = list(range(1,n+1))
        # print(l)
        def fn(n, k, l):
            if n == 1:
                return l[0]

            fac = dp[n-1]
            first_dig =  math.ceil(k/fac)
            place = k % fac

            first = l[first_dig - 1]
            l.remove(first)
            temp = fn(n-1, place, l)

            # print(first_dig, place)

            return str(first) + str(temp)


        ans = str(fn(n, k, l))

        return ans


