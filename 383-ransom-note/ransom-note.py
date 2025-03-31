class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        h = {}
        for m in magazine:
            if m not in h.keys():
                h[m]=0
            h[m]+=1

        for r in ransomNote:
            if r not in h.keys():
                return False
            h[r]-=1
            if(h[r]<0):
                return False

        return True
        