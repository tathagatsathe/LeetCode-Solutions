class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_freq = [0]*26
        freq = [0]*26
        ans = float("inf")

        for c in "balloon":
            balloon_freq[ord(c) - ord('a')]+=1

        for c in text:
            freq[ord(c) - ord('a')]+=1

        for c in "balloon":
            ans = min(ans, freq[ord(c) - ord('a')]//balloon_freq[ord(c) - ord('a')])

        return ans
