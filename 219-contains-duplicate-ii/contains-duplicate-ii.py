class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        mp = {}
        i = 0
        s = set()
        while i<n and i<=k:
            if nums[i] in s:
                return True
            s.add(nums[i])
            i+=1

        i=0

        while i+k+1<n:
            s.remove(nums[i])

            if nums[i+k+1] in s:
                return True
            s.add(nums[i+k+1])
            i+=1  

        return False
