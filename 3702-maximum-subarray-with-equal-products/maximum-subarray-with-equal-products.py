class Solution:
    def maxLength(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b > a:
                a, b = b, a

            while a % b:
                a, b = b, a % b
                
            return b

        def lcm(a, b):
            divisor = gcd(a, b)
            return (a // divisor) * b

        n = len(nums)

        ans = 1

        for i in range(n):
            product = curr_gcd = curr_lcm = nums[i]
            for j in range(i+1, n):
                product*=nums[j]
                curr_gcd = gcd(curr_gcd, nums[j])
                curr_lcm = lcm(curr_lcm, nums[j])

                if product == curr_lcm * curr_gcd:
                    ans = max(j - i + 1, ans)


        return ans

