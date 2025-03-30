class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.strip().split(" ")
        ans = ""
        for i in range(len(t)-1,-1,-1):
            if(t[i]!=""):
                ans+=t[i] + " "
        
        return ans.strip()
        