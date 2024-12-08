class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1]*(len(text2)+1) for _ in range(len(text1)+1)]

        def LCS(text1,text2, i,j,memo):
            if(i<0 or j<0):
                return 0
            if(memo[i][j]!=-1):
                return memo[i][j]
            if(text1[i]==text2[j]):
                memo[i][j] = 1 + LCS(text1, text2, i-1, j-1, memo)
            else:
                memo[i][j] = max(LCS(text1, text2, i-1,j, memo), LCS(text1, text2, i,j-1, memo))

            return memo[i][j]

        return LCS(text1, text2, len(text1)-1,len(text2)-1, memo)