from collections import deque

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dq = deque([])
        dp = [0]*(len(s)+1)

        for i, c in enumerate(s):
            if c == "(":
                dq.append(i)
            elif c == ")" and len(dq) > 0:
                idx = dq[-1]
                dp[i] = dp[idx - 1] + (i - idx + 1)
                dq.pop()

        return max(dp)