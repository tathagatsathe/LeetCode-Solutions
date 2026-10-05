class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        open_ = 0

        flag = False
        for c in s:
            if c == "(":
                open_+=1
                flag = True
            else:
                if flag:
                    ans+=2**(open_ - 1)
                open_-=1
                flag = False

        return ans