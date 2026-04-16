import bisect

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        q = len(queries)
        ans = [-1]*q
        mp = {}
        for i in range(n):
            if nums[i] not in mp:
                mp[nums[i]] = []
            mp[nums[i]].append(i)

        for j in range(q):
            if len(mp[nums[queries[j]]]) > 1:
                idx = bisect.bisect_left(mp[nums[queries[j]]], queries[j])
                m = len(mp[nums[queries[j]]])
                x = abs(mp[nums[queries[j]]][(idx+1)%m] - mp[nums[queries[j]]][idx])
                y = abs(mp[nums[queries[j]]][idx] - mp[nums[queries[j]]][(m+idx-1)%m])

                if idx == m - 1:
                    x = n - mp[nums[queries[j]]][idx] + mp[nums[queries[j]]][0]
                if idx == 0:
                    y = n - mp[nums[queries[j]]][-1] + mp[nums[queries[j]]][idx]

                ans[j] = min(x, y)
                
        return ans
