class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        l = len(landStartTime)
        w = len(waterStartTime)

        earliest_land_end_time = min([landStartTime[i] + landDuration[i] for i in range(l)])
        earliest_water_end_time = min([waterStartTime[i] + waterDuration[i] for i in range(w)])

        earliest_time1 = float("inf")
        earliest_time2 = float("inf")

        for i in range(l):
            earliest_time1 = min(earliest_time1, max(earliest_water_end_time, landStartTime[i]) + landDuration[i])

        for i in range(w):
            earliest_time2 = min(earliest_time2, max(earliest_land_end_time, waterStartTime[i]) + waterDuration[i])
            
        return min(earliest_time1, earliest_time2)

        