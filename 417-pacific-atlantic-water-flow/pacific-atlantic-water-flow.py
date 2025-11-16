class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        m = len(heights)
        n = len(heights[0])

        res = [[""]*n for _ in range(m)]

        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        def dfs(i, j, ocean, prev):
            if i<0 or j<0 or i>=m or j>=n or res[i][j]==ocean or res[i][j]=="B" or prev>heights[i][j]:
                return 

            if res[i][j] == "":
                res[i][j] = ocean
            elif res[i][j] != ocean:
                res[i][j] = "B"
            
            for (x,y) in directions:
                dfs(i+x, j+y, ocean, heights[i][j])

        for j in range(n):
            dfs(0, j, 'P',-1)
            dfs(m-1, j, 'A',-1)

        for i in range(m):
            dfs(i, 0, 'P',-1)
            dfs(i, n-1, 'A',-1)

        ans = []
        for i in range(m):
            for j in range(n):
                if res[i][j] == "B":
                    ans.append([i,j])

        return ans

