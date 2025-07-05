import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        r = 1
        if(dividend == 0):
            return 0
        if((dividend<0 and divisor>0) or (dividend>0 and divisor<0)):
            r = -1
        
        dividend = abs(dividend)
        divisor = abs(divisor)
        a = math.log(dividend,2) + math.log(1/divisor,2)
        # print(2**a)
        if(2**a % 1 > 0.9999999999999):
            res = math.ceil(2**a)*r
        else:
            res = math.floor(2**a)*r

        if(r==-1 and res<=-2**31):
            return -2**31
        elif(r==1 and res>2**31 - 1):
            return 2**31 - 1

        return res