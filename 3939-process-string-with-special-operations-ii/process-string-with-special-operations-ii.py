class Solution:
    def processStr(self, s: str, k: int) -> str:
        n = len(s)
        result = ""
        l = 0
        
        for c in s:
            match c:
                case "*":
                    if l>0:
                        l-=1
                case "#":
                    l*=2
                case "%":
                    l = l
                case _:
                    l+=1

        # print('l: ',l)
        ans = "."

        if k>=l:
            return ans

        p = ""
        for c in s[::-1]:
            if c == "#":
                l//=2
                if l!=0 and k >= l:
                    k = k%l
            elif c == "%":
                k = l - k - 1
            elif c == "*":
                l+=1
            elif ord('a')<=ord(c)<=ord('z'):
                l-=1
                p+=c

            # print('k: ', k,' l:', l, ' p: ',p)
            if len(p) > 0 and k == l:
                return p[-1]

            

        return ans

# %#*

# gmgmxib