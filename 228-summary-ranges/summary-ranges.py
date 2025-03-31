class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if(nums==[]):
            return []
        i=1
        prev = nums[0]
        curr = nums[0]
        while(i<len(nums)):
            if((nums[i]-nums[i-1])!=1):
                if(prev==curr):
                    ans.append(str(curr))
                else:
                    ans.append(str(prev)+"->"+str(curr))
                prev = nums[i]

            curr = nums[i]
            i+=1

        if(prev==curr):
            ans.append(str(curr))
        else:
            ans.append(str(prev)+"->"+str(curr))

        return ans
        