from sortedcontainers import SortedList
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        ans = 0
        n = len(nums)
        
        pref = [0]*(2*n+1)
        pref[n] = 1
        pref_sum = 0
        idx = n

        for num in nums:
            if num == target:
                pref_sum+=pref[idx]
                idx+=1
            else:
                idx-=1
                pref_sum-=pref[idx]
            pref[idx]+=1
            ans+=pref_sum

        return ans