class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cst = []
        n = len(gas)
        sub = 0
        ans = 0
        for i in range(n):
            val = gas[i]-cost[i]
            sub+=val
            if(sub<0):
                ans=i+1
                sub = 0
            cst.append(val)

        if sum(cst)<0:
            return -1


        return ans

        
        