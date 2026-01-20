import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        h1 = []
        h2 = []
        count = [0]*n
        for start, end in meetings:
            heapq.heappush(h1, (start, -1, end))

        room = 0
        empty_rooms = list(range(n))
        heapq.heapify(empty_rooms)

        while h1:
            if len(h2) < n:
                start, c, end = heapq.heappop(h1)
                while h2 and h2[0][0]<=start:
                    en, room = heapq.heappop(h2)
                    heapq.heappush(empty_rooms, room)
                room = heapq.heappop(empty_rooms)
                heapq.heappush(h2, (end, room))
                count[room]+=1
            else:
                # print('h1: ', h1)
                # print('h2: ', h2)
                st, c, en = heapq.heappop(h1)
                while h2 and h2[0][0]<=st:
                    end, room = heapq.heappop(h2)
                    heapq.heappush(empty_rooms, room)
                if empty_rooms:
                    room = heapq.heappop(empty_rooms)
                    heapq.heappush(h2, (en, room))
                else:
                    end2, room = heapq.heappop(h2)
                    delay = max(end2 - st, 0)
                    heapq.heappush(h2, (en + delay, room))
                count[room]+=1

        # print('count: ',count)

        return count.index(max(count))

# h1:  [(29, -1, 49), (41, -1, 43), (47, -1, 49)]
# h2:  [(15, 1), (27, 0), (36, 2)]
# count = [1, 1, 1]


# h1: [(41, -1, 43), (47, -1, 49)]
# h2: [(36, 2),(49, 0)]
# empty_rooms: [1]
# count = [2, 1, 1]


# h1: [(47, -1, 49)]
# h2: [(36, 2),(43, 1), (49, 0)]
# empty_rooms: []


# [[1,27],[11,15],[15,36],[29,49],[41,43],[47,49]]

