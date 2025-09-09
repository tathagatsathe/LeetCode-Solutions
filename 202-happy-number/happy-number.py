class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()

        def intSquare(n):
            s = 0
            while(n):
                t = n%10
                n = int((n - t)/10)
                s+= t**2
            return s

        
        if(n==1):
            return True

        while(n!=1 and n not in s):
            s.add(n)
            n = intSquare(n)
            if(n==1):
                return True


        return False
            

        
        