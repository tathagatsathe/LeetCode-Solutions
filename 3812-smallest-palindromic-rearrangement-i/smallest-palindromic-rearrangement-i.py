class Solution:
    def smallestPalindrome(self, s: str) -> str:
        char_count = [0]*26

        for c in s:
            char_count[ord(c) - ord('a')]+=1

        ans = []
        odd_char_string = []

        for i in range(26):
            if char_count[i] == 1 :
                odd_char_string.append(chr(i+ord('a')))
            else:
                ans.append(chr(i+ord('a'))*(char_count[i]//2))
                if char_count[i]%2 == 1:
                    odd_char_string.append(chr(i+ord('a')))

        ans = "".join(ans) + "".join(odd_char_string) + "".join(ans[::-1])

        return ans