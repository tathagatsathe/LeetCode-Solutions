import math, heapq

class SparseTableRMQ:
    def __init__(self, arr):
        self.n = len(arr)
        # K = floor(log2(N)) + 1
        self.K = math.floor(math.log2(self.n)) + 1
        self.st = [[0] * self.K for _ in range(self.n)]
        self.st1 =  [[0] * self.K for _ in range(self.n)]
        
        # 1. Initialize for intervals of length 2^0 = 1
        for i in range(self.n):
            self.st[i][0] = arr[i]
            self.st1[i][0] = arr[i]
            
        # 2. Build the Sparse Table using powers of 2
        for j in range(1, self.K):
            for i in range(self.n - (1 << j) + 1):
                # Take minimum of two halves
                left = self.st[i][j - 1]
                right = self.st[i + (1 << (j - 1))][j - 1]
                self.st[i][j] = min(left, right)
                self.st1[i][j] = max(self.st1[i][j - 1], self.st1[i + (1 << (j - 1))][j - 1])

    def query(self, L, R):
        length = R - L + 1
        k = math.floor(math.log2(length))
        
        # Merge two overlapping blocks of length 2^k
        return max(self.st1[L][k], self.st1[R - (1 << k) + 1][k]) - min(self.st[L][k], self.st[R - (1 << k) + 1][k])
        
class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return 0
        ans = 0
        rmq = SparseTableRMQ(nums)
        h = []
        for i in range(n):
            heapq.heappush(h, (-rmq.query(i, n-1), i, n-1))

        for _ in range(k):
            if h:
                val, l, r = heapq.heappop(h)
                if r - 1 > l:
                    heapq.heappush(h,(-rmq.query(l, r-1), l, r-1))
                ans-=val
        
        return ans