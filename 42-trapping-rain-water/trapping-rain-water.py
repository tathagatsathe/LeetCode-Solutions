class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        max_height = 0

        for h in height:
            max_height = max(max_height, h)
            ans+=max_height - h

        mx_ht = 0
        for h in height[::-1]:
            mx_ht = max(mx_ht, h)
            if max_height == h:
                break
            ans = ans - (max_height - h) + (mx_ht - h)

        return ans