import copy

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k = k%n
        transformed_mat = []

        for i in range(m):
            if i % 2:
                transformed_mat.append(mat[i][k:] + mat[i][:k])
            else:
                transformed_mat.append(mat[i][n-k:] + mat[i][:n-k])

        return mat == transformed_mat