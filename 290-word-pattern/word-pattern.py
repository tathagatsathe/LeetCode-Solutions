class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        mp1 = {}
        mp2 = {}
        n = len(pattern)
        s = s.split(" ")

        if len(s) != len(pattern):
            return False
            
        for i in range(n):
            if pattern[i] not in mp1:
                mp1[pattern[i]] = s[i]
            elif mp1[pattern[i]]!=s[i]:
                print(mp1, s[i])
                return False

            if s[i] not in mp2:
                mp2[s[i]] = pattern[i]
            elif mp2[s[i]]!=pattern[i]:
                return False

        for k in mp1:
            if mp2[mp1[k]]!=k:
                return False

        return True