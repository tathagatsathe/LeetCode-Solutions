class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        ans = ""

        for word in words:
            wt = 0
            for c in word:
                wt+=weights[ord(c) - ord('a')]

            wt = wt%26
            ans+=chr(ord('z') - wt)

        return ans