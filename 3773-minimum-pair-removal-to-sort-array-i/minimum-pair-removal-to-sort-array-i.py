class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while len(nums)>1:
            res = []
            minimum = float("inf")
            idx = -1
            nonDecreasing = True
            for i in range(1,len(nums)):
                if nums[i-1]>nums[i]:
                    nonDecreasing = False
                if nums[i-1]+nums[i]<minimum:
                    minimum = nums[i-1]+nums[i]
                    idx = i-1

            if nonDecreasing == False:
                nums[idx] = nums[idx] + nums[idx+1]
                del nums[idx+1]
                ans+=1
            else:
                break

        return ans