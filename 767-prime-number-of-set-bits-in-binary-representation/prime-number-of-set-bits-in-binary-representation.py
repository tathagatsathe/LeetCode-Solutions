class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def noOfBits(n):
            count = 0
            while n:
                if n%2:
                    count+=1    
                n = n>>1
            return count
        
        ans = 0

        for i in range(left, right+1):
            res = noOfBits(i)
            if res in [2,3,5,7,11,13,17,19]:
                ans+=1

        return ans
        