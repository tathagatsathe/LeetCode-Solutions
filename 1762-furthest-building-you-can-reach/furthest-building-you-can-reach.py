import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        sum_ = 0
        n = len(heights)
        # print(n)
        for i in range(1, n):
            if heights[i] > heights[i-1]:
                diff = heights[i] - heights[i-1]
                # print('diff: ',diff, sum_, ladders, i)
                if sum_ + diff <= bricks:
                    heapq.heappush(h, -diff)
                    sum_+=diff
                elif ladders !=0:
                    if h and -h[0]>diff:
                        d = heapq.heappop(h)
                        sum_ = sum_ + d
                        if sum_+ diff <=bricks:
                            heapq.heappush(h, -diff)
                            sum_+=diff
                    ladders-=1
                else:
                    return i-1

        return n-1

