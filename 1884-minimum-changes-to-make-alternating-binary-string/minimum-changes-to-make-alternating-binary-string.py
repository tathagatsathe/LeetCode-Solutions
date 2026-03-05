import math

class Solution:
    def minOperations(self, s: str) -> int:
        no_of_ones_at_odd_pos = no_of_ones_at_even_pos = 0
        n = len(s)
        for i in range(n):
            if s[i] == "1":
                if i % 2:
                    no_of_ones_at_even_pos+=1
                else:
                    no_of_ones_at_odd_pos+=1

        odd = n//2
        even = n//2
        if n%2:
            odd+=1
        
        if no_of_ones_at_odd_pos > no_of_ones_at_even_pos:
            return odd - no_of_ones_at_odd_pos + no_of_ones_at_even_pos
        else:
            return even - no_of_ones_at_even_pos + no_of_ones_at_odd_pos
