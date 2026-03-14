class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def fn(n):
            hs = ['a','b','c']
            if n == 1:
                return hs

            temp = fn(n-1)
            res = []
            for h in hs:
                for t in temp:
                    if t[0]!=h:
                        res.append(h+t)

            return res

        res = fn(n)

        if k > len(res):
            return ""


        return res[k-1]