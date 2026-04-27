class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        map_ = {
            1: ['L', 'R'],
            2: ['U', 'D'],
            3: ['L', 'D'],
            4: ['R', 'D'],
            5: ['L', 'U'],
            6: ['R', 'U']
            }

        nxt_direction = {'R': 'L', 'D': 'U', 'L': 'R', 'U':'D'}

        direction = {'U': (-1,0), 'D': (1,0), 'L': (0,-1), 'R': (0,1)}
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]

        def fn(i, j, d):
            # print(i, j, d)
            if i == m-1 and j == n-1:
                return True

            visited[i][j] = True
            x, y = i + direction[d][0], j + direction[d][1]
            if x < 0 or y < 0 or x >= m or y >= n or visited[x][y] == True or nxt_direction[d] not in map_[grid[x][y]]:
                return False
            
            direc = None

            for l in map_[grid[x][y]]:
                if nxt_direction[d] != l:
                    print(l)
                    direc = l

            # print('____________________')
            return fn(x, y, direc)

        # print(map_[grid[0][0]])
        return fn(0, 0, map_[grid[0][0]][0]) or fn(0, 0, map_[grid[0][0]][1])
