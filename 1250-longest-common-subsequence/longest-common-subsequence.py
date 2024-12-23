class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*len(text2) for _ in range(len(text1))]

        def LCS(text1, text2, i, j):
            if (i<0 or j<0):
                return 0
            if(memo[i][j] !=-1):
                return memo[i][j]
                
            if(text1[i]==text2[j]):
                memo[i][j] =  1 + LCS(text1, text2, i-1, j-1)
            else:
                memo[i][j] =  max(LCS(text1,text2, i-1, j), LCS(text1, text2, i, j-1))

            return memo[i][j]

        return LCS(text1, text2, len(text1)-1, len(text2)-1)


