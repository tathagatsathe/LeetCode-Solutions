class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if(sum(gas)<sum(cost)):
            return -1
        n = len(gas)
        sub = 0
        ans = 0
        for i in range(n):
            val = gas[i]-cost[i]
            sub+=val
            if(sub<0):
                ans=i+1
                sub = 0

        return ans

        
        