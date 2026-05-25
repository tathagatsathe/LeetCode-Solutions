from collections import deque

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        visited = [False]*n
        dq = deque([0])
        visited[0] = True
        last_index = 0

        while dq:
            idx = dq.popleft()

            if idx == n-1:
                return True

            for j in range(max(idx+minJump, last_index), min(idx+maxJump+1,n)):
                if s[j] == "0" and visited[j] == False:
                    dq.append(j)
                    visited[j] = True

            last_index = min(idx+maxJump+1,n)

        return False