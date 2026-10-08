class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l = 0
        open_ = 0

        ans = ""

        for i in range(len(s)):
            if s[i] == "(":
                open_+=1
            else:
                open_-=1
            if open_ == 0:
                ans+=s[l+1:i]
                l = i+1

        return ans