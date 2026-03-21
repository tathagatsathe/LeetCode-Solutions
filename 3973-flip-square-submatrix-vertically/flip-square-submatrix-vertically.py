class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        c = 1
        for i in range(x, x+k//2):
            temp = grid[i][y:y+k]
            grid[i][y:y+k] = grid[x+k-c][y:y+k]
            grid[x+k-c][y:y+k] = temp
            c+=1

        return grid
        