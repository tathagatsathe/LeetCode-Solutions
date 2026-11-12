class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 1
        temp = 1
        incr = None

        for i in range(1, n):
            if nums[i] > nums[i-1]:
                if incr == None:
                    temp = 2
                elif incr:
                    temp+=1
                else:
                    temp = 2
                incr = True
            elif nums[i] < nums[i-1]:
                if incr == None:
                    temp = 2
                elif incr:
                    temp = 2
                else:
                    temp+=1
                incr = False
            else:
                temp = 1
                incr = None
            ans = max(ans, temp)

        return ans        