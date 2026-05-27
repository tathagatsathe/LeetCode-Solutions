class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        chars = set()
        ans = 0
        char_arr = [0]*26
        for w in word[::-1]:
            if ord('a') <= ord(w) <= ord('z') and w.upper() in chars and w not in chars:
                char_arr[ord(w) - ord('a')] = 1
            elif ord('A') <= ord(w) <= ord('Z') and w in chars and w.lower() in chars:
                char_arr[ord(w.lower()) - ord('a')] = 0
            chars.add(w)

        return sum(char_arr)