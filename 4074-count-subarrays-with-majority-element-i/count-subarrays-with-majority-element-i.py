class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        for i in range(1, n+1):
            start = 0
            end = i
            count = nums[start:end].count(target)
            if count > (i)//2:
                ans+=1
            for j in range(i, n):
                if nums[j] == target:
                    count+=1
                if nums[start] == target:
                    count-=1
                start+=1
                if count > (i)//2:
                    ans+=1
        return ans
