class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def countWaves(num, tight=True):
            memo = {}
            num = str(num)

            def dp(idx, tight, leadingZero, lastDigit, secondLastDigit):

                if idx == len(num):
                    return 0

                state = (idx, tight, leadingZero, lastDigit, secondLastDigit)
                if state in memo:
                    return memo[state]

                limit = int(num[idx]) if tight else 9
                ans = 0

                for digit in range(limit+1):
                    nextTight = tight and digit == limit

                    if leadingZero:
                        if digit == 0:
                            ans+=dp(idx+1, nextTight, True, None, None)
                        else:
                            ans+=dp(idx+1, nextTight, False, digit, None)
                    else:
                        if secondLastDigit is None:
                            ans+=dp(idx+1, nextTight, False, digit, lastDigit)
                        else:
                            if (secondLastDigit > lastDigit < digit or secondLastDigit < lastDigit > digit):
                                ans+=combinations(idx+1, nextTight)
                            ans+=dp(idx+1, nextTight, False, digit, lastDigit)

                memo[state] = ans

                return ans


            comb_memo = {}

            def combinations(idx, tight):
                if idx == len(num):
                    return 1
                if (idx, tight) in comb_memo:
                    return comb_memo[(idx, tight)]

                limit = int(num[idx]) if tight else 9
                res = 0
                for digit in range(limit+1):
                    res+=combinations(idx+1, tight and digit == limit)

                comb_memo[(idx, tight)] = res
                return res

            return dp(0, True, True, None, None)

        return countWaves(num2) - countWaves(num1-1)