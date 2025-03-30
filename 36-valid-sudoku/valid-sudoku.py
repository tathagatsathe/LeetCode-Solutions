class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            v = [0]*10
            for j in range(len(board[0])):
                val = 0 if board[i][j]=="." else int(board[i][j])
                if(val!=0 and v[val]!=0):
                    return False
                v[val]+=1

        for i in range(len(board)):
            v = [0]*10
            for j in range(len(board[0])):
                val = 0 if board[j][i]=="." else int(board[j][i])
                if(val!=0 and v[val]!=0):
                    return False
                v[val]+=1


        v = 0
        vl = 3
        h = 0
        hl = 3

        while(v<9):
            d = [0]*10
            for i in range(v, vl):
                for j in range(h, hl):
                    val = 0 if board[i][j]=="." else int(board[i][j])
                    if(val!=0 and d[val]!=0):
                        return False
                    d[val]+=1
            if(hl==9):
                h = 0
                hl = 3
                v+= 3
                vl+=3
            else:
                h+=3
                hl+=3

        return True

