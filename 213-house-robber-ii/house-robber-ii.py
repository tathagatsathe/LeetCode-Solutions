class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums)


        prev1 = max(nums[:2])
        prev2 = nums[0]
        for i in range(2, n-1):
            curr1 = max(nums[i]+prev2, prev1)
            prev2, prev1 = prev1, curr1

        temp1 = prev1
        
        prev1 = max(nums[1:3])
        prev2 = nums[1]
        for i in range(3, n):
            curr2 = max(nums[i]+prev2, prev1)
            prev2, prev1 = prev1, curr2

        return max(prev1, temp1)