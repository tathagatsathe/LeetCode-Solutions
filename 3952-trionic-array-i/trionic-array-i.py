class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        increasing1 = False
        decreasing = False
        increasing2 = False

        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i-1]:
                return False
            if increasing1 == False:
                if nums[i] > nums[i-1]:
                    increasing1 = True
                else:
                    return False
            elif increasing1 == True:
                if decreasing == False:
                    if nums[i] < nums[i-1]:
                        decreasing = True
                else:
                    if nums[i] > nums[i-1]:
                        increasing2 = True
                    elif increasing2 == True:
                        return False

        return increasing1 and increasing2 and decreasing