class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        diff_0 = False
        diff_2 = 0
        ans = 1
        curr_len = 1

        print(nums)
        temp_len = 1

        for i in range(1, n):
            if nums[i] - nums[i-1] == 1:
                curr_len+=1
                temp_len+=1
            elif nums[i] - nums[i-1] == 2:
                if diff_0 or (i >= 2 and nums[i-1] == nums[i-2]):
                    curr_len+=1
                elif diff_2 == 1:
                    curr_len = temp_len+1
                else:
                    curr_len+=1
                temp_len = 1
                diff_2 = 1
                diff_0 = False
            elif nums[i] - nums[i-1] == 0:
                if diff_0 == False:
                    curr_len+=1
                diff_0 = True
            else:
                curr_len = 1
                diff_0 = False
                diff_2 = 0
            # print(i, curr_len, )
            ans = max(ans, curr_len)

        return ans


# [1, 4, 4, 8, 10, 10, 11, 12, 12, 14, 14, 16, 17, 17, 18, 20]
# [1, 4, 4, 9, 10, 10, 11, 12, 13, 14, 15, 16, 16, 18, 19, 20]
# [8, 10, 10, 11, 12, 12, 14, 14, 16, 17, 17, 18, 20]
# [9, 10, 11, 12, 13, 12, 14, 15, 16, 17, 18, 19, 20]
        
# [1, 3, 5, 5, 7, 8, 8, 9, 9, 10, 12, 15, 18]
# []