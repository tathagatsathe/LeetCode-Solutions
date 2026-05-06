class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        ans = [["."]*m for _ in range(n)]

        for i in range(m):
            obstacle_idx = n
            for j in range(n-1,-1,-1):
                if boxGrid[i][j] == "*" or (boxGrid[i][j] == "#" and (obstacle_idx - j) <= 1):
                    obstacle_idx = j
                elif boxGrid[i][j] == "#":
                    boxGrid[i][obstacle_idx-1] = boxGrid[i][j]
                    boxGrid[i][j] = "."
                    obstacle_idx-=1

        for i in range(m):
            for j in range(n):
                ans[j][m-i-1] = boxGrid[i][j]

        return ans