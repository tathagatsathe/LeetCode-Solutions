class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        curr_row = board[0].copy()
        # print('i','j', 'live_c', 'dead_c')
        
        for i in range(m):
            if(i>0):
                prev_row = curr_row.copy()
                curr_row = board[i].copy()
            if(i<m-1):
                nxt_row = board[i+1].copy()
            for j in range(n):
                live_c = 0
                dead_c = 0
                if(i>0):
                    for k, l in [(-1,1),(-1,0),(-1,-1)]:
                        if(j+l>=0 and j+l<n):
                            if(prev_row[j+l]==1):
                                live_c+=1
                            else:
                                dead_c+=1
                # print(i,j, live_c, dead_c, '1')

                if(i<m-1):
                    for k, l in [(1,-1),(1,0),(1,1)]:
                        if(j+l>=0 and j+l<n):
                            if(nxt_row[j+l]==1):
                                live_c+=1
                            else:
                                dead_c+=1
                
                # print(i,j, live_c, dead_c, '2', curr_row)
                if(j>0):
                    if(curr_row[j-1]==1):
                        live_c+=1
                    else:
                        dead_c+=1

                # print(i,j, live_c, dead_c, '3')
                
                if(j+1<n):
                    if(curr_row[j+1]==1):
                        live_c+=1
                    else:
                        dead_c+=1

                # print(i,j, live_c, dead_c)
                if(live_c<2 or live_c>3):
                    board[i][j]=0
                if(live_c==3):
                    board[i][j]=1

                
        

                

