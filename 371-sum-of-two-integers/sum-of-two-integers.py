class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32-bit bitmask to force Python to act like C++/Java
        mask = 0xFFFFFFFF
        
        # We use 'b' to represent the carry. When carry is 0, we are done.
        while b:
            # 1. Calculate sum without carry, and strictly bound it to 32 bits
            sum_without_carry = (a ^ b) & mask
            
            # 2. Calculate carry, shift left by 1, and strictly bound it to 32 bits
            carry = ((a & b) << 1) & mask
            a = sum_without_carry
            b = carry

        # 4. Handle Python's infinite precision for negative numbers at the end
        # 0x7FFFFFFF is the maximum positive 32-bit integer.
        # If 'a' is larger than this, it means the sign bit is 1 (it's a negative number).
        max_int = 0x7FFFFFFF
        
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)