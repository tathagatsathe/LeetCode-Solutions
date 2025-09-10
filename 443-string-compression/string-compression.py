class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j, n = 0, 0, len(chars)
        c = 0

        def intToArr(n):
            s = []
            while(n):
                s.append(str(n%10))
                n//=10

            return s[::-1]

        while(i<n):
            if(j<n and chars[i]==chars[j]):
                c+=1
                j+=1
            else:
                if(c!=1):
                    ch = intToArr(c)
                    i+=1
                    l = 0
                    c = 0
                    while(l<len(ch)):
                        chars[i] = ch[l]
                        l+=1
                        i+=1
                    d = j-i
                    while(d>0):
                        chars.pop(i)
                        d-=1
                        n-=1
                    j=i
                else:
                    i+=1
                    c=0

        return len(chars)