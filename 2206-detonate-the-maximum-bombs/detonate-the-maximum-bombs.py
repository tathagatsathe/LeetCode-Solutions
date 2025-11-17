import math

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        visited = [False]*n
        def distance(x1, y1, x2, y2):
            return math.sqrt((x1-x2)**2 +(y1-y2)**2)

        def dfs(i):
            if visited[i] != False:
                return

            visited[i] = True

            for j in range(n):
                if i!=j:
                    dist = distance(bombs[i][0],bombs[i][1], bombs[j][0], bombs[j][1])
                    if dist<=bombs[i][2]:
                        dfs(j)
            
            
        ans = 0
        for i in range(n):
            dfs(i)
            if visited.count(True) > ans:
                ans = visited.count(True)
            visited = [False]*n

        return ans

        