import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        h = []

        for x, y in points:
            heapq.heappush(h, (-x**2 - y**2, [x, y]))

        while len(h)>k:
            heapq.heappop(h)
        ans = []

        while h:
            temp = heapq.heappop(h)
            ans.append(temp[1])
        return ans