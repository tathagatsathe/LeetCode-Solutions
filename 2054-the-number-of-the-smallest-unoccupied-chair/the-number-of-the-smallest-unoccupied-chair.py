import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        h = []
        h2 = []
        chair_counter = 0
        times = [[time[0], time[1], idx] for idx, time in enumerate(times)]
        times.sort()
        ans = 0
        # print('times: ',times)
        for i in range(len(times)):
            # print('i: ',i)
            # print('h: ',h)
            # print('h2: ',h2)
            while h and h[0][0] <= times[i][0]:
                leav_time, chair = heapq.heappop(h)
                heapq.heappush(h2, chair)
            if h2:
                # print('h2: ',h2)
                # print('h: ',h)
                chair = heapq.heappop(h2)
                heapq.heappush(h, (times[i][1], chair))
                ans = chair
                # print('existing chair: ',ans, i)
            else:
                heapq.heappush(h, (times[i][1], chair_counter))
                ans = chair_counter
                chair_counter+=1
            if times[i][2] == targetFriend:
                # print('i: ',i)
                break
            # print('_________________________________________________________')
            # print('h: ',h)
            # print('h2: ',h2)
            # print('\n')


        return ans
