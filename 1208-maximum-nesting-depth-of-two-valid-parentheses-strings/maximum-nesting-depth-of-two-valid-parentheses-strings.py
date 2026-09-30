class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        open_ = 0
        ans = []

        for s in seq:
            if s == "(":
                open_+=1
                if open_ % 2:
                    ans.append(1)
                else:
                    ans.append(0)
            elif s == ")":
                open_-=1
                if open_ % 2:
                    ans.append(0)
                else:
                    ans.append(1)

        return ans

