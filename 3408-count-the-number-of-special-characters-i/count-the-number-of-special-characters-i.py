class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        chars = set()

        for w in word:
            if w in chars:
                continue
            if ord('a') <= ord(w) <= ord('z') and w.upper() in chars:
                ans+=1
            elif ord('A') <= ord(w) <= ord('Z') and w.lower() in chars:
                ans+=1
            chars.add(w)

        return ans