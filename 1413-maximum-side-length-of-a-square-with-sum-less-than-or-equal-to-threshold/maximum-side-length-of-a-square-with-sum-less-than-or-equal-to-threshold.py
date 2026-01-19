class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        max_size = min(m, n)
        topLeft = []
        
        for side in range(max_size, 0, -1):
            sum_ = 0
            dp = [[0]*(n-side+1) for _ in range(m-side+1)]
            for i in range(side):
                for j in range(side):
                    sum_+=mat[i][j]

            dp[0][0] = sum_

            dp = []
            for i in range(m):
                sum_ = sum(mat[i][:side])
                temp = [sum_]
                for k in range(1,n-side+1):
                    sum_ = sum_ - mat[i][k-1] + mat[i][k+side-1]
                    temp.append(sum_)

                dp.append(temp)

            temp = []

            for k in range(len(dp[0])):
                sum_=0
                for j in range(side):
                    sum_+=dp[j][k]

                if sum_<=threshold:
                    return side
                temp.append(sum_)

            DP = []
            DP.append(temp)
            
            for j in range(1, m-side+1):
                temp = []
                sum_ = dp[j-1][0]
                for k in range(len(dp[0])): 
                    sum_ = DP[j-1][k] - dp[j-1][k] + dp[j+side-1][k]
                    if sum_<=threshold:
                        return side
                    temp.append(sum_)
                    
                DP.append(temp)

        return 0

