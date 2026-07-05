class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        mod = 10**9 + 7
        n = len(board)
        ans = [0, 0]
        directions = [(1,0), (1,1), (0, 1)]
        sum_arr = [[[0,0]]*n for _ in range(n)]

        sum_arr[0][0] = [0, 1]
        for i in range(1, n):
            if not (board[i][0] == "X" or (i > 1 and sum_arr[i-1][0][0] == 0)):
                sum_arr[i][0] = [sum_arr[i-1][0][0] + int(board[i][0]), 1]
            if not (board[0][i] == "X" or (i > 1 and sum_arr[0][i-1][0] == 0)):
                sum_arr[0][i] = [sum_arr[0][i-1][0] + int(board[0][i]), 1]

        for i in range(1, n):
            for j in range(1, n):
                if board[i][j] == 'X':
                    continue
                val = int(board[i][j]) if board[i][j]!='S' else 0
                prev_max_val = max([sum_arr[i][j-1][0], sum_arr[i-1][j-1][0], sum_arr[i-1][j][0]])

                if board[i][j]!='S' and prev_max_val == 0:
                    continue

                combinations = 0
                for mx_val, comb in [sum_arr[i][j-1], sum_arr[i-1][j-1], sum_arr[i-1][j]]:
                    if mx_val == prev_max_val:
                        combinations = (combinations + comb) % mod
                sum_arr[i][j] = [prev_max_val + val, combinations]
                
        return sum_arr[-1][-1]
