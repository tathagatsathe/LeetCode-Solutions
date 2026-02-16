class Solution:
    def reverseBits(self, n: int) -> int:
        
        def toBinary(n):
            res = ""
            while n:
                res= str(n%2) + res
                n//=2

            res = "0"*(32-len(res)) + res
            return res

        def toDecimal(b):
            res = 0
            for i in range(len(b)):
                res+=int(b[i])*2**i

            return res

        binary = toBinary(n)
        res = toDecimal(binary)
        return res