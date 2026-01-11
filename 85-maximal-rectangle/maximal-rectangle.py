from collections import deque

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        dp = [[int(matrix[j][i] if i<n else 0) for i in range(n+1)] for j in range(m)]
        
        ans = 1 if sum(dp[0]) > 0 else 0
    
        temp = 0
        for i in range(n):
            if dp[0][i] == 1:
                temp+=1
                if temp > ans:
                    ans = temp
            else:
                temp = 0
            
        
        for i in range(1,m):
            stack = deque([])
            for j in range(n+1):
                # print(i, j, 'stack: ',stack)
                if dp[i][j] == 1:
                    dp[i][j] = dp[i-1][j] + 1
                t = j
                while stack and stack[-1][0]>dp[i][j]:
                    temp = stack[-1][0] * (j - stack[-1][1])
                    if temp > ans:
                        ans = temp
                    t = stack[-1][1]
                    stack.pop()
                if dp[i][j] > 0:
                    stack.append([dp[i][j],t])

                # print('ans: ',ans ,' i: ',i, ' j: ',j)


        # print('dp: ',dp)
        return ans


    # h:  
    #     [0, 0, 1, 0], 
    #     [0, 0, 1, 0], 
    #     [0, 0, 1, 0],
    #     [0, 0, 1, 2],
    #     [0, 1, 2, 3],
    #     [0, 1, 2, 3],
    #     [1, 2, 3, 4]

    # v:  [0, 0, 1, 0],
    #     [0, 0, 2, 0],
    #     [0, 0, 3, 0],
    #     [0, 0, 4, 1],
    #     [0, 1, 5, 2],
    #     [0, 2, 6, 3],
    #     [1, 3, 7, 4]

    # dp: [0, 0, 1, 0]
    #     [0, 0, 2, 0]
    #     [0, 0, 3, 0]
    #     [0, 0, 4, 2]
    #     [0, 1, 5, 4]
    #     [0, 2, 4, 9]
    #     [1, 3, 6, 12]