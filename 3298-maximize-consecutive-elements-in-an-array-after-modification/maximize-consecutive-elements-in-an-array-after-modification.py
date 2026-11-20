class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        diff_0 = False
        diff_2 = False
        ans = 1
        curr_len = 1
        temp_len = 1

        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                curr_len+=1
                temp_len+=1
            elif nums[i] - nums[i-1] == 2:
                if diff_0 or (i >= 2 and nums[i-1] == nums[i-2]):
                    curr_len+=1
                elif diff_2:
                    curr_len = temp_len+1
                else:
                    curr_len+=1
                temp_len = 1
                diff_2 = True
                diff_0 = False
            elif nums[i] - nums[i-1] == 0:
                if diff_0 == False:
                    curr_len+=1
                diff_0 = True
            else:
                curr_len = 1
                diff_0 = False
                diff_2 = False
            ans = max(ans, curr_len)

        return ans
