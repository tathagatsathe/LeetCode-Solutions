class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def decimal_to_base_n(num, base):
            if num == 0:
                return 0

            res = []
            while num:
                res.append(str(num % base))
                num = num // base

            return "".join(res[::-1])

        base_converted = decimal_to_base_n(8, 2)

        # print(base_converted)
                
        
        for i in range(2, n-1):
            s = decimal_to_base_n(n, i)
            # print(s)
            l = len(s)

            for j in range(l//2):
                if s[j] != s[l- j - 1]:
                    return False

        return True
