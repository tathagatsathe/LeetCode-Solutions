import heapq

class Solution:
    def assignTasks(self, servers: list[int], tasks: list[int]) -> list[int]:
        m = len(tasks)
        ans = []
        h = []
        servers = [(server, i) for i, server in enumerate(servers)]
        heapq.heapify(servers)
        current_time = 0

        for i in range(m):
            current_time = max(current_time, i)

            if len(servers) == 0:
                current_time = max(h[0][0], current_time)

            while h and h[0][0] <= current_time:
                time, server, idx = heapq.heappop(h)
                heapq.heappush(servers, (server, idx))

            server, idx = heapq.heappop(servers)
            heapq.heappush(h, (current_time+tasks[i], server, idx))                
            ans.append(idx)

        return ans

