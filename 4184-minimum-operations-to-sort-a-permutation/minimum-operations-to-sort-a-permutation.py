class Solution:
    def minOperations(self, nums: List[int]) -> int:
        min_idx = 0
        n = len(nums)
        if n == 1:
            return 0

        increasing = None
        idx = None

        count_with_diff_more_than_one = 0
        if abs(nums[-1] - nums[0]) > 1:
            count_with_diff_more_than_one+=1

        for i in range(n-1):
            if abs(nums[i+1] - nums[i]) > 1:
                count_with_diff_more_than_one+=1
                if count_with_diff_more_than_one > 1:
                    return -1

        if nums[1] - nums[0] == 1:
            increasing = True
        elif nums[0] - nums[-1] == 1:
            increasing = False

        for i in range(n-1):
            if increasing and nums[i+1] - nums[i] != 1:
                idx = -1
                break
            elif increasing == False and nums[i] - nums[i+1] != 1:
                idx = -1 
                break

        if increasing != None and idx == None:
            if increasing:
                return 0
            else:
                return 1

        idx = nums.index(0)

        ans = 0
        reverse = False
        if nums[idx - 1] == 1:
            ans+=1
            reverse = True

        if reverse:
            new_idx = n - idx - 1
            return min(n - new_idx, new_idx) + 1

        return min(n - idx + 2, idx)
            

# 1,2,3,4,0
# 0,4,3,2,1
# 4,3,2,1,0
# 0,1,2,3,4


# 2,3,4,5,0,1
# 1,0,5,4,3,2
# 0,5,4,3,2,1
# 5,4,3,2,1,0
# 0,1,2,3,4,5


# 1,2,3,0
# 0,3,2,1
# 3,2,1,0
# 0,1,2,3


# 1,2,3,4,0
# 0,4,3,2,1
# 4,3,2,1,0
# 0,1,2,3,4

# 2,3,4,5,6,0,1
# 1,0,6,5,4,3,2
# 0,6,5,4,3,2,1
# 6,5,4,3,2,1,0
# 0,1,2,3,4,5,6