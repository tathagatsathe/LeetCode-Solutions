import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = nums
        heapq.heapify(self.h)
        self.n = len(nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        self.n+=1
        res = None
        while self.n>self.k:
            heapq.heappop(self.h)
            self.n-=1
        res = heapq.heappop(self.h)
        heapq.heappush(self.h, res)
        return res


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

