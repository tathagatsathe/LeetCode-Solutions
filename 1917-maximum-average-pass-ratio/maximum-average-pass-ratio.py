import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        h = []
        n = len(classes)
        for cl in classes:
            temp = (cl[0]+1)/(cl[1]+1) - cl[0]/cl[1]
            heapq.heappush(h, ( -temp, cl[0], cl[1]))

        while extraStudents:
            ratio, ps, tot = heapq.heappop(h)
            extraStudents-=1
            tot+=1
            ps+=1
            temp = ((ps+1)/(tot+1)) - (ps/tot)
            heapq.heappush(h, ( -temp, ps, tot))

        ans = 0

        while h:
            ratio, ps, tot = heapq.heappop(h)
            ans+=(ps/tot)

        return ans/n