import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        visited = [[False]*n for _ in range(n)]
        h = []
        heapq.heappush(h, (matrix[0][0], 0, 0))
        visited[0][0] = True
        while h and k>0:
            val, i, j = heapq.heappop(h)
            # print(val, i, j, k)
            k-=1
            if k == 0:
                return val
            
            if i+1<n and visited[i+1][j]==False:
                heapq.heappush(h, (matrix[i+1][j], i+1, j))
                visited[i+1][j] = True
            if j+1<n and visited[i][j+1]==False:
                heapq.heappush(h, (matrix[i][j+1], i, j+1))
                visited[i][j+1] = True


        return 0