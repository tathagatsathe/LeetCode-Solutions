import heapq

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        h = []
        meetings.sort()
        empty_rooms = list(range(n))
        heapq.heapify(empty_rooms)
        count = [0]*n
        
        for start, end in meetings:
            while h and h[0][0]<=start:
                _, room = heapq.heappop(h)
                heapq.heappush(empty_rooms, room)

            if empty_rooms:
                room = heapq.heappop(empty_rooms)
                heapq.heappush(h, (end, room))
                count[room]+=1
            else:
                en, room = heapq.heappop(h)
                delay = en - start
                heapq.heappush(h, (end+delay, room))
                count[room]+=1

        return count.index(max(count))
