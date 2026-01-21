class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            if num%2:
                r = 0
                temp = num
                while temp % 2:
                    r+=1
                    temp = temp >> 1
                ans.append(num - 2**(r - 1))
            else:
                ans.append(-1)

        return ans