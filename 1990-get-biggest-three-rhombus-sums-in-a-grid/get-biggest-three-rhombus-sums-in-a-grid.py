import math

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        max_size = math.ceil(min(m, n)/2)
        sums = set()
        c = 0

        def sumOfRhombus(i, j, size, t):
            sum_ = 0
            for x in range(size):
                sum_+=grid[i+x][j+x] + grid[i+x][j-x] + grid[i+t-x][j-x] + grid[i+t-x][j+x]

            sum_-= (grid[i][j] + grid[i+t][j] + grid[i+ t//2][j - t//2] + grid[i+ t//2][j+t//2])

            return sum_

        t = 2
        for i in range(m):
            for j in range(n):
                sums.add(grid[i][j])
            
        for size in range(2, max_size+1):
            for i in range(m - size - c):
                for j in range(size-1, n - size+1):
                    sum_ = sumOfRhombus(i, j, size, t)
                    sums.add(sum_)
                    
            c+=1
            t+=2

        sums = list(sums)
        sums.sort(reverse=True)

        return sums[:3]
