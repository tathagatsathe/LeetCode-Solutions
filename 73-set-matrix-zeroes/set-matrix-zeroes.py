class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        m = len(matrix)
        n = len(matrix[0])
        i=0
        j=0
        k = -1
        l = -1
        while(i<m):
            j = 0
            while(j<n):
                if(matrix[i][j]==0):
                    if(i==0):
                        k=0
                    if(j==0):
                        l=0
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                j+=1
            i+=1

        
        for i in range(m):
            if(matrix[i][0]==0):
                for j in range(1, n):
                    if(i!=0):
                        matrix[i][j] = 0

        for i in range(n):
            if(matrix[0][i]==0):
                for j in range(1, m):
                    if(i!=0):
                        matrix[j][i] = 0

        if(k==0):
            for i in range(n):
                matrix[0][i] = 0

        if(l==0):
            for i in range(m):
                matrix[i][0] = 0

