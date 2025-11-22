import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        visited = [False]*n
        grid = [[] for _ in range(n)]

        for i in range(len(edges)):
            grid[edges[i][0]].append((edges[i][1], succProb[i]))
            grid[edges[i][1]].append((edges[i][0], succProb[i]))

        h = []

        heapq.heappush(h, (-1, start_node))
        ans = 0
        while h:
            max_prob, node = heapq.heappop(h)
            if node == end_node:
                if max_prob*-1>ans:
                    ans = -1 * max_prob
            if visited[node] == True:
                continue
            visited[node] = True
            for g in grid[node]:
                if visited[g[0]] == False:
                    heapq.heappush(h, (max_prob*g[1], g[0]))

        return ans
