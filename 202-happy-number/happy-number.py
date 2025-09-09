class Solution:
    def isHappy(self, n: int) -> bool:
        
        def intSquare(n):
            s = 0
            while(n):
                t = n%10
                n = int((n - t)/10)
                s+= t**2
            return s

        if(n==1):
            return True

        slow, fast = n, intSquare(n)

        while(fast!=1 and slow!=fast):
            slow = intSquare(slow)
            fast = intSquare(intSquare(fast))


        return fast==1
            

        
        