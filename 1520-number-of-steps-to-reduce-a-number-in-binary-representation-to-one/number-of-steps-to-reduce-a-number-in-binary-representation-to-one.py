class Solution:
    def numSteps(self, s: str) -> int:
        ans = 0

        def addOne(b):
            res = ""
            carry = "1"
            n = len(b)

            for i in range(n-1,-1,-1):
                if s[i] == "1" and carry == "1":
                    res = "0" + res
                else:
                    if s[i] == "1" or carry == "1":
                        res = "1" + res
                    else:
                        res = "0" + res
                    carry = "0"

            if carry == "1":
                res = "1" + res

            return res

        while s != "1":
            if s[-1] == "1":
                s = addOne(s)
            else:
                s = s[:-1]
            ans+=1

        return ans