class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n = len(digits)
        zero_count = digits.count(0)
        even_count = 0
        set_ = set()

        def fn(digits):
            two_digits = []

            for i, val in enumerate(digits):
                for j, val2 in enumerate(digits):
                    if i != j and val!=0:
                        two_digits.append(val*10 + val2)

            return two_digits

        for i, val in enumerate(digits):
            if val % 2 == 0:
                two_digit = fn(digits[:i] + digits[i+1:])
                for digit in two_digit:
                    set_.add(digit*10 + val)

        
        return len(set_)
