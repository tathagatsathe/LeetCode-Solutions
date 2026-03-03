class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def inverse(s):
            res = ""
            for i in s:
                res+= str(int(not int(i)))

            return res

        
        def fn(n):
            if n == 1:
                return "0"

            s_n_1 = fn(n-1)

            return s_n_1 + "1" + inverse(s_n_1)[::-1]


        s = fn(n)

        return s[k-1]