class Solution:
    def minimumSteps(self, s: str) -> int:
        i=0
        c=0
        ans = 0
        while(i<len(s)):
            if(s[i]=='0'):
                ans+=i-c
                c+=1
            i+=1
        
        return ans
        