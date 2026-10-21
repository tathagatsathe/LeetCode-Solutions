class Solution:
    def minOperations(self, s: str) -> int:
        sorted_s = "".join(sorted(s))

        if sorted_s == s:
            return 0

        if sorted_s[0] == s[0] or sorted_s[-1] == s[-1]:
            return 1

        if len(s) == 2 and s[1] < s[0]:
            return -1

        if sorted_s[0] not in s[:-1] and sorted_s[-1] not in s[1:]:
            return 3

        return 2