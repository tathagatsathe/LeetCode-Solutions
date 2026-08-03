class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        memo = {}
        n = len(stoneValue)
        dp = [None]*n

        def fn(i):
            if i >= n:
                return 0

            if dp[i]!=None:
                return dp[i]

            sum_i2 = fn(i+2)
            sum_i3 = fn(i+3)
            sum_i4 = fn(i+4)
            sum_i5 = fn(i+5)
            sum_i6 = fn(i+6)

            temp1 = stoneValue[i] + min(sum_i2, sum_i3, sum_i4)
            temp2 = temp3 = float("-inf")
            if i+1 < n:
                temp2 = stoneValue[i] + stoneValue[i+1] + min(sum_i3, sum_i4, sum_i5)
            if i+2 < n:
                temp3 = stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] + min(sum_i4, sum_i5, sum_i6)
            dp[i] = max(temp1, temp2, temp3)

            return dp[i]

        sum_ = sum(stoneValue)
        alice_score = fn(0)
        bob_score = sum_ - alice_score

        if alice_score == bob_score:
            ans = "Tie"
        elif alice_score > bob_score:
            ans = "Alice"
        else:
            ans = "Bob"

        return ans