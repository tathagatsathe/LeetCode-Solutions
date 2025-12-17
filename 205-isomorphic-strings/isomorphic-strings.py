class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mp1 = {}
        mp2 = {}
        if len(s)!=len(t):
            return False
        for i in range(len(s)):
            if s[i] not in mp1:
                mp1[s[i]] = t[i]
            elif mp1[s[i]] != t[i]:
                return False
            if t[i] not in mp2:
                mp2[t[i]] = s[i]
            elif mp2[t[i]]!=s[i]:
                return False

        for k in mp1:
            if mp2[mp1[k]] != k:
                return False

        return True