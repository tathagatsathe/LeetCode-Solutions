from collections import deque
from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.dq = deque([])
        self.sl = SortedList([])
        self.sum_ = 0
        self.k = k
        self.m = m

    def addElement(self, num: int) -> None:
        self.dq.append(num)
        flag = False
        if len(self.dq) < self.m:
            return
        if len(self.dq) == self.m:
            self.sl = SortedList(list(self.dq))
            self.sum_ = sum(self.sl[self.k:self.m-self.k])
            return
        if len(self.dq) > self.m:
            p = self.dq.popleft()
            idx = self.sl.bisect_left(p)
            if self.k<=idx<self.m - self.k:
                self.sum_-=p
                self.sum_+=self.sl[self.m - self.k]
                flag = True
            elif idx<self.k:
                self.sum_+=self.sl[self.m-self.k] - self.sl[self.k]
            self.sl.remove(p)
        self.sl.add(num)
        idx = self.sl.bisect_left(num)
        if self.k<=idx<self.m - self.k:
            self.sum_+=num - self.sl[self.m - self.k]
        elif idx<self.k:
            self.sum_+=self.sl[self.k] - self.sl[self.m - self.k]


    def calculateMKAverage(self) -> int:
        if len(self.dq) < self.m:
            return -1
        return int(self.sum_/(self.m- 2*self.k))


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()