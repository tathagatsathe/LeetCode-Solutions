import heapq, bisect

class Solution:
    def busiestServers(self, k: int, arrival: list[int], load: list[int]) -> list[int]:
        n = len(arrival)
        freq = [0]*k
        servers = list(range(k))
        h = []

        for i in range(n):
            server_no = (i)%k
            while h and h[0][0] <= arrival[i]:
                _, server = heapq.heappop(h)
                bisect.insort_left(servers, server)

            if servers:
                s_id = bisect.bisect_left(servers, server_no)
                s_id = s_id if s_id < len(servers) else 0
                freq[servers[s_id]]+=1
                heapq.heappush(h, (arrival[i] + load[i], servers[s_id]))
                del servers[s_id]
                
        max_ = max(freq)

        return [i for i, val in enumerate(freq) if val == max_]