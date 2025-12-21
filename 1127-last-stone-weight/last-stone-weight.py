import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)

        while len(h)>1:
            y = heapq.heappop(h)
            x = heapq.heappop(h)
            if x!=y:
                heapq.heappush(h, y-x)

        if len(h) == 0:
            return 0

        return -h[0]
