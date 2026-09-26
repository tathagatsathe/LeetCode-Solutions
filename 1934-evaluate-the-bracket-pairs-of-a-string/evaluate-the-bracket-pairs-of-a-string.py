class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        dict_ = {}

        for key, val in knowledge:
            dict_[key] = val

        for key, val in dict_.items():
            s = s.replace('(' + key + ')', val)


        if '(' in s:
            res = []
            closed = True
            for c in s:
                if c == '(':
                    closed = False
                if closed:
                    res.append(c)
                if c == ')':
                    res.append('?')
                    closed = True

            s = "".join(res)

        return s