class Solution:
    def minInsertions(self, s: str) -> int:
        open_ = 0
        ans = 0
        i = 0
        n = len(s)

        while i < n:
            if s[i] == "(":
                open_+=1
            else:
                if open_ == 0:
                    if i+1 < n and s[i] == s[i+1] == ")":
                        ans+=1
                        i+=1
                    else:
                        ans+=2
                elif i == n-1:
                    ans+=1
                    open_-=1
                else:
                    if i+1 < n and s[i] == s[i+1] == ")":
                        i+=1
                        open_-=1
                    elif i+1 < n and s[i] != s[i+1] and s[i] == ")":
                        ans+=1
                        open_-=1
            i+=1

        return ans + 2*open_