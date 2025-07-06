class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        m = len(isConnected)
        n = len(isConnected[0])
        ans = 0

        visited = [[False]*n for _ in range(m)]

        def recursivelyVisit(i,j):
            visited[i][j] = True
            visited[j][i] = True
            ad = isConnected[i]
            # print('___________________________________')
            for k, v in enumerate(ad):
                # print('i: ', i, 'j: ', j, 'k: ',k, 'ad: ',ad, 'visited[i][k]: ',visited[i][k])
                if(ad[k]==1 and visited[i][k]==False):
                    if(i==k or j==k):
                        visited[i][k] = True
                        visited[k][i] = True
                    else:
                        recursivelyVisit(k, i)

        for i in range(m):
            for j in range(i, n):
                if(isConnected[i][j]==1 and visited[i][j]==False):
                    recursivelyVisit(i,j)
                    ans+=1
                    # print(i,j, ans)

        return ans
# i:  0 j:  0 k:  1 ad:  [1, 1, 0]
# 0 0 1
# i:  1 j:  1 k:  0 ad:  [1, 1, 0]
# 1 1 2
# 2 2 3
        
# i:  0 j:  0 k:  0 ad:  [1, 1, 0] visited[i][k]:  True
# i:  0 j:  0 k:  1 ad:  [1, 1, 0] visited[i][k]:  False
# ___________________________________
# i:  1 j:  0 k:  0 ad:  [1, 1, 0] visited[i][k]:  True
# i:  1 j:  0 k:  1 ad:  [1, 1, 0] visited[i][k]:  False
# i:  1 j:  0 k:  2 ad:  [1, 1, 0] visited[i][k]:  False
# i:  0 j:  0 k:  2 ad:  [1, 1, 0] visited[i][k]:  False
# 0 0 1
# ___________________________________
# i:  1 j:  1 k:  0 ad:  [1, 1, 0] visited[i][k]:  True
# i:  1 j:  1 k:  1 ad:  [1, 1, 0] visited[i][k]:  True
# i:  1 j:  1 k:  2 ad:  [1, 1, 0] visited[i][k]:  False
# 1 1 2
# ___________________________________
# i:  2 j:  2 k:  0 ad:  [0, 0, 1] visited[i][k]:  False
# i:  2 j:  2 k:  1 ad:  [0, 0, 1] visited[i][k]:  False
# i:  2 j:  2 k:  2 ad:  [0, 0, 1] visited[i][k]:  True
# 2 2 3