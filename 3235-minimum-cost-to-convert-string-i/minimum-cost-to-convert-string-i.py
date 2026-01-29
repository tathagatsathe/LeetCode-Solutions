class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        ans = 0
        n = len(original)
        dp = [[0 if i == j else float("inf") for i in range(26)] for j in range(26)]

        def toNum(c):
            return ord(c) - ord('a')

        for i in range(n):
            dp[toNum(original[i])][toNum(changed[i])] = min(dp[toNum(original[i])][toNum(changed[i])], cost[i])

        for k in range(26):
            for i in range(26):
                for j in range(26):
                    if dp[i][k]!=float("inf") and dp[k][j]!=float("inf"):
                        dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])


        for i in range(len(source)):
            res = dp[toNum(source[i])][toNum(target[i])]
            if res == float("inf"):
                return -1
            ans+=res


        return ans