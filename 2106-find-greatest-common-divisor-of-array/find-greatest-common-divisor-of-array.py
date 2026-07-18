class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a, b = max(nums), min(nums)
        
        while b:
            a, b = b, a%b

        return a