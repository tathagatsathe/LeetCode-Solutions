class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i', 'o', 'u','A','E','I', 'O', 'U']
        vowels_sequence = []

        for c in s:
            if c in vowels:
                vowels_sequence.append(c)

        vowels_sequence = vowels_sequence[::-1]

        i = 0
        ans = ""
        for c in s:
            if c in vowels:
                ans+=vowels_sequence[i]
                i+=1
            else:
                ans+=c

        return ans