class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]

        dp = [[0] * n for _ in range(n)]
        max_l = [[0] * n for _ in range(n)]
        max_r = [[0] * n for _ in range(n)]

        for i in range(n):
            max_l[i][i] = stoneValue[i]
            max_r[i][i] = stoneValue[i]

        for length in range(2, n + 1):
            m = -1
            
            for i in range(n - length + 1):
                j = i + length - 1
                
                m = max(m, i - 1)
                while m + 1 < j and get_sum(i, m + 1) <= get_sum(m + 2, j):
                    m += 1

                res = 0
                
                if m >= i:
                    res = max(res, max_l[i][m])

                if m >= i and get_sum(i, m) == get_sum(m + 1, j):
                    res = max(res, max_r[m + 1][j])
                else:
                    if m + 2 <= j:
                        res = max(res, max_r[m + 2][j])

                dp[i][j] = res
                max_l[i][j] = max(max_l[i][j - 1], get_sum(i, j) + res)
                max_r[i][j] = max(max_r[i + 1][j], get_sum(i, j) + res)

        return dp[0][n - 1]