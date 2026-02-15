class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = a[::-1]
        b = b[::-1]

        # print(a, b)
        ans = ""
        if len(b) > len(a):
            t = a
            a = b
            b = t

        n = min(len(a), len(b))
        m = max(len(a), len(b))


        carry = "0"
        for i in range(n):
            if a[i] == "1" and b[i] == "1":
                if carry == "1":
                    temp = "1"
                else:
                    temp = "0"
                carry = "1"
            elif a[i] == "1" or b[i] == "1":
                if carry == "1":
                    temp = "0"
                    carry = "1"
                else:
                    temp = "1"
                    carry = "0"
            else:
                if carry == "1":
                    temp = "1"
                else:
                    temp = "0"
                carry = "0"
            ans= temp + ans
            # print(ans, carry)

        # print('ans: ',ans)

        for i in range(n, m):
            if a[i] == "1":
                if carry == "1":
                    temp = "0"
                    carry = "1"
                else:
                    temp = "1"
                    carry = "0"
            else:
                if carry == "1":
                    temp = "1"
                    carry = "0"
                else:
                    temp = "0"
                    carry = "0"

            ans=temp + ans

        if carry == "1":
            ans = "1" + ans

        return ans

#   11
# 010011 
# 11101
# 1001
