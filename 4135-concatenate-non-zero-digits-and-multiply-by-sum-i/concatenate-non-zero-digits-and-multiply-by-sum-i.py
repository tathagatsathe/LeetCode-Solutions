class Solution:
    def sumAndMultiply(self, n: int) -> int:
        s = ""
        sum = 0
        while n!=0:
            temp = n%10
            n = n//10
            sum+=temp
            s = (str(temp) if temp!=0 else "") + s

        non_zero_number = int(s) if s!="" else 0

        return non_zero_number * sum
        