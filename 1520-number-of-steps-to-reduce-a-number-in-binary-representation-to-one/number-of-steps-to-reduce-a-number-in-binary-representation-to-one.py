class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0

        def binaryToDecimal(s):
            res = 0
            n = len(s)
            for i in range(n):
                res+=int(s[i])*2**(n-i-1)

            return res

        n = binaryToDecimal(s)


        while n!=1:
            if n%2:
                n+=1
            else:
                n//=2

            ans+=1

        return ans