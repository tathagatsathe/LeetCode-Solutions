class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        t = {}
        b = {}
        i = 0
        s = set()
        l = len(tops)
        p = -1
        c=0
        while(i < l):
            if tops[i] not in t:
                t[tops[i]]=0
            
            if bottoms[i] not in b:
                b[bottoms[i]] = 0

            if(tops[i]==bottoms[i]):
                p = tops[i]
                c+=1

            t[tops[i]]+=1
            b[bottoms[i]]+=1
            s.add(tops[i])
            s.add(bottoms[i])
            i+=1
        # print('p: ',p, c)
        if(p!=-1):
            if(t[p]+b[p]==l+c):
                return min(t[p]-c,b[p]-c)
            else:
                return -1

        ans = l+1
        # print('s: ',s)
        # print('t: ',t)
        # print('b: ',b)
        for k in s:
            if(k not in t):
                t[k]=0
            if(k not in b):
                b[k]=0
            if(t[k]+b[k]==l):
                mn = min(t[k],b[k])
                print('mn: ',mn,'k: ',k)
                if(mn<ans):
                    ans = mn

        if(ans==l+1):
            ans=-1
        return ans