class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        mp = {}
        ans = float("inf")

        for i in range(n):
            x = int(str(nums[i])[::-1])
            y = int(str(nums[i]))

            if y in mp:
                ans = min(ans, i - mp[y])
            mp[x] = i

        return -1 if ans == float("inf") else ans
        