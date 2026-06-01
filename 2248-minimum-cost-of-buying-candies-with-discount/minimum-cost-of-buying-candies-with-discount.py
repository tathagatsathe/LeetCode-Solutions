class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        ans = 0

        for i in range(0,len(cost), 3):
            ans+=sum(cost[i:i+2])

        return ans