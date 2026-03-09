class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)

        def fn(nums):
            ans = []
            n = len(nums)
            if n == 0:
                return [[]]

            for i in range(n):
                temp = fn(nums[i+1:])
                # print('temp: ',temp)
                ans.extend(temp)
                for t in temp:
                    ans.append([nums[i]]+t)

            # print(nums, ans)
            return ans


        temp = fn(nums)

        temp.sort()

        # print(temp)
        ans = []

        for i in temp:
            t = sorted(i)
            if t not in ans:
                ans.append(t)
        
        return ans