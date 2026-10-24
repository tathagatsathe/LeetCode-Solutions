class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        startMonth = max(int(arriveAlice.split("-")[0]),int(arriveBob.split("-")[0]))
        endMonth = min(int(leaveAlice.split("-")[0]),int(leaveBob.split("-")[0]))

        if int(arriveAlice.split("-")[0]) == int(arriveBob.split("-")[0]):
            startDate = max(int(arriveAlice.split("-")[1]), int(arriveBob.split("-")[1]))
        elif int(arriveAlice.split("-")[0]) > int(arriveBob.split("-")[0]):
            startDate = int(arriveAlice.split("-")[1])
        else:
            startDate = int(arriveBob.split("-")[1])

        if int(leaveAlice.split("-")[0]) == int(leaveBob.split("-")[0]):
            endDate = min(int(leaveAlice.split("-")[1]), int(leaveBob.split("-")[1]))
        elif int(leaveAlice.split("-")[0]) < int(leaveBob.split("-")[0]):
            endDate = int(leaveAlice.split("-")[1])
        else:
            endDate = int(leaveBob.split("-")[1])
        
        totalDays = 0

        for i in range(startMonth, endMonth+1):
            if i == startMonth and i == endMonth:
                if endDate >= startDate:
                    totalDays+=(endDate - startDate)+1
            elif i == startMonth:
                totalDays+=(days_per_month[i-1] - startDate)+1
            elif i == endMonth:
                totalDays+=endDate
            else:
                totalDays+=days_per_month[i-1]

        return totalDays
            