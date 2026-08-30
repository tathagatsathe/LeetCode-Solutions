class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)

        left = n
        right = n

        if intervals == []:
            return [newInterval]

        i = 0
        while i < n:
            start, end = intervals[i]
            if newInterval[0] < start:
                break
            i+=1

        intervals.insert(i, newInterval)

        idx = max(0, i-1)

        while idx < n:
            if intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx] = [min(intervals[idx][0], intervals[idx+1][0]), max(intervals[idx][1], intervals[idx+1][1])]
                intervals.pop(idx+1)
                n-=1
            else:
                idx+=1

        return intervals