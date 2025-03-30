class Solution:
    def convert(self, s: str, numRows: int) -> str:
        ans = ""
        n = len(s)
        r = 2*numRows - 2
        d = r
        i = 0
        if(n<=numRows or numRows==1):
            return s

        while(len(ans)<n):
            j = i
            while(j<n):
                ans+=s[j]
                nj = j + d
                if(d!=r and d>0 and nj<n):
                    ans+=s[nj]
                j+=r

            i+=1
            d-=2

        return ans