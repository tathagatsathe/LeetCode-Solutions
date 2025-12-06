class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[int(matrix[j][i]) for i in range(n)] for j in range(m)]

        # print(dp)
        v = [[0]*n for _ in range(m)]
        h = [[0]*n for _ in range(m)]

        h[0][0], v[0][0] = int(matrix[0][0]), int(matrix[0][0])
        ans = 0
        for i in range(m):
            temp = 0
            for j in range(n):
                if matrix[i][j] == "0":
                    temp = 0
                else: 
                    temp+=1
                    ans = 1
                h[i][j] = temp

        for j in range(n):
            temp = 0
            for i in range(m):
                if matrix[i][j] == "0":
                    temp = 0
                else: 
                    temp+=1
                    ans = 1
                v[i][j] = temp


        # print('h: ', h)
        # print('v: ', v)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == "1":
                    if dp[i-1][j-1] == 0:
                        matrix[i][j] = 1
                    elif v[i][j]>dp[i-1][j-1] and h[i][j]>dp[i-1][j-1]:
                        dp[i][j] = dp[i-1][j-1] + 1
                        if dp[i][j]>ans:
                            ans = dp[i][j]
                    else:
                        dp[i][j] = 1+min(v[i-1][j], h[i][j-1])
                        if dp[i][j]>ans:
                            ans = dp[i][j]

        # print('dp: ',dp)

        return ans**2


# [
# ["0","0","0","1"]
# ["1","1","0","1"]
# ["1","1","1","1"]
# ["0","1","1","1"]
# ["0","1","1","1"]
# ]

# h:  
# [
# [0, 0, 0, 1]
# [1, 2, 0, 1]
# [1, 2, 3, 4]
# [0, 1, 2, 3]
# [0, 1, 2, 3]
# ]
# v:  
# [
# [0, 0, 0, 1]
# [1, 1, 0, 2]
# [2, 2, 1, 3]
# [0, 3, 2, 4]
# [0, 4, 3, 5]
# ]
# dp:
# [
# [0, 0, 0, 1]
# [1, 1, 0, 1]
# [1, 2, 1, 1]
# [0, 1, 1, 2]
# [0, 1, 2, 2]
# ]


# [
#     [1, 0, 1, 0, 0]
#     [1, 0, 1, 2, 3]
#     [1, 2, 3, 4, 5]
#     [1, 0, 0, 1, 0]
# ]
# [
#     [1, 0, 1, 0, 0]
#     [2, 0, 2, 1, 1]
#     [3, 1, 3, 2, 2]
#     [4, 0, 0, 3, 0]
#  ]