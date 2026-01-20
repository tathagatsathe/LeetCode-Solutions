import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        h1 = []
        h2 = []
        empty_rooms = list(range(n))
        heapq.heapify(empty_rooms)
        count = [0]*n
        
        for start, end in meetings:
            heapq.heappush(h1, (start, -1, end))

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

        return count.index(max(count))
