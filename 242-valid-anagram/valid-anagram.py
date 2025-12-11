class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = [0]*26

        for i in s:
            mp[ord(i) - ord('a')]+=1

        for i in t:
            mp[ord(i) - ord('a')]-=1

        for i in range(26):
            if mp[i] != 0:
                return False
                
        return True