class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()

        res = []

        for i in range(n-2):
            left = i+1
            right = n - 1

            while left < right:
                sum_ = nums[i] + nums[left] + nums[right]
                if sum_ == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                elif sum_ < 0:
                    left+=1
                else:
                    right-=1

        res.sort()
        ans = []
        for i in range(len(res)):
            if ans == [] or ans[-1] != res[i]:
                ans.append(res[i])

        return ans
