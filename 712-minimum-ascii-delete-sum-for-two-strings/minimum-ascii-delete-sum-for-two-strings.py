class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        dp = [[None]*(n+1) for _ in range(m+1)]
        def mds(i, j):
            ans = 0
            if dp[i][j]!=None:
                return dp[i][j]

            if i >= m or j >= n:
                for idx in range(i, m):
                    ans+=ord(s1[idx])
                for idx in range(j, n):
                    ans+=ord(s2[idx])
                return ans

            temp1 = mds(i+1, j) + ord(s1[i])
            temp2 = mds(i, j+1) + ord(s2[j])
            temp3 = mds(i+1, j+1)

            if s1[i] != s2[j]:
                temp3+=ord(s1[i]) + ord(s2[j])

            dp[i][j] = min(temp1, min(temp2, temp3))
            return dp[i][j]


        return mds(0, 0)