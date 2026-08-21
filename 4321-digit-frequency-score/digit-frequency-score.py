class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        ans = 0
        while n:
            rem = n%10
            ans+=rem
            n//=10
        
        return ans