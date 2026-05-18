from collections import deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        dq = deque([0])
        visited = [False]*n
        v = {}
        ans = 0
        map_ = {}
        for i, val in enumerate(arr):
            if val not in map_:
                map_[val] = []
            map_[val].append(i)

        # print('n: ',n)
        i = 0
        while dq:
            # print(dq, ans)
            q = set()
            for _ in range(len(dq)):
                i = dq.popleft()
                if i == n-1:
                    break

                if visited[i]:
                    continue
                
                visited[i] = True
                
                if i - 1 >= 0 and visited[i-1] == False:
                    dq.append(i-1)
                if i + 1 < n and visited[i+1] == False:
                    dq.append(i+1)

                if arr[i] in v:
                    continue

                for idx in map_[arr[i]]:
                    if idx!=i and visited[idx] == False:
                        dq.append(idx)
                v[arr[i]] = True


            if i == n-1:
                break
            ans+=1

        # print('dq: ',dq, ' i: ',i)
            

        return ans



