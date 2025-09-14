class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        i = 1
        ans = []
        c = 1
        if(k==1):
            return nums

        while(i<len(nums)):
            if(nums[i]-nums[i-1]==1):
                c+=1
            else:
                c=1
            
            if(c>=k):
                ans.append(nums[i])
            elif(c<k and i>=k-1):
                ans.append(-1)
            i+=1

        return ans