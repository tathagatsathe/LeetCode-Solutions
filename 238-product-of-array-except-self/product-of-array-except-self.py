class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        mul = 1
        zeroExist= 0
        idx = 0
        for i, val in enumerate(nums):
            if(val==0):
                zeroExist+=1
                if(zeroExist == 1):
                    idx = i
            else:    
                mul*=val

        if zeroExist>1:
            return ans
        
        if zeroExist == 1:
            ans[idx] = mul
            return ans

        for i, val in enumerate(nums):
            ans[i] = int(mul/val)

        return ans

        