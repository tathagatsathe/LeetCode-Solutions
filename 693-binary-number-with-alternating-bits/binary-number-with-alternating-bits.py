class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        ans = False
        if n % 2:
            n = n>>1
        while n:
            if n % 2 == 0:
                n = n >> 1
            else:
                return False
            if n!=0 and n % 2:
                n = n >> 1
            else:
                return False

        return True
