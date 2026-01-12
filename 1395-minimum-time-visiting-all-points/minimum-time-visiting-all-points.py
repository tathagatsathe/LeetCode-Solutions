class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1, len(points)):
            x1, y1 = points[i-1]
            x2, y2 = points[i]
            temp = min(abs(x2-x1), abs(y2-y1))
            ans += abs(temp) + abs(abs(y2 - y1) - temp) + abs(abs(x2 - x1) - temp)
        return ans
