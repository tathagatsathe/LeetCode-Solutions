class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        temp = 0
        ans = float("-inf")
        for num in nums:
            if num>temp+num:
                temp = num
            else:
                temp+=num
            if temp>ans:
                ans = temp

        return ans

        