class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = 0

        for i, color in enumerate(colors):
            for j, col in enumerate(colors):
                if color != col:
                    ans = max(abs(j-i), ans)

        return ans