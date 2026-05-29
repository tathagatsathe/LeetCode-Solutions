class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float("inf")

        for num in nums:
            sum_ = 0
            while num:
                sum_+=num%10
                num = (num - num%10)//10
            if sum_ < ans:
                ans = sum_

        return ans