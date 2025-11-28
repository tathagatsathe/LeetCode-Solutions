class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {}
        for i in range(n):
            if nums[i] not in mp:
                mp[nums[i]] = []
            mp[nums[i]].append(i)

        for key in mp:
            m = len(mp[key])
            j = 1
            while j<m:
                if abs(mp[key][j] - mp[key][j-1])<=k:
                    return True
                j+=1
            

        return False