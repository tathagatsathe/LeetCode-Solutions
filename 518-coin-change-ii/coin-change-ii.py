class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[None]*(amount+1) for _ in range(n+1)]

        def fn(i, amount):
            if amount<0 or i>=n:
                return 0
            if amount == 0:
                return 1
            if dp[i][amount]!=None:
                return dp[i][amount]

            dp[i][amount] = fn(i, amount-coins[i]) + fn(i+1, amount)

            return dp[i][amount]

        ans = fn(0, amount)

        return ans

        