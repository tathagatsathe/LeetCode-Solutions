class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def fn(nums):
            res = []
            n = len(nums)
            if n == 0:
                return [[]]

            for i in range(n):
                temp = fn(nums[:i] + nums[i+1:])
                for t in temp:
                    res.append([nums[i]] + t)

            return res

        res = fn(nums)
        res.sort()

        ans = []
        for r in res:
            if r not in ans:
                ans.append(r)

        return ans