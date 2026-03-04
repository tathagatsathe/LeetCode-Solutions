class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        def checkRowCol(i, j):
            sum_=0
            for x in range(m):
                sum_+=mat[x][j]
                if sum_ > 1:
                    return False

            sum_ = sum(mat[i])

            return sum_==1

        ans = 0

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1 and checkRowCol(i, j):
                    ans+=1


        return ans



