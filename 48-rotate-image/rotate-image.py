class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        for i in range(n//2):
            for j in range(i, n-i-1):
                count = 4
                x, y = i, j
                temp = matrix[x][y]

                while count:
                    matrix[y][n-1-x], temp = temp, matrix[y][n-1-x]
                    x, y = y, n - 1 - x
                    count-=1


