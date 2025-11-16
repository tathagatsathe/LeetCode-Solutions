from collections import deque

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        dq = deque([0])
        n = len(rooms)
        visited = [False]*n
        count = 0

        while dq:
            room = dq.popleft()
            if visited[room] == True:
                continue

            visited[room] = True
            n-=1

            for r in rooms[room]:
                dq.append(r)

        return n == 0
                