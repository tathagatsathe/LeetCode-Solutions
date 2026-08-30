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
        # print(i)
        idx = max(0, i-1)
        # print(idx)

        while idx < n:
            if intervals[idx][1] >= intervals[idx+1][0]:
                intervals[idx] = [min(intervals[idx][0], intervals[idx+1][0]), max(intervals[idx][1], intervals[idx+1][1])]
                intervals.pop(idx+1)
                n-=1
            else:
                idx+=1

        return intervals

        for i, (start, end) in enumerate(intervals):
            if left == n and (newInterval[0] <= start or start <= newInterval[0] <= end):
                left = i
            if start <= newInterval[1] <= end:
                right = i
            elif right == n and newInterval[1] < start:
                right = max(i - 1, 0)
    

        print(left, right)
        

        if left == right and left == n:
            intervals.append(newInterval)
        elif left == right and right != n:
            intervals[left] = [min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]
        elif left != n:
            if right == n:
                right-=1
            intervals[left] = [min(intervals[left][0], newInterval[0]), max(intervals[right][1], newInterval[1])]
            for i in range(right - left):
                intervals.pop(left+1)

        return intervals
