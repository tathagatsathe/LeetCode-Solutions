class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        preSum = [0]*n
        prefixGcd = [1]*n
        mx = nums[0]

        def gcd(a, b):
            if a > b:
                a, b = b, a
            while a:
                a, b = b%a, a
            return b

        for i in range(n):
            mx = max(mx, nums[i])
            prefixGcd[i] = gcd(mx, nums[i])
        

        prefixGcd.sort(reverse=True)
        pairsGcd = [0]*(n//2)

        for i in range(n//2):
            pairsGcd[i] = gcd(prefixGcd[i], prefixGcd[n-1-i])

        return sum(pairsGcd)



