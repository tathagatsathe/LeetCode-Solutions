import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        h1 = []
        h2 = []
        n = len(tasks)

        for i in range(n):
            heapq.heappush(h2, (tasks[i][0], tasks[i][1], i))

        enq, prc, idx = heapq.heappop(h2)
        heapq.heappush(h1, (prc, idx))
        time = enq
        
        while h1:
            prc, idx = heapq.heappop(h1)
            ans.append(idx)
            time+=prc
            if len(h1) == 0 and h2 and h2[0][0]>time:
                enq1, prc1, idx1 = heapq.heappop(h2)
                heapq.heappush(h1, (prc1, idx1))
                time = enq1
                continue
            while h2 and h2[0][0]<=time:
                enq1, prc1, idx1 = heapq.heappop(h2)
                heapq.heappush(h1, (prc1, idx1))

        return ans

#     0       1       2       3     4        5      6      7      8       9       10      11  
# [[35,36],[11,7],[15,47],[34,2],[47,19],[16,14],[19,8],[7,34],[38,15],[16,18],[27,22],[7,15],
#    12     13    14     15
# [43,2],[10,5],[5,4],[3,11]]


# [3,11], 
# [15 ,14 ,13 ,1 , 6, 3 ,12 ,5 , 8, 11 ,9 ,4 ,10 ,7 ,0 ,2 ]
#  14  18  23  30. 38 40 42. 56


# [3,11].  15

# [5,4], [10,5],[11,7], [7,15], [7,34]      14

# [10,5], [11,7], [16,14], [16,18], [7,15], [7,34], [15,47]     13

# [11,7], [19,8], [16,14], [16,18], [7,15], [7,34], [15,47]     1

# [19,8], [16,14], [16,18], [7,15], [27,22], [7,34], [15,47]       6

# [16,14], [16,18], [7,15], [27,22], [7,34], [15,47].           5


# [[3, 11], [5, 4], [7, 15], [7, 34], [10, 5], [11, 7], [15, 47], [16, 14], [16, 18], [19, 8], [27, 22], [34, 2], [35, 36], [38, 15], [43, 2], [47, 19]]