class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        def fn(nums):

            res = []
            n = len(nums)

            if n == 1:
                return [nums] 
            for i in range(n):
                temp = fn(nums[:i]+nums[i+1:])
                for t in temp:
                    res.append([nums[i]]+t)

            return res

        ans = fn(nums)

        return ans