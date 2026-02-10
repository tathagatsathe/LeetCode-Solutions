class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        for i in range(n):
            odd = set()
            even = set()
            for j in range(i, n):
                if nums[j] % 2:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])
                
                if len(odd) == len(even) and (j-i+1) > ans:
                    ans = j-i+1

        return ans