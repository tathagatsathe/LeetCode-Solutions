class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        i = 0
        l = len(tops)
        p = -1
        c=0
        t = [0]*(7)
        b = [0]*(7)

        while(i < l):
            if(tops[i]==bottoms[i]):
                p = tops[i]
                c+=1
            t[tops[i]]+=1
            b[bottoms[i]]+=1
            i+=1
        
        if(p!=-1):
            if(t[p]+b[p]==l+c):
                return min(t[p]-c,b[p]-c)
            else:
                return -1

        ans = -1
        for k in range(1,7):
            if(t[k]+b[k]==l):
                mn = min(t[k],b[k])
                if(mn<ans or ans==-1):
                    ans = mn

        return ans