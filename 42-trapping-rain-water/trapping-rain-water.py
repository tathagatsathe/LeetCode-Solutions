class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        m = height[0]
        tr = 0
        for h in height:
            if(h<m):
                tr += (m - h)
            elif(h>=m):
                ans+=tr
                tr=0
            m = max(h,m)

        tr = 0
        m = height[-1]
        for h in height[::-1]:
            if(h<m):
                tr += (m - h)
            elif(h>m):
                ans+=tr
                tr=0
            m = max(h,m)


        return ans
