class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l = len(landStartTime)
        w = len(waterStartTime)

        ans = float("inf")

        for i in range(l):
            land_end_time = landStartTime[i] + landDuration[i]
            for j in range(w):
                if max(land_end_time, waterStartTime[j])  + waterDuration[j] < ans:
                    ans = max(land_end_time, waterStartTime[j]) + waterDuration[j]

        for i in range(w):
            water_end_time = waterStartTime[i] + waterDuration[i]
            for j in range(l):
                if max(landStartTime[j], water_end_time) + landDuration[j] < ans:
                    ans = max(landStartTime[j], water_end_time) + landDuration[j]

        return ans
