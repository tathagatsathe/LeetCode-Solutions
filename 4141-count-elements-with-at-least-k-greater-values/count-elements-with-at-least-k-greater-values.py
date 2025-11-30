class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        ans = 0
        i = 0
        if k==0:
            return n

        while i<n:
            j=i+1
            while j<n and nums[j]==nums[i]:
                j+=1
            greater = n - j
            if j<n and greater>=k:
                ans+=j-i
            i = j
                
        return ans