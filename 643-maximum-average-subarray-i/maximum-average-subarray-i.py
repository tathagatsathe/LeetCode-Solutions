class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i=0
        s = 0
        while(i<k):
            s+=nums[i]
            i+=1

        ans = s/k
        j=0
        while(i<len(nums)):
            s = s - nums[j] + nums[i]
            avg = s/k
            if(ans<avg):
                ans = avg

            i+=1
            j+=1

        return ans