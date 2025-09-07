class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        ans = min(height[i],height[j])*(j-i)

        while(i+1<=j):
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
            temp = min(height[i], height[j])*(j-i)
            if(temp>ans):
                ans = temp

        return ans

        