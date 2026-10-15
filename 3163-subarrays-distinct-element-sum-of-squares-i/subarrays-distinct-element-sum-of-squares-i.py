class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(n):
            for j in range(n - i):
                ans+=len(set(nums[j:j+i+1]))**2
            
        return ans