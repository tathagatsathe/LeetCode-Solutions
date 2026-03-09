class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()

        def fn(nums):
            ans = []
            n = len(nums)
            if n == 0:
                return [[]]

            for i in range(n):
                temp = fn(nums[i+1:])
                ans.extend(temp)
                for t in temp:
                    ans.append([nums[i]]+t)

            return ans

        temp = fn(nums)
        temp.sort()

        ans = []

        for i in temp:
            if i not in ans:
                ans.append(i)
        
        return ans