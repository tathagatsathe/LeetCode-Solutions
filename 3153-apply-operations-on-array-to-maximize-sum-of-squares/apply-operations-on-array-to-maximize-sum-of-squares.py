class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        mod = 10**9 + 7
        bits_counts = [0]*32
        ans = 0

        for num in nums:
            for i in range(32):
                if (num >> i) & 1:
                    bits_counts[i]+=1

        for _ in range(k):
            current_num = 0

            for i in range(32):
                if bits_counts[i] > 0:
                    current_num+=(1<<i)
                    bits_counts[i]-=1

            ans=(ans+current_num**2)%mod

        return ans
