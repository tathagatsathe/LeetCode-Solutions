class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        sum_ = odd = even = 0
        MOD = 10**9 + 7
        ans = 0

        for val in arr:
            sum_+=val
            if sum_ % 2:
                ans = (ans+1)%MOD
                odd+=1
                ans = (ans+even)%MOD
            else:
                even+=1
                ans = (ans+odd)%MOD
            
        return ans