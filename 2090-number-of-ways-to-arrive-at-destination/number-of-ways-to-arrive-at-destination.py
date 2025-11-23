import heapq

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod = 10**9 + 7
        grid = [[] for _ in range(n)]
        dp = [float("inf")]*n

        for i in range(len(roads)):
            grid[roads[i][0]].append((roads[i][1], roads[i][2]))
            grid[roads[i][1]].append((roads[i][0], roads[i][2]))


        h = []
        heapq.heappush(h, (0, 0))
        dp[0] = 0
        min_time = float("inf")
        adj = [[] for _ in range(n)]
        ways = [0]*n
        ways[0] = 1

        while h:
            time, node = heapq.heappop(h)

            if time> dp[node]:
                continue

            if node == n-1:
                min_time = time
                break

            for nd, t in grid[node]:
                new_time = time+t
                if new_time < dp[nd]:
                    dp[nd] = time+t
                    ways[nd] = ways[node]
                    heapq.heappush(h, (time + t, nd))

                elif new_time == dp[nd]:
                    ways[nd] = (ways[nd]+ ways[node])%mod

        return ways[n-1]


