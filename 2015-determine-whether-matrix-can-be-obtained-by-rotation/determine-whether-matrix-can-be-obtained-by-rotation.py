class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = 4
        def rotateBy90(mat):
            m, n = len(mat), len(mat[0])
            res = [[0]*m for _ in range(n)]

            for i in range(m):
                for j in range(n):
                    res[n-j-1][i] = mat[i][j]

            return res


        while n:
            if mat == target:
                return True

            mat = rotateBy90(mat)
            n-=1

        return False
