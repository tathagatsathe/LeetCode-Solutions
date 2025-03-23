class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = 0
        k = 0
        mx_idx = 1

        while(mx_idx<len(nums)):
            j = nums[k]
            ans+=1
            if(k+j+1>=len(nums)):
                break
            mx = k+1
            for i in range(k+1,k+j+1):
                if(nums[i]+i>=mx):
                    mx=nums[i]+i
                    mx_idx = i
            k = mx_idx
            mx_idx = k+1

        return ans
        