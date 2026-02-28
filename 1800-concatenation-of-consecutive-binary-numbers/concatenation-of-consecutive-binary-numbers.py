class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = 10**9 + 7
        def addOne(s):
            carry = "1"
            res = ""
            n = len(s)
            for i in range(n-1,-1,-1):
                if s[i] == "1" and carry == "1":
                    res = "0" + res
                    carry = "1"
                else:
                    if s[i]=="1" or carry == "1":
                        res = "1" + res
                    else:
                        res = "0" + res
                    carry = "0"

            if carry == "1":
                res = "1" + res

            return res

        ans = 0

        def fn(n):
            if n == 1:
                return "1", 1

            binary, dec = fn(n-1)

            b = addOne(binary)

            return b, ((dec*2**len(b))%modulo + n)%modulo

        b, ans = fn(n)

        return ans