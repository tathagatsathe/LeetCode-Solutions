class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        last_digit = n % 10

        if n == 1:
            return True

        if last_digit != 9 and last_digit != 7 and last_digit != 1 and last_digit != 3:
            return False


        no_of_digits = len(str(n))*2

        return n/3**(no_of_digits) == 1 or n/3**(no_of_digits-1) == 1
