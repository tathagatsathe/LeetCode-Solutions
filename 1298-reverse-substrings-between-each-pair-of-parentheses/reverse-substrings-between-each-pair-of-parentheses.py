from collections import deque
class Solution:
    def reverseParentheses(self, s: str) -> str:
        dq = deque([])
        ans = ""

        for c in s:
            if c != ")":
                dq.append(c)
            else:
                temp = []
                while dq[-1]!='(':
                    temp.append(dq.pop())
                dq.pop()
                dq.extend(temp)

        ans = "".join(dq)
        
        return ans
        