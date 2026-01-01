class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        quotient = 1
        while i>=0:
            if digits[i] + quotient <= 9:
                digits[i]+=1
                return digits
            else:
                digits[i] = 0
                quotient = 1
            i-=1

        return [1] + digits