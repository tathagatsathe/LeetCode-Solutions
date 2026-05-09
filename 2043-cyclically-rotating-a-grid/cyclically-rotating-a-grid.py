class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])

        for d in range(min(m,n)//2):
            left, right = d, n - d - 1
            top, bottom = d, m - d - 1 
            temp = []
            for i in range(left, right + 1):
                temp.append(grid[top][i])
            for i in range(top+1, bottom):
                temp.append(grid[i][right])
            for i in range(right, left-1, -1):
                temp.append(grid[bottom][i])
            for i in range(bottom-1, top, -1):
                temp.append(grid[i][left])

            l = len(temp)
            temp_k = k % l

            temp = temp[temp_k:] + temp[:temp_k]

            idx = 0
            for i in range(left, right + 1):
                grid[top][i] = temp[idx]
                idx+=1
            for i in range(top+1, bottom):
                grid[i][right] = temp[idx]
                idx+=1
            for i in range(right, left-1, -1):
                grid[bottom][i] = temp[idx]
                idx+=1
            for i in range(bottom-1, top, -1):
                grid[i][left] = temp[idx]
                idx+=1

        
        return grid

