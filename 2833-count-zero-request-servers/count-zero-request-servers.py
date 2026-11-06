class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        len_q = len(queries)
        len_l = len(logs)
        arr = [0]*len_q
        # print(arr)
        
        queries = [(i, q) for i, q in enumerate(queries)]
        queries.sort(key = lambda x: x[1])
        logs.sort(key = lambda x: x[1])

        # print(queries)
        # print(logs)
        # print('\n\n')
        logs_idx = 0
        q_idx = 0
        res = 0

        left = 0
        right = -1

        d = {}
        while left < len_l and q_idx < len_q:
            while left < len_l and logs[left][1] < queries[q_idx][1] - x:
                if logs[left][0] in d:
                    d[logs[left][0]]-=1
                    if d[logs[left][0]] == 0:
                        del d[logs[left][0]]
                left+=1
                
            if left < len_l and left > right:
                d = {}
                right = left

            while right < len_l and queries[q_idx][1] - x <= logs[right][1] <= queries[q_idx][1]:
                if logs[right][0] not in d:
                    d[logs[right][0]] = 0
                d[logs[right][0]]+=1
                right+=1

            # print(q_idx, d, [left, right])
            # print('______________________________')
            arr[queries[q_idx][0]] = n - len(d)
            q_idx+=1

        while q_idx < len_q:
            arr[queries[q_idx][0]] = n - len(d)
            q_idx+=1

        return arr