class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        small_grid_nos = [[[0]*10 for _ in range(3)] for _ in range(3)]        

        for i in range(9):
            h_numbers_found = [0]*10
            v_numbers_found = [0]*10
            for j in range(9):
                if board[i][j] != ".":
                    if h_numbers_found[int(board[i][j])] != 0 or small_grid_nos[i//3][j//3][int(board[i][j])] != 0:
                        return False
                    h_numbers_found[int(board[i][j])]+= 1
                    small_grid_nos[i//3][j//3][int(board[i][j])]+= 1
                if board[j][i] != ".":
                    if v_numbers_found[int(board[j][i])] != 0:
                        return False
                    v_numbers_found[int(board[j][i])]+= 1

        return True