import heapq, math

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        h = [-x for x in gifts]
        heapq.heapify(h)
        while k>0:
            x = heapq.heappop(h)
            x = int(math.sqrt(-x))
            heapq.heappush(h, -x)
            k-=1

        return -sum(h)