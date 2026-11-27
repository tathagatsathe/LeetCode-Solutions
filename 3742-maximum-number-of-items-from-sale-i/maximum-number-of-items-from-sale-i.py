class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        free_copies = [0]*n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free_copies[i]+=1

        dp = [0] * (budget + 1)
        for i in range(n):
            cost = items[i][1]
            val = 1 + free_copies[i]

            for b in range(budget, cost - 1, -1):
                if dp[b - cost] + val > dp[b]:
                    dp[b] = dp[b - cost] + val

        min_cost = min(item[1] for item in items)
        ans = 0
        for w in range(budget + 1):
            extra_copies = (budget - w) // min_cost
            if dp[w] + extra_copies > ans:
                ans = dp[w] + extra_copies

        return ans
            