class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)-1
        i = n
        while(i>0 and nums[i]<=nums[i-1]):
            i-=1
            
        if(i==0):
            nums.sort()
        else:
            j = i
            mx = i
            while(j<=n):
                if(nums[j]>nums[i-1] and nums[j]<nums[mx]):
                    mx = j
                j+=1
            temp = nums[i-1]
            nums[i-1] = nums[mx]
            nums[mx] = temp
            arr = nums[i:]
            arr.sort()
            nums[i:] = arr