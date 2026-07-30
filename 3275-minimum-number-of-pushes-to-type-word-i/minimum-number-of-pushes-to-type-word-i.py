class Solution:
    def minimumPushes(self, word: str) -> int:
        char_set = set()
        ans = 0

        for c in word:
            if len(char_set) < 8:
                ans+=1
            elif len(char_set) < 16:
                ans+=2
            elif len(char_set) < 24:
                ans+=3
            else:
                ans+=4
            char_set.add(c)

        return ans