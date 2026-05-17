from collections import deque

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        dq = deque([])
        n = len(arr)
        visited = [False]*n
        dq.append(start)

        while dq:
            for _ in range(len(dq)):
                i = dq.popleft()
                visited[i] = True
                if arr[i] == 0:
                    return True

                if i + arr[i] < n and visited[i+arr[i]] == False:
                    dq.append(i+arr[i])
                if i - arr[i] >= 0 and visited[i-arr[i]] == False:
                    dq.append(i-arr[i])


        return False
                

