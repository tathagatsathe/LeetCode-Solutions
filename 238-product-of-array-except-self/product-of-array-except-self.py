class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        mul = 1
        zeroCount= 0
        idx = 0
        for i, val in enumerate(nums):
            if(val==0):
                zeroCount+=1
                idx = i
                if(zeroCount>1):
                    return [0]*n
            else:    
                mul*=val

        # if zeroCount == 1:
        #     ans[idx] = mul
        #     return ans

        for i, val in enumerate(nums):
            if(zeroCount>0):
                if(val!=0):
                    ans.append(0)
                else:
                    ans.append(mul)
            else:
                ans.append(mul//val)

        return ans

        