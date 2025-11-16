class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0
        m = len(grid1)
        n = len(grid1[0])
        visited = [[False]*n for _ in range(m)]
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return 

            if grid2[i][j] == 1:
                return False

            if visited[i][j]==True or grid2[i][j]==0:
                return 

            visited[i][j] = True
            for (x, y) in directions:
                ret = dfs(i+x, j+y)
                if ret == False:
                    grid2[i][j] = 1
                    return False

            return True

        for i in range(m):
            for j in range(n):
                if grid1[i][j]==1 and grid2[i][j]==1:
                    grid2[i][j] = 2
                elif grid1[i][j]==1 and grid2[i][j]==0:
                    grid2[i][j] = 0

        # print(grid2)

        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 2 and visited[i][j]==False:
                    ret = dfs(i, j)
                    # print(i,j, ret)
                    # if i==9 and j==0:
                    #     print(grid2)
                    if ret != False:
                        ans+=1
        # print(grid2)
        return ans

# [1,1,1,1,0,0],
# [1,1,0,1,0,0],
# [1,0,0,1,1,1],
# [1,1,1,0,0,1],
# [1,1,1,1,1,0],
# [1,0,1,0,1,0],
# [0,1,1,1,0,1],
# [1,0,0,0,1,1],
# [1,0,0,0,1,0],
# [1,1,1,1,1,0]

# [1,1,1,1,0,1],
# [0,0,1,0,1,0],
# [1,1,1,1,1,1],
# [0,1,1,1,1,1],
# [1,1,1,0,1,0],
# [0,1,1,1,1,1],
# [1,1,0,1,1,1],
# [1,0,0,1,0,1],
# [1,1,1,1,1,1],
# [1,0,0,1,0,0]

# [2,2,2,2,0,1],
# [0,0,1,0,1,0],
# [2,1,1,2,2,2],
# [0,2,2,1,1,2],
# [2,2,2,0,2,0],
# [0,1,2,1,2,1],
# [1,2,0,2,1,2],
# [2,0,0,1,0,2],
# [2,1,1,1,2,1],
# [2,0,0,2,0,0]

# [1, 1, 1, 2, 0, 1],
# [0, 0, 1, 0, 1, 0],
# [1, 1, 1, 1, 1, 1],
# [0, 1, 1, 1, 1, 1],
# [1, 1, 1, 0, 1, 0],
# [0, 1, 1, 1, 1, 1],
# [1, 1, 0, 1, 1, 1],
# [1, 0, 0, 1, 0, 1],
# [1, 1, 1, 1, 1, 1],
# [1, 0, 0, 1, 0, 0]



# 0 0 False
# 2 0 False
# 2 3 False
# 3 1 False
# 4 0 False
# 4 4 False
# 6 1 False
# 6 3 False
# 6 5 False
# 7 0 False
# 8 4 False
# 9 0 True
# 9 0 True
# 9 3 False