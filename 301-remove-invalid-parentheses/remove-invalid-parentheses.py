class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        min_removals = 0
        open_ = 0

        for c in s:
            if c == "(":
                open_+=1
            elif c == ")":
                if open_ == 0:
                    min_removals+=1
                else:
                    open_-=1
        
        min_removals+=open_

        n = len(s)
        ans = []

        def fn(st, i, removals_count, open_):
            nonlocal ans

            if i == n and removals_count == 0 and open_ == 0:
                ans.append(st)

            if open_ < 0 or i == n:
                return

            new_open_ = open_
            if s[i] == "(":
                new_open_+=1
            if s[i] == ")":
                new_open_-=1


            fn(st + s[i], i+1, removals_count, new_open_)
            if removals_count > 0:
                if s[i] == "(":
                    fn(st, i+1, removals_count-1, open_)
                if s[i] == ")":
                    fn(st, i+1, removals_count-1, open_)

        fn("", 0, min_removals, 0)


        ans = list(set(ans))

        return ans

    