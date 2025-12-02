class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)
        coins.sort(reverse=True)
        dp = {}
        dp = [[None]*(amount+1) for _ in range(n+1)]
        def fn(coins, i, amount):
            if amount == 0:
                return 0
            if amount < 0 or i>=n:
                return -1

            if dp[i][amount]!=None:
                return dp[i][amount]
            # print('i: ',i,' amount: ',amount)
            while i<n and coins[i]>amount:
                i+=1
            if i>=n:
                return -1
            temp1 = fn(coins, i, amount - coins[i])
            temp2 = fn(coins, i+1, amount)
            # print('i: ',i,' amount: ',amount, ' temp1: ',temp1, ' temp2: ',temp2)
            ans = 0
            if temp1!=-1 and temp2!=-1:
                ans = min(temp1+1, temp2)
            elif temp2 !=-1:
                ans = temp2
            elif temp1 !=-1:
                ans = temp1+1
            else:
                ans = temp1

            dp[i][amount] = ans 
            return dp[i][amount]

        return fn(coins, 0, amount)
                

            