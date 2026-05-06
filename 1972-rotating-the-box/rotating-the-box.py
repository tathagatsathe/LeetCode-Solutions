class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m, n = len(boxGrid), len(boxGrid[0])
        ans = [["."]*m for _ in range(n)]

        for i in range(m):
            obstacle_idx = n
            for j in range(n-1,-1,-1):
                if boxGrid[i][j] == "*" or (boxGrid[i][j] == "#" and (obstacle_idx - j) <= 1):
                    obstacle_idx = j
                    ans[j][i] = boxGrid[i][j]
                elif boxGrid[i][j] == "#":
                    # print(obstacle_idx, boxGrid[i][j])
                    boxGrid[i][obstacle_idx-1] = boxGrid[i][j]
                    boxGrid[i][j] = "."
                    ans[obstacle_idx-1][i] = boxGrid[i][j]
                    ans[j][i] = "."
                    obstacle_idx-=1

        for i in range(m):
            for j in range(n):
                # print(i, j, m- i - 1)
                ans[j][m-i-1] = boxGrid[i][j]



        # print(boxGrid)
        return ans
        # obstacle_idx = 0
        # 2 - 1

# [[
#     "#","#","*",".","*","."],
#     ["#","#","#","*",".","."],
#     ["#","#","#",".","#","."]
# ]

# [
# ['#', '#', '*', '.', '*', '.'],
# ['#', '#', '#', '*', '.', '.'],
# ['.', '.', '.', '.', '.', '#']
# ]

# [
# [".","#","#"],
# [".","#","#"],
# ["#","#","*"],
# ["#","*","."],
# ["#",".","*"],
# ["#",".","."]
# ]