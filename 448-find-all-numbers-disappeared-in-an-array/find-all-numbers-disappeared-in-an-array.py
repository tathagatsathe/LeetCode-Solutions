class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        n = len(nums)
        l = [None]*n

        for i in range(n):
            l[nums[i]-1] = nums[i]

        for i in range(n):
            if l[i] == None:
                ans.append(i+1)

        return ans