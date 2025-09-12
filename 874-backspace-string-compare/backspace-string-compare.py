class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i = len(s) - 1
        c = 0
        while(i>=0):
            if(s[i]=='#'):
                s = s[:i]+s[i+1:]
                c+=1
            elif(c!=0):
                s = s[:i]+s[i+1:]
                c-=1
            i-=1

        i = len(t) - 1
        c=0
        while(i>=0):
            if(t[i]=='#'):
                t = t[:i]+t[i+1:]
                c+=1
            elif(c!=0):
                t = t[:i]+t[i+1:]
                c-=1
            i-=1
            

        return s == t
        