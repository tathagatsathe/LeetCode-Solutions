class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [[-1,0],[0,-1],[1,0],[0,1]]
        m = len(board)
        n = len(board[0])
        visited = [[False]*n for _ in range(m)]

        def dfs(i,j):
            if(i<0 or j<0 or i>=m or j>=n or visited[i][j]==True or board[i][j]!='O'):
                return 
            
            visited[i][j] = True
            board[i][j] = 'M'
            for d in directions:
                dfs(i+d[0],j+d[1])

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)

        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)

        def modifyMatrix(board, old, new):
            for i in range(m):
                for j in range(n):
                    if board[i][j] == old:
                        board[i][j] = new
            
            return 

        modifyMatrix(board,'O','X')
        modifyMatrix(board,'M','O')

        ["X","O","X","O","X","O"],
        ["O","X","O","X","O","X"],
        ["X","O","X","O","X","O"],
        ["O","X","O","X","O","X"]
