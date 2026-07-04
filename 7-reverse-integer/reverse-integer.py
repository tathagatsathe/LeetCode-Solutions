class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        i = 0
        while x >= 10**i:
            i+=1

        while x:
            i-=1
            digit = x % 10
            x = (x - digit)//10
            temp = digit*(10**i)
            if 2**31 - ans - sign < temp:
                return 0
            ans+=temp
            
        return ans * sign


