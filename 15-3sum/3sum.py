from bisect import bisect_left

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()

        if(nums[0]==0 and nums[0]==nums[-1]):
            return [[0,0,0]]

        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while(j<k):
                s = nums[i]+nums[j]+nums[k]
                temp = [nums[i],nums[j],nums[k]]
                if(s==0):
                    ans.append(temp)
                    j+=1
                    k-=1
                elif(s<0):
                    j+=1
                else:
                    k-=1

        i = 1
        ans.sort()
        while(i<len(ans)):
            if(ans[i-1]==ans[i]):
                ans.pop(i)
            else:
                i+=1
        
        return ans

            
        
        