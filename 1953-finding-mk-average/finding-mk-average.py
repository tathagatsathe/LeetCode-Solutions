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
        # print(self.sum_, num, self.sl, self.dq)
        self.dq.append(num)
        flag = False
        if len(self.dq) < self.m:
            return
        if len(self.dq) == self.m:
            self.sl = SortedList(list(self.dq))
            self.sum_ = sum(self.sl[self.k:self.m-self.k])
            # print('self.sum_: ',self.sum_)
            return
        if len(self.dq) > self.m:
            p = self.dq.popleft()
            idx = self.sl.bisect_left(p)
            # print('p: ',p, 'idx: ',idx, 'self.k: ',self.k, ' self.m - self.k: ',self.m - self.k)
            if self.k<=idx<self.m - self.k:
                self.sum_-=p
                self.sum_+=self.sl[self.m - self.k]
                flag = True
                # print('self.sum____ : ',self.sum_)
            elif idx<self.k:
                self.sum_+=self.sl[self.m-self.k] - self.sl[self.k]
            self.sl.remove(p)
        self.sl.add(num)
        idx = self.sl.bisect_left(num)
        # print('idx: ',idx, ' self.sl: ', self.sl, ' self.sum_: ', self.sum_)
        if self.k<=idx<self.m - self.k:
            self.sum_+=num - self.sl[self.m - self.k]
        elif idx<self.k:
            self.sum_+=self.sl[self.k] - self.sl[self.m - self.k]

        # print(self.sum_, num, self.sl, self.dq)
        # print('_____________________________')

    def calculateMKAverage(self) -> int:
        if len(self.dq) < self.m:
            return -1
        return int(self.sum_/(self.m- 2*self.k))


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()