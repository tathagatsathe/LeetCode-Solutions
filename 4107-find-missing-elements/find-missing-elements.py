class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()
        ans = []
        min_, max_ = min(nums), max(nums)

        i = 0
        for val in range(min_, max_+1):
            if nums[i] != val:
                ans.append(val)
            else:
                i+=1

        return ans
