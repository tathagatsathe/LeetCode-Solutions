class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def digitProduct(n):
            product = 1
            while n:
                product*=n%10
                n//=10
            return product
        
        while n <= 100:
            product = digitProduct(n)
            if product % t == 0:
                return n
            n+=1

        return n