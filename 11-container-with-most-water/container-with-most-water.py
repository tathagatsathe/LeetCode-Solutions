class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, len(height) - 1

        ans = float("-inf")

        while left < right:
            print(left, right)
            min_height = min(height[left], height[right])
            ans = max(ans, (right - left)*min_height)

            if min_height == height[left]:
                left+=1
            else:
                right-=1

        return ans