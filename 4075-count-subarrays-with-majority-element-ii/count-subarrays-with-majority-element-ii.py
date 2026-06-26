from sortedcontainers import SortedList
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        pref = [0]*(n+1)
        count = 0
        
        for i in range(1,n+1):
            temp = -1
            if nums[i-1] == target:
                temp=1
            pref[i] = pref[i-1] + temp

        sl = SortedList()
        
        for val in pref:
            ans += sl.bisect_left(val)
            sl.add(val)

        return ans