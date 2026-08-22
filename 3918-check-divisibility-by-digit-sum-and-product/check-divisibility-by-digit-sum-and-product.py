class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum_ = 0
        product_ = 1
        m = n
        
        while m:
            digit = m % 10
            sum_+=digit
            product_*=digit
            m//=10

        return n%(sum_+ product_) == 0