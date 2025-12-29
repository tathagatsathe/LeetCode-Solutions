import heapq

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        arr = []
        
        for i in range(n):
            arr.append(wage[i]/quality[i])

        temp = list(zip(arr, quality))
        temp.sort()
        h = []
        ans = float("inf")
        quality_sum = 0
        for i in range(k):
            heapq.heappush(h, -temp[i][1])
            quality_sum+=temp[i][1]

        ans = quality_sum*temp[k-1][0]

        for i in range(k, n):
            q = heapq.heappop(h)
            quality_sum= quality_sum+q+temp[i][1]
           
            if quality_sum*temp[i][0] < ans:
                ans = quality_sum*temp[i][0]

            heapq.heappush(h, -temp[i][1])

        return ans

