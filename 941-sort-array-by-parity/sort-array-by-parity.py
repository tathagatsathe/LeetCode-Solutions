class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i=0
        n = len(nums)

        while(i<n):
            if(nums[i]%2==1):
                nums.append(nums[i])
                nums.pop(i)
                n-=1
            else:
                i+=1

        return nums
        