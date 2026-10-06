class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        ans = 0
        open_ = 0

        for c in s:
            if c == "(":
                open_+=1
            else:
                if open_ == 0:
                    ans+=1
                else:
                    open_-=1

        return ans + open_    