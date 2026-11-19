class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        max_, min_ = max(nums), min(nums)
        min_1 = min_2 = max_1 = max_2 = None

        n = len(nums)
        nums.sort()

        for i in range(1, n):
            if min_1 == None and nums[i] > min_:
                min_1 = nums[i]
                if i+1 < n:
                    min_2 = nums[i+1]

        for i in range(n-1, -1, -1):
            if max_1 == None and nums[i] < max_:
                max_1 = nums[i]
                if i-1 >= 0:
                    max_2 = nums[i-1]

        # print(nums)
        score = float("inf")

        if nums[0] != nums[1] and nums[-1] != nums[-2]:
            score = max_1 - min_1
            if min_2 != None:
                score = min(score, max_ - min_2)
            if max_2 != None:
                score = min(score, max_2 - min_)
            return score

        lowest_1 = min_2
        highest_1 = max_2
        if nums[0] == nums[1] and nums[-1] == nums[-2]:
            return nums[-1] - nums[0]
            
        if nums[0] == nums[1]:
            lowest_1 = min_1

        if nums[-1] == nums[-2]:
            highest_1 = max_1

        score = min(max_ - lowest_1, highest_1 - min_)

    
        return score

# 1,4,5,7,8

# 8,28,42,58,75
# 28,28,42,58,58
# 42,42,42,58,75
# 8,28,42,42,42


# [1,1,1,4,4,4,5,7,8]
# [6, 14, 17, 32, 42, 46, 51, 65, 65, 87]


