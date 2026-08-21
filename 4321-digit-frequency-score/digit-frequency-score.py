class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        freq = {}

        while n:
            rem = n%10
            if rem not in freq:
                freq[rem] = 0
            freq[rem]+=1
            n//=10
        
        ans = 0

        for d, val in freq.items():
            ans+=(d*val)

        return ans