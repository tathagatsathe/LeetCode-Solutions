class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        if sum < 0 or sum > 9*num:
            return ""

        if sum == 0 and num > 0:
            return "0"*num

        ans = []
        for _ in range(num):
            min_digit = min(9, sum)
            ans.append(str(min_digit))
            sum-=min_digit

        return "".join(ans)
        