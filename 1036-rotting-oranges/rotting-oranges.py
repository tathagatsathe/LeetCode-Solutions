from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rotten_org = []
        fresh_org_count = 0
        q = deque([])

        def adjVertices(i,j):
            adj = [(i-1, j), (i, j-1), (i+1, j), (i, j+1)]
            i = 0
            while(i<len(adj)):
                if(adj[i][0]<0 or adj[i][0]>=m or adj[i][1]<0 or adj[i][1]>=n or grid[adj[i][0]][adj[i][1]]!=1):
                    adj.pop(i)
                else:
                    i+=1

            return adj

        for i in range(m):
            for j in range(n):
                if(grid[i][j]==2):
                    q.append((i,j))
                    rotten_org.append((i,j))
                elif(grid[i][j]==1):
                    fresh_org_count+=1

        if(fresh_org_count==0):
            return 0

        ans = -1

        while(q):
            ans+=1
            rot = q.popleft()
            l = []
            adj = adjVertices(rot[0], rot[1])
            l.extend(adj)
            while(q):
                rot = q.popleft()
                adj = adjVertices(rot[0], rot[1])
                l.extend(adj)

            for v in l:
                if(grid[v[0]][v[1]]==1):
                    fresh_org_count-=1
                    grid[v[0]][v[1]] = 2
                    q.append((v[0],v[1]))

        if(fresh_org_count>0):
            return -1

        return ans

        
        