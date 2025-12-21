import heapq

class MedianFinder:

    def __init__(self):
        self.h1 = []
        self.h2 = []

    def addNum(self, num: int) -> None:
        if self.h1 == []:
            heapq.heappush(self.h1, -num)
            return

        if self.h1[0]*-1 > num:
            if len(self.h2) < len(self.h1):
                x = heapq.heappop(self.h1)
                heapq.heappush(self.h1, -num)
                heapq.heappush(self.h2, -x)
            else:
                heapq.heappush(self.h1, -num)
        else:
            heapq.heappush(self.h2, num)
            if len(self.h2) > len(self.h1):
                x = heapq.heappop(self.h2)
                heapq.heappush(self.h1, -x)

        # print(self.h1, self.h2, -self.h1[0])


    def findMedian(self) -> float:
        if len(self.h1) == len(self.h2):
            return (self.h2[0]-self.h1[0])/2
        
        return -self.h1[0]


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
