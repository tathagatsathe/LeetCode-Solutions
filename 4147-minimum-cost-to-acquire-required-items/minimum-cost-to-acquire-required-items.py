class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        
        cost = min(need1, need2)*costBoth + (need2-need1)*cost2
        if need1 > need2:
            cost = min(need1, need2)*costBoth + (need1-need2)*cost1
            
        return min(need1*cost1 + need2*cost2, max(need1, need2)*costBoth, cost)