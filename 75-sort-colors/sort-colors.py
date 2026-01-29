class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r, w, b = 0, 0, 0

        for num in nums:
            if num == 0:
                r+=1
            elif num == 1:
                w+=1
            else:
                b+=1

        for i in range(len(nums)):
            if r!=0:
                nums[i] = 0
                r-=1
            elif w!=0:
                nums[i] = 1
                w-=1
            else:
                nums[i] = 2
                b-=1

        return nums