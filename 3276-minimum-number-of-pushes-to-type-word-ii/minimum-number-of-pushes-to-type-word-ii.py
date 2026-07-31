class Solution:
    def minimumPushes(self, word: str) -> int:
        char_set = set()
        ans = 0

        freq = [0]*26
        for c in word:
            freq[ord(c) - ord('a')]+=1

        freq.sort(reverse=True)

        for i in range(26):
            if freq[i] == 0:
                break
            if i < 8:
                ans+=freq[i]
            elif i < 16:
                ans+=2*freq[i]
            elif i < 24:
                ans+=3*freq[i]
            else:
                ans+=4*freq[i]

        return ans
