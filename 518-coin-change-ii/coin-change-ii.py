class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[None]*(amount+1) for _ in range(n+1)]
        
        def dfs(amount, i):
            if amount < 0 or i >= n:
                return 0
            if amount == 0:
                return 1

            if dp[i][amount] != None:
                return dp[i][amount]

            dp[i][amount] = dfs(amount - coins[i], i) + dfs(amount, i+1)

            return dp[i][amount]
            

        return dfs(amount, 0)
