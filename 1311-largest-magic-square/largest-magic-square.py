class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        topLeft = []

        for j in range(n, 1, -1):
            dp = [[0]*(n-j+1) for _ in range(m)]
            for i in range(m):
                temp_sum = sum(grid[i][:j])
                dp[i][0] = temp_sum
                for k in range(1,n-j+1):
                    temp_sum = temp_sum - grid[i][k-1] + grid[i][k+j-1]
                    dp[i][k] = temp_sum
                    
            for k in range(m-j+1):
                count = 1
                temp_i = 0
                for i in range(len(dp[0])):
                    sum_ = dp[k][i]
                    count = 1
                    for l in range(k+1, j+k):
                        if dp[l][i] == sum_:
                            count+=1
                    temp_i = i
                    if count == j:
                        topLeft.append([k, i, j, sum_])

        for x, y, j, sum_ in topLeft:
            c = 0
            checkDiag = False
            for i in range(y, y+j):
                temp = 0
                for q in range(x, x+j):
                    temp+=grid[q][i]

                if temp == sum_:
                    c+=1
                if c == j:
                    checkDiag = True

            if checkDiag:
                sum1 = 0
                sum2 = 0
                for i in range(j):
                    sum1+=grid[x+i][y + i]
                    sum2+=grid[x+j-i-1][y+i]
                if sum1 == sum_ and sum2 == sum_:
                    return j

        return 1