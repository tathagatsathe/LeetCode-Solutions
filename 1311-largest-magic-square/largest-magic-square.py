class Solution:
    def largestMagicSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # m, n = 50, 50
        topLeft = []
        for j in range(n, 1, -1):
            dp = [[0]*(n-j+1) for _ in range(m)]
            for i in range(m):
                temp_sum = sum(grid[i][:j])
                dp[i][0] = temp_sum
                for k in range(1,n-j+1):
                    temp_sum = temp_sum - grid[i][k-1] + grid[i][k+j-1]

                    dp[i][k] = temp_sum
                    

            
            # print(dp)
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
                        # print('k: ',k, 'i: ',i)
                        # break

        # print(topLeft)

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
                # print(j, x, temp_i)
                sum1 = 0
                sum2 = 0
                for i in range(j):
                    # print('index1: ', x+i, temp_i+i, grid[x+i][y+i])
                    # print('index2: ',x+j-i-1, y+i, grid[x+j-i-1][y+i])
                    sum1+=grid[x+i][y + i]
                    sum2+=grid[x+j-i-1][y+i]
                # print('sum1, sum2, sum_: ', sum1, sum2, sum_)
                if sum1 == sum_ and sum2 == sum_:
                    return j

                # if count == j:
                #     c = 0
                #     checkDiag = False
                #     topleft = [temp_i, k]
                #     for i in range(temp_i, temp_i+j):
                #         temp = 0
                #         for q in range(k, k+j):
                #             temp+=grid[q][i]

                #         if temp == sum_:
                #             c+=1
                #         if c == j:
                #             checkDiag = True

                #     if checkDiag:
                #         print(j, k, temp_i)
                #         sum1 = 0
                #         sum2 = 0
                #         for i in range(j):
                #             print('index1: ', k+i, temp_i+i, grid[k+i][temp_i + i])
                #             print('index2: ',k+j-i-1, temp_i+i, grid[k+j-i-1][temp_i+i])
                #             sum1+=grid[k+i][temp_i + i]
                #             sum2+=grid[k+j-i-1][temp_i+i]
                #         print('sum1, sum2, sum_: ', sum1, sum2, sum_)
                #         if sum1 == sum_ and sum2 == sum_:
                #             return j
                        
                



        # print('________________________________________')

        # for j in range(m, 1, -1):
        #     dp = [[0]*n for _ in range(m-j+1)]
        #     for i in range(n):
        #         temp_sum = 0
        #         for l in range(j):
        #             temp_sum+=grid[l][i]

        #         dp[0][i] = temp_sum
        #         for k in range(1, m-j+1):
        #             temp_sum = temp_sum - grid[k-1][i] + grid[k+j-1][i]
        #             dp[k][i] = temp_sum
            
        #     print(dp)

        return 1

# [8, 5, 9, 11]
# [7, 6, 7, 10]
# [6, 9, 7, 5]
# [3, 9, 10, 7]


# [12, 10, 15]
# [8, 12, 11]
# [10, 12, 9]
# [10, 12, 14]]