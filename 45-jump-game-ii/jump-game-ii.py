class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        k = 0
        mx_idx = 1
        if(len(nums)==1):
            return ans

        while(mx_idx<len(nums)):
            # print(nums[k], mx_idx, ans, k)
            j = nums[k]
            ans+=1
            if(k+j+1>=len(nums)):
                break
            mx = k+1
            for i in range(k+1,k+j+1):
                if(nums[i]+i>=mx):
                    mx=nums[i]+i
                    mx_idx = i
                # if(nums[i]>=nums[mx_idx]):
                #     mx_idx = i
            k = mx_idx
            mx_idx = k+1
            # ans+=1

        return ans
        