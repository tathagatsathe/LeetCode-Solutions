class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        mirr_rotate = ['2','5','6','9']

        for num in range(1,n+1):
            mirror_digit_found = False
            invalid_digit_found = False
            for digit in str(num):
                if digit in mirr_rotate:
                    mirror_digit_found = True
                elif digit in ['3','4','7']:
                    invalid_digit_found = True
                    break
            if mirror_digit_found and invalid_digit_found == False:
                ans+=1

        return ans


