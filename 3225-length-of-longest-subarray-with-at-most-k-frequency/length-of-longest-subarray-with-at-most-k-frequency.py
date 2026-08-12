class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        start = 0
        end = None
        for num in nums:
            freq[num] = 0

        freq[nums[0]] = 1
        n = len(nums)
        ans = 1

        for i in range(1, n):
            freq[nums[i]]+=1
            ans = max(i-start, ans)
            while start < i and freq[nums[i]] > k:
                freq[nums[start]]-=1
                start+=1

        ans = max(n-start, ans)
        
        return ans