class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i + 1 < n:
            if nums[i+1] < nums[i]:
                break
            i+=1

        if i == n - 1:
            return True

        print(i)
        i+=1
        while i + 1 < n:
            if nums[i+1] < nums[i]:
                break
            i+=1

        print(i)

        if i == n-1 and nums[i] <= nums[0]:
            return True

        return False


        