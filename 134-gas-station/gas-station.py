class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        temp = [x - y for x, y in zip(gas, cost)]
        # print(temp)

        prefix = []
        suffix = []

        pre = suff = 0
        for val in temp:
            pre+=val
            prefix.append(pre)

        for val in temp[::-1]:
            pre+=val
            suffix.append(pre)

        suffix = suffix[::-1]

        # print(prefix)
        # print(suffix)
        max_idx = 0

        for i in range(n):
            if suffix[i] > suffix[max_idx]:
                max_idx = i

        return max_idx if suffix[max_idx] + prefix[max_idx-1] >= 0 else -1
        