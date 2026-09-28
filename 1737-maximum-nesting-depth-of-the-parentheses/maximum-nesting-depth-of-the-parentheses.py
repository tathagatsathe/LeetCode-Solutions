class Solution:
    def maxDepth(self, s: str) -> int:
        open = 0
        ans = 0
        
        for c in s:
            if c == "(":
                open+=1
            elif c == ")":
                open-=1
            ans = max(ans, open)

        return ans