class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0]*(len(text2)) for _ in range(len(text1))]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if((i==0 or j==0) and text1[i]==text2[j]):
                    dp[i][j]=1
                    continue
                if(text1[i]==text2[j]):
                    dp[i][j] = 1+dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
                
        return dp[len(text1)-1][len(text2)-1]
